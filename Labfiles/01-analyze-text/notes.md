### Azure AI Language

*Azure AI Language helps analyze text for key insights like language, sentiment, and entities.*

#### Key Features:

- **Language Detection**:
  - Determines the language of the text input.
  - Useful for content with unknown language, e.g., chatbots, content stores.
  - Returns a **language identifier** and **confidence score** (0-1).
  - Handles documents under **5,120 characters**; up to **1,000 items** per collection.
  - **Multilingual content**: Identifies the language with the largest representation, but returns a lower confidence score.
  - In cases of ambiguity (e.g., character encoding issues), the language is marked as **unknown** with a score of **0**.

- **Key Phrase Extraction**:
  - Identifies important words/phrases that reflect the main points of the document.
  - Best suited for **larger documents**, with a limit of **5,120 characters**.
  - Can process multiple documents at once using the REST API.

- **Sentiment Analysis**:
  - Quantifies the sentiment (positive, neutral, negative) of text.
  - Useful for analyzing reviews, customer service emails, and social media messages.
  - Provides:
    - **Overall document sentiment**: Summarized from sentence-level sentiment.
    - **Sentence-level sentiment**: Each sentence classified as positive, negative, or neutral.
  - **Sentiment classification**:
    - All sentences neutral = overall neutral.
    - Positive + neutral = overall positive.
    - Negative + neutral = overall negative.
    - Positive + negative = mixed sentiment.

- **Named Entity Recognition (NER)**:
  - Detects entities like people, locations, organizations, and more within the text.
  - Entities are categorized (e.g., Person, Location, Organization, Email, URL).
  - Helps to extract structured information from unstructured text.

- **Entity Linking**:
  - Disambiguates entities with similar names by linking to knowledge base references (like Wikipedia).
  - Useful when an entity can refer to multiple things (e.g., "Venus" could mean the planet or goddess).

#### Use Cases:

- **Language Detection**: Ideal for systems where the text language is unknown (e.g., chatbots).
- **Key Phrase Extraction**: Helpful for summarizing long documents by identifying key points.
- **Sentiment Analysis**: Used to prioritize customer feedback or assess opinions in reviews.
- **Named Entity Recognition (NER)**: Extracts structured information like names, locations, dates from text.
- **Entity Linking**: Helps clarify ambiguous terms by linking to knowledge bases like Wikipedia.

#### Important Considerations:
- **Mixed-language documents**: The dominant language is identified but with lower confidence.
- **Unknown language**: If text can't be analyzed (e.g., encoding issues), the language is marked as "unknown".
- **Document size**: Maximum document size for analysis is **5,120 characters**.