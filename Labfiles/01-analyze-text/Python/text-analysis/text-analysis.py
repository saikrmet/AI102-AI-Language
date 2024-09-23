from dotenv import load_dotenv
import os

# Import namespaces
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client using endpoint and key
        lang_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=AzureKeyCredential(ai_key))


        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get language
            detected_language_result = lang_client.detect_language(documents=[text])

            if detected_language_result is not None:
                print('\nLanguage: {}'.format(detected_language_result[0].primary_language.name))

            # Get sentiment
            detected_sentiment_result = lang_client.analyze_sentiment(documents=[text])

            if detected_sentiment_result is not None:
                print('\Sentiment: {}'.format(detected_sentiment_result[0].sentiment))

            # Get key phrases
            extract_key_phrases_result = lang_client.extract_key_phrases(documents=[text])

            if extract_key_phrases_result is not None:
                print('\Key Phrases: {}'.format(extract_key_phrases_result[0].key_phrases))


            # Get entities
            entities = lang_client.recognize_entities(documents=[text])[0].entities

            if len(entities) > 0:
                print("\nEntities:")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))


            # Get linked entities
            entities = lang_client.recognize_linked_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nLinks")
                for linked_entity in entities:
                    print('\t{} ({})'.format(linked_entity.name, linked_entity.url))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()