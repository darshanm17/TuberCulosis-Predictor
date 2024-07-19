import os
from data_preprocessing import create_data_generators
from feature_extraction import extract_features, flatten_features
from train_classifiers import train_logistic_regression, train_naive_bayes, train_knn, train_decision_tree, train_svm
from evaluate_classifiers import evaluate_classifier

# Paths to your data
train_dir = r'C:\Users\DARSHAN M\OneDrive\Desktop\DataSet\train'
val_dir = r'C:\Users\DARSHAN M\OneDrive\Desktop\DataSet\train'

# Data generators
train_generator, val_generator = create_data_generators(train_dir, val_dir)

# Sample counts
train_sample_count = train_generator.samples
val_sample_count = val_generator.samples

# Extract features
train_features, train_labels = extract_features(train_dir, train_sample_count)
val_features, val_labels = extract_features(val_dir, val_sample_count)

# Flatten features
train_features = flatten_features(train_features)
val_features = flatten_features(val_features)

# Train classifiers
log_reg = train_logistic_regression(train_features, train_labels)
naive_bayes = train_naive_bayes(train_features, train_labels)
knn = train_knn(train_features, train_labels)
decision_tree = train_decision_tree(train_features, train_labels)
svm = train_svm(train_features, train_labels)

# Evaluate classifiers
log_reg_accuracy = evaluate_classifier(log_reg, val_features, val_labels)
print('Logistic Regression Accuracy:', log_reg_accuracy)

naive_bayes_accuracy = evaluate_classifier(naive_bayes, val_features, val_labels)
print('Naive Bayes Accuracy:', naive_bayes_accuracy)

knn_accuracy = evaluate_classifier(knn, val_features, val_labels)
print('KNN Accuracy:', knn_accuracy)

decision_tree_accuracy = evaluate_classifier(decision_tree, val_features, val_labels)
print('Decision Tree Accuracy:', decision_tree_accuracy)

svm_accuracy = evaluate_classifier(svm, val_features, val_labels)
print('SVM Accuracy:', svm_accuracy)
