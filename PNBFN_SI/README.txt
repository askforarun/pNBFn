Execute the following command from PNBFN_SI folder to build box of polymers. 
./scripts/create_polymersystems.sh

The script will create five folders, PNBF0, PNBF4, PNBF6, PNBF8, PNBF10. Each folder will contain three subfolders named replica_1, replica_2, replica_3. After running the script, the ouput will be PNBbox.gro. Please note modef suite must be installed before running this script. 
The recipe for building the polymer chain, PNBFN.py is in PNBFN_SI/mol2_ff_files 

