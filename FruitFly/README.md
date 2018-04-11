# Implementing the fruit fly's similarity hashing

This is an implementation of the random indexing method described by Dasgupta et al (2017) in [A neural algorithm for a fundamental computing problem](http://science.sciencemag.org/content/358/6364/793/tab-figures-data).

### Description of the data

Your data/ directory contains two small semantic spaces:

- one from the British National Corpus, containing lemmas expressed in 4000 dimensions.
- one from a subset of Wikipedia, containing words expressed in 1000 dimensions.

The cells in each semantic space are normalised co-occurrence frequencies *without any additional weighting* (PMI, for instance).

The directory also contains test pairs from the [MEN similarity dataset](https://staff.fnwi.uva.nl/e.bruni/MEN), both in lemmatised and natural forms.


### Running the fruit fly code

To run the code, you need to enter the corpus you would like to test on, and the number of Kenyon cells you are going to use for the experiment. For instance, for the BNC space:

    python3 projection.py bnc 8000

Or for the Wikipedia space:

    python3 projection.py wiki 4000

The program returns the Spearman correlation with the MEN similarity data, as calculated a) from the raw frequency space; and b) after running the fly's random projections.
