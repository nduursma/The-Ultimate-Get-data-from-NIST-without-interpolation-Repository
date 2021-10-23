# The Ultimate 'Get data from NIST/JANAF without interpolation' Repository

This repository contains the code to obtain thermochemical data from NIST and JANAF. The Python code does the database searching and interpolation for you, easy! 
## Installation

Open Anaconda prompt and clone this repository.
```bash
 git clone -c core.longpaths=true https://github.com/nduursma/The-Ultimate-Get-data-from-NIST-without-interpolation-Repository
```
Change your working directory.
```bash
cd The-Ultimate-Get-data-from-NIST-without-interpolation-Repository
```

Create a new environment.
```bash
conda env create -f TRP.yml

```

Activate the environment and open the file "get_data.py" in Spyder.
```bash
conda activate TRP
spyder get_data.py
```

Enter your temperature, the molecular formula, and the phase in the code.

![The datafields.](https://github.com/nduursma/The-Ultimate-Get-data-from-NIST-without-interpolation-Repository/blob/main/enterdata.PNG)

If you do not know what molecular formula or phase to select, you can search for molecules by entering a part/ some atoms in the 'formula_' variable, and run the code to see what options are available. Note that the JANAF formula for 'OH' is specified as 'HO'.

![Find the right formula and phase.](https://github.com/nduursma/The-Ultimate-Get-data-from-NIST-without-interpolation-Repository/blob/main/formulatable.PNG)

After choosing the right molecular formula and phase, you will find the thermochemical properties.

![Output of the thermochemical properties.](https://github.com/nduursma/The-Ultimate-Get-data-from-NIST-without-interpolation-Repository/blob/main/output.PNG)



```diff
-                                                GOOD LUCK!!                                             - 
-                                           Made by Nadine Duursma                                       - 
+                           Created for the course AE4S01 Thermal Rocket Propulsion                      +
+                                Delft University of Technology, The Netherlands                         +
``` 
#### References
+ JANAF: https://janaf.nist.gov/ 
+ The thermochem library: https://github.com/adelq/thermochem

