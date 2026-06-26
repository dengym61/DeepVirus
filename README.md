# DeepVirus 🦠

[![Python 3.9](https://img.shields.io/badge/python-3.9.9-blue.svg)](https://www.python.org/)
[![PyTorch 1.10.1](https://img.shields.io/badge/PyTorch-1.10.1-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DeepVirus is a deep learning-based framework designed for virus-related prediction tasks, enabling efficient mapping of sequence-to-phenotype landscapes.

---

## 📌 Overview

This repository provides the official source code, environment configuration, and examples for running DeepVirus. The model helps capture global epistatic trends and biophysical traits from deep mutational scanning (DMS) datasets.

---

## 💻 Requirements

The project has been tested and verified under the following environment:

* **Python** 3.9.9
* **PyTorch** 1.10.1
* **NumPy** 1.21.2
* **pandas** 1.4.2
* **scikit-learn** 1.0.2
* **SciPy** 1.8.0
* **Matplotlib** 3.5.1
* **Seaborn** 0.11.2
* **pyreadr** 0.4.4

---

## ⚙️ Installation

We highly recommend using [Conda](https://docs.conda.io/en/latest/) to manage your virtual environments.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/DeepVirus.git
cd DeepVirus
```

### 2. Create the virtual environment
Create an isolated environment using the provided `deepvirus.yaml` file:
```bash
conda env create -f deepvirus.yaml
```

### 3. Activate the environment
Once the installation is complete, activate the environment with:
```bash
conda activate deepvirus
```

---

## 📊 Data Preparation

Before running the model, please format your input datasets as specified below. 

Each input file should contain at least the following fields:

| Column | Description |
| :--- | :--- |
| `aa_seq` | DMS sequence (Amino acid sequence) |
| `Nham_aa` | Number of amino acid mutations relative to WT (Wild Type) |
| `fitness_sigma` | Fitness variance / standard deviation |

> 📂 **Note:** Please place all your processed datasets under the `data/` directory.

---

## 🚀 Usage

### 1. Running the Demo
Verify your installation by running the provided demo script:
```bash
python demo_virus.py
```

### 2. Running VIRUS Command Line Tool
To run your customized pipeline, execute the following command (replace `./data/model_design.txt` with the path to your design file):
```bash
python run_virus.py --model_design ./data/model_design.txt
```

Get help and explore additional command-line parameters:
```bash
python run_virus.py -h
```

---

## 📝 Model Design File Configuration

VIRUS requires a plain-text, **tab-separated (TSV)** model design file describing the measured phenotypes and how they relate to the underlying additive (biophysical) traits. 

The design file must contain the following 4 columns:

| Column | Description | Example / Supported Values |
| :--- | :--- | :--- |
| **trait** | One or more additive trait names | `binding_trait`, `cell entry_trait` |
| **transformation** | The shape of the global epistatic trend | `Linear`, `ReLU`, `SiLU`, `Sigmoid`, `SumOfSigmoids`, `TwoStateFractionFolded`, `ThreeStateFractionBound` |
| **phenotype** | The observed phenotype | `Binding`, `Cell entry`, `Antibody escape` |
| **file** | Path to the corresponding input dataset | `data/your_input_data.csv` |

*(See `./data/model_design.txt` for a concrete example).*

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🐛 Bugs and Feedback

If you encounter any issues or have feedback:
* Feel free to open an **[Issue](https://github.com/your-username/DeepVirus/issues)** on GitHub.
* Alternatively, you can contact the authors directly via email at: 📧 [dengym61@163.com](mailto:dengym61@163.com)
