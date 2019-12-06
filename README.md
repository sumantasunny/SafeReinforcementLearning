# Self-Driving Car

This code has been adapted from the following [github repo](https://github.com/safe-rl/safe-rl-shielding.git).This is part of the work done by M. Alshiekh et. al. in the paper: ["Safe Reinforcement Learning via Shielding"](https://arxiv.org/abs/1708.08611). This repo contains the following work done by me:

* A presentation summarizing the paper
* A Jupyter Notebook describing how the self-driving car example works
* An slightly modified version of the original self-driving car code found in [github repo](https://github.com/safe-rl/safe-rl-shielding.git)

## Installing:

This repository was tested on a fresh install of Ubuntu 18.04. First install the required dependencies:

```
$ sudo apt-get install python3-pip
$ sudo apt-get install cmake
$ sudo apt-get install swig
$ sudo apt install python3-notebook jupyter jupyter-core python-ipykernel
$ pip3 install jupyter
$ pip3 install -r requirements.txt
$ pip3 install matplotlib
```

For notes on the changes made to the original codebase please look inside the Jupyter Notebook.

## Running the Code:

You can run the code using the following commands:

```
## No Shield
$ python3 krl.py -v

## Big Negative Reward
$ python3 krl.py -v -bn

## Preemtive Shield
$ python3 krl.py -v -p

## Post Shield
$ python3 krl.py -v -s
```

You can then plot the results using:

```
$ python3 plot_score.py
```

# Running the Jupyter Notebook

Launch the notebook
$ jupyter notebook