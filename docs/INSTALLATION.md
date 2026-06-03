**[< Table Of Contents](https://github.com/lehner-lab/VIRUS#table-of-contents)**
<p align="left">
  <img src="../Virus.png" width="100">
</p>

# Installation Instructions

## System requirements

DiMSum is expected to work on all operating systems.

## Installing VIRUS and its dependencies using Conda (recommended)

The easiest way to install VIRUS is by using the [bioconda package](http://bioconda.github.io/recipes/deepvirus/README.html).

Firstly, install the [Conda](https://docs.conda.io/) package/environment management system (if you don't already have it).

On MacOS, run:
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh
sh Miniforge3-MacOSX-x86_64.sh
```
On Linux, run:
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
sh Miniforge3-Linux-x86_64.sh
```

**IMPORTANT:** If in doubt, respond with "yes" to the following question during installation: "Do you wish the installer to initialize Miniforge3 by running conda init?". In this case Conda will modify your shell scripts (*~/.bashrc* or *~/.bash_profile*) to initialize Miniforge3 on startup. Ensure that any future modifications to your *$PATH* variable in your shell scripts occur **before** this code to initialize Miniforge3.

After installing Conda you will need to add the bioconda channel as well as the other channels bioconda depends on. Start a new console session (e.g. by closing the current window and opening a new one) and run the following:
```
conda config --add channels bioconda
conda config --add channels conda-forge
```

Next, create a dedicated Conda environment to install the [VIRUS bioconda package](http://bioconda.github.io/recipes/deepvirus/README.html) and it's dependencies:
```
conda create -n deepvirus deepvirus
conda activate deepvirus
```
**TIP:** See [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information about managing conda environments.

To check that you have a working installation of VIRUS, run the [Demo](#demo-virus)

## Installing VIRUS from source (GitHub)

Installing VIRUS from source is not recommended. The easiest way to install VIRUS (and its dependencies) is by using the [VIRUS bioconda package](http://bioconda.github.io/recipes/deepvirus/README.html). See [Installing VIRUS and its dependencies using Conda](#installing-virus-and-its-dependencies-using-conda-recommended).

This [this yaml file](../deepvirus.yaml) can be used to create a dedicated Conda environment with all necessary dependencies (as explained below).

1. Install the [Conda](https://docs.conda.io/) package/environment management system (if you already have Conda skip to step 2):

  On MacOS, run:
  ```
  curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh
  sh Miniforge3-MacOSX-x86_64.sh
  ```
  On Linux, run:
  ```
  curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
  sh Miniforge3-Linux-x86_64.sh
  ```
  
  **IMPORTANT:** If in doubt, respond with "yes" to the following question during installation: "Do you wish the installer to initialize Miniforge3 by running conda init?". In this case Conda will modify your shell scripts (*~/.bashrc* or *~/.bash_profile*) to initialize Miniforge3 on startup. Ensure that any future modifications to your *$PATH* variable in your shell scripts occur **before** this code to initialize Miniforge3.

2. Clone the VIRUS GitHub repository:
   ```
   $ git clone https://github.com/lehner-lab/VIRUS.git
   ```

3. Create the deepvirus Conda environment:
   ```
   $ conda env create -f VIRUS/deepvirus.yaml
   ```

4. Install VIRUS:
   ```
   $ conda activate deepvirus
   $ cd VIRUS
   $ pip install -e ./
   ```

## Demo VIRUS

Run the demo to ensure that you have a working VIRUS installation (expected run time <10min):
   ```
   $ demo_virus.py
   ```
