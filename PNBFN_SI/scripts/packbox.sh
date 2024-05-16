#!/bin/bash
python PNBFN.py "$1" "$2"
nmol="$3"
sed -n '/moleculetype/q;p' PNB.top > forcefield.itp
sed '/moleculetype/,$!d' PNB.top > PNB.itp
sed -n -i '/system/q;p' PNB.itp 

gmx editconf -f PNB.pdb -o PNB.gro -bt triclinic -box 50 50 50 -angles 90 90 90
gmx grompp -f minim.mdp -c PNB.gro  -p PNB.top -o em.tpr -r PNB.gro
gmx mdrun -v -deffnm em

gmx editconf -f em.gro -o PNB.pdb

python packbox.py $nmol  $RANDOM

sed  "s/nmol/$nmol/g" topology.top > topol.top
gmx editconf -f PNBbox.pdb -o PNBbox.gro 
gmx grompp -f minim.mdp -c PNBbox.gro  -p topol.top -o em.tpr -r PNBbox.gro
