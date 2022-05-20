import sqlite3

connection = sqlite3.connect('ARThub.bd')
cursor = connection.cursor()


def User_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (User_id INTEGER PRIMARY KEY, User_name TEXT)''')
    connection.commit()

def Order_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS OrderR (Order_id  INTEGER PRIMARY KEY, User_id INTEGER, User_FIO Text, Adres Text, User_Phone INTEGER, ART_name Text)''')
    connection.commit()

def Artist_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Artists (Artist_id INTEGER PRIMARY KEY, Artist_Name TEXT, Artist_About TEXT)''')
    connection.commit()

def Event_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Events (Event_id INTEGER PRIMARY KEY, Event_Name TEXT, Event_About TEXT)''')
    connection.commit()

def Arts_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Arts ( Art_id INTEGER PRIMARY KEY, Art_Name TEXT, Event_Name TEXT, Artist_Name TEXT, Price INTEGER, pic TEXT, Art_type TEXT)''')
    connection.commit()

# name  and about artist out of the ARTIST NAME
def get_Artist(text):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Artists where Artist_Name=?; ''', [text])
    three_results = cursor.fetchall()
    connection.commit()
    return three_results[0][1]+'\n\n'+three_results[0][2]

# name  and about artist out of the Artist_id
def get_All_Artist(x):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Artists where Artist_id=?; ''', [x])
    three_results = cursor.fetchall()
    connection.commit()
    return three_results[0][1] + '\n\n' + three_results[0][2]

# name  out of the Artist_id
def get_All_Artist_Name(x):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Artists where Artist_id=?; ''', [x])
    three_results = cursor.fetchall()
    connection.commit()
    return three_results[0][1]

def get_All_Arts_Artist(text,y):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Arts where Artist_Name=?; ''', [text])
    results = cursor.fetchall()
    connection.commit()
    return results[y][1] + '\n\nНазвание события: ' + results[y][2]+'\n\nАвтор:'+ results[y][3]+ '\n\nСтоимость:'+str(results[y][4])


def get_Arts_Artist(text,y):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Arts where Artist_Name=?; ''', [text])
    results = cursor.fetchall()
    connection.commit()
    return results[y][1]

def get_All_Arts_Name(x):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Arts where Art_id=?; ''', [x])
    three_results = cursor.fetchall()
    connection.commit()
    return three_results[0][1]

# name  and about artist out of the Artist_id
def get_All_Events(x):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Events where Event_id=?; ''', [x])
    three_results = cursor.fetchall()
    connection.commit()
    return three_results[0][1] + '\n\n' + three_results[0][2]

# count arts of this num event
def Count_Arts_of_Event(numofevent):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Events where Event_id=?; ''', [numofevent])
    results = cursor.fetchall()
    nameofevent= results[0][1]
    cursor.execute('''SELECT COUNT(*) FROM Arts where Event_Name=?; ''', [nameofevent])
    result = cursor.fetchall()
    connection.commit()
    return result

def get_Arts_OfEvent(numofevent,y):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Events where Event_id=?; ''', [numofevent])
    results = cursor.fetchall()
    nameofevent= results[0][1]

    cursor.execute('''SELECT * FROM Arts where Event_Name=?; ''', [nameofevent])
    results = cursor.fetchall()
    connection.commit()
    return results[y][1] + '\n\nНазвание события: '+results[y][2]+'\n\nАвтор:'+results[y][3]+'\n\nСтоимость:'+str(results[y][4])

def get_Pic_of_Arts_OfEvent(numofevent,y):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Events where Event_id=?; ''', [numofevent])
    results = cursor.fetchall()
    nameofevent= results[0][1]

    cursor.execute('''SELECT * FROM Arts where Event_Name=?; ''', [nameofevent])
    results = cursor.fetchall()
    connection.commit()

    imgArtist = results[y][1] + ".jpg"
    img = open(imgArtist, 'rb')
    return img

# 1-Arts 2-Artists
def makePIC_Artist(type,text):
    if type==1:
        imgArtist = get_All_Artist_Name(text) + ".jpg"
        img = open(imgArtist, 'rb')
        return img
    elif type==2:
        imgArtist = text + ".jpg"
        img = open(imgArtist, 'rb')
        return img

def User_Poisk(x):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM Users where User_name=?; ''', [x])
    results = cursor.fetchall()
    if int(''.join(map(str,results[0])))==0:
        return True
    else:
        return False


def get_Price_ofArt(Arts_name):
    connection = sqlite3.connect('ARThub.bd')
    cursor = connection.cursor()
    cursor.execute('''SELECT Price FROM Arts where Art_Name=?; ''', [Arts_name])
    results = cursor.fetchall()
    return int(''.join(map(str,results[0])))