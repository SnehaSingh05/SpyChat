
from datetime import datetime
class Spy:

    def __init__(own, name, salutation, age, rating, marital):
        own.name = name
        own.salutation = salutation
        own.age = age
        own.rating = rating
        own.marital = marital
        own.is_online = True
        own.chats = []
        own.current_status_message = None


# ChatMessage class contains all chat related info.
class ChatMessage:

    def __init__(own, message, sent_by_me, avg, sender):
        own.message = message
        own.time = datetime.now()
        own.sent_by_me = sent_by_me
        own.avg = avg
        own.sender = sender

# Spy class has been initialized with some values.
spy = Spy('Satyam', 'Mr.', 21, 3.4, 'Not Married')

# Few friends pre-added
friend_one = Spy('Eakansh', 'Mr.', 15, 3.5, 'Not Married')
friend_two = Spy('Sankriti', 'Ms.', 16, 3.7, 'Married')
friend_three = Spy('Sanskar', 'Mr.', 18, 3.9, 'Married')

# Friends list contains 3 friends.
friends = [friend_one, friend_two, friend_three]
