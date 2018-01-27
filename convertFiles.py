import csv
import time
import os
import moveFiles
import renameFiles
import pycountry

path = os.getcwd()
DHL_export = path + '\\DHL_export\\'
dir_src = path + os.path.join('\\DEAR_import\\')

def checkCsvFiles():
    for root,dirs,files in os.walk(dir_src):
        for file in files:
           if file.endswith(".csv"):
               #printfile
            readFiles(file)

def readFiles(dear_files):
    #print(dear_files)
    with open(dir_src + dear_files) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')


        for row in readCSV:
            recordType = row[0]
            Customer = row[1]
            Contact = row[15]
            Address1 = row[29]
            Address2 = row[30]
            Address3 = row[32]
            City = row[31]
            PostCode = row[33]
            Phone = row[16]
            DeclaredValue = row[43]
            Weight = row[44]
            Pieces = row[45]
            Ref  = row[2]
            Contents = row[46]
            CountryCode = row[34]
            ProdCode = row[47]
            Incoterm = ''
            eMailAlert = ''
            emailaddress = row[17]



            if ',' in City:
                #print('There is a comma')
                City = City.replace(',','')

            if recordType == 'invoice':
                timestr = time.strftime("%Y%m%d-%H%M%S")
                text_file = open(DHL_export + timestr + '_exportDHL.txt', 'a')

                #Convert the contry to an alpha 2 code
            if CountryCode == "ShippingCountry*":
                continue

            if len(CountryCode) > 2:
                CodeAlpha = pycountry.countries.get(name=CountryCode).alpha_2

                #Add the details to the new CSV.txt file

                companyDetail = (Customer + ';' + Address1 + ';' + Address2 + ';' + City + ';' + \
                                    Address3 + ';'+ PostCode + ';'+ Contact + ';'+ Phone + ';' + \
                                    DeclaredValue + ';'+ Weight + ';'+ Pieces +  ';'+ Ref + ';'+ \
                                    Contents + ';'+ CountryCode + ';'+ CodeAlpha + ';' + ProdCode + ';'+ Incoterm + \
                                    ';'+ eMailAlert + ';'+ emailaddress + '\n')

                text_file.write(companyDetail)
                #text_file.close()


checkCsvFiles()
moveFiles.moveFiles()
renameFiles.renameFile()
