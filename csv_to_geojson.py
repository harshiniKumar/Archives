#Insert this method in your python file and send the csv file as argument.
#The GeoJSON will be generated in the same path as CSV
def CsvToJSON(path):
    print('Generating GEOJSON')
    
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        #Fields that your CSV contains
        fields=['Ships','Geometry','X co-ordinate','Y co-ordinate','Latitude','Longitude','Width','Length','Style']

        with open('Final.csv', 'w', newline='') as csvfile2:
            spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            next(csvfile)
            next(csvfile)
            spamwriter.writerow(fields)
            for rows in spamreader:
                spamwriter.writerow(rows)
    with open('input.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
                writer.writerow(row)
                
    os.system('cmd /c "csvjson --lat Latitude --lon Longitude --k Ships --crs EPSG:4269 --indent 4 output.csv > output.json"')
