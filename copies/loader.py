import os
import pandas as pd

class CorpusLoader:
    """
    A class which loads all text files in a folder calling the DataLoader() class.

    For more info on the return type, see the README.

        Parameters:
            folder(string): Filepath for the folder with texts to be loaded

        Returns:
            corpus_dict(dict): Nested dict comprising a corpus ID, and the doc ID, raw text, and tokenized text
    """
    def __init__(self, data_path): #<- something goes here
        # initialization parameters - read the doc string above
        self.data_path = data_path

    def _get_values(self, data_path):# <- something goes here
        """
        A private method that can only be called by the class itself, not from outside the class.

        Private methods are indicated by the use of a leading underscore.
        
        Parameters:
        filepath(string): A filepath for an individual text to be loaded and parsed

        Returns:
            vals(dict): Dict comprising a doc ID, raw text, and tokenized text
        """
        # load data with pandas
        # hint: check out pd.read_fwf

        text = pd.read_fwf(data_path)

        # using pandas methods to split all strings
        # removing unnessecary columns
        raw = text.iloc[:, 0] # something goes in here

        # return a dictionary of values
        vals = {} # something goes in here
        # create a counter for looping over all split data
        i = 0 
        # for every entry in the split dataframe
        for row in raw:
            sentence = {}
            # get the original data as a str from the dataframe
            sentence['raw'] = row # something goes in here
            # create a dictionary entry with the raw data and split data
            sentence['split'] = row.split() # something goes in here
            vals[i] = sentence
            # increment by 1
            i += 1
        return vals

    def show_values(self, data_path): # <- something goes in here:
        """
        A public method which loads all text files and parses them using the _get_values() method above.

        Note no leading underscore, so this is a public method.

            Parameters:
                folder(string): Filepath for the folder with texts to be loaded

            Returns:
                corpus_dict(dict): Nested dict comprising a corpus ID, and the doc ID, raw text, and tokenized text
        """
        # intialise empty dictionary
        corpus_dict = {}
        # get a sorted list of all files in the folder 
        input_dir = os.listdir(self.data_path) # something goes here
        # intialise counter at 0
        i = 0
        # for every file in the specific folder
        for filename in input_dir:
            # return a dictionary of values like above
            # this means calling the _get_values(folder + filename)
            # how to use a private method in a class? 
            # This might help - https://www.geeksforgeeks.org/private-methods-in-python/
            text_file = filename
            text_data_path = os.path.join(data_path, text_file)
            vals = self._get_values(text_data_path)
            # append to dict
            corpus_dict[i] = vals# something goes here
            # increment counter
            i += 1
        # when finished, return complete dictionary
        return corpus_dict

if __name__=="__main__":
    CorpusLoader()
    # if called from the command line, nothing should happen