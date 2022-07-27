import praw
import os
import json


def reddit(username, password, subreddit, limit):
    reddit_instance = praw.Reddit(client_id="rICByAUUdVJLgsjvNX4_OQ", 
                                client_secret="JRPtEpMBirmFCivVAEMOpkqIjnlGdA",
                                username=username,
                                password=password,
                                user_agent="Stargate Reddit")
    

    random_subreddit = reddit_instance.subreddit(f"{subreddit}")

    subreddit = subreddit.upper()

    print(f"{subreddit}\n\n")

    for submission in random_subreddit.hot(limit=limit):
        print(f"TITLE: {submission.title}\nURL: {submission.url}\n")




if __name__ == "__main__":
    print("STARGATE REDDIT READER")
    print("----------------------\n\n")

    if os.listdir().__contains__("data.json"):
        with open("data.json", "r") as f:
            data = json.load(f)     
            username = data["username"]
            password = data["password"]
            subreddit = data["subreddit"]
            limit = data["limit"]

        reddit(username, password, subreddit, int(limit))
        
        

    else:
        username = input("Enter your Reddit username: ")
        password = input("Enter your Reddit password: ")
        subreddit = input("Enter a subreddit name: ")
        limit = input("Enter a limit: ")
        save = input("Would you like to save this information, for next time? (y/n): ")

        if save == "y":
            with open("data.json", "w") as f:
                json.dump({"username": username, "password": password, "subreddit": subreddit, "limit": int(limit)}, f)
            
        reddit(username, password, subreddit, int(limit))
