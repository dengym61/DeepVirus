![example workflow](https://github.com/lehner-lab/VIRUS/actions/workflows/CI.yaml/badge.svg)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/deepvirus/README.html)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/deepvirus/badges/version.svg?branch=master&kill_cache=1)](https://anaconda.org/bioconda/deepvirus)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/deepvirus/badges/latest_release_relative_date.svg?branch=master&kill_cache=1)](https://anaconda.org/bioconda/deepvirus)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/deepvirus/badges/downloads.svg?branch=master&kill_cache=1)](https://anaconda.org/bioconda/deepvirus)

<p align="left">
  <img src="./Virus.png" width="100">
</p>

# VIRUS

Welcome to the GitHub repository for VIRUS: Neural networks to fit interpretable models and quantify energies, energetic couplings, epistasis, and allostery from deep mutational scanning data.

# Table Of Contents

1. **[Installation](#installation)**
1. **[Usage](#usage)**
   1. **[Option A: VIRUS command line tool](#option-a-virus-command-line-tool)**
   1. **[Option B: Custom Python script](#option-b-custom-python-script)**
   1. **[Demo](#demo-virus)**
1. **[Manual](#manual)**
1. **[Bugs and feedback](#bugs-and-feedback)**
1. **[Citing VIRUS](#citing-virus)**

# Installation

The easiest way to install VIRUS is by using the [bioconda package](http://bioconda.github.io/recipes/deepvirus/README.html):
```
conda install -c bioconda deepvirus
```

See the full [Installation Instructions](docs/INSTALLATION.md) for further details and alternative installation options.

# Usage

You can run a standard VIRUS workflow using the command line tool or a custom analysis by taking advantage of the "deepvirus" package in your own python script.

VIRUS requires a plain text model design file containing a table describing the measured phenotypes and how they relate to the underlying additive (biophysical) traits. The table should have the following 4 tab-separated columns (see example [here](deepvirus/data/model_design_example.txt)):
 - `trait`: One or more additive trait names 
 - `transformation`: The shape of the global epistatic trend (Linear/ReLU/SiLU/Sigmoid/SumOfSigmoids/TwoStateFractionFolded/ThreeStateFractionBound)
 - `phenotype`: A unique phenotype name e.g. Abundance, Binding or Kinase Activity
 - `file`: Path to DiMSum output (.RData) or plain text file with variant fitness and error estimates for the corresponding phenotype(s) (nucleotide sequence example [here](https://github.com/lehner-lab/VIRUS/blob/master/deepvirus/data/fitness_example_nt.txt), amino acid sequence example [here](https://github.com/lehner-lab/VIRUS/blob/master/deepvirus/data/fitness_example_aa.txt))

## Option A: VIRUS command line tool

Replace `MY_MODEL` with the path to your model design file (see example [here](deepvirus/data/model_design_example.txt)).
```
run_virus.py --model_design MY_MODEL
```

Get help with additional command line parameters:
```
run_virus.py -h
```

## Option B: Custom Python script

Below is an example of a custom VIRUS workflow (written in Python) to infer the underlying free energies of folding and binding from [doubledeepPCA](https://www.nature.com/articles/s41586-022-04586-4) data.

```
#Imports
import deepvirus
from deepvirus.data import VirusData
from deepvirus.models import VirusTask
from deepvirus.report import VirusReport
import pandas as pd
from pathlib import Path

#####################
# Step 1: Create a *VirusTask* object with one-hot encoded variant sequences, interaction terms and 10 cross-validation groups
#####################

#Globals
k_folds = 10
abundance_path = str(Path(deepvirus.__file__).parent / "data/fitness_abundance.txt") #VIRUS demo data
binding_path = str(Path(deepvirus.__file__).parent / "data/fitness_binding.txt") #VIRUS demo data

#Define model
my_model_design = pd.DataFrame({
   'phenotype': ['Abundance', 'Binding'],
   'transformation': ['TwoStateFractionFolded', 'ThreeStateFractionBound'],
   'trait': [['Folding'], ['Folding', 'Binding']],
   'file': [abundance_path, binding_path]})

#Create Task
virus_task = VirusTask(
   directory = 'my_task',
   data = VirusData(
      model_design = my_model_design,
      k_folds = k_folds))

#####################
# Step 2: Hyperparameter tuning and model fitting
#####################

#Perform grid search overy hyperparameters
virus_task.grid_search() 

#Fit model using optimal hyperparameters
for i in range(k_folds):
   virus_task.fit_best(fold = i+1)

#####################
# Step 3: Generate report, phenotype predictions, inferred additive trait summaries and save task
#####################

temperature_celcius = 30

virus_report = VirusReport(
   task = virus_task,
   RT = (273+temperature_celcius)*0.001987)

energies = virus_task.get_additive_trait_weights(
   RT = (273+temperature_celcius)*0.001987)
 
virus_task.save()
```
Report plots, predictions and additive trait summaries will be saved to the `my_task/report`, `my_task/predictions` and `my_task/weights` subfolders.

## Demo VIRUS

Run the demo to ensure that you have a working VIRUS installation (expected run time <10min):
```
demo_virus.py
```

# Manual

Comprehensive documentation is coming soon, but in the meantime get more information about specific classes/methods in python e.g.
```
help(VirusData)
```

# Bugs and feedback

You may submit a bug report here on GitHub as an issue or you could send an email to ajfaure@gmail.com.

# Citing VIRUS

Please cite the following publication if you use VIRUS:

Faure, A. J. & Lehner, B. VIRUS: neural networks to fit interpretable models and quantify energies, energetic couplings, epistasis, and allostery from deep mutational scanning data. Genome Biol 25, 303 (2024). [10.1186/s13059-024-03444-y](https://doi.org/10.1186/s13059-024-03444-y)

#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.6.

(Vector illustration credit: <a href="https://www.vecteezy.com">Vecteezy!</a>)
