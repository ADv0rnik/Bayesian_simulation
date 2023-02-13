import os
import matplotlib.pyplot as plt
import arviz as az
import numpy as np
import pymc3 as pm

from scipy import stats
from tabulate import tabulate

from collector import Collector
from utils import save_to_file


DIR_NAME = 'sample_dir/'
SAMPLE_DIR = os.path.join(os.path.dirname(__file__), DIR_NAME)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'data/')


collector = Collector(SAMPLE_DIR)
data = np.array(collector.get_list_of_values)


def return_base_statistics(data_: np.ndarray):
    mean = np.mean(data_)
    std = np.std(data_)
    sem = stats.sem(data_)
    min_ = min(data_)
    max_ = max(data_)
    return float(mean), float(sem), float(std), int(max_), int(min_)


d = [return_base_statistics(data)]

basic_stats = tabulate(d, headers=['Mean', 'Std', 'StError', 'Max', 'Min'])
save_to_file(basic_stats, 'basic_stats')

az.plot_kde(data, rug=True)
plt.yticks([0], alpha=0)
plt.savefig(OUTPUT_DIR + 'fig1.png')

with pm.Model() as model:
    mu = pm.Uniform(name='mu', lower=return_base_statistics(data)[-1], upper=return_base_statistics(data)[-2])
    sig = pm.HalfNormal(name='sig', sd=17.8)
    val = pm.Normal(name='val', mu=mu, sd=sig, observed=data)
    trace_g = pm.sample(1000, tune=1000, return_inferencedata=True)

axes = az.plot_trace(trace_g)
fig = axes.ravel()[0].figure
fig.savefig(OUTPUT_DIR + 'fig2.png')

az.plot_pair(trace_g, kind='kde', fill_last=False)
plt.yticks([0], alpha=0)
plt.savefig(OUTPUT_DIR + 'fig3.png')

az.summary(trace_g).to_csv(OUTPUT_DIR+'post_sum.txt')

az.plot_posterior(trace_g)
plt.yticks([0], alpha=0)
plt.savefig(OUTPUT_DIR + 'fig4.png')
