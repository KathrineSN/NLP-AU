python3 -m pip install --upgrade pip
python3 -m pip install pandas # note -m is the short name for module

python3 src/test.py --name $1 --age $2

# run this with:  bash src/run.sh Kathrine 23
# best practice is to always have the bash script at the top level