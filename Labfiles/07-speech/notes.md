### **Azure AI Speech: Provisioning and Features**  

Azure AI Speech enables **speech recognition (speech-to-text), speech synthesis (text-to-speech), and speech customization** through a REST API and SDKs.  

---

### **Provisioning Azure AI Speech**  

To use Azure AI Speech, you need to **create a resource** in your **Azure subscription**.  

You can choose between:  

1. **Azure AI Speech Resource** (Dedicated for speech services).  
2. **Azure AI Services Multi-Service Resource** (Includes Speech, Text Analytics, Translator, and other services).  

After provisioning, you need:  
- **Location** (e.g., eastus).  
- **API Key** (Available in Azure portal under Keys and Endpoint).  

---

### **Speech-to-Text API (Transcription)**  

Azure AI Speech supports two APIs for **speech recognition**:  

| API | Use Case |
|------|----------|
| **Speech to Text API** | Primary API for speech recognition (interactive or batch transcription). |
| **Speech to Text Short Audio API** | Optimized for audio up to **60 seconds**. |

You can use the **Speech to Text API** for **real-time transcription** or **batch processing** of multiple audio files.  

---

### **Using the Speech-to-Text API with SDK**  

1. **Create a `SpeechConfig` object** with your API key and location.  
2. **Specify the audio source** using an `AudioConfig` object (microphone or audio file).  
3. **Create a `SpeechRecognizer` object** to interact with the API.  
4. **Call `RecognizeOnceAsync()`** to transcribe a single spoken utterance.  
5. **Process the response** to get the recognized text.  

**Example Response Properties**:  

- **Text**: The transcribed speech.  
- **Duration**: Length of the speech in ticks.  
- **Reason**: `RecognizedSpeech`, `NoMatch`, or `Canceled`.  
- **ResultId**: Unique identifier for the response.  

If `Reason` is `Canceled`, check the **CancellationReason** property to debug errors.  

---

### **Text-to-Speech API (Speech Synthesis)**  

Azure AI Speech supports two APIs for **text-to-speech**:  

| API | Use Case |
|------|----------|
| **Text to Speech API** | Converts text to speech in real time. |
| **Batch Synthesis API** | Converts large volumes of text to speech (e.g., generating audiobooks). |

---

### **Using the Text-to-Speech API with SDK**  

1. **Create a `SpeechConfig` object** with your API key and location.  
2. **Specify the output using `AudioConfig`** (speaker, file, or audio stream).  
3. **Create a `SpeechSynthesizer` object**.  
4. **Call `SpeakTextAsync()`** to generate speech.  
5. **Process the response to retrieve the generated audio**.  

**Example Response Properties**:  

- **AudioData**: The synthesized speech data.  
- **Reason**: `SynthesizingAudioCompleted` if successful.  
- **ResultId**: Unique identifier for the response.  

---

### **Audio Format Customization**  

Azure AI Speech supports different **audio formats** based on:  
- **File Type** (e.g., WAV, MP3).  
- **Sample Rate** (e.g., 24 kHz, 16 kHz).  
- **Bit Depth** (e.g., 16-bit, 32-bit).  

To specify an audio format, use:  
```python
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
```

---

### **Customizing Speech Output with Different Voices**  

Azure AI Speech provides **two types of voices**:  

| Voice Type | Description |
|------------|------------|
| **Standard Voices** | Pre-recorded synthetic voices. |
| **Neural Voices** | More natural-sounding AI-generated voices. |

Voices are named based on **locale and speaker name** (e.g., `en-GB-George`).  

To specify a voice:  
```python
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
```

---

### **Advanced Speech Customization with SSML**  

Speech Synthesis Markup Language (SSML) allows greater control over synthesized speech, including:  

- **Speaking styles** (e.g., cheerful, excited).  
- **Pauses and silence**.  
- **Phonetic pronunciations** (e.g., pronounce "SQL" as "sequel").  
- **Adjusting pitch, speed, and tone**.  
- **Custom formatting (e.g., dates, phone numbers)**.  

**Example SSML Script**:  

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
                     xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US"> 
    <voice name="en-US-AriaNeural"> 
        <mstts:express-as style="cheerful"> 
          I say tomato 
        </mstts:express-as> 
    </voice> 
    <voice name="en-US-GuyNeural"> 
        I say <phoneme alphabet="sapi" ph="t ao m ae t ow"> tomato </phoneme>. 
        <break strength="weak"/> Let's call the whole thing off! 
    </voice> 
</speak>
```

### **SSML Features in the Example**  
- **AriaNeural voice speaks in a "cheerful" style**.  
- **GuyNeural voice pronounces "tomato" differently using phoneme notation**.  
- **A pause is inserted using `<break>`**.  

To submit SSML to the service, use:  
```python
speech_synthesizer.SpeakSsmlAsync(ssml_text)
```
