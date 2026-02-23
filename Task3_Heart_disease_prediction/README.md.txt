# Heart Disease Prediction

## Objective
Predict the likelihood of heart disease using machine learning models based on clinical and medical attributes.

## Dataset
UCI Heart Disease Dataset (Kaggle version)

## Model Used
- Logistic Regression

## Evaluation Metrics
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC Curve (AUC Score)

## Key Findings
- Logistic Regression achieved **79.51% accuracy** on the test dataset.
- The dataset was balanced, ensuring unbiased model evaluation.
- From the confusion matrix:
  - 86 heart disease cases were correctly identified (True Positives).
  - 76 healthy patients were correctly classified (True Negatives).
  - 17 heart disease cases were missed (False Negatives).
  - 26 healthy patients were incorrectly predicted as having heart disease (False Positives).
- The model achieved **84% recall for heart disease cases**, meaning it successfully identified most high-risk patients.

Overall, the model demonstrates strong baseline performance for a medical classification task.
