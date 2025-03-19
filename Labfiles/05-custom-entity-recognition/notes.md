### **Custom vs Built-in Named Entity Recognition (NER) in Azure AI Language**  

Azure AI Language provides **built-in entity recognition** for common categories such as **person names, locations, organizations, and URLs**. Built-in NER requires minimal setup and extracts standard entities automatically.  

Custom NER allows users to **define and train models** for extracting domain-specific entities from text, such as financial details in bank statements or medical terms in patient records.  

---

### **Steps to Create a Custom Entity Recognition Model**  

1. **Define Entities**  
   - Identify and define the entities relevant to your dataset.  
   - Example: Extracting details from bank statements such as **customer name, loan amount, account number**.  

2. **Tag Data**  
   - Label the text by associating words or phrases with their respective entity types.  
   - Ensure labels are **accurate and comprehensive** for the best model performance.  

3. **Train the Model**  
   - Train the model after tagging the data.  
   - The model learns to identify and classify the labeled entities.  

4. **Evaluate Model Performance**  
   - The model provides a **score from 0 to 1**, indicating how well it recognizes entities.  
   - Review which entities perform well and which need improvement.  

5. **Improve the Model**  
   - Identify failed or incorrect entity extractions.  
   - Add more labeled data or refine existing labels to enhance accuracy.  

6. **Deploy the Model**  
   - Once satisfied with performance, **deploy the model** to make it accessible via API.  
   - The model can now process real-world text data and extract entities.  

7. **Extract Entities via API**  
   - Submit a request using the **CustomEntityRecognition** task in the API.  
   - The model extracts entities based on trained data.  

---

### **Example API Request for Custom NER**  
```json
{
    "displayName": "MyNERModel",
    "analysisInput": {
        "documents": [
            {
                "id": "doc1", 
                "text": "John Doe opened an account with a loan of $10,000 at ABC Bank."
            }
        ]
    },
    "tasks": [
        {
            "kind": "CustomEntityRecognition",
            "taskName": "MyRecognitionTask",
            "parameters": {
                "projectName": "BankingNERProject",
                "deploymentName": "BankingModelV1"
            }
        }
    ]
}
```

---

### **Project Limits and API Constraints**  

- **Training Requirements**:  
  - Minimum **10** files required  
  - Maximum **100,000** files  
- **Deployment Limits**:  
  - Up to **10 deployment names per project**  
- **API Limits**:  
  - **Authoring API**: 10 POST and 100 GET requests per minute  
  - **Analysis API**: 20 GET or POST requests per minute  
- **Entity Constraints**:  
  - Maximum **200 entity types**  
  - Each entity can be up to **500 characters**  

---

### **How to Label Data in Language Studio**  

- Use **Azure Language Studio** to label text data by selecting entity spans.  
- The tool automatically generates a **JSON file** storing labeled data for training.  
- The JSON format includes labeled entities, their positions in text, and their assigned category.  

**Example JSON Format for Custom NER**:  
```json
{
  "projectFileVersion": "2024-03-10",
  "metadata": {
    "projectKind": "CustomEntityRecognition",
    "projectName": "BankingNERProject",
    "language": "en-us"
  },
  "assets": {
    "entities": [
      { "category": "CustomerName" },
      { "category": "LoanAmount" }
    ],
    "documents": [
      {
        "location": "bank_statement_01.txt",
        "language": "en",
        "entities": [
          {
            "offset": 0,
            "length": 8,
            "labels": [{ "category": "CustomerName" }]
          },
          {
            "offset": 45,
            "length": 6,
            "labels": [{ "category": "LoanAmount" }]
          }
        ]
      }
    ]
  }
}
```

---

### **Understanding Model Performance Metrics**  

| **Metric**  | **Description** |
|-------------|----------------|
| **Precision** | Measures correct entity recognition among all recognized entities. High precision means recognized entities are labeled correctly. |
| **Recall** | Measures how well the model finds entities in the dataset. High recall means most entities are identified, even if some are misclassified. |
| **F1 Score** | A combined measure of **precision and recall** for overall model accuracy. |

- **Low Precision, High Recall**: Model identifies most entities but may misclassify some.  
- **High Precision, Low Recall**: Model correctly classifies entities but fails to identify all entities in a document.  

---

### **Summary**  

- Built-in NER extracts **common entity types** with minimal setup.  
- Custom NER allows you to **define and train a model** for industry-specific entity recognition.  
- **Training involves tagging data, evaluating performance, and improving the model**.  
- **Use Azure Language Studio** for easy data labeling and model training.  
- **API calls allow real-time entity extraction** for deployed models.  

Azure AI Language provides a **flexible, scalable solution** for named entity recognition across different use cases.