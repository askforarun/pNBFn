#!/bin/bash
system=(PNBF0 PNBF4 PNBF6 PNBF8 PNBF10)
replica=(replica_1 replica_2 replica_3)


cwd=$(pwd)

for i in "${system[@]}"
do
echo $cwd
(cd $cwd && mkdir $i  )
for j in "${replica[@]}"
do
echo $cwd/$i
echo $j
(cd $cwd/$i && mkdir $j  )
done
done

