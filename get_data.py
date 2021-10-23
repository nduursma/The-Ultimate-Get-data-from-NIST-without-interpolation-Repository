"""
Created on Sat Oct 23 15:02:26 2021

@author: nadin
"""
from tabulate import tabulate

# =================================================================================================================
# Enter your data here
# =================================================================================================================

T = 3500;                # Reaction temperature [K]
formula_ = 'H2O'         # Molecule, find by running the file and printing the options
phase_ = 'g'             # Phase, choose from 'cr', 'l', 'cr,l', 'g', 'ref', 'cd', 'fl', 'am', 'vit', 'mon', 'pol', 'sln', 'aq', 'sat'
show_options = True      # Print the formulas in the data base to choose from

# ================================================================================================================= 
# Constants
# ================================================================================================================= 
 
R = 8.314472            #  Universal gas constant R 
Tr = 298.15             # Reference temp [K]

# ================================================================================================================= 
# Code
# ================================================================================================================= 
 
if 'db' not in globals():
    from thermochem.janaf import Janafdb
    db = Janafdb()


if show_options == True:
    options = db.search(formula_)
    print(options)


p = db.getphasedata(formula=formula_, phase=phase_)
# p = db.getphasedata(formula=formula_, name = name_, phase=phase_)

# ================================================================================================================= 
# Print the results
# ================================================================================================================= 

print('\n ======================================================================================')
print('\n ---------------------- Properties of', formula_, 'at', T, '[K] ---------------------------------')
print('\n ====================================================================================== \n')

l1 = ['Enthalpy','H(T)-H(Tr)', p.hef(T), '[kJ/mol]']
l2 = ['Heat capacity','C_p', p.cp(T), '[J/mol/K]']
l3 = ['Enthalpy of formation','DeltaH', p.DeltaH(Tr), '[kJ/mol]']
l4 = ['Equilibrium constant', 'K_p', 10**(p.logKf(T)), '[-]']
l5 = ['Entropy', 'S', p.S(T), '[J/mol/K]']
                           
L = [l1, l2, l3, l4, l5]

headers_ = ['Property', 'Symbol', 'Value', 'Unit']

print(tabulate(L, headers=headers_))









