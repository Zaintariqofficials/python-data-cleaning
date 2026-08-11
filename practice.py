import json

#load file 
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data

data=load_data("customers(1).json")


#clean data
def clean_data(data):
    clean_data=[]
    unique_users=set()   

    #clean the rating part
    text_to_num={"one":1 , "two":2 ,"three":3 ,"four":4 ,"five":5}

    for user in data:
        raw_rating=user["rating"].strip().lower()

        if raw_rating in text_to_num:
            raw_rating=text_to_num[raw_rating]
            user["rating"]=raw_rating

        #handling missing values
        raw_age=user.get("age")
        if (raw_age==" "):
            user["age"]=None

        #deduplication part
        if(user["name"].strip() in unique_users):
            continue

        unique_users.add(user["name"].strip())   
        clean_data.append(user)

    return clean_data


clean_data(data)