# The Ulitmate 'Get data from NIST/JANAF without interpolation' Repository

This repository contains the code to obtain thermochemical data from NIST and JANAF. The Python code does the database searching and interpolation, so you do not need to do it yourself anymore :).

## Installation

Clone this repository.
```bash
 git clone -c core.longpaths=true https://github.com/nduursma/The-Ulitmate-Get-data-from-NIST-without-interpolation-Repository
```
Change your working directory.
```bash
cd The-Ulitmate-Get-data-from-NIST-without-interpolation-Repository
```

Create a new environment and activate it.
```bash
conda env create -f TRP.yml
conda activate TRP
```

Open the file "get_data.py", run the following command if you prefer to use Spyder.
```bash
spyder get_data.py
```

Enter your temperature, the molecular formula, and the phase in the code.