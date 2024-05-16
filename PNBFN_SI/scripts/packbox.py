import mbuild as mb
import sys
monomer = mb.load("PNB.pdb")
monomer.box=None
seed=sys.argv[2]
n=int(sys.argv[1])
density=40
box=mb.fill_box([monomer], n_compounds=n, density=density , overlap=0.2,seed=seed)
box.save("PNBbox.pdb", overwrite= True)
