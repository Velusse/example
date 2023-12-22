import csv

def read_csv(path):
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data=[]
        for row in reader:
            row_with_header=zip(header,row)
            dictionary_by_country={ key: value for key,value in row_with_header }
            data.append(dictionary_by_country)
        return data
            
        
            


if __name__=="__main__":
    data=read_csv("C:\\Users\EQUIPO\OneDrive\Escritorio\Python\ManejoCSV\data_population.csv") 
    print(data)