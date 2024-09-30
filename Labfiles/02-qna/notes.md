### Question Answering vs. Conversational Language Understanding


#### Feature Comparison:
| **Feature**                      | **Question Answering**                                       | **Language Understanding**                                       |
|----------------------------------|--------------------------------------------------------------|------------------------------------------------------------------|
| **Usage Pattern**                | User submits a question, expecting an answer                 | User submits an utterance, expecting a response or action        |
| **Query Processing**             | Matches the question to an answer in the knowledge base      | Interprets the utterance, identifies intent, and recognizes entities |
| **Response**                     | Static answer to a known question                            | Identifies the most likely intent and referenced entities        |
| **Client Logic**                 | Presents the answer to the user                              | Client performs an action based on the detected intent           |

#### Creating a Question Answering Solution:
1. **Azure Portal**:
   - Sign in and search for **Azure AI Services**.
   - Create a **Language Service** resource.
   - Enable the **Question Answering** feature.
   - Create or select an **Azure AI Search** resource for the knowledge base index.

2. **Language Studio**:
   - Select your Azure AI Language resource.
   - Create a **Custom Question Answering Project**.

3. **Populate the Knowledge Base**:
   - Add data sources, such as:
     - URLs for web pages with FAQs.
     - Files containing structured text for question-answer pairs.
     - Predefined chit-chat datasets for conversational questions and responses.

4. **Define and Edit Q&A Pairs**:
   - Manually edit question-answer pairs.
   - Define **follow-up prompts** for multi-turn conversations when additional information is needed.

#### Multi-Turn Conversations:
- Useful for complex questions that need clarification.
- Example: Initial question is *"How can I cancel a reservation?"*; a follow-up prompt could be *"Is it a hotel or flight reservation?"*.

- Define follow-up prompts to link to existing answers or create new ones.

#### Testing the Knowledge Base:
- Use **Language Studio** to test the knowledge base interactively.
- Review confidence scores and possible alternate answers for each question.

#### Deploying the Knowledge Base:
- Deploy to a **REST endpoint** for client applications to submit questions and receive answers.
- Endpoint response includes:
  - Closest question match.
  - Associated answer.
  - Confidence score.
  - Metadata.

#### Enhancing the Knowledge Base:
- **Active Learning**:
  - Continuously improve by reviewing alternate questions suggested by the system.
  - Accept or reject suggestions in the **Review Suggestions** pane.

- **Defining Synonyms**:
  - Handle different terminologies that refer to the same concept (e.g., "reservation" vs. "booking").
  - Helps the system provide relevant answers regardless of the term used.

#### Best Use Cases:
- **Question Answering**: Use when users ask questions expecting specific answers.
- **Conversational Language Understanding**: Use when users provide utterances expecting actions or dynamic responses based on detected intents.
