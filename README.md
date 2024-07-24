# AutomindGPT

AutomindGPT is an AI-driven assistant that leverages advanced language models and speech-to-text/text-to-speech functionalities to provide an interactive user experience. This project integrates various tools and APIs to deliver seamless voice and text-based interactions.

## Features

- **Voice Recording and Transcription**: Record audio and transcribe it to text using the WhisperModel.
- **Text-to-Speech**: Convert text responses to audio using ElevenLabs.
- **Advanced Language Models**: Use OpenAI's GPT-4 for intelligent conversations and task handling.
- **Secure and Sanitized Input**: Ensure all user inputs are sanitized for safety.
- **Automated Task Execution**: Employs autogen's AssistantAgent and UserProxyAgent for task automation.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/automindgpt.git
    cd automindgpt
    ```

2. **Set up the environment**:
    Ensure you have the necessary API keys and environment variables set up. Refer to [FAQ](https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints) for more details.

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Recording Audio**:
    ```python
    from autogen import Cache
    from elevenlabs import play

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 15
    WAVE_OUTPUT_FILENAME = "file.wav"

    def recording(WAVE_OUTPUT_FILENAME):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("recording...")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("finished recording")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
    ```

2. **Transcribing Audio**:
    ```python
    def transcribe(WAVE_OUTPUT_FILENAME):
        with open(WAVE_OUTPUT_FILENAME, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(WAVE_OUTPUT_FILENAME, file.read()),
                model="whisper-large-v3",
                prompt="Specify context or spelling",
                response_format="json",
                language="en",
                temperature=0.0
            )
            print(transcription.text)
            return transcription.text
    ```

3. **Text-to-Speech**:
    ```python
    ELEVENLABS_API_KEY = "api-key"

    def synthesis(text):
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        audio = client.generate(
            optimize_streaming_latency="0",
            text=text,
            voice="06oPEcZqPWhZ2IeTcOJc",
            model="eleven_turbo_v2"
        )
        play(audio)
    ```

4. **Setting up the Assistant and User Proxy**:
    ```python
    from autogen import AssistantAgent, UserProxyAgent
    from autogen.coding import LocalCommandLineCodeExecutor

    llm_config = {
        "config_list": [{"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}],
    }

    assistant = autogen.AssistantAgent(
        name="assistant",
        llm_config=llm_config
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="TERMINATE",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
        },
        llm_config=llm_config,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
        Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
    )
    ```

5. **Sanitizing Input**:
    ```python
    import re

    def sanitize_input(user_input: str) -> str:
        sanitized_input = re.sub(r'[^\w\s]', '', user_input)
        return sanitized_input
    ```

6. **Initiating Chat**:
    ```python
    synthesis("Welcome to AutomindGPT! Select 1 for Voice or 2 for manual input.")
    choice = input("Welcome to AutomindGPT! Select 1 for Voice or 2 for manual input.")

    if choice == "1":
        record = recording(WAVE_OUTPUT_FILENAME)
        autogen_input_1 = transcribe(WAVE_OUTPUT_FILENAME)
        synthesis(f"Write your prompt for autogen: {autogen_input_1}")
        autogen_input = sanitize_input(autogen_input_1)

    elif choice == "2":
        autogen_input_1 = input(f"Write your prompt for autogen: (default: 'Plot a chart of NVDA and TESLA stock price change YTD.'):")
        synthesis(f"Write your prompt for autogen: {autogen_input_1}")
        autogen_input = sanitize_input(autogen_input_1)
        if autogen_input_1 == "":
            autogen_input = "Plot a chart of NVDA and TESLA stock price change YTD."
            synthesis(autogen_input)

    with Cache.disk() as cache:
        messages = user_proxy.initiate_chat(assistant, message=autogen_input, cache=cache, summary_method="reflection_with_llm")
    ```

## Contributing

Feel free to open issues and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
