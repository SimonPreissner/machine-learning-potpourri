# Mapping semantic spaces for translation

In this tutorial, you will map from a small English semantic space to a Catalan semantic space.


### Preliminaries

Familiarise yourself with the content of the data/ directory. The *pairs.txt* file contains gold standard translations from English to Catalan. *english.subset.dm* and *catalan.subset.dm* are subsets of an English and a Catalan semantic space corresponding to the words occurring in *pairs.txt*.

Just looking at the data (before running anything), can you tell where the model might do well and where it might fail?


### Running the regression code

Running the code will split the data into training and test set, calculate the regression matrix on the training data and evaluate it on the test set:

    python3 regression.py

The output first gives the predictions for each pair:

    bird ocell ['arbre', 'peix', 'ocell', 'gos', 'animal'] 1

Here, *bird* should have been translated with *ocell*. The 5 nearest neighbours of the predicted vector are *arbre, peix, ocell, gos* and *animal*, meaning the gold translation can be found in those close neighbours.

The last line gives the precision @ *k*, where *k* is the number of nearest neighbours considered for evaluation.

What can you say about the system's errors? (You may need a Catalan dictionary. Here's a good one: *https://www.diccionaris.cat/*.)



### Running the visualisation code

Running the following will create pictures of the Enlglish and Catalan spaces in your directory, split in train and test sets.

    python3 viz.py


