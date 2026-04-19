import telebot
import os
 
bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN", "TUMHARA_TOKEN_YAHAN"))
 
# State yaad rakhne ke liye
user_state = {}
 
# ─────────────────────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def start(message):
    user_state[message.chat.id] = None
    bot.send_message(message.chat.id,
"""🙏 Namaste! Main Sahayak hoon.
Mediokart | Buxar, Bihar 🇮🇳
 
Aapko kya problem hai? Likhiye:
 
1️⃣ Bukhar (Fever)
2️⃣ Chot / Khoon (Injury)
3️⃣ Jalan (Burn)
4️⃣ Dil ka Daura (Heart Attack) ❤️
5️⃣ Saanp / Keeda Kaatna 🐍
6️⃣ Brain Haemorrhage / Stroke 🧠
7️⃣ Pregnancy Emergency 🤰
8️⃣ Pet Dard / Ulti / Dast 🤢
9️⃣ Chakkar / Behoshi 😵
 
📍 /pharmacy — Paas mein pharmacy dhundho
🚑 /ambulance — Paas mein ambulance dhundho
🏥 /doctor — Free online doctor
🆘 /emergency — Sabhi emergency numbers
 
⚠️ Yeh jankari WHO, MoHFW aur Red Cross
guidelines par aadharit hai.
Serious situation mein 108 zaroor call karein.""")
 
# ─────────────────────────────────────────────────────────────
# /emergency
# ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['emergency'])
def emergency(message):
    bot.send_message(message.chat.id,
"""🚨 EMERGENCY NUMBERS — INDIA
 
📞 108 — Ambulance (FREE)
📞 102 — Pregnancy / Maternity (FREE)
📞 104 — Health Helpline (FREE)
📞 112 — Police / Fire / Ambulance
📞 1800-180-1104 — Poison Control (FREE)
📞 9152987821 — iCall Mental Health
 
⚡ Jab tak ambulance aaye:
• Mareez ko leitaayein
• Ghabrao mat — shant rahein
• Khaana / paani mat dein
• Akele mat chhodein
 
📌 Source: MoHFW, Govt. of India""")
 
# ─────────────────────────────────────────────────────────────
# /pharmacy — OpenStreetMap se (FREE, no API key)
# ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['pharmacy'])
def pharmacy(message):
    bot.send_message(message.chat.id,
"""💊 Paas mein Pharmacy Dhundho
 
🗺️ OpenStreetMap (FREE):
https://www.openstreetmap.org/search?query=pharmacy
 
🏪 Jan Aushadhi Store (Govt — Sasti Dawa):
https://janaushadhi.gov.in/StoreLocator.aspx
 
🗺️ Google Maps:
https://www.google.com/maps/search/medical+store+near+me
 
💡 Jan Aushadhi mein 50-90% sasti
generic medicines milti hain!
 
📌 Source: Jan Aushadhi, Govt. of India""")
 
# ─────────────────────────────────────────────────────────────
# /ambulance — OpenStreetMap se nearest hospital
# ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['ambulance'])
def ambulance_cmd(message):
    bot.send_message(message.chat.id,
"""🚑 Ambulance / Nearest Hospital
 
📞 ABHI 108 CALL KARO (FREE)
 
🗺️ Paas mein hospital dhundho (FREE):
https://www.openstreetmap.org/search?query=hospital
 
🗺️ Google Maps:
https://www.google.com/maps/search/hospital+near+me
 
🏥 PHC / CHC / Sadar Hospital —
Sabse paas wala Govt hospital FREE hai!
 
⚡ 108 call karo — woh location track
karke khud aayenge!""")
 
# ─────────────────────────────────────────────────────────────
# /doctor
# ─────────────────────────────────────────────────────────────
@bot.message_handler(commands=['doctor'])
def doctor_cmd(message):
    bot.send_message(message.chat.id,
"""🏥 Free Online Doctor
 
🆓 eSanjeevani (Govt of India — BILKUL FREE):
https://esanjeevani.mohfw.gov.in
 
🗺️ Paas mein doctor:
https://www.openstreetmap.org/search?query=clinic
 
📱 Google Maps:
https://www.google.com/maps/search/doctor+near+me
 
💡 eSanjeevani pe video call se
doctor se baat karo — FREE hai!
 
📌 Source: MoHFW, Govt. of India""")
 
