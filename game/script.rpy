# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Narrator")

default rune_emotion = "Blush"
default aura_emotion = "Smile"
default gisha_emotion = "Evil"
default faramir_emotion = "Happy"
image rune = "images/sprites/rune/Girl_[rune_emotion].png"
image aura = "images/sprites/aura/Boy_[aura_emotion].png"
image gisha = "images/sprites/gisha/Female_[gisha_emotion].png"
image faramir = "images/sprites/faramir/Male_[faramir_emotion].png"

define r = Character("Rune")
define a = Character("Aura")
define g = Character("Gisha")
define f = Character("Faramir")

image bg forest = "images/backgrounds/forest.png"

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# The game starts here.

# Mulai permainan
label start:
  play music gamemusic

  # Latar belakang hutan
  scene bg forest

  # Menampilkan karakter di layar
  show gisha with dissolve

  # Dialog dimulai
  g "Ada yang tidak beres. Pohon ini... auranya berubah."
  
  # Menampilkan karakter Gisha di sebelah kiri dengan ekspresi serius
  $ gisha_emotion = "Surprised"
  g "Sepertinya ada yang mencoba mencuri kekuatan pohon ini."

  # Menampilkan karakter Aura di sebelah kanan dengan ekspresi bersemangat
  $ aura_emotion = "Smile"
  show gisha at left with dissolve
  show aura at right with dissolve
  a "Siapapun mereka, aku yakin bisa menghajar mereka!"

  # Mengubah ekspresi Rune yang pemalu
  $ rune_emotion = "Blush"
  hide gisha
  show rune at left with dissolve
  r "Tapi... bagaimana kalau kekuatan itu lebih kuat dari kita?"

  # Mengubah ekspresi Faramir yang menenangkan di sebelah kanan
  $ faramir_emotion = "Happy"
  hide rune
  hide aura
  show faramir at center with dissolve
  f "Tenang saja. Selama kita bersama, kita pasti bisa mengatasinya."

  # Mengubah ekspresi Gisha menjadi berpikir serius
  $ gisha_emotion = "Confused"
  hide faramir
  show gisha with dissolve
  g "Aura, ini bukan saatnya bermain-main. Kita harus menyusun rencana."

  # Mengubah ekspresi Aura menjadi santai
  $ aura_emotion = "Evil"
  hide gisha
  show aura with dissolve
  a "Baiklah, tapi jangan salahkan aku kalau aku jadi yang pertama menyerang!"

  # Menyembunyikan semua karakter untuk melanjutkan scene berikutnya
  hide gisha
  hide rune
  hide aura
  hide faramir

  # Melanjutkan cerita
  return
