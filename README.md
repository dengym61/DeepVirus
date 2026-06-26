========================================================================
                              DeepVirus
========================================================================

DeepVirus is a deep learning-based model for virus-related prediction tasks.

OVERVIEW
------------------------------------------------------------------------
This repository provides the source code, environment configuration, and 
examples for running DeepVirus.


REQUIREMENTS
------------------------------------------------------------------------
The project was tested with the following environment:
- Python 3.9.9
- PyTorch 1.10.1
- NumPy 1.21.2
- pandas 1.4.2
- scikit-learn 1.0.2
- SciPy 1.8.0
- Matplotlib 3.5.1
- Seaborn 0.11.2
- pyreadr 0.4.4


INSTALLATION
------------------------------------------------------------------------
We recommend using Conda to create the environment and manage dependencies.

1. Clone the repository
   git clone https://github.com/your-username/DeepVirus.git
   cd DeepVirus

2. Create the virtual environment
   Create the Conda environment using the provided YAML file:
   conda env create -f deepvirus.yaml

3. Activate the environment
   Once the environment is created, activate it using the following command:
   conda activate deepvirus


DATA PREPARATION
------------------------------------------------------------------------
Please prepare the input data in the required format before running the 
model. Place your dataset under the "data/" directory.

Each input file should contain the following fields:

Column      | Description
--------------------------------------------------
aa_seq      | DMS sequence
Nham_aa     | WT (wild type)
fitness     |Variance



USAGE
------------------------------------------------------------------------

[ Demo VIRUS ]
Run the demo to ensure that you have a working VIRUS installation:
   python bin/demo_virus.py

[ VIRUS Command Line Tool ]
Replace MY_MODEL with the path to your model design file. 
   python bin/run_virus.py --model_design ./data/model_design.txt

Get help with additional command line parameters:
   python bin/run_virus.py -h

[ Model Design File ]
VIRUS requires a plain text model design file containing a table 
describing the measured phenotypes and how they relate to the underlying 
additive (biophysical) traits. The table should have the following 4 
tab-separated columns:

* trait          : One or more additive trait names.
* transformation : The shape of the global epistatic trend 
                   (Supported: Linear / ReLU / SiLU / Sigmoid / 
                   SumOfSigmoids / TwoStateFractionFolded / 
                   ThreeStateFractionBound).
* phenotype      : e.g., Binding, Cell entry, Antibody escape.
* file           : Path to the input data file.


LICENSE
------------------------------------------------------------------------
This project is released under the MIT License. 
See the LICENSE file for more details.


BUGS AND FEEDBACK
------------------------------------------------------------------------
You may submit a bug report on GitHub as an issue or you can send an 
email to: dengym61@163.com
