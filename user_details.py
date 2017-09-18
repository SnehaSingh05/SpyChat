# To access Steganography library.
from steganography.steganography import Steganography
# All basic class and list is imported from spy_info file.
from spyinfo import spy, Spy, ChatMessage, friends
# randint function has been imported from random library
from random import randint
# Regular expression module
import re
from time import sleep
from time import strftime
from termcolor import colored
import datetime

print('Hi there!')
patternm = '^[Male|MALE|M|m|male]'
patternf = '^[Female|FEMALE|F|f|female]'
patterno = '^(OTHER|other|others|OTHERS)'

def add_spy():
    print('Enter Your gender:-')
    while True:
        gender = input('Male or Female or Others:')
        if re.match(patternm, gender) is not None:
            while True:
                spy.name =input("Enter your name:")
                pattern = '^[a-zA-Z\s]+$'
                if re.match(pattern, spy.name) is not None:
                    print('')
                    sleep(0.5)
                    print('I am a Spy')
                    print('Just for folks!!!\n')
                    break
                else:
                    print('Enter alphabets only.')
            while True:
                marital = input('Mr.or Master.:')
                pattern = '^(Mr.|Master.|MR.|MASTER.|mr.|master.)+$'
                if re.match(pattern, marital)is not None:
                    print('Welcome,')
                    break
                else:
                    print('Enter Mr. or Master. only.')
            if marital.upper() == 'MR.':
                    spy.salutation = 'Mr.'
                    spy.marital = 'Married'
                    print(spy.salutation + spy.name)
            else:
                    spy.marital = 'Not Married'
                    spy.salutation = 'Master.'
                    print(spy.salutation + spy.name)
            print('\nAlright,I would like to know a little more about you...')
            while True:
                 spy.age = input('Enter you age:')
                 pattern = '^[0-9]+$'
                 if re.match(pattern, spy.age) is not None:
                     break
                 else:
                     print('Enter numerals only.')
            year = datetime.date.today().year - int(spy.age)
            print('So lemme guess...')
            sleep(1)
            print('You were born in:', year)
            if int(spy.age) < 100:
                old = 100 + int(year)
                print('You will be 100 years old in:', old)
            else:
                old = 100 + int(year)
                print('You were 100 years older in:', old)
            while True:
                spy.rating = input('Enter your spy rating:')
                pattern = '^[0-9]+\.[0-9]+$'
                if re.match(pattern, spy.rating) is not None:
                    spy.rating = float(spy.rating)
                    break
                else:
                    print('Enter floating values.')
            print('Let\'s get started...')
            print('Here\'s your profile Sir:-\n')
            show_profile()
            start_chat()

        elif re.match(patternf, gender) is not None:
            while True:
                spy.name = input("Enter your name:")
                pattern = '^[a-zA-Z\s]+$'
                if re.match(pattern, spy.name) is not None:
                    print('')
                    sleep(0.5)
                    print('I am a Spy \n')
                    break
                else:
                    print('Enter alphabets only.')
            while True:
                marital = input('Miss.or Mrs.:')
                pattern = '^(Miss.|Mrs.|MISS.|MRS.|miss.|mrs.)+$'
                if re.match(pattern, marital) is not None:
                    print('Welcome,')
                    break
                else:
                    print('Enter Miss. or Mrs. only.')
            if marital.upper() == 'MRS.':
                spy.salutation = 'Mrs.'
                spy.marital = 'Married'
                print(spy.salutation + spy.name)
            else:
                spy.marital = 'Not Married'
                spy.salutation = 'Miss.'
                print(spy.salutation + spy.name)
            print('\nAlright,I would like to know a little more about you...')
            while True:
                spy.age = input('Enter you age:')
                pattern = '^[0-9]+$'
                if re.match(pattern, spy.age) is not None:
                    break
                else:
                    print('Enter numerals only.')
                year = datetime.date.today().year - int(spy.age)
                print('So lemme guess...')
                sleep(1)
                print('You were born in:', year)
                if int(spy.age) < 100:
                    old = 100 + int(year)
                    print('You will be 100 years old in:', old)
                else:
                    old = 100 + int(year)
                    print('You were 100 years older in:', old)
            while True:
                spy.rating = input('Enter your spy rating:')
                pattern = '^[0-9]+\.[0-9]+$'
                if re.match(pattern, spy.rating) is not None:
                    spy.rating = float(spy.rating)
                    break
                else:
                    print('Enter floating values.')
            print('Let\'s get started...')
            print('Here\'s your profile Mam:-\n')
            show_profile()
            start_chat()

        elif re.match(patterno, gender):
            print('Sorry! I can\'t help you out... It\'s a mystery you\'ve landed into\!')
            sleep(2.1)
            print('Just joking!!!')
            spy.salutation = ''
            spy.marital = 'Not Known'
            while True:
                spy.name = input('Enter your name:')
                pattern = '^[a-zA-z\s]+$'
                if re.match(pattern, spy.name) is not None:
                    break
                else:
                    print('Enter alphabets only.')
            print('Welcome,')
            print(spy.name)
            print('\nAlright,I would like to know a little more about you...')
            while True:
                spy.age = input('Enter you age:')
                pattern = '^[0-9]+$'
                if re.match(pattern, spy.age) is not None:
                    break
                else:
                    print('Enter numerals only.')
            year = datetime.date.today().year - int(spy.age)
            print('So lemme guess...')
            sleep(1)
            print('You were born in:', year)
            if int(spy.age) < 100:
                old = 100 + int(year)
                print('You will be 100 years old in:', old)
            else:
                old = 100 + int(year)
                print('You were 100 years older in:', old)
            while True:
                spy.rating = input('Enter your spy rating:')
                pattern = '^[0-9]+\.[0-9]+$'
                if re.match(pattern, spy.rating) is not None:
                    spy.rating = float(spy.rating)
                    break
                else:
                    print('Enter floating values.')
            print('Let\'s get started...')
            print('Here\'s your profile,\n')
            show_profile()
            start_chat()
        else:
            print('Enter Male or Female or Others')
            print('Only!!!')


