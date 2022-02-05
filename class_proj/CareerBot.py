import pandas as pd



def read_file(path):
    with open(path) as file:
        df = pd.read_csv(file)
        df = df[['Major', 'Major_Category']]        
    return df

def to_dict(df):
    return dict(zip(df.Major.str.lower(), df.Major_Category.str.lower()))

def ask_user():
    return input('Field of study? : ')


def check_major(val, data):
    temp = []
    for k, v in data.items():
        if val == v:
            temp.append(k)    
    if len(temp) > 0:
        temp.sort()
        print("\n\nHere are some of our suggestion base on your interest: ")
        for e,i in enumerate(temp):
            print('\n', f"{e}. {i.upper()}")
    else:
        print('Nothing')
        
            

if __name__ == "__main__":
    
    path = 'majors-list.csv'

    df = read_file(path)
    
    database = to_dict(df)
    
    while True:
        val = input("Need help? ")    
        
        if val == "yes":
            val = input('Field of interest? ').lower()
            check_major(val, database)
            break
        elif val == 'no':
            break
        else:
            print('\nInvalid answer!\n\nType no to Exit\n')
            

    
    
    
    

