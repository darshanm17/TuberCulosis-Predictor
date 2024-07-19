import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def train_logistic_regression(train_features, train_labels):
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(train_features, train_labels)
    return log_reg

def train_naive_bayes(train_features, train_labels):
    naive_bayes = GaussianNB()
    naive_bayes.fit(train_features, train_labels)
    return naive_bayes

def train_knn(train_features, train_labels, n_neighbors=5):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(train_features, train_labels)
    return knn

def train_decision_tree(train_features, train_labels):
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(train_features, train_labels)
    return decision_tree

def train_svm(train_features, train_labels, kernel='linear'):
    svm = SVC(kernel=kernel)
    svm.fit(train_features, train_labels)
    return svm
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def train_logistic_regression(train_features, train_labels):
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(train_features, train_labels)
    return log_reg

def train_naive_bayes(train_features, train_labels):
    naive_bayes = GaussianNB()
    naive_bayes.fit(train_features, train_labels)
    return naive_bayes

def train_knn(train_features, train_labels, n_neighbors=5):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(train_features, train_labels)
    return knn

def train_decision_tree(train_features, train_labels):
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(train_features, train_labels)
    return decision_tree

def train_svm(train_features, train_labels, kernel='linear'):
    svm = SVC(kernel=kernel)
    svm.fit(train_features, train_labels)
    return svm
