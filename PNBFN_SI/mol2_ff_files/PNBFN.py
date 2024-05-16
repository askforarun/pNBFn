import warnings 
warnings.filterwarnings("ignore")
import foyer
from foyer import Forcefield
import os as os
import sys

import mbuild as mb 
from mbuild.lib.moieties.ch2 import CH2
from mbuild.lib.recipes import Polymer

path_mol2=str(sys.argv[1])
path_ff = str(sys.argv[2])




print(path_mol2)
print(path_ff)

name_mol2=path_mol2.split("/")

monomer = mb.load(path_mol2)
monomer.box=None

#print(type(name_mol2[-1]))
#sys.exit("Error message")

if  name_mol2[-1]=="PNBF0.mol2":
    print(type(name_mol2[-1]))
 




    c_to_remove = [
        monomer[14], 
        monomer[15],
    ]
    h_to_remove = [
        monomer[34], 
        monomer[35], 
        monomer[36], 
        monomer[37],
    ]


    for particle in c_to_remove + h_to_remove:
        monomer.remove(particle)
    print(monomer.all_ports())

    monomer.labels["up"] = monomer['Compound[0]']['port[1]']
    monomer.labels["down"] = monomer['Compound[0]']['port[7]']

    monomer["up"].update_separation(0.07)
    monomer["down"].update_separation(0.07)

    ch2 = CH2()
    ch2.remove(ch2["down"])

    polymer = Polymer(
    monomers=[monomer], 
    end_groups=[mb.clone(ch2), mb.clone(ch2)]
    )



else:

   


    c_to_remove = [
    monomer[20], 
    monomer[21],
    ]
    h_to_remove = [
    monomer[52], 
    monomer[53], 
    monomer[54], 
    monomer[55],
    ]


    


    for particle in c_to_remove + h_to_remove:
        monomer.remove(particle)
    print(monomer.all_ports())

    monomer.labels["up"] = monomer['Compound[0]']['port[1]']
    monomer.labels["down"] = monomer['Compound[0]']['port[7]']

    monomer["up"].update_separation(0.07)
    monomer["down"].update_separation(0.07)

    ch2 = CH2()
    ch2.remove(ch2["down"])

    polymer = Polymer(
    monomers=[monomer], 
    end_groups=[mb.clone(ch2), mb.clone(ch2)]
    )


polymer.build(n=15)
oplsaa  =  Forcefield(forcefield_files=path_ff)
top = oplsaa.apply(polymer)
top.save("PNB.pdb", overwrite=True)
top.save("PNB.top", overwrite=True)
monomer = mb.load("PNB.pdb")
print(monomer.mass)

