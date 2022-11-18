
import argparse
import pandas as pd

def arg_inputs():    
    # initialize parser
    my_parser = argparse.ArgumentParser(description="A script that says hello.")

    # add arguments (-n is short name, --n is long name)
    my_parser.add_argument("-n",
                            "--name",
                            type = str,
                            required=True,
                            help = "The name to say hello.")
                            
    my_parser.add_argument("-a",
                            "--age",
                            type = int,
                            required=True,
                            help = "The age of the person.")

    # the list of arguments given
    args = my_parser.parse_args()

    return args

def hello(name:str) -> str:
    print(f"hello, my name is {name}!")

def person_info(name:str, age:int) -> pd.DataFrame:
    df = pd.DataFrame([[name, age]], columns=["name", "age"])
    print(df)

def main():
    # get the command line arguments
    arguments = arg_inputs()
    #hello(arguments.name) 
    # print the hello function
    person_info(arguments.name, arguments.age)

if __name__ == "__main__":
    # this means that this runs if this script is explicitly run from the command line
    main()

# Run script in command line
#python3 test.py --name Kathrinex

# Easy way to run your script and parse arguments to your scripts

