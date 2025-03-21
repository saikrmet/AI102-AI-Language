from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk


def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = os.getenv('SPEECH_REGION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=true)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)


    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech.sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)


    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)



    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()