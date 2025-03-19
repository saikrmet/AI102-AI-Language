### **Azure AI Translator: Provisioning and Features**  

Azure AI Translator enables **language detection, translation, transliteration, and customization** through a REST API.  

---

### **Provisioning Azure AI Translator**  

You must provision an **Azure AI Translator resource** in your **Azure subscription**. You can choose between:  

1. **Single-Service Azure AI Translator Resource**  
   - Dedicated to translation services.  

2. **Multi-Service Azure AI Services Resource**  
   - Includes **Text Analytics API** and **Translator API** in a single resource.  

---

### **Language Detection Using REST API**  

You can detect the language of a given text using the **Detect function**.  

**Example API Call (Detect Language using cURL)**  
```bash
curl -X POST "https://api.cognitive.microsofttranslator.com/detect?api-version=3.0" \
-H "Ocp-Apim-Subscription-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '[{"text": "Bonjour tout le monde"}]'
```
**Response Example**
```json
[
    {
        "language": "fr",
        "score": 1.0
    }
]
```
This indicates that the detected language is **French** with **100 percent confidence**.

---

### **Translating Text**  

To **translate text** between languages, use the **Translate function** and specify:  
- **`from`**: Source language (optional; auto-detected if not provided).  
- **`to`**: Target languages (one or more).  

**Example API Call (Translate from Japanese to English and French)**  
```bash
curl -X POST "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=ja&to=fr&to=en" \
-H "Ocp-Apim-Subscription-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '[{"text": "こんにちは"}]'
```
**Response Example**
```json
[
    {
        "translations": [
            {
                "text": "Bonjour",
                "to": "fr"
            },
            {
                "text": "Hello",
                "to": "en"
            }
        ]
    }
]
```
This response provides translations in **French (Bonjour)** and **English (Hello)**.

---

### **Transliteration (Converting Text Between Scripts)**  

Transliteration changes text **from one script to another** without translating it.  

**Example API Call (Japanese to Latin Script)**  
```bash
curl -X POST "https://api.cognitive.microsofttranslator.com/transliterate?api-version=3.0&fromScript=Jpan&toScript=Latn" \
-H "Ocp-Apim-Subscription-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '[{"text": "こんにちは"}]'
```
**Response Example**
```json
[
    {
        "text": "konnichiwa"
    }
]
```
This converts **Japanese Hiragana "こんにちは"** into **Latin script "konnichiwa"**.

---

### **Additional Translation Features**  

1. **Word Alignment**  
   - Some languages do not use spaces between words.  
   - Use **`includeAlignment=true`** to align words in translation.  

2. **Sentence Length**  
   - Use **`includeSentenceLength=true`** to check translation length.  
   - Useful for UI layout adjustments.  

3. **Profanity Filtering**  
   - **`profanityAction`** parameter:  
     - `NoAction`: Translate profanity as-is.  
     - `Deleted`: Remove profanity.  
     - `Marked`: Replace profanity using **profanityMarker** (`Asterisk` or `Tag`).  

---

### **Custom Translator for Industry-Specific Translations**  

If your business needs **custom vocabulary translations**, you can create a **Custom Translator Model**.  

#### **Steps to Create a Custom Translation Model**  

1. **Create a Workspace** linked to an Azure AI Translator resource.  
2. **Create a Project** for a specific translation task.  
3. **Upload Training Data** with domain-specific translations.  
4. **Train the Model** using Azure AI Translator.  
5. **Test and Publish** the model.  
6. **Use the Custom Model** via API for translation calls.  
