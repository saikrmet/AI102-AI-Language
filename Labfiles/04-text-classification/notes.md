### Custom Text Classification in Azure AI Language

*Custom text classification enables Azure AI Language to categorize text by user-defined labels.*

**Using the REST API**: https://learn.microsoft.com/en-us/training/modules/custom-text-classification/3-understand-how-to-build-projects 

#### Types of Custom Text Classification Projects
- **Single Label Classification**: Each text file can be assigned only one label (e.g., "Adventure" or "Strategy").
- **Multiple Label Classification**: Text files can receive multiple labels (e.g., "Adventure" and "Strategy").

#### Key Differences: Single vs. Multiple Label Projects
- **Single Label**: Each file is assigned one label only.
- **Multiple Label**: Files can have multiple labels, requiring a broader and well-distributed dataset for effective model learning.

#### Labeling Data for Classification
- **Single Label Projects**: Assign one class to each file during labeling.
- **Multiple Label Projects**: Multiple classes can be assigned per file; good data distribution is essential for learning varied classifications.

#### Evaluating and Improving Your Model
- **Correct Classifications**: Occur when the actual label matches the predicted label.
- **Error Types**:
  - **False Positive**: Model predicts label x incorrectly.
  - **False Negative**: Model misses label x, though it applies.

#### Performance Metrics
- **Recall**: True positives to all relevant items ratio.
- **Precision**: True positives to all positive predictions ratio.
- **F1 Score**: Balances recall and precision for overall model quality.

### Custom Text Classification Steps

1. **Define Labels**: Identify the categories (e.g., "Action", "Adventure") for classification.
2. **Tag Data**: Label the dataset with appropriate categories for model learning.
3. **Train Model**: Use labeled data to train the model.
4. **View Model**: Evaluate model performance with a score from 0 to 1 based on precision and recall.
5. **Improve Model**: Analyze misclassifications, adjust label distribution, and add data as needed.
6. **Deploy Model**: Make the model available via API.
7. **Classify Text**: Use the model to classify new text based on the trained labels.

#### Dataset Splitting for Training and Testing
- **Training Dataset**: Comprises about 80% of labeled data; used to train the model.
- **Testing Dataset**: The remaining labeled data; used to assess model performance.

#### Training Options
- **Automatic Split**: Azure divides data randomly into training and testing sets.
- **Manual Split**: Allows manual allocation of files into training and testing datasets for controlled distribution.

#### Deployment Options
- **Multiple Models & Deployments**: Allows testing, side-by-side model comparison, and version control for enhanced project flexibility.

