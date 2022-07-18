import os
import threading
import pickle
from pyrogram import Client
from pyrogram import filters
from pykeyboard import ReplyKeyboard, ReplyButton, ReplyKeyboardRemove
import pycolorizer
import positive

#bot
bot_token = "5358186417:AAEd2C0Ne7SZE2ShfdGe8XFhI3_p4ceCUNc"#os.environ.get("TOKEN", "") 
api_hash = "ac6664c07855e0455095d970a98a082d"#os.environ.get("HASH", "") 
api_id = "11223922"#os.environ.get("ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

CHOOSE = ReplyKeyboard(row_width=3,one_time_keyboard=True,placeholder="choose",resize_keyboard=True,selective=True)
CHOOSE.add(
            ReplyButton('/color'),
            ReplyButton('/positive'),
          )  

# negative to positive
def negetivetopostive(message):
    file = app.download_media(message)
    output = file.split("/")[-1]

    print("using c41lab")
    os.system(f'./c41lab.py "{file}" "{output}"')
    app.send_document(message.chat.id,document=output,caption="used tool -> c41lab")
    os.remove(output)

    print("using negfix8")
    os.system(f'./negfix8 "{file}" "{output}"')
    app.send_document(message.chat.id,document=output,caption="used tool -> negfix8")
    os.remove(output)

    print("using simple tool")
    positive.positiver(file,output)
    app.send_document(message.chat.id,document=output,caption="used tool -> simple tool")
    os.remove(output)

    os.remove(file)

# color image
def colorizeimage(message):
    file = app.download_media(message)
    output = file.split("/")[-1]

    print("using simple tool")
    pycolorizer.colorize_image(output,file)
    app.send_document(message.chat.id,document=output,caption="used tool -> simple tool")
    os.remove(output)

    print("using colorize tool")
    output = output.replace(".","_color.")
    os.system(f'ml color colorize "{file}"')
    app.send_document(message.chat.id,document=output,caption="used tool -> colorize tool")
    os.remove(output)

    os.remove(file)

@app.on_message(filters.command(["start"]))
def echo(client, message):
    app.send_message(message.chat.id,'Send me Image file')

@app.on_message(filters.photo)
def photo(client, message):
    with open(f'{message.from_user.id}.json', 'wb') as handle:
        pickle.dump(message, handle)
    app.send_message(message.chat.id,text="Choose",reply_markup=CHOOSE)

@app.on_message(filters.document)
def documnet(client, message):
    if 'png' in message.document.file_name or 'jpg' in message.document.file_name or 'jpeg' in message.document.file_name:
        with open(f'{message.from_user.id}.json', 'wb') as handle:
            pickle.dump(message, handle)
        app.send_message(message.chat.id,text="Choose",reply_markup=CHOOSE)
    else:
        app.send_message(message.chat.id,'File Type not Suported')

@app.on_message(filters.command(["color"]))
def cdocumnet(client, message):
    app.send_message(message.chat.id,'Processing',reply_markup=ReplyKeyboardRemove())
    if os.path.exists(f'{message.from_user.id}.json'):
        with open(f'{message.from_user.id}.json', 'rb') as handle:
            nmessage = pickle.loads(handle.read())
        os.remove(f'{message.from_user.id}.json')
    else:
        app.send_message(message.chat.id,"First send me a File")

    col = threading.Thread(target=lambda:colorizeimage(nmessage),daemon=True)
    col.start()
    
@app.on_message(filters.command(["positive"]))
def pdocumnet(client, message):
    app.send_message(message.chat.id,'Processing',reply_markup=ReplyKeyboardRemove())
    if os.path.exists(f'{message.from_user.id}.json'):
        with open(f'{message.from_user.id}.json', 'rb') as handle:
            nmessage = pickle.loads(handle.read())
        os.remove(f'{message.from_user.id}.json')
    else:
        app.send_message(message.chat.id,"First send me a File")

    pos = threading.Thread(target=lambda:negetivetopostive(nmessage),daemon=True)
    pos.start()   

app.run()