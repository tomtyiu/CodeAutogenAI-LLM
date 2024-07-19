import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen import ConversableAgent
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
import os
from faster_whisper import WhisperModel
import pyaudio
import wave
from groq import Groq
import os
from autogen import Cache
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from elevenlabs import play
from autogen.coding import LocalCommandLineCodeExecutor
import re


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "file.wav"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )


def recording(WAVE_OUTPUT_FILENAME):
    audio = pyaudio.PyAudio()
 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")
 
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
 
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    
def transcribe(WAVE_OUTPUT_FILENAME):
    with open(WAVE_OUTPUT_FILENAME, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(WAVE_OUTPUT_FILENAME, file.read()),
        model="whisper-large-v3",
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        language="en",  # Optional
        temperature=0.0  # Optional
        )
        print(transcription.text)
        return transcription.text

ELEVENLABS_API_KEY = "api-key"
#os.getenv("ELEVENLABS_API_KEY")
    
def synthesis(text):
    client = ElevenLabs(
        api_key=ELEVENLABS_API_KEY, # Defaults to ELEVEN_API_KEY
        )

    audio = client.generate(
        optimize_streaming_latency="0",
        text=text,
        voice="06oPEcZqPWhZ2IeTcOJc",
        model="eleven_turbo_v2"
        #stream=True
     )
    play(audio)


llm_config = {
    "config_list": [{"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}],
}

# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)
#user_proxy = UserProxyAgent("user_proxy", human_input_mode="TERMINATE", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
# create a UserProxyAgent instance named "user_proxy"

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        # the executor to run the generated code
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
    },# Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

def sanitize_input(user_input: str) -> str:
    # Remove any harmful characters or patterns
    sanitized_input = re.sub(r'[^\w\s]', '', user_input)
    return sanitized_input


synthesis("Welcome to AutomindGPT! select 1 for Voice or 2 for manual input.")
choice=input("Welcome to AutomindGPT! select 1 for Voice or 2 for manual input.")
if choice == "1":
    record=recording(WAVE_OUTPUT_FILENAME)
    autogen_input_1 = transcribe(WAVE_OUTPUT_FILENAME)
    print(f"Write your prompt for autogen: {autogen_input_1}")
    synthesis(f"Write your prompt for autogen: {autogen_input_1}")
    autogen_input=sanitize_input(autogen_input_1)
    
elif choice == "2":
    autogen_input_1=input(f"Write your prompt for autogen: (default: {"Plot a chart of NVDA and TESLA stock price change YTD."}):")
    synthesis(f"Write your prompt for autogen: (default: {"Plot a chart of NVDA and TESLA stock price change YTD."}): {autogen_input_1}")
    autogen_input=sanitize_input(autogen_input_1)
    if autogen_input_1 == "":
        autogen_input = "Plot a chart of NVDA and TESLA stock price change YTD."
        synthesis("Plot a chart of NVDA and TESLA stock price change YTD.")
        autogen_input=sanitize_input(autogen_input_1)
    

# Use DiskCache as cache
with Cache.disk() as cache:
    messages =user_proxy.initiate_chat(assistant, message=autogen_input, cache=cache,summary_method="reflection_with_llm",)
    
# old user_proxy.initiate_chat(assistant, message=autogen_input)
# This initiates an automated chat between the two agents to solve the task
