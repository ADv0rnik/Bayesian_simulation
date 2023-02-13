### Bayesian simulation

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

#### Background

A small script demonstrated application of Bayesian probabilistic model to radiation measurements data. 

The program focuses on how to do Bayesian analysis and visualization with PyMC3 & ArviZ

The program require Python version 3.10 or older. For Windows users the oldest version of python interpreter can be found here http://www.python.org. Python interpreter is usually pre-installed on Ubuntu Linux. However, you may want to update it. In this case use the following guideline

The list of packages required for program is presented in requirements.txt

```python
arviz
numpy
pymc3
scipy
tabulate
matplotlib
```

#### Installation

To install the program use `git clone https://github.com/ADv0rnik/Bayesian_simulation.git` command (git must be preinstalled on your machine) to clone the repository from GitHub

Run:

```bash
pip install -r requirements.txt
```

Run model.py from the terminal by using following command (you must be inside corresponding directory):

```bash
python model.py
```

Sample data available via this link: 
https://drive.google.com/drive/folders/1LRt4xuW9M2uCYrDU6Qv_bM_OzOEzSsRK?usp=share_link