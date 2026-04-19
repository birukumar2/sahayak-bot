import telebot
import os
 
# Token environment variable se lo — file mein mat likho!
bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN", "TUMHARA_TOKEN_YAHAN"))
 
# State yaad rakhne ke liye — kaun kahan hai conversation mein
user_state = {}
 
# /start command
@bot.message_handler(commands=['start'])
def start(message):
    user_state[message.chat.id] = None  # State reset
    bot.send_message(message.chat.id,
"""🙏 Namaste! Main Sahayak hoon.
 
Main aapki emergency mein madad karunga.
 
Aapko kya problem hai? Likhiye:
1️⃣ Bukhar (Fever)
2️⃣ Chot / Khoon (Injury)
3️⃣ Jalan (Burn)
 
⚠️ Yeh sirf prarambhik jankari hai.
Serious situation mein 108 zaroor call karein.""")
 
# Saare messages handle karo
@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id
    text = message.text.lower().strip()
    state = user_state.get(chat_id)
 
    # ── BUKHAR ──────────────────────────────────────────────
    if any(word in text for word in ["bukhar", "fever", "bukhaar"]) or text == "1":
        user_state[chat_id] = "bukhar"
        bot.send_message(chat_id,
"""🌡️ Bukhar hai — Temperature kitna hai?
 
A) Halka (99-101°F) — thoda uncomfortable
B) Zyada (101-103°F) — bahut takleef
C) Bahut zyada (103°F+) — emergency""")
 
    # ── CHOT / KHOON ─────────────────────────────────────────
    elif any(word in text for word in ["chot", "khoon", "bleeding", "cut", "injury", "lagi"]) or text == "2":
        user_state[chat_id] = "chot"
        bot.send_message(chat_id,
"""🩸 Chot lagi — Kitna khoon aa raha hai?
 
A) Thoda (band ho sakta)
B) Zyada (lagatar aa raha)
C) Bahut zyada (band nahi ho raha)""")
 
    # ── JALAN / BURN ─────────────────────────────────────────
    elif any(word in text for word in ["jalan", "burn", "jala", "aag"]) or text == "3":
        user_state[chat_id] = "jalan"
        bot.send_message(chat_id,
"""🔥 Jalan hui — Kitna bada hissa jala?
 
A) Thoda (ungli/haath ka chhota hissa)
B) Zyada (haath/pair ka bada hissa)
C) Bahut zyada (seena/peeth/chehra)""")
 
    # ── A / B / C — State ke hisaab se reply ─────────────────
    elif text in ["a", "a)"] and state:
        if state == "bukhar":
            bot.send_message(chat_id,
"""✅ Ghabrao mat — Yeh normal hai.
 
Abhi karo:
1. Paani aur ORS zyada piyo
2. Aaram karo — school/kaam mat jao
3. Mathe pe geela kapda rakho
4. Agar 2 din mein theek na ho → Doctor dikhao
 
⚠️ DISCLAIMER: Yeh sirf prarambhik jankari hai.
Doctor se zaroor milein.""")
 
        elif state == "chot":
            bot.send_message(chat_id,
"""✅ Ghabrao mat — Halki chot hai.
 
Abhi karo:
1. Saaf paani se dhoo
2. Saaf kapde se 5-10 min dabao
3. Antiseptic lagao
4. Bandage karo
 
⚠️ Agar dard badhe ya sujan aaye → Doctor dikhao""")
 
        elif state == "jalan":
            bot.send_message(chat_id,
"""✅ Ghabrao mat — Halki jalan hai.
 
Abhi karo:
1. 20 min thande paani mein rakho (BARF NAHI!)
2. Toothpaste / Tel / Ghee BILKUL MAT lagao
3. Saaf kapde se dhako
4. Chhale mat phodo
 
⚠️ Agar sujan badhe → Doctor dikhao""")
 
        user_state[chat_id] = None
 
    elif text in ["b", "b)"] and state:
        if state == "bukhar":
            bot.send_message(chat_id,
"""⚠️ Dhyan do — Yeh serious ho sakta hai.
 
Abhi karo:
1. Paani/ORS baar baar piyo
2. Mathe + baahon pe thanda kapda
3. Halke kapde pehno
4. Akele mat raho
 
🔴 3 din se zyada? → Doctor zaroor dikhao
📞 Health Helpline: 104 (Free)
 
⚠️ DISCLAIMER: Sirf prarambhik jankari hai.""")
 
        elif state == "chot":
            bot.send_message(chat_id,
"""⚠️ Dhyan do — Thodi gehri chot hai.
 
Abhi karo:
1. Saaf kapde se kaskar dabao (10-15 min)
2. Haath/pair upar uthao
3. Kapda bhigo jaye toh upar se aur kapda rakho
4. Doctor ke paas jao — tanka lag sakta hai
 
📞 Helpline: 104 (Free)""")
 
        elif state == "jalan":
            bot.send_message(chat_id,
"""⚠️ Dhyan do — Badi jalan hai.
 
Abhi karo:
1. 20 min thande paani se dhoo
2. Kapde dheeray utaaro (chipke toh mat kheecho)
3. Toothpaste/Tel NAHI lagana
4. ABHI doctor ke paas jao
 
📞 Helpline: 104 (Free)""")
 
        user_state[chat_id] = None
 
    elif text in ["c", "c)"] and state:
        if state == "bukhar":
            bot.send_message(chat_id,
"""🚨 EMERGENCY — TURANT ACTION LO!
 
ABHI KARO:
1. 📞 108 CALL KARO — Ambulance (FREE)
2. Mathe pe thanda kapda rakho
3. Kapde dhile karo
4. Kuch khilao/pilao MAT
5. Akele mat chodo
 
📞 108 — Ambulance (FREE)
📞 104 — Health Helpline (FREE)
 
⚠️ Bot band karo aur 108 DIAL KARO ABHI!""")
 
        elif state == "chot":
            bot.send_message(chat_id,
"""🚨 EMERGENCY — TURANT ACTION LO!
 
ABHI KARO:
1. 📞 108 CALL KARO — Ambulance (FREE)
2. Saaf kapde se kaskar dabao
3. Hilao mat — leitao rakho
4. Kuch khilao/pilao MAT
5. Akele mat chodo
 
📞 108 — Ambulance (FREE)""")
 
        elif state == "jalan":
            bot.send_message(chat_id,
"""🚨 EMERGENCY — TURANT ACTION LO!
 
ABHI KARO:
1. 📞 108 CALL KARO — Ambulance (FREE)
2. Thande paani se dhote raho
3. Kapde mat kheecho — chipke toh rehne do
4. Akele mat chodo
 
📞 108 — Ambulance (FREE)
⚠️ Bot band karo aur 108 DIAL KARO ABHI!""")
 
        user_state[chat_id] = None
 
    # ── UNRECOGNIZED ──────────────────────────────────────────
    else:
        bot.send_message(chat_id,
"""Samajh nahi aaya 🙏
 
Likhiye:
1 → Bukhar (Fever)
2 → Chot / Khoon
3 → Jalan (Burn)
 
Ya /start dabao.""")
 
# Bot start
print("✅ Sahayak Bot chal raha hai...")
print("🟢 Ctrl+C se band karein")
bot.polling(none_stop=True)
 