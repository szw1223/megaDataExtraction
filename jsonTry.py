import json

data = {}
data['url'] = "https://answers.yahoo.com/question/index?qid=20180716022759AA7khh2"
data['question'] =  'My neck always cracks when I move it and it hurts so bad and it has been for months and a chiropractor adjusted it but it didnt do anything?'
data["question_content"] = 'none'
data["question_timestamp"] = '20180716022759'
data["followers"] = 0
data["number_of_answers"] = 2
data["categories"] = [" Health"," General Health Care"," Pain & Pain Management"]
data["answers"] = [{
    "answer_content":" Talk to your doctor about seeing a physical therapist ",
    "author_link":"https://answers.yahoo.com/activity/questions?show=WI2YP67BGBOQVXVOTMOMODMNTU&t=g",
    "author_name":"Patricia",
    "best":"true",
    "dislikes":'0',
    "likes":'0',
    "timestamp":"7/16/2018 2:37:30 AM UTC-4"},{
    "answer_content":" See a real doctor.",
    "author_link":"https://answers.yahoo.com/activity/questions?show=5MPNZ6HATCREEOFGKQZBKDRCPA&t=g",
    "author_name":"Mike G",
    "best":'false',
    "dislikes":'0',
    "likes":'0',
    "timestamp":"7/15/2018 11:24:08 PM UTC-4"}]
data['authorInfor'] = "none"
data["last_updata_data"] = "now"



with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
