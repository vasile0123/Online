import pandas as pd

def token(row):
    '''    
    Helper function to split C1 and take the first word --- organiztion--- and last word --country--
    Not all countries may be extracted correctly (e.g. USA), but Canada is.
    Args: 
        row of the dataset
    '''
    if pd.isna(row['C1']):
        return None    
    else:
        #C1 column intricacies
        x = row['C1'].split("; [")        
        y2=[z[z.find(']')+2:] for z in x]
        y3=[z.split(", ") for z in y2]        
        return [list(map(z.__getitem__, (0, len(z)-1))) for z in y3]             


def token_country(row):
    '''
    Helper function to extract the list of countries. 
    Args:
        row of the dataset
    '''
    return None if not row['token'] else [ z[1] for z in row['token']]   
    

def inter_collab(row):
    '''
    Helper function to determine whether the publication is internationl collaboration. 
    Args:
        row of the dataset
    '''
    return None if not row['token_country'] else any(z !="Canada" and z !="Canada;" for z in row['token_country'])



