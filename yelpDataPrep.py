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


def flattenRow(row):
    flattenRow = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        # Take care of different type here:
        # elif type(x) is list:
        #     i = 0
        #     for a in x:
        #         flatten(a, name + str(i) + '_')
        #         i += 1
        else:
            flattenRow[name[:-1]] = x

    flatten(row)
    return flattenRow



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
    # Loop through column
    for key in row.keys():

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






