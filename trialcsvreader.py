import csv

with open('data.csv', newline='') as d:
    reader = csv.reader(d, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id = int(row[0])
        country_name = row[1]
        city_name = row[2]
        gender = row[3]
        ethnicity_name = row[4]
        animal_type = row[5]
        animals = row[6]
        humans = row[7]
        is_required = row[8]
        last_updated_date = row[9]
    
    print("Done!")
d.close()