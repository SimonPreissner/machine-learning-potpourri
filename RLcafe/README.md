# Intro to reinforcement learning

## Preliminaries: playing frozen lake

To get you started with RL, play for a while with the Frozen Lake puzzle from the [OpenAI gym](https://gym.openai.com/envs/FrozenLake-v0/). A Q-table implementation that tackles the puzzle can be found [here](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/Q%20Learning%20with%20FrozenLake.ipynb) as a Jupyter notebook. In this repo, you will also find a version of the same code that you can simply run from the terminal (frozen_lake.py).

Understand the environment and the steps taken by the algorithm. Try to modify the parameters to see their influence on the result.


## Learning politeness

Now, let's implement our own RL problem. It is a much simpler problem than the frozen lake but it will make things more transparent.

An Italian café has the following sign above the counter:

```
un caffè / a coffee: 3 EUR
buongiorno, un caffè / hello, a coffee: 2 EUR
bungiorno, un caffè per favore / hello, a coffee please: 1 EUR
```

Let's design an RL agent that will learn some obvious politeness rules.

We're going to make the environment a little more challenging in the following ways:

* When we ask for our coffee using the most polite form, things sometimes go wrong. The café owner is so busy that she doesn't wait to hear the end of the sentence, leading her to think that we simply said *Buongiorno, un caffè!* This displeases her.

* Sometimes, the café owner is in a really good mood, and even though we were not that polite (we only said *Buongiorno, un caffè!*, or perhaps *Un caffè, per favore!*) she still makes us pay 1 EUR only.


### Let's write down the environment

This is a pen and paper exercise. Try to write down the environment: which states we have, which actions we can take, and which rewards we will be given. 

NB: all rewards are 0 apart from the ones we get at the end of the utterance, which match the price of the coffee: -1 for 1 EUR, -2 for 2 EUR, -3 for 3 EUR.


