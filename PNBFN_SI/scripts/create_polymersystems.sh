#!/bin/bash

system=(PNBF0 PNBF4 PNBF6 PNBF8 PNBF10)
nmol=(60 32 27 23 21)
replica=(replica_1 replica_2 replica_3)



ff_file_name=oplsaa_mod.xml
cwd=$(pwd)
path_ff=$cwd/mol2_ff_files/$ff_file_name
k=0
for i in "${system[@]}"
do
path_mol2=$(echo $cwd/mol2_ff_files/$i.mol2)
echo ${nmol[k]}  
for j in "${replica[@]}"
do
(cd $cwd/$i/$j &&  cp -v $cwd/mol2_ff_files/PNBFN.py .)
(cd $cwd/$i/$j &&  cp -v $cwd/scripts/packbox.sh .)
(cd $cwd/$i/$j &&  cp -v $cwd/scripts/packbox.py .)
(cd $cwd/$i/$j &&  cp -v $cwd/scripts/topology.top .)
(cd $cwd/$i/$j &&  cp -v $cwd/mdpfiles/* .)
(cd $cwd/$i/$j &&  rm -v PNBbox.gro)
(cd $cwd/$i/$j &&  ./packbox.sh $path_mol2 $path_ff ${nmol[k]})
exit 130
done
((k++))
done