# A function to add status
def add_status():
    dic = dict()
    dic.update({'Status': '', 'Time': ''})
    print('Time to update the status!')
    print('Wanna update from your pre-set updates:')
    answ = input('Yes or No:')
    if answ.upper() == 'NO':
        while True:
            dic['Status'] = input('Enter your status:')
            pattern = '^[a-zA-Z0-9\s!#@$%&.]+$'
            if re.match(pattern, dic['Status']) is not None:
                break
            else:
                print('Don\'t enter anything.')
        dic['Time'] = strftime("%H:%M:%S")
        if len(dic['Status']) > 0:
            spy.chats.append(dic)
            print('Updating...')
            sleep(0.8)
            print('Status updated!')
        else:
            print('You haven\'t entered anything.')
    elif answ.upper() == 'YES':
        it_num = 0
        print('Select from these one:')
        pre_status = ['Available', 'Busy', 'Offline', 'Cool!']
        for it in range(len(pre_status)):
            it_num += 1
            print('%d.%s' %(it_num, pre_status[it]))
        while True:
            cho = input('Which one:')
            pattern = '^[0-9]+$'
            if re.match(pattern, cho) is not None:
                cho = int(cho)
                break
            else:
                print('Enter it\'s position as shown.')
        if cho == 1:
            dic['Status'] = 'Available'
            dic['Time'] = strftime("%H:%M:%S")
            spy.chats.append(dic)
            print('Updating...')
            sleep(0.8)
            print('Status updated!')
        if cho == 2:
            dic['Status'] = 'Busy'
            dic['Time'] = strftime("%H:%M:%S")
            spy.chats.append(dic)
            print('Updating...')
            sleep(0.8)
            print('Status updated!')
        if cho == 3:
            dic['Status'] = 'Offline'
            dic['Time'] = strftime("%H:%M:%S")
            spy.chats.append(dic)
            print('Updating...')
            sleep(0.8)
            print('Status updated!')
        if cho == 4:
            dic['Status'] = 'Cool!'
            dic['Time'] = strftime("%H:%M:%S")
            spy.chats.append(dic)
            print('Updating...')
            sleep(0.8)
            print('Status updated!')


