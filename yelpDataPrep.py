import io
import pandas as pd
import json
from pandas.io.json import json_normalize
from flatten_json import flatten

#import h2o
import pan
#h2o.init()
yelpList=[]

with open("yelp_academic_dataset_business.json") as df:
    for dic in df:
        yelpList.append((json.loads(dic)))
print(len(yelpList))
print(yelpList[0].keys()  )


def customFlatten(row):
    for value in row.values()

        if isinstance(value, dict)
            customFlatten()(value)

        return value




firstRow = flatten(yelpList[0])

print(firstRow)
features=[]
for dic in yelpList:
    if dic.get("review_count") > 650 and dic.get("stars") >= 4:
        rowString = ''

        for value in dic.values():
            rowString += str(value) + ','

        features.append(rowString);


print(features)

print(len(features))


#
# features = []
# for dic in yelpList:
#     if dic.get("review_count") > 650 and dic.get("stars") >= 4:
#         varReviewCount =import io
# import json
# from pandas.io.json import json_normalize
# from flatten_json import flatten
#
# #import h2o
# import pandas as pd
# #h2o.init()
# yelpList=[]
#
# with open("yelp_academic_dataset_business.json") as df:
#     for dic in df:
#         yelpList.append((json.loads(dic)))
# print(len(yelpList))
# print(yelpList[0].keys()  )
#
#
# def customFlatten(row):
#     for value in row.values()
#
#         if isinstance(value, dict)
#             customFlatten()(value)
#
#         return value
#
#
#
#
# firstRow = flatten(yelpList[0])
#
# print(firstRow)
# features=[]
# for dic in yelpList:
#     if dic.get("review_count") > 650 and dic.get("stars") >= 4:
#         rowString = ''
#
#         for value in dic.values():
#             rowString += str(value) + ','
#
#         features.append(rowString);
#
#
# print(features)
#
# print(len(features))
#
#
# #
# # features = []
# # for dic in yelpList:
# #     if dic.get("review_count") > 650 and dic.get("stars") >= 4:
# #         varReviewCount = dic.get("review_count")
# #         name = dic.get("name")
# #         #id = dic.get("business_id")
# #         state = dic.get("state")
# #         zipCode = dic.get("postal_code")
# #         category = dic.get("categories")
# #         noiseLevel = dic.get("NoiseLevel")
# #         attire = dic.get("RestaurantsAttire")
# #         rating = dic.get("stars")
# #         features.append(str(id)+","
# #                         +str(name)+","
# #                         +str(rating)+","
# #                         +str(varReviewCount)+","
# #                         +str(state)+","
# #                         +str(category)+","
# #                         +str(attire)+","
# #                         +str(noiseLevel)+","
# #                         +str(zipCode))
#
# #print(yelpList[0])
#
#
# #print(goodStore)
#
#
#
# #transform the string to dictionary format
# #df3 = json.loads(df1)
# #print(df3)
# #turn the dictionary into list type
#
#
#
#
#
# #for line in df:
#         #print(line)
#
#
#
#
# #from pandas.io.json import json_normalize dic.get("review_count")
#         name = dic.get("name")
#         #id = dic.get("business_id")
#         state = dic.get("state")
#         zipCode = dic.get("postal_code")
#         category = dic.get("categories")
#         noiseLevel = dic.get("NoiseLevel")
#         attire = dic.get("RestaurantsAttire")
#         rating = dic.get("stars")
#         features.append(str(id)+","
#                         +str(name)+","
#                         +str(rating)+","
#                         +str(varReviewCount)+","
#                         +str(state)+","
#                         +str(category)+","
#                         +str(attire)+","
#                         +str(noiseLevel)+","
#                         +str(zipCode))

#print(yelpList[0])


#print(goodStore)



#transform the string to dictionary format
#df3 = json.loads(df1)
#print(df3)
#turn the dictionary into list type





#for line in df:
        #print(line)




#from pandas.io.json import json_normalize