# ─────────────────────────────────────────────────────────────
# MAIN HANDLER
# ─────────────────────────────────────────────────────────────
@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id
    text = message.text.lower().strip()
    state = user_state.get(chat_id)
 
    # ══ 1. BUKHAR ════════════════════════════════════════════
    if any(w in text for w in ["bukhar","fever","bukhaar","temperature","tap"]) or text == "1":
        user_state[chat_id] = "bukhar"
        bot.send_message(chat_id,
"""🌡️ Bukhar hai — Temperature kitna hai?
 
A) Halka (99-101°F)
B) Zyada (101-103°F)
C) Bahut zyada (103°F+) — emergency""")
 
    # ══ 2. CHOT / KHOON ══════════════════════════════════════
    elif any(w in text for w in ["chot","khoon","bleeding","cut","injury","ghav","lagi"]) or text == "2":
        user_state[chat_id] = "chot"
        bot.send_message(chat_id,
"""🩸 Chot lagi — Kitna khoon aa raha hai?
 
A) Thoda (band ho sakta)
B) Zyada (lagatar aa raha)
C) Bahut zyada (band nahi ho raha)""")
 
    # ══ 3. JALAN / BURN ══════════════════════════════════════
    elif any(w in text for w in ["jalan","burn","jala","aag","jhulsa"]) or text == "3":
        user_state[chat_id] = "jalan"
        bot.send_message(chat_id,
"""🔥 Jalan hui — Kitna bada hissa jala?
 
A) Thoda (ungli/haath ka chhota hissa)
B) Zyada (haath/pair ka bada hissa)
C) Bahut zyada (seena/peeth/chehra)""")
 
    # ══ 4. HEART ATTACK ══════════════════════════════════════
    elif any(w in text for w in ["heart attack","dil ka daura","seene mein dard","chest pain","dil","cardiac"]) or text == "4":
        user_state[chat_id] = None
        bot.send_message(chat_id,
"""❤️ DIL KA DAURA — HEART ATTACK
🚨 TURANT 108 CALL KARO!
 
⚡ Jab tak ambulance aaye:
1. Bithao — seedhe, aaram se
2. Kapde dhile karo — belt, tie, button
3. Shant rakho — ghabrao mat
4. Agar hosh hai → ek aspirin (300mg)
   chaba ke khilaao (allergy na ho toh)
5. Agar hosh nahi + saanso nahi →
   CPR shuru karo TURANT:
   • Seene ke beech haath rakho
   • 30 baar tezi se dabaao
   • 2 baar saanso do
   • Repeat karo jab tak help aaye
 
❌ YEH MAT KARO:
• Akela mat chodo
• Khaana/paani mat do
• Letaao mat (bithao)
 
📞 108 — Ambulance (FREE) — ABHI!
📞 112 — Alternative emergency
 
📌 Source: Fortis Healthcare, MoHFW,
Indian Red Cross Society Guidelines""")
 
    # ══ 5. SAANP / KEEDA ═════════════════════════════════════
    elif any(w in text for w in ["saanp","snake","keeda","bichhu","scorpion","kutta","dog bite","kaata","dasa","daank"]) or text == "5":
        user_state[chat_id] = None
        bot.send_message(chat_id,
"""🐍 SAANP / KEEDA KAATNA
🚨 TURANT 108 CALL KARO!
 
⚡ ABHI KARO:
1. HILNA MAT — pulse slow karo
   (hilne se zeher tezi se failta hai)
2. Kaate hisse ko dil se NEECHE rakho
3. Tight kapde / jewellery / ghadi hatao
4. Kaate jagah ko saaf kapde se
   dheeray se dhako — dabaao nahi
5. Saanp ka rang/size yaad rakho
   (doctor ko batana hoga)
6. Akele mat raho
 
❌ YEH BILKUL MAT KARO:
• Daant se zeher mat choosna ❌
• Kaata jagah mat kaatna/jalana ❌
• Tight bandage mat lagana ❌
• Barf/thanda NAHI lagana ❌
• Khaana/paani NAHI dena ❌
• Traditional healer ke paas
  time waste mat karna ❌
 
📞 108 — Ambulance (FREE) — ABHI!
🏥 Govt hospital mein Anti-Snake
   Venom (ASV) FREE milta hai!
 
📌 Source: MoHFW Standard Treatment
Guidelines — Snake Bite Management,
NCDC Guidelines 2017""")
 
    # ══ 6. BRAIN HAEMORRHAGE / STROKE ════════════════════════
    elif any(w in text for w in ["brain","stroke","laqwa","paralysis","haemorrhage","hemorrhage","brain attack","ek taraf","muh tedha","baat nahi","samajh nahi"]) or text == "6":
        user_state[chat_id] = None
        bot.send_message(chat_id,
"""🧠 BRAIN HAEMORRHAGE / STROKE
🚨 TURANT 108 CALL KARO!
 
⚡ FAST Test se pehchano:
F — Face: Chehra ek taraf tedha?
A — Arms: Ek haath uthane mein dikkat?
S — Speech: Baat karne mein dikkat?
T — Time: Haan → TURANT 108!
 
⚡ ABHI KARO:
1. 📞 108 CALL KARO — ABHI!
2. Leitao — sar thoda upar rakho
3. Tight kapde dhile karo
4. Agar ulti ho → karwat pe leto
5. Khaana/paani BILKUL MAT do
6. Akele mat chodo
7. Time note karo — kab symptoms shuru
 
❌ YEH MAT KARO:
• Aspirin/koi dawa mat do
• Letne se uthao mat
• Ghar pe mat rakho — HOSPITAL ZAROOR
 
⏱️ Golden Hour: Pehle 4.5 ghante mein
   hospital pahuncho — bahut zaroori!
 
📞 108 — Ambulance (FREE)
 
📌 Source: MoHFW Stroke Guidelines,
AIIMS Emergency Protocols,
WHO Stroke Management Guidelines""")
 
    # ══ 7. PREGNANCY EMERGENCY ════════════════════════════════
    elif any(w in text for w in ["pregnancy","pregnant","delivery","prasav","labour","labor","dard utha","pani toot","baby","bachcha","garbh"]) or text == "7":
        user_state[chat_id] = "pregnancy"
        bot.send_message(chat_id,
"""🤰 Pregnancy Emergency — Kya ho raha hai?
 
A) Pet mein dard / contractions
B) Paani toot gaya (water break)
C) Khoon aa raha hai""")
 
    # ══ 8. PET DARD / ULTI / DAST ════════════════════════════
    elif any(w in text for w in ["pet","ulti","dast","vomit","loose motion","diarrhea","matli","nausea","pait"]) or text == "8":
        user_state[chat_id] = "pet"
        bot.send_message(chat_id,
"""🤢 Pet ki problem — Kya ho raha hai?
 
A) Sirf pet dard
B) Ulti aa rahi hai
C) Dast lag rahe hain (loose motion)""")
 
    # ══ 9. CHAKKAR / BEHOSHI ══════════════════════════════════
    elif any(w in text for w in ["chakkar","behoshi","behosh","faint","girna","unconscious","hosh nahi","dizzy"]) or text == "9":
        user_state[chat_id] = "chakkar"
        bot.send_message(chat_id,
"""😵 Chakkar / Behoshi — Kya situation hai?
 
A) Sirf chakkar aa raha (hosh hai)
B) Behosh hone wala hai
C) Behosh hai — hosh nahi aa raha""")
 
    # ══════════════════════════════════════════════════════════
    # A / B / C REPLIES — State ke hisaab se
    # ══════════════════════════════════════════════════════════
 
    elif text in ["a","a)"] and state:
 
        if state == "bukhar":
            bot.send_message(chat_id,
"""✅ Halka Bukhar — Ghabrao mat.
 
Abhi karo:
1. Paani aur ORS zyada piyo
2. Aaram karo
3. Mathe pe geela kapda rakho
4. Halke kapde pehno
5. 2 din mein theek na ho → Doctor
 
⚠️ Disclaimer: Yeh prarambhik jankari hai.
📌 Source: WHO First Aid Guidelines,
National Health Portal India (nhp.gov.in)""")
 
        elif state == "chot":
            bot.send_message(chat_id,
"""✅ Halki Chot — Ghabrao mat.
 
Abhi karo:
1. Saaf paani se achhi tarah dhoo
2. Saaf kapde se 5-10 min dabao
3. Antiseptic lagao (Dettol/Savlon)
4. Bandage karo
 
⚠️ Sujan aaye ya dard badhe → Doctor
📌 Source: Indian Red Cross First Aid Manual""")
 
        elif state == "jalan":
            bot.send_message(chat_id,
"""✅ Halki Jalan — Ghabrao mat.
 
Abhi karo:
1. 20 min thande paani mein rakho
   (BARF NAHI — sirf thanda paani!)
2. Toothpaste/Tel/Ghee BILKUL MAT lagao
3. Saaf kapde se dhako
4. Chhale mat phodo
 
⚠️ Sujan badhe → Doctor zaroor
📌 Source: WHO Burn Management Guidelines,
Indian Red Cross Society""")
 
        elif state == "pregnancy":
            bot.send_message(chat_id,
"""🤰 Contractions / Pet Dard
 
Abhi karo:
1. 📞 102 CALL KARO (FREE — Maternity)
2. Lait jao — seedhe
3. Contractions ka time note karo
4. Paani piyo
5. Hospital jaane ki taiyari karo
6. Akele mat raho
 
📞 102 — Maternity Ambulance (FREE)
📞 108 — Ambulance (FREE)
📌 Source: MoHFW Maternal Health Guidelines""")
 
        elif state == "pet":
            bot.send_message(chat_id,
"""🤢 Pet Dard — Ghabrao mat.
 
Abhi karo:
1. Thoda thoda paani piyo
2. 2-3 ghante khaana band karo
3. Seedhe leto — ghutne mor lo
4. Garam paani ki bottle pet pe rakho
 
🔴 6 ghante baad bhi dard → Doctor
📌 Source: National Health Portal India""")
 
        elif state == "chakkar":
            bot.send_message(chat_id,
"""😵 Chakkar — Ghabrao mat.
 
Abhi karo:
1. Baith jao ya lait jao
2. Thanda paani piyo
3. Khaana nahi khaya → kuch khao
4. Fan/AC ke paas aao
5. Thodi der aaram karo
 
🔴 Baar baar chakkar → Doctor
📌 Source: WHO First Aid Guidelines""")
 
        user_state[chat_id] = None
 
    elif text in ["b","b)"] and state:
 
        if state == "bukhar":
            bot.send_message(chat_id,
"""⚠️ Zyada Bukhar — Dhyan do.
 
Abhi karo:
1. ORS/paani baar baar piyo
2. Thanda kapda mathe + baahon pe
3. Halke kapde pehno
4. Akele mat raho
 
🔴 3 din se zyada → Doctor zaroor
📞 104 — Health Helpline (FREE)
📌 Source: WHO Fever Management,
NHP India Guidelines""")
 
        elif state == "chot":
            bot.send_message(chat_id,
"""⚠️ Gehri Chot — Dhyan do.
 
Abhi karo:
1. Kaskar dabao (15 min)
2. Haath/pair upar uthao
3. Kapda bhige → upar se aur lagao
4. Doctor ke paas jao — tanka lagega
 
📞 104 — Helpline (FREE)
📌 Source: Indian Red Cross First Aid Manual""")
 
        elif state == "jalan":
            bot.send_message(chat_id,
"""⚠️ Badi Jalan — Dhyan do.
 
Abhi karo:
1. 20 min thande paani se dhoo
2. Kapde dheeray utaaro
   (chipke toh mat kheecho)
3. Toothpaste/Tel NAHI
4. ABHI doctor ke paas jao
 
📌 Source: WHO Burn Guidelines""")
 
        elif state == "pregnancy":
            bot.send_message(chat_id,
"""🚨 Paani Toot Gaya — EMERGENCY!
 
ABHI KARO:
1. 📞 102 CALL KARO TURANT!
2. Lait jao
3. Kuch mat khilao/pilao
4. Hospital ke liye nikal jao ABHI
5. Akele mat raho
 
📞 102 — Maternity (FREE)
📞 108 — Ambulance (FREE)
📌 Source: MoHFW Maternal Health Guidelines""")
 
        elif state == "pet":
            bot.send_message(chat_id,
"""🤢 Ulti — Dhyan do.
 
Abhi karo:
1. Thoda thoda paani piyo (ghunt ghunt)
2. ORS piyo — baar baar
3. Solid khaana band karo
4. Thoda uthke baitho — seedhe mat leto
 
🔴 Khoon aaye ulti mein → TURANT 108!
🔴 12 ghante se zyada → Doctor
📌 Source: WHO ORS Guidelines,
NHP India""")
 
        elif state == "chakkar":
            bot.send_message(chat_id,
"""⚠️ Behosh Hone Wala — Sambhalo!
 
ABHI KARO:
1. Bithao ya laitao TURANT
2. Pair thoda upar uthao
3. Tight kapde/belt dhile karo
4. Hawa karo
5. Thoda paani (hosh ho toh)
 
🔴 5 min mein theek na ho → 108
📌 Source: WHO First Aid Guidelines""")
 
        user_state[chat_id] = None
 
    elif text in ["c","c)"] and state:
 
        if state in ["bukhar","chot","jalan"]:
            bot.send_message(chat_id,
"""🚨 EMERGENCY — TURANT ACTION LO!
 
ABHI KARO:
1. 📞 108 CALL KARO — Ambulance (FREE)
2. Akele mat raho
3. Kuch khilao/pilao MAT
4. Leitao rakho — hilao mat
 
📞 108 — Ambulance (FREE)
📞 104 — Health Helpline (FREE)
⚠️ Bot band karo — 108 ABHI DIAL KARO!
📌 Source: MoHFW Emergency Guidelines""")
 
        elif state == "pregnancy":
            bot.send_message(chat_id,
"""🚨 Pregnancy mein Khoon — EMERGENCY!
 
ABHI KARO:
1. 📞 102 CALL KARO TURANT (FREE)
2. 📞 108 bhi call karo
3. Lait jao — pair thoda upar
4. Kuch mat khilao/pilao
5. Akele BILKUL mat raho
 
📞 102 — Maternity (FREE)
📞 108 — Ambulance (FREE)
📌 Source: MoHFW Maternal Health Guidelines""")
 
        elif state == "pet":
            bot.send_message(chat_id,
"""💧 Dast / Loose Motion — Dhyan do.
 
Abhi karo:
1. ORS ZAROOR piyo — baar baar
2. Ghar par ORS:
   1L paani + 6 tsp cheeni + ½ tsp namak
3. Coconut water bhi theek hai
4. Solid khaana band karo
 
🔴 Khoon aaye dast mein → TURANT 108!
🔴 Bachcha 2 saal se chhota → TURANT!
📞 104 — Health Helpline (Free)
📌 Source: WHO ORS Guidelines, UNICEF""")
 
        elif state == "chakkar":
            bot.send_message(chat_id,
"""🚨 BEHOSH HAI — EMERGENCY!
 
ABHI KARO:
1. 📞 108 CALL KARO TURANT!
2. Seedhe laitao — pair upar uthao
3. Gardan seedhi rakho
4. Kuch khilao/pilao BILKUL MAT
5. Saanso nahi → CPR shuru karo:
   • Seene ke beech haath rakho
   • 30 baar tezi se dabaao
   • 2 baar saanso do — repeat
 
📞 108 — Ambulance (FREE)
⚠️ Bot band karo — 108 ABHI DIAL KARO!
📌 Source: WHO CPR Guidelines,
Indian Red Cross Society""")
 
        user_state[chat_id] = None
 
    # ══ UNRECOGNIZED ══════════════════════════════════════════
    else:
        bot.send_message(chat_id,
"""Samajh nahi aaya 🙏
 
Number type karein:
1 → Bukhar
2 → Chot / Khoon
3 → Jalan
4 → Heart Attack ❤️
5 → Saanp / Keeda 🐍
6 → Brain / Stroke 🧠
7 → Pregnancy 🤰
8 → Pet Dard / Ulti
9 → Chakkar / Behoshi
 
Ya /start dabao.""")
 
# ─────────────────────────────────────────────────────────────
print("✅ Sahayak Bot chal raha hai...")
print("📍 Mediokart | Buxar, Bihar")
print("🟢 Ctrl+C se band karein\n")
bot.polling(none_stop=True)
 
