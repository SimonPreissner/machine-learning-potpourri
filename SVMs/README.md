# SVMs for topic classification

This is an implementation of an SVM classifier for topic classification, given a set of documents expressed as vectors.

### The data

In your data/ directory, you will find some csv files created by the [PeARS](http://pearsearch.org/) search engine. These files contain representations of web documents as 400-dimensional vectors, sorted by topics (one file per topic).

### Running the SVM

The SVM implementation used here comes from the [scikit-learn toolkit](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC). It lets you build a classifier for the data using a range of different kernels and various parameter values.

Run the classifier with e.g.

    python3 doc_class.py 100 linear

Instead of *linear*, you could also use *poly* for a polynomial kernel or *rbf* for an RBF Gaussian kernel. 100 is the C hyperparameter, which you can also change.

The program will ask you to choose two topics out of a list (remember that SVMs are binary classifiers). For instance:

    ['string theory', 'harry potter', 'star wars', 'black panther film', 'black panthers', 'opera']
    Enter topic 1: harry potter
    Enter topic 2: star wars

We then get the output of the SVM, the score over the test data, and the URL corresponding to the support vectors for the classification.


### Inspecting support vectors

Run the classifier with different kernels and notice the difference in number of support vectors selected by the classifier (that is the *nSV* value in the output. What do you conclude?

Open the web pages for a few support vectors. What do you notice?

