### Azure AI Language Service Features

*Overview of pre-configured and learned features available in Azure AI Language service.*

#### Pre-configured Features
- **No training required.**
- **Key Phrase Extraction**: Extracts important phrases from text.
- **Named Entity Recognition (NER)**: Identifies names of people, organizations, locations, and more.
- **Sentiment Analysis**: Analyzes text to determine positive, negative, or neutral sentiment.
- **Question Answering**: Provides answers based on input questions from sources like FAQs or manuals.

#### Learned Features
- **Requires data labeling, model training, and deployment.**
- **Conversational Language Understanding (CLU)**: 
  - Builds custom natural language understanding models.
  - Predicts intents and extracts entities from user input.
  - Requires tagging data for accurate predictions.

- **Custom Named Entity Recognition**: 
  - Trains models to recognize custom entities in unstructured text (e.g., extracting parties in contracts).

- **Custom Text Classification**: 
  - Classifies text into custom categories (e.g., grouping news articles by topics like News or Entertainment).

#### Question Answering
- **Mostly pre-configured**.
- Uses documents such as FAQs to answer questions.
- Supports virtual chat assistants to provide automated responses.

#### Building and Deploying Models
- **Methods**: Can be done via Language Studio or REST API.
- **REST API Process**:
  1. **Create project**.
  2. **Import data**.
  3. **Train model**.
  4. **Deploy model**.
  5. **Use model**.

#### REST API Example for CLU Deployment

```json
POST {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}?api-version={API-VERSION}

Headers:
  - Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY

Response:
{
  "jobId": "{JOB-ID}",
  "createdDateTime": "String",
  "lastUpdatedDateTime": "String",
  "expirationDateTime": "String",
  "status": "running"
}
```

- **Check Deployment Job Status**:
```json
GET {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
```

#### Sample Response for CLU Model Prediction
```json
{
  "kind": "ConversationResult",
  "result": {
    "query": "String",
    "prediction": {
      "topIntent": "intent1",
      "projectKind": "Conversation",
      "intents": [
        {
          "category": "intent1",
          "confidenceScore": 1
        },
        {
          "category": "intent2",
          "confidenceScore": 0
        }
      ],
      "entities": [
        {
          "category": "entity1",
          "text": "text",
          "offset": 7,
          "length": 4,
          "confidenceScore": 1
        }
      ]
    }
  }
}
```

---

### Defining Intents and Utterances in Language Models

*Intents and utterances help in defining the behavior and understanding of a language model.*

- **Utterances**: User-input phrases that the application must interpret.
- **Intent**: Represents the task or meaning behind an utterance.

#### Example of Intents and Associated Utterances:

- **GetTime**:
  - "What time is it?"
  - "What is the time?"
  - "Tell me the time."

- **GetWeather**:
  - "What is the weather forecast?"
  - "Do I need an umbrella?"
  - "Will it snow?"

- **TurnOnDevice**:
  - "Turn the light on."
  - "Switch on the light."
  - "Turn on the fan."

- **None**:
  - "Hello."
  - "Goodbye."

#### Best Practices for Creating Intents and Utterances
- **Define intents that cover the application's domain and user actions.**
- **Capture diverse utterances** to represent the same intent, varying in structure, length, and grammar.
- **Include a "None" intent** for out-of-domain or irrelevant utterances.

#### Labeling Utterances for Intent and Entity Recognition
- **Label Precisely**: Ensure each entity is labeled to the correct type.
- **Label Consistently**: Maintain the same labels across all similar utterances.
- **Label Completely**: Make sure all instances of entities in the data are labeled.

#### Entity Types in Models
- **Learned Entities**: Used for most contexts; defined in training data and learned through patterns.
- **List Entities**: Pre-defined list values, useful for specific sets like days of the week.
- **Prebuilt Entities**: Standard types such as numbers or dates, automatically recognized by the model.

#### Handling Similar Utterances Across Different Intents

- When multiple intents share similar utterance structures, differentiate using patterns.
  
  - Example:
    - **TurnOnDevice**: "Turn on the kitchen light."
    - **GetDeviceStatus**: "Is the kitchen light on?"
    - **TurnOffDevice**: "Turn off the kitchen light."

#### Iterative Model Development Process
1. **Train** the model using example utterances for intents and entities.
2. **Test** the model interactively or with a test dataset.
3. **Deploy** the model to a public endpoint for app integration.
4. **Review Predictions** and improve utterances for better performance.