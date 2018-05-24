# Fast-mapping with an addition model

In this tutorial, you are provided with the definitional dataset of [Herbelot & Baroni (2017)](http://aurelieherbelot.net/resources/papers/emnlp2017_final.pdf). You will find both train and test sets in the folder *definitions*.

You are to run an addition model over that dataset and provide a thorough error analysis, as well as recommendations for improvement.

A background semantic space is provided in *spaces*. Note that this is only a toy space containing around 4800 entries. It needs to be unpacked with

`tar -xzf ukwac_reduced.tar.gz`

(to be run in the *spaces* directory).


### Running the addition model

You can run a simple addition model, with stopword list, by doing

`python3 test_def_nonces.py spaces/ukwac_reduced.txt definitions/nonce.definitions.300.test > results.txt`

Look at the file results.txt. Note the final MRR and average rank of the predicted vectors. Get familiar with the type of nearest neighbours returned by the system.

Check also the effect of the stopwords on results, by removing the filter in *utils.py* (function *centroid*) and re-running the test.


### Investigating rank

Sort the test instances by rank and consider their distribution. What is the maximum / minimum rank? Which words correspond to the worst errors? Why do you think the system ended up making such errors?

To help with your investigation, you can look at the neighbourhood of the gold vectors by using the visualisation tool. For instance, if you want to see the 20 nearest neighbours of the word *research*, you can do

`python3 viz.py spaces/ukwac_reduced.txt research 20`

NB: if you are on pythonanywhere, you won't be able to display the produced image from your terminal. Instead, go the your *utils.py* file, and uncomment the line *png.savefig(savefile)* in function *run_PCA*. This will save the image to your local directory.

Do you think removing some words in the input would help? Which ones? You can test your prediction by making a reduced test file with just the instances you are interested in, and modifying the original sentence. (You can also cheat and *add* words to see the impact this has on the result.)


### Investigating density

Rank evaluation has a problem: it does not take into account the density of the neighbourhood of the gold vector. Add a density function to the code and see whether density affects results. (Hint: you want to compute the correlation between density figures and rank.)


### Investigating subsampling

Write a subsampling function to remove words from the input before testing. You will first have to calculate word probabilities: do it over the training sentences (not ideal, but quick!) 

Try two setups:

* random subsampling: remove words randomly. Words with higher probability also have a higher probability to be subsampled.
* frequency-based sampling: only keep words over a certain frequency threshold.

How does your filter improve results?
