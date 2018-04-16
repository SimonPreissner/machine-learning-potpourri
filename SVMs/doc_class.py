import os
import sys
from utils import parse_pod, plot_confusion_matrix
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

train1_size = 100
train2_size = 100
C = int(sys.argv[1])
kernel = sys.argv[2]

def get_topics():
    topics = {}
    files = [os.path.join('./data/', f) for f in os.listdir('./data/') if os.path.isfile(os.path.join('./data/', f))]
    for f in files:
        pod_dict, topic = parse_pod(f)
        topics[topic] = pod_dict
    return topics

def mk_arrays(space, n):
    training = []
    training_urls = []
    test = []
    test_urls = []
    c = 0
    for k,v in space.items():
        if c < n:
            training.append(v)
            training_urls.append(k)
            c+=1
        else:
            test.append(v)
            test_urls.append(k)
    return np.array(training), np.array(test), training_urls, test_urls

def mk_labels(size1,size2):
    y = []
    for i in range(size1):
        y.append(1)
    for i in range(size2):
        y.append(-1)
    y = np.array(y)
    return y
    

topic_dict = get_topics()
topics = list(topic_dict.keys())
print(topics)

t1 = input("Enter topic 1: ")
while t1 not in topics:
    t1 = input("Enter topic 1: ")
t2 = input("Enter topic 2: ")
while t2 not in topics:
    t2 = input("Enter topic 2: ")

t1_train, t1_test, t1_training_urls, t1_test_urls = mk_arrays(topic_dict[t1], train1_size)
t2_train, t2_test, t2_training_urls, t2_test_urls = mk_arrays(topic_dict[t2], train2_size)
training_urls = t1_training_urls + t2_training_urls

print("\n***\n")
print("Size training, class 1:",train1_size)
print("Size training, class 2:",train2_size)
print("Size test, class 1:",len(t1_test))
print("Size test, class 2:",len(t2_test))
print("\n***\n")


X_train = np.concatenate([t1_train,t2_train])
y_train = mk_labels(train1_size, train2_size)

X_test = np.concatenate([t1_test,t2_test])
y_test = mk_labels(len(t1_test), len(t2_test))

clf = SVC(C=C,verbose=True, kernel=kernel)
model = clf.fit(X_train,y_train)
print(model)

print("\nScore: ",clf.score(X_test,y_test))
y_pred = clf.predict(X_test)

print("\n\nPrinting support vectors...")
print([training_urls[s] for s in clf.support_])


# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=[t1,t2], title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=[t1,t2], normalize=True, title='Normalized confusion matrix')

plt.show()

