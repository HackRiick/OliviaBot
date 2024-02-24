from imports import *

blocklist = ["5627792037"]
ifsagrupkanallari = {}
groupdb = set()
userdb = set()
channel_blocklist = 'Oliviablocklist'
api_id = api_id
api_hash = api_hash
bot_token = bot_token

app = Client("Olivia", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
button3 = InlineKeyboardButton('➕ GRUBUNA EKLE ➕', url='https://t.me/OliviaMissbot?startgroup=true')
button4 = InlineKeyboardButton('Kanala Katıl 🚶🏼‍♀️',url = 'https://t.me/Enobots')


message_idd = 9

def update_blocklist():

    message = app.get_messages(channel_blocklist, message_idd)

    message_ids = set(line.strip() for line in message.text.split('\n') if line.strip().isnumeric())

    new_ids = message_ids.difference(blocklist)
    blocklist.extend(new_ids)
    
    removed_ids = set(blocklist).difference(message_ids)
    blocklist[:] = [id_ for id_ in blocklist if id_ not in removed_ids]

    print("Güncellenmiş blocklist:", blocklist)

# reload command 
@app.on_message(filters.command("reload"))
def reload_command(client, message):  
    user_id = message.from_user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
        
    update_blocklist()
    
    channel_info_message = app.get_messages('D9_xP2b6KsLqE1YvZ0oFtN4GcRjMw', 2)
    channel_info_lines = channel_info_message.text.split('\n')

    new_ifsagrupkanallari = {}
    for line in channel_info_lines:
        parts = line.split(':')
        if len(parts) == 2:
            chat_id = int(parts[0].strip())
            kanal_isim = parts[1].strip()
            new_ifsagrupkanallari[chat_id] = kanal_isim
                
    global ifsagrupkanallari
    ifsagrupkanallari = new_ifsagrupkanallari

    message.reply("Bot, güncellendi..")
    print(ifsagrupkanallari)
    
# START COMMAND
@app.on_message(filters.command("start"))
def start_command(client, message):
    user = message.from_user

    photo_url = "https://mpost.io/wp-content/uploads/image-56-239.jpg"
    caption = f"{user.mention} Naberrr? Ben Olivia 🪂"

    keyboard = [
        [InlineKeyboardButton("🧸 𝙶𝚛𝚞𝚋𝚞𝚗𝚊 𝙴𝚔𝚕𝚎 🧸", url="https://t.me/OliviaMissbot?startgroup=true")],
        [InlineKeyboardButton("💡 𝙺a𝚗𝚊𝚕", url="https://t.me/Enobots"), InlineKeyboardButton("🛠️ 𝙺𝚘𝚖𝚞𝚝𝚕𝚊𝚛", callback_data="button3")],
        [InlineKeyboardButton("🕵🏻‍♂️ 𝚂𝚊𝚑𝚒𝚋𝚒𝚖", url="http://t.me/Mrsherrman")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    client.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=caption,
        reply_markup=reply_markup
    )


@app.on_callback_query(filters.regex("button3"))
def button3_callback(client, callback_query):
    caption = "**⚙️ Komutlar:\n➺/help - yardım al\n\n➺/tag - tag modlarını gösterir\n➺/shipp - Günün aşkını seçer\n➺/stat - toplam mesaj sayı gösterir \n➺/hava - hava durumu gösterir\n➺/ses - yazıyı sese çevirir\n➺/ifsa - ifşa edin\n\nV:5.8.7**"

    keyboard = [
        [InlineKeyboardButton("💡 𝙺a𝚗𝚊𝚕", url="https://t.me/Enobots"), InlineKeyboardButton("👈🏻 𝙶𝚎𝚛𝚒", callback_data="button6")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    callback_query.message.edit_caption(
        caption=caption,
        reply_markup=reply_markup
    )
  
@app.on_callback_query(filters.regex("button6"))
def button6_callback(client, callback_query):
    caption = "**Selaam 🧚🏻‍♂️ Naber? ben Olivia. Senin için burdayım 🪂**"

    keyboard = [
        [InlineKeyboardButton("🧸 𝙶𝚛𝚞𝚋𝚞𝚗𝚊 𝙴𝚔𝚕𝚎 🧸", url="https://t.me/OliviaMissbot?startgroup=true")],
        [InlineKeyboardButton("💡 𝙺a𝚗𝚊𝚕", url="https://t.me/Enobots"), InlineKeyboardButton("🛠️ 𝙺𝚘𝚖𝚞𝚝𝚕𝚊𝚛", callback_data="button3")],
        [InlineKeyboardButton("🕵🏻‍♂️ 𝚂𝚊𝚒𝚑𝚒𝚋𝚒𝚖",url="http://t.me/Mrsherrman")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    callback_query.message.edit_caption(
        caption=caption,
        reply_markup=reply_markup
    )

# BC COMMAND
@app.on_message(filters.command("bc"))
def bc_command(client, message):
    user_id = str(message.from_user.id)

    if not user_id == "6437355772":
        message.reply(f"**☠️ Bu komutu yalnız, [MrSherman](tg://user?id=5920628764) kullana bilir!**")        
        return
        
    if len(message.command) == 2:
        blocked_user = message.command[1]
        chat_id = message.chat.id
        current_message =  app.get_messages('Oliviablocklist',9,)
        new_info = f"{current_message.text}\n{blocked_user}"
        current_message.edit_text(new_info)
        update_blocklist()
        message.reply(f"**📍 [Kullanıcı](tg://user?id={blocked_user}) yasaklandı!**")
    else:
        message.reply('**bir id yazın**')

@app.on_message(filters.command("ses"))
async def ses(_, event):
        
    args = event.text.split()
    
    if len(args) < 2:
        await event.reply_text("❗Sese çevirmem için bir mesaj yazın.\n\n/ses olivia")
        return
        
    text = " ".join(args[1:])
    tts = gTTS(text=text, lang='tr')
    filename = 'Sesli Mesaj (olivia).mp3'
    tts.save(filename)

    await app.send_voice(
        chat_id=event.chat.id,
        voice=filename,
        reply_to_message_id=event.id
    )

    await asyncio.sleep(1.5)
    os.remove(filename)


@app.on_message(filters.regex(re.compile(r'(?i)\başk\b')))
def respond_to_ask(client, message):
    if re.search(r'(?i)\başk\b', message.text):
        yanit = random.choice(askmesaji)
        message.reply_text(yanit)

@app.on_message(filters.regex(re.compile(r'(?i)\bolivia\b')))
def respond_to_ask(client, message):
    if re.search(r'(?i)\bolivia\b', message.text):
        yanit = random.choice(oliviamesaji)
        message.reply_text(yanit)

# HAVA COMMAND 
weather_api_key = WEATHER_API_KEY
@app.on_message(filters.command("hava"))
def get_weather(client, message):
    command = message.text.split()
    
    user_id = message.from_user.id
        
    if len(command) < 2:
        message.reply_text("**Şehir belirtmelisin, yoksa seni kale almam 🤦\n\n/hava Ankara**")
        return
    
    city = " ".join(command[1:])
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == "404":

        message.reply_text(f"{city} şehrini bulamadım")
        return
    
    weather = data["weather"][0]
    description = weather["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]
    sunrise_timestamp = data["sys"]["sunrise"]
    sunset_timestamp = data["sys"]["sunset"]

    sunrise_datetime = datetime.fromtimestamp(sunrise_timestamp, tz=pytz.timezone('Asia/Baku'))
    sunset_datetime = datetime.fromtimestamp(sunset_timestamp, tz=pytz.timezone('Asia/Baku'))
    temperature_celsius = temperature - 273.15
    description_az = translations.get(description.lower(), description)
    response_text = f"**🌤 {city} hava durumu:**\n\n**{description_az}**\n\n**🌡 Sıcaklık:**  {temperature_celsius:.2f} °C\n\n**🌬️ Rüzgar:** {windspeed} m/s\n\n**☀️ Gün doğumu:**  {sunrise_datetime.strftime('%H:%M:%S')}\n\n**🌑 Gün batımı:**  {sunset_datetime.strftime('%H:%M:%S')}"
    message.reply_text(response_text)

# STAT COMMAND
@app.on_message(filters.command("stat"))
def stat_command(client, message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    user_id = message.from_user.id
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("Bu komut gruplar için")
        return
        
    last_message_id = message.id - 1
    client.send_message(chat_id, f"🧮 **Toplam mesaj: **{last_message_id}",reply_markup=InlineKeyboardMarkup([[button4]]))

# GREKLAM COMMAND
@app.on_message(filters.command("greklam") & filters.user("@Sananebekardesim"))
def greklam_command(client, message):
    replied_message = message.reply_to_message
    if replied_message is None:
        message.reply_text("bir mesaja yanit at")
        return

    for group_id in groupdb:
        try:
            client.forward_messages(group_id, message.chat.id, replied_message.id)
        except Exception as e:
            print(f"hata oluştu: {e}")

# PREKLAM COMMAND
@app.on_message(filters.command("preklam") & filters.user("@Sananebekardesim"))
def preklam_command(client, message):
    replied_message = message.reply_to_message
    if replied_message is None:
        message.reply_text("Bu komut bir yanıt gerektirir.")
        return
    for user_id in userdb:
        try:
            client.forward_messages(user_id, message.chat.id, replied_message.id)
        except Exception as e:
            print(f"Hata oluştu: {e}")

def check_blocklist(user_id):
    if user_id in blocklist:
        return False
    return True

@app.on_message(filters.command("setifsa") & filters.group)
async def set_ifsa_command(_, message: Message):
    if len(message.command) == 2:
        kanal_isim = message.command[1]
        user_id = str(message.from_user.id)
        chat_id = message.chat.id
        group_name = message.chat.title
        
        if not check_blocklist(user_id):
            await message.reply_text("Sizin kullanımınız yasaklanmıştır!")
            return

        if kanal_isim.startswith('@'):
            await message.reply("❌ @ işareti olmadan yazmalısınız")
            return

        try:
            # Gönderenin admin veya sahip olduğunu kontrol et
            user = await app.get_chat_member(chat_id, user_id)
            if user.status in [ChatMemberStatus.OWNER]:
                kanal = await app.get_chat(kanal_isim)
                await app.send_message(kanal_isim, f"✅ Bu kanal - {group_name} - grubu için ifşa kanalı olarak kayd edildi")
                ifsagrupkanallari[chat_id] = kanal_isim
                print(ifsagrupkanallari)
                await message.reply(f"✅ ifşa kanalı olarak @{kanal_isim} kayd edildi")
                
                current_message = await app.get_messages('D9_xP2b6KsLqE1YvZ0oFtN4GcRjMw',2,)
                new_info = f"{current_message.text}\n{chat_id}:{kanal_isim}"
            
                await current_message.edit_text(new_info)
            else:
                await message.reply("❌ Bunu yalnız grup sahibi yapa bilir")
        except Exception as e:
            await message.reply(f"**⚠️ Hata: başarısız oldu** \n\n• Benim, kanalda admin olduğumu ve mesaj gönderme yetkimin olduğunu kontrol edin!\n\n• Girdiğiniz kanalın, kullanıcı adının doğru olduğunu kontrol edin ve tekrar deneyin.\n\n|•|\n\n__{e}__")
    else:
        await message.reply("❔Doğru kullan:\n\n/setifsa kanal_kullanıcı_adı")



@app.on_message(filters.command("ifsa", prefixes="/") & filters.group)
async def ifsa_command(_, message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    chat = await app.get_chat(message.chat.id)
    group_name = chat.title

    if not check_blocklist(user_id):
        await message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return

    if message.reply_to_message is None:
        await message.reply_text('**Ifşa etmem için bir mesaja yanıt verin 💅🏻**')
        return

    replied_message = message.reply_to_message
    channel_username = ifsagrupkanallari.get(chat_id)

    if channel_username:
        try:
            if replied_message.sticker is not None:
                await app.send_sticker(
                    chat_id=channel_username,
                    sticker=replied_message.sticker.file_id
                )
            else:
                await app.forward_messages(
                    chat_id=channel_username,
                    from_chat_id=replied_message.chat.id,
                    message_ids=replied_message.id
                )

            buttonifsakanal = InlineKeyboardButton('🪬 İfşa Kanalı 🪬', url=f'https://t.me/{channel_username}')
            await app.send_message(
                chat_id=message.chat.id,
                text=f'**⁉️ İfşa paylaşıldı**',
                reply_markup=InlineKeyboardMarkup([[buttonifsakanal]]),
                reply_to_message_id=message.id
            )
        except Exception as e:
            error_message = str(e)
            await message.reply_text(f"⚠️ DİKKAT:\n Botu, @{channel_username}'da admin yapın ve mesaj gönderme yetkisi verin!`{error_message}`")
    else:
        await message.reply_text("**⚠️ Bu grup için, ifşa kanalı kayd  edilmemiş! lütfen, /setifsa komutu ile grubunuz için bir ifşa kanalı kayd edin**")

group_status = {}
tagged_users = {}

def is_admin(user_id, chat_id):
    chat_member = app.get_chat_member(chat_id, user_id)
    return chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]


# tek-tek tag islevi
def do_tagging(chat_id, message):
    group_status[chat_id] = chat_id
    group_status[chat_id] = True  
    members = app.get_chat_members(chat_id)
    members_list = list(members)
    tsay = 0
    for member in members_list:
        if not member.user.is_bot and not member.user.status in [UserStatus.LAST_WEEK, UserStatus.LAST_MONTH, UserStatus.LONG_AGO]:
            app.send_message(chat_id, f"{member.user.mention} {message}")
            time.sleep(2.5)
            tsay += 1
            if not chat_id in group_status or group_status[chat_id] == False:
                break
                
    message = f"**🪧 Grubun aktiv {tsay} kullanıcısı etiketlendi**"

    if group_status[chat_id]:
        app.send_message(chat_id, message)
        group_status[chat_id] = False
        tsay = 0

@app.on_message(filters.command("ttag", prefixes="/"))
def tag_command(_, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    chat_type = message.chat.type
    user_id = user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
        
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("**Bu komut yalnız gruplar için!**")
        return
        
    if not is_admin(message.from_user.id, message.chat.id):
        message.reply("**Çok bilmiş. Admin olmadığın için seni takmiycam!**")
        return
        
    if len(message.command) > 1:
        if chat_id not in group_status or not group_status[chat_id]:
            tag_message = " ".join(message.command[1:])
            message.reply(f"**🗨️ {user.mention} Tag başlatdı.\n\nDurdurmak için /dur yazın**")
            do_tagging(chat_id, tag_message)
        else:
            message.reply("**Zaten tag ediyorum?!**")
    else:
        message.reply("**Doğru kullan:\n/ttag acele et evleniyorum!**")

# 5-5 tag etmek
@app.on_message(filters.command(["ftag"]))
def ftag_command(_, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    chat_type = message.chat.type
    user_id = user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("**Bu komut yalnız gruplar içindir!**")
        return
        
    if not is_admin(message.from_user.id, message.chat.id):
        message.reply("**Çok bilmiş. Admin olmadığın için seni takmiycam!**")
        return
        
    if len(message.command) > 1:
        if chat_id not in group_status or not group_status[chat_id]:
            tag_message = " ".join(message.command[1:])
            message.reply(f"**🗨️ {user.mention} Tag başlatdı.\n\nDurdurmak için /dur yazın\n\n**")
            group_status[chat_id] = chat_id
            group_status[chat_id] = True 
            tagged_users = ""
            kisi= 0
            tsay = 0
            members = app.get_chat_members(message.chat.id)
            for index, member in enumerate(members):
                if not member.user.is_bot and member.user.status not in [ UserStatus.LAST_WEEK, UserStatus.LAST_MONTH, UserStatus.LONG_AGO]:
                    tagged_users += f"{member.user.mention}, "
                    kisi += 1
                    tsay += 1
                    if kisi == 5:
                        app.send_message(message.chat.id, f"{tag_message}\n {tagged_users}")
                        tagged_users = ""
                        kisi = 0
                time.sleep(2)
                if not chat_id in group_status or group_status[chat_id] == False:
                     break
            
            if tagged_users:
                if group_status[chat_id] == False:
                    pass
                else:
                    app.send_message(message.chat.id, f"{tag_message}\n {tagged_users}")
   
            message = f"**🪧 Grubun aktiv {tsay} kullanıcısı etiketlendi**"
        
            if group_status[chat_id]:
                   app.send_message(chat_id, message)
                   tsay = 0
                   group_status[chat_id] = False
        else:
           message.reply("**Zaten tag ediyorum?!**")
    else:
        message.reply("**Doğru kullan:\n/ftag acele gel evleniyorum!**")

# adminleri tag etmek
@app.on_message(filters.command(["atag"]))
def atag(_, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    chat_type = message.chat.type
    user_id = user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("**Bu komut yalnız gruplar içindir!**")
        return
        
    if len(message.command) > 1:
        if chat_id not in group_status or not group_status[chat_id]:
            message.reply(f"**🗨️ {user.mention} Tag başlatdı.\n\nDurdurmak için /dur yazın**")
            group_status[chat_id] = chat_id
            group_status[chat_id] = True 
            tag_message = " ".join(message.command[1:])
            members = app.get_chat_members(chat_id)
            admins = []
            for member in members:
                if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not member.user.is_bot:
                    admins.append(member)
            for admin in admins:
                app.send_message(chat_id, f"{admin.user.mention} {tag_message}")
                time.sleep(1.2)
                if not chat_id in group_status or group_status[chat_id] == False:
                     break
                     
            message = f"**🪧 Grubun {len(admins)} admini etiketlendi**"
                
            if group_status[chat_id]:
                app.send_message(chat_id, message)
                group_status[chat_id] = False
                
        else:
           message.reply("**Zaten tag ediyorum?!**")
    else:
        message.reply("**Doğru kullan:\n/atag acele et evleniyorum**")

@app.on_message(filters.command(["tag"]))
def ftag_command(_, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    chat_type = message.chat.type
    user_id = user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("**Bu komut yalnız gruplar içindir!**")
        return
    
    message.reply("**💡 Tag başlatmak için:\n    -  /ttag (mesajınız) tek-tek tag\n   -  /ftag (mesajınız) 5-5 tag\n  - /atag (mesajınız) adminleri tag**")
    
@app.on_message(filters.command("dur", prefixes="/"))
def dur_command(_, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    chat_type = message.chat.type
    user_id = user.id
    
    if not check_blocklist(user_id):
        message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        message.reply("**Bu komut yalnız gruplar içindir!**")
        return
        
    if not is_admin(message.from_user.id, message.chat.id):
        message.reply("**Çok bilmiş. Admin olmadığın için seni takmiycam!**")
        return
        
    if chat_id in group_status:     
        
        if group_status[chat_id] == False:
            message.reply(f"**{user.mention}, Zaten kimseyi tag etmiyorum. Neden beni rahatsız ediyosun?🥲**")
            return
            
        group_status[chat_id] = False
        message.reply(f"**⛔ {user.mention} tagı durdurdu**")
    
initial_message = None
initial_buttons = None


@app.on_message(filters.command("help"))
def help_command(client, message):
    global initial_message, initial_buttons
    text = "**Sen seslenirsinde ben gelmemmi?!☃️**"

    buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🪩 Etiket", callback_data="tag"),
                    InlineKeyboardButton("🎭 İfşa", callback_data="ifsa"),
                ],
                [
                    InlineKeyboardButton("⛈️ Hava", callback_data="hava"),
                ],
                [
                    InlineKeyboardButton("🩷 Shipp", callback_data="shipp"),
                    InlineKeyboardButton("🎙️ Seslendirme", callback_data="seslendirme"),
                ],
                [
                    InlineKeyboardButton("⚜️ Sudo komutları", callback_data="sudo"),
                ],
            ]
        )

    initial_message = client.send_message(
        chat_id=message.chat.id,
        text=text,
        reply_to_message_id=message.id,
        reply_markup=buttons,
        )

    initial_buttons = buttons

@app.on_callback_query()
def callback_handler(client, query: CallbackQuery):
    global initial_message, initial_buttons

    data = query.data
    message = query.message

    if data == "back" and initial_message is not None and initial_buttons is not None:
        try:
            client.edit_message_text(
                chat_id=message.chat.id,
                message_id=initial_message.id,
                text=initial_message.text,
                reply_markup=initial_buttons,
            )
        except MessageNotModified:
            pass
            
    else:

        if data == "tag":
            text =  "🪩 Grupta etiketleme yardımı: \n\n⚙️ Komutlar: \n\n/ttag mesajınız tek tek etiketlenecek\n/ftag mesajınız 5-5 etiketleyecek\n/atag mesajınız adminleri etiketleyecek\n/dur mevcut etiketi durduracak\n\nSadece adminler yapabilir."
        elif data == "ifsa":
            text = "🎭 Ifsa'yı paylaşmaya yardım:\n\n📖 Bu fonksiyon sayesinde grubunuzda yaşanan ilginç anları kanala yükleyerek ölümsüzleştirebileceksiniz.  \n\n⚙️ Komut kullanımı: öncelikle grubunuz için /setifsa kanal adıyla bir kanal kaydedin.\n\nKanalda paylaşmak istediğiniz şeyi yanıt olarak /ifsa komutunu yazın"
        elif data == "hava":
            text = "⛈️ Hava durumu bilgisi için yardım:\n\n📖 Bu fonksiyon sayesinde istediğiniz şehrin anlık hava durumu bilgisini alabilirsiniz.  Yazdığınız şehir adı görünmüyorsa veya hata gösteriyorsa İngilizce yazın.\n\n⚙️ Komut kullanımı: \n\n/hava şehir adı"
        elif data == "shipp":
            text = "🩷 Shipp Yardımı:\n\n📖 Bu işlevle, bir gruptan rastgele iki kişiyi shipplemek için kullana bilirsiniz\n\n⚙️\n\n/shipp komutuyla seçilir.\n\n🫡 Unutmayın günde yalnızca bir kez çift seçilir"
        elif data == "seslendirme":
            text = "🎙️ Metni sese dönüştürme:\n\nBu komutla yazılı mesajlarınızı botun sesli olarak söylemesini sağlayabilirsiniz:\nBu aramızda kalsın ama ses biraz robotik 🤫\n\n⚙️ Komut kullanımı: \n\n/ses metni..."
        elif data == "sudo":
            text = "⚜️ Bu bölümü yalnızca bot sahibi göre bilir!" 
        
        try:
            client.edit_message_text(
                chat_id=message.chat.id,
                message_id=message.id,
                text=text,
                reply_markup=get_back_button(),
            )
        except MessageNotModified:
            pass
            
def get_back_button():
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Geri 👈🏼", callback_data="back")]])
    return keyboard

@app.on_message(filters.command("shipp"))
async def handler(client, message):
    user_id = message.from_user.id
    
    if not check_blocklist(user_id):
        await  message.reply_text("Sizin kullanımınız yasaklanmıştır!")
        return
        
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        db_name = f'shipped_{message.chat.id}.csv'
        shipped = {}
        participants=[]

        if os.path.exists(db_name):
            with open(db_name) as f:
                for line in f:
                    time_str, user1, user2 = line.strip().split(",")
                    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
                    shipped[time] = (user1, user2)

        async for user in app.get_chat_members(message.chat.id):
            if not user.user.is_bot and user.user.status not in [enums.UserStatus.LAST_WEEK, enums.UserStatus.LAST_MONTH, enums.UserStatus.LONG_AGO]:
                participants.append(user)
     
      
        if len(participants) < 2:
          await message.reply('⚠️ Ne?! grupta en az 2 kişi olmalı.')
          return

        users = random.sample(participants, 2)
        tags = [f"[{user.user.first_name}](tg://user?id={user.user.id})" for user in users]
        tags_str = " ❤️‍🔥 ".join(tags)
        message_text = f"{tags_str}"
        if shipped:
            prev_time = list(shipped.keys())[0]
            if datetime.now() - prev_time > timedelta(hours=24):
                shipped.clear()
            else:
                time_diff = prev_time + timedelta(hours=24) - datetime.now()
                hours = time_diff.seconds // 3600
                minutes = (time_diff.seconds % 3600) // 60
                remaining_time = f"{hours} saat, {minutes} dakika sonra"
                await message.reply(f"**Aşıklar zaten seçilmiş:\n\n{shipped[list(shipped.keys())[0]][0]} ❤️‍🔥 {shipped[list(shipped.keys())[0]][1]}\n\nSonraki shipp:\n{remaining_time}**",reply_markup=InlineKeyboardMarkup([[button4]]))
                return

        shipped[datetime.now()] = (users[0].user.first_name, users[1].user.first_name)

        with open(db_name, 'w') as f:
            for time, (user1, user2) in shipped.items():
                f.write(f"{time},{user1},{user2}\n")

        await message.reply(f"**🧚‍♀️ Günün Aşkııı:\n\n{message_text}\n\n⏰ Sonrakı shipp: 23 saat, 59 dakika sonra**", reply_markup=InlineKeyboardMarkup([[button3]]))
    else:
        await message.reply('**Bu komut yalnız gruplar içindir!**')
        
# REYTİNG COMMAND
@app.on_message(filters.command('reyting') & filters.user('Sananebekardesim'))
def reyting_command(client, message):
    user_count = len(userdb)
    group_count = len(groupdb)
    response = f"user: {user_count} grup: {group_count}"
    message.reply_text(response)


@app.on_message(filters.private | filters.group )
def listen_messages(client, message):
    chat_type = message.chat.type
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        if message.from_user.id not in userdb:
            userdb.add(message.from_user.id)
            
    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]:
        if message.chat.id not in groupdb:
            groupdb.add(message.chat.id)

app.run()
