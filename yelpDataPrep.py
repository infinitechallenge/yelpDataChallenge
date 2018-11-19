import io
import json


#####################
# HELPER FUNCTIONS
#####################

# Read Json Function: Return list as an array
def readJsonFile(fileName, limit = None):
    data = []
    i = 0
    with open(fileName) as f:
        for row in f:
            if ( limit != None and  i >= limit ):
                break
            data.append(json.loads(row))
            i += 1
    return data


# Recursive function
def flattenRow(row):
    tranformedRow = {}

    def flatten(x, name=''): #flatten("False","attributes_BikeParking_" )
        if type(x) is dict:
            for key in x:
                flatten(x[key], name + key + '_')
                #flatten("False","attributes_BikeParking_")
                #flatten(x[attributes])
                #x[attributes] -> {}> 
                #({a:b,c:d,...,z:x}, '' + "attributes" + "_")
        # Take care of different type here:
        # elif type(x) is list:
        #     i = 0
        #     for a in x:
        #         flatten(a, name + str(i) + '_')
        #         i += 1
        else:
            tranformedRow[name[:-1]] = x 
            # tranformedRow["business_id"] = "Apn5Q_b6Nz61Tq4XzPdf9A"
            # transformedRow[attributes_BikeParking] = "False"
            # "attributes_BikeParking":"False"

    flatten(row)
    return tranformedRow



######################
# SCRIPT STARTS HERE
######################

data = readJsonFile("./data/yelp_academic_dataset_business.json", 100)


####################################
# DATA TRANSFORMATION LOOP STARTS HERE
####################################

newData = []
# Loop through the list
for row in data:

    convertedRow = {}

    flattenedRow = flattenRow(row)

    # Loop through column
    for key in flattenedRow.keys():
        # value
        value = row.get(key)

        # Column Name: key
        # Value: value

        # Assign key to value
        convertedRow[key] = value 

        ############
        # DATA TRANSFORMATION EXAMPLE
        ############
        #
        # if key === "stars":
        #   if value > 3
        #       convertedRow[isGoodEnough] = True
        #   else:
        #       convertedRow[isGoodEnough] = False
        #

    newData.append(convertedRow)

# PRINT CONVERTED DATA
#print(newData)



########################################
# EXPORT NEW DATA INTO OTHER FORM HERE
#######################################
# csvList = []
# for row in newData:
#    csvForm = ''
#    for key in row.keys():
#       value = row.get(key)
#       csvForm += value ','
#
#   csvList.append(csvForm)






