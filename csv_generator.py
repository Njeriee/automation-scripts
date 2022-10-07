import csv

# fist sotre the data in a list
data = [['whitman',38],['carl',42],['james',45],['simon',76]]

# open the file in wite mode
with open('names.csv','w') as names_csv:
    # call the writer method from the csv module
    # include writenamrow which writes one row at a time and writerows which writes may rows alltogether
    writer = csv.writer(names_csv)
    writer.writerows(data)

# using a dictionary to write a csv

# first the list of dictionaries
users = [{'name':'carl','username':'carl22','department':'IT'},{'name':'Moh','username':'mo1','department':'sales'},{'name':'nancy','username':'nancy-1','department':'IT'},{'name':'otieno','username':'otis','department':'frontoffice'}]

# specify the keys which will be used as row headers in the csv file
keys = ['name','username','department']
with open('departments.csv','w') as deps:
    writer = csv.DictWriter(deps, fieldnames= keys)
   
    # now create the row header
    writer.writeheader()
    
    # now populate the csv
    writer.writerows(users)

# reading csv file as a dictionary
# Dictreader method is used which lets one access the values using the column names in the header row
# dictreader turns each entry/row in the csv file into a dictionary
with open('departments.csv') as deps:
    reader = csv.DictReader(deps)
    for row in reader:
        print('{} is in {} department'.format(row['name'],row['department'])) 