# A function to add new friend.
def add_frnd():
    new_friend = Spy('', '', 0, 0.0, '')
    while True:
        new_friend.name = input("Please add your friend's name: ")
        pattern = '^[a-zA-z\s]+$'
        if re.match(pattern, new_friend.name) is not None:
            new_friend.name = str(new_friend.name)
            break
        else:
            print('Enter alphabets only.')
    while True:
        new_friend.salutation = input("Salutation(Mr/Mrs)?: ")
        pattern = '^(Miss.|Mr.|Mrs.|Ms.|mr.|ms.|miss.|mrs.)+$'
        if re.match(pattern, new_friend.salutation) is not None:
            new_friend.salutation = str(new_friend.salutation)
            break
        else:
            print('Enter proper salutation.')
    while True:
        new_friend.age = input("Age?:")
        pattern = '^[0-9]+$'
        if re.match(pattern, new_friend.age) is not None:
            new_friend.age = int(new_friend.age)
            break
        else:
            print('Enter digits only.')
    while True:
        new_friend.rating = input("Spy rating?:")
        pattern = '^[0-9]+\.[0-9]+$'
        if re.match(pattern, new_friend.rating) is not None:
            new_friend.rating = float(new_friend.rating)
            break
        else:
            print('Enter floating values only.')
    while True:
        marital_status = input('Married?(Y/N)')
        pattern = '^[Y|N|n|y]+$'
        if re.match(pattern, marital_status) is not None:
            new_friend.marital = str(new_friend.marital)
            break
        else:
            print('Enter Y or N only.')
    if marital_status.upper() == 'Y':
        new_friend.marital = 'Married'
    else:
        new_friend.marital = 'Not Married'
    print('Adding Friend...')
    sleep(1)
    print('Name:', new_friend.salutation+new_friend.name)
    print('Age:', new_friend.age)
    print('Rating:', new_friend.rating)
    print('Marital Status:', new_friend.marital)
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print('Friend Added!')
    else:
        print('Sorry! We can\'t add you because you are not eligible.')
        print('Be logical while entering age and rating')
    return len(friends)


# A function to select among online friends.
def select_friend():
    item_number = 0
    for friend in friends:
        print('%d. %s %s aged %d with rating %.2f is online.' % (item_number+1, friend.salutation, friend.name, friend.age, friend.rating))
        item_number = item_number + 1
    while True:
        friend_choice = input("Choose from your friends:")
        pattern = '^[0-9]+$'
        if re.match(pattern, friend_choice) is not None:
            if int(friend_choice) <= item_number:
                friend_choice_position = int(friend_choice) - 1
                return friend_choice_position
            else:
                print('Enter valid position of your friend.')
        else:
            print('Wrong Input')
            print('Enter the position in numerals')


# Function to encrypt message inside an image file.
def send_message():
    frnd = select_friend()
    avg = 0
    pattern = '^[a-zA-Z0-9\s]+\.jpg$'
    while True:
        original_image = input('Name of image:')
        if re.match(pattern, original_image) is not None:
            break
        else:
            print('File should must have .jpg extension')
    while True:
        output_image = input('Name of output image:')
        if re.match(pattern, output_image):
            break
        else:
            print('File should must have .jpg extension')
    while True:
        text = input('Enter your message:')
        pattern = '^[a-zA-Z0-9@$%&\s]+$'
        if re.match(pattern, text) is not None:
            break
        else:
            print('Enter alphabets only')
    msg1 = 'CALL ME'
    msg2 = 'HELP'
    msg3 = 'LONG TIME NO SEE!'
    msg4 = 'EMERGENCY'
    # help1 = text.find(msg1) + text.find(msg1.lower())
    # help2 = text.find(msg2) + text.find(msg2.lower())
    # help3 = text.find(msg3) + text.find(msg3.lower())
    # help4 = text.find(msg4) + text.find(msg4.lower())
    # Checking for an emergency message
    if msg1 or msg1.lower() or msg2.lower() or msg3.lower() or msg4.lower() in text:
        # Encryption of image:
        try:
            Steganography.encode(original_image, output_image, text)
            avg = len(text)
            new_chat = ChatMessage(text, True, avg, frnd)
            friends[frnd].chats.append(new_chat)
            print('\nIt seems you are in danger.')
            print('Don\'t you worry my friend.')
            print('I\'m on my way.')
            print("Your secret message image is ready!")
        except IOError:
            print('No such file present in your directory.')
            print('Try:demo.jpg\n')
            sleep(0.5)
    else:
        # Encryption of image:
        try:
            Steganography.encode(original_image, output_image, text)
            new_chat = ChatMessage(text, True, avg, frnd)
            friends[frnd].chats.append(new_chat)
            print("Your emergency secret message image is ready!")
        except IOError:
            print('No such file present in your directory.')
            print('Try:picture.jpg\n')
            sleep(0.5)


# Function to read encrypted message encoded inside an image file.
def read_message():
    frnd = select_friend()
    sender = frnd
    avgg = 0
    flag = 0
    while True:
        output_path = input('Name of image which contains secret message:')
        pattern = '^[a-zA-Z0-9\s]+\.jpg$'
        if re.match(pattern, output_path) is not None:
            # Handling I/O error
            try:
                # Decryption of encrypted image
                secret_text = Steganography.decode(output_path)
                pattern = '^[a-zA-z]+$'
                # Handling cases of image having no secret message.
                if re.match(pattern, secret_text) is not None:
                    print('This is your message:')
                    print(secret_text)
                    avg = len(secret_text)
                    new_chat = ChatMessage(secret_text, False, avg, sender)
                    friends[frnd].chats.append(new_chat)
                    print("Your secret message has been saved!")
                    break
                else:
                    print('This file doesn\'t contain any secret message.')
                    print('Try again.')
            except IOError:
                print ('No such file present in the directory.')
        else:
            print('Invalid image name.. ')
            print('It must end with .jpg association.')
            print('Try Again!')
            sleep(0.8)
        if new_chat.sender == 1:
            flag += 1
            av = len(new_chat.message) / flag
            avgg = avgg + av
            if avgg > 100:
                friends.pop(new_chat.sender)
                print('He has been removed.')
                print('He has been speaking too much.')





# Function to read chat messages from the users.
def read_chat():
    read_for = select_friend()
    try:
        for chat in friends[read_for].chats:
            if chat.sent_by_me:
                # Printing time in blue
                time = colored(chat.time.strftime("%d %B %Y"), 'blue')
                # Printing spy name in red.
                said = colored('You said:')
                # Printing message in cyan as black color was not there in the library.
                msg = colored(chat.message, 'red', 'on_cyan')
                print('[%s] %s: %s' % (time, said, msg))
            else:
                # Printing time in blue
                time = colored(chat.time.strftime("%d %B %Y"), 'blue')
                # Printing spy name in red.
                said = colored(friends[read_for].name, 'red') + ' said:'
                # Printing message in cyan as black color was not there in the library.
                msg = colored(chat.message, 'cyan')
                print('[%s] %s %s' % (time, said, msg))
    except AttributeError:
        print('No previous messages.')
        read_chat()
    except IndexError:
        print('You don\'t have that much online friends.')
        read_chat()


# Function to show user's profile
def show_profile():
    if len(spy.name) > 0:
        print('Name:', spy.salutation + spy.name.title())
        print('Age:', spy.age)
        print('Rating:', spy.rating)
        print('Marital Status:', spy.marital)
        print('Status Updates:', spy.chats)
        print('Online:', spy.is_online)
    else:
        print('No credentials found.')


# Function to start Menu which will call other functions required to perform their respective tasks.
def start_chat():
    show_menu = True
    print('Checking eligibility...')
    sleep(1.5)
    if int(spy.age) > 12 and int(spy.age) < 50:
        print('You\'re eligible.')
        print(spy.salutation+spy.name)
        print('It is good to see you.')
    try:
        while show_menu:
            print('\nSelect any of the following:')
            choices = '1.Add a status update \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read Chats from user \n6.Show your profile \n7.Terminate \n\n'
            ch = int(input(choices))
            if ch == 1:
                add_status()
            elif ch == 2:
                add_frnd()
            elif ch == 3:
                print('Wanna send some secret messages...!')
                sleep(0.8)
                send_message()

            elif ch == 4:
                print('To proceed further you have to prove yourself:')
                a = randint(1, 11)
                b = randint(1, 11)
                r = 0
                print('%s+%s' % (str(a), str(b)))
                c = a+b
                while True:
                    r = input('What will be the sum?\n')
                    pattern = '^[0-9]+$'
                    if re.match(pattern,r) is not None:
                         break
                    else:
                        print('Invalid Input!')
                if c == int(r):
                    print('Access Granted!')
                    read_message()
                else:
                    print('Access Denied!')
                    print('Program Terminating!!!')
                    show_menu = False

            elif ch == 5:
                read_chat()

            elif ch == 6:
                print('Your profile:')
                show_profile()

            elif ch == 7:
                show_menu = False
                print('Terminating...')
                sleep(0.8)
                break

    except ValueError:
        print('Invalid Choice!')
        print('Enter your choice as shown.')
        start_chat()

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
while True:
    answer = input(question)
    patternc = '^(Y|y|N|n)+$'
    if re.match(patternc, answer) is not None:
        break
    else:
        print('Enter Y or N only.')
if answer.upper() == 'Y':
    print('Welcome,')
    show_profile()
    print('\nLet\'s begin!')
    start_chat()
else:
    add_spy()
# End of the code.
