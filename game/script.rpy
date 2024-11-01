# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default rune_emotion = "Blush"
default aura_emotion = "Smile"
default gisha_emotion = "Evil"
default faramir_emotion = "Happy"
image rune = "images/sprites/rune/Girl_[rune_emotion].png"
image aura = "images/sprites/aura/Boy_[aura_emotion].png"
image gisha = "images/sprites/gisha/Female_[gisha_emotion].png"
image faramir = "images/sprites/faramir/Male_[faramir_emotion].png"
image monster = "images/sprites/werewolf.png"

define s = Character("Narrator")
define r = Character("Rune")
define a = Character("Aura")
define g = Character("Gisha")
define f = Character("Faramir")
define m = Character("Monster")
define anon = Character("???")

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# The game starts here.

# Mulai permainan
label start:
  play music gamemusic

  # Menampilkan latar belakang hutan
  scene forest1 with fade

  # Menampilkan deskripsi awal
  s "Rune, gadis kecil pemalu dengan rambut hitam panjang yang hampir menutupi wajahnya, sedang berjalan sendirian di pinggir hutan Elir."
  s "Hutan itu dipenuhi pepohonan tinggi dan bayang-bayang misterius yang bergerak-gerak di antara semak-semak. Meskipun takut, ada sesuatu yang menariknya semakin masuk ke dalam."

  # Menampilkan Rune yang pemalu
  show rune at center with dissolve
  r "(menarik napas) Hutan ini... terasa aneh, tapi aku harus melanjutkan..."

  # Menampilkan Aura yang mendekat dengan ekspresi penasaran
  show rune at left with moveinleft
  show aura at right with dissolve
  anon "Hei, kamu ngapain di sini sendirian, anak kecil? Kamu gak takut?"

  # Mengubah ekspresi Rune menjadi lebih pemalu
  r "(berbisik sambil menunduk) Aku... cuma jalan-jalan..."

  # Menampilkan Gisha yang datang dengan ekspresi tegas
  hide rune
  hide aura
  show gisha at center with dissolve
  anon "Aura! Berhenti menakuti orang!"

  # Aura merespon dengan santai
  show gisha at left with moveinleft
  show aura at right with moveinright
  a "(tertawa pelan) Santai aja, Gisha. Aku cuma tanya."

  # Gisha berbicara pada Rune
  hide aura
  show gisha at center with dissolve
  g "(beralih pada Rune) Namamu siapa, anak kecil? Kenapa kamu masuk ke hutan ini?"

  # Rune memilih responsnya
  menu:
    "Berterus terang pada Gisha":
      # Pilihan ini menyebabkan Rune mengungkapkan dirinya pada Gisha
      hide gisha
      show rune at center with dissolve
      r "Namaku... Rune. Aku merasa hutan ini memanggilku..."
      show rune at left with moveinleft
      show gisha at right with moveinright
      g "Hmm... Hutan memang memiliki misteri, tetapi kamu harus berhati-hati."

      # Reaksi Aura
      hide rune
      hide gisha
      show aura at center with dissolve
      a "Menarik! Jadi kamu merasa ada yang memanggilmu?"
        
    "Berbohong untuk menyembunyikan ketakutannya":
      # Pilihan ini menyebabkan Rune menutupi ketakutannya
      hide gisha
      show rune at center with dissolve
      r "Aku... hanya ingin melihat-lihat. Tidak ada yang khusus."
      show rune at left with moveinleft
      show gisha at right with moveinright
      g "Benarkah? Di hutan ini, orang asing biasanya memiliki alasan tersendiri."

      # Reaksi Aura
      hide rune
      hide gisha
      show aura at center with dissolve
      a "Tapi kelihatannya kamu takut, Rune. Tidak apa-apa, kami akan menemanimu!"

  # Menampilkan Faramir yang mendekat dengan ekspresi ramah
  hide aura
  show faramir at center with dissolve
  anon "Ah, lihat siapa yang kita temui! Rune, bukan? Kita bertemu lagi ya."
  anon "Jangan takut pada Aura dan Gisha, mereka memang suka bercanda dan galak."

  # Rune tersenyum tipis
  show rune at right with dissolve
  show faramir at left with moveinleft
  r "Paman Faramir?! Terima kasih, Paman…"

  # Melanjutkan ke pilihan respons terhadap Faramir
  menu:
    "Bertanya tentang hutan pada Faramir":
      hide faramir
      show rune at center with dissolve
      r "Paman Faramir, apa ada sesuatu yang istimewa di hutan ini?"
      hide rune
      show faramir at center with dissolve
      f "Ah, banyak sekali cerita tentang hutan Elir ini."
      f "Banyak misteri dan juga keajaiban yang tersembunyi. Suatu saat, kamu mungkin akan mengetahuinya sendiri."

    "Meminta Faramir untuk menemani":
      hide faramir
      show rune at center with dissolve
      r "Paman Faramir, bisakah aku ikut dengan kalian?"
      hide rune
      show faramir at center with dissolve
      f "Hmm.. Tapi ingat, hutan ini juga punya banyak rahasia. Kita harus berhati-hati."

  # Deskripsi suasana setelah pertemuan
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Sejak pertemuan itu, Rune mulai merasa lebih nyaman. Tanpa disadari, takdir mulai mengikat mereka dalam sebuah perjalanan penuh misteri dan petualangan."

  # Mengakhiri adegan pertama
  jump chapter_two

  # Label untuk bab kedua
label chapter_two:
  # Menampilkan latar belakang hutan yang lebih dalam
  scene forest2 with fade

  # Dialog awal saat mereka berjalan di dalam hutan
  s "Aura yang selalu penuh semangat memimpin mereka semakin dalam ke hutan, diikuti oleh Rune yang semakin penasaran."
  s "Gisha mengawasi di belakang dengan tatapan waspada, sementara Faramir berjalan dengan tenang, mengawasi mereka semua."

  show aura at center with dissolve
  a "Hutan ini punya banyak rahasia, kan? Mungkin kita bisa menemukan sesuatu yang keren!"

  show aura at left with moveinleft
  show gisha at right with dissolve
  g "(mengerutkan dahi) Aura, kita bukan di sini untuk bermain. Jangan sampai tersesat."

  show faramir at center with dissolve
  f "Aura benar, tapi juga dengarkan Gisha. Di hutan Elir, kita harus berhati-hati."

  # Menampilkan latar kolam besar
  scene pool with dissolve

  # Dialog saat mereka tiba di kolam tua
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Mereka tiba di sebuah kolam besar dengan bangunan kuno berada di sekelilingnya."
  s "Rune tiba-tiba merasakan sesuatu yang aneh dan mendekati kolam itu."

  show rune at center with dissolve
  r "(sambil menyentuh air kolam) Seperti… ada yang memanggilku…"

  # Reaksi Aura dan Gisha
  hide rune
  show aura at left with dissolve
  a "(bingung) Apa maksudmu, Rune?"
  show gisha at right with dissolve
  g "Apa yang kamu rasakan, Rune?"

  # Faramir memberikan petunjuk tentang kolam tua
  show faramir at center with dissolve
  f "Instingmu benar, Rune. Suasana daerah ini berbeda dari yang lain."

  # Rune mengalami kejadian ajaib dengan kolam
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Tiba-tiba, cahaya lembut muncul dari air kolam itu saat Rune menyentuh airnya."
  s "Cahaya itu seperti menelusuri tubuh Rune, dan semua yang ada di situ melihatnya dengan terkejut."

  # Pilihan untuk Rune merespons kejadian ajaib tersebut
  menu:
    "Rune merasa takut dan mundur":
      show rune at center with dissolve
      r "Aku… aku tidak tahu mengapa ini terjadi! Aku merasa takut!"
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Tidak perlu takut, Rune. Kolam ini hanya menunjukkan siapa dirimu yang sebenarnya."

      # Reaksi Aura dan Gisha yang mencoba menenangkan Rune
      hide rune
      hide faramir
      show aura at left with dissolve
      a "Aku yakin kamu akan baik-baik saja, Rune. Kami di sini bersamamu!"
      show gisha at right with dissolve
      g "Benar, kamu tidak sendirian, Rune."

    "Rune merasa penasaran dan bertanya pada Faramir":
      show rune at center with dissolve
      r "(penasaran) Paman Faramir, mengapa air kolam ini bereaksi padaku?"
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "(tersenyum samar) Sepertinya air kolam ini menyimpan kekuatan yang hanya bisa dibangkitkan olehmu, Rune."
      f "Mungkin, hutan ini telah memilihmu untuk suatu alasan yang akan kita ketahui nanti."

      # Reaksi Aura yang penuh antusiasme
      hide rune
      hide faramir
      show aura at center with dissolve
      a "Keren! Mungkin Rune punya kekuatan khusus yang bisa bantu kita!"

    "Rune mencoba menyembunyikan rasa terkejutnya":
      show rune at center with dissolve
      r "(berusaha tenang) Mungkin hanya kebetulan… aku tidak tahu apa yang terjadi."
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "(tersenyum) Terkadang, kebetulan adalah petunjuk dari hutan ini."
      f "Kamu akan memahami ini lebih baik seiring berjalannya waktu."

      # Reaksi Aura dan Gisha yang sedikit bingung
      hide rune
      hide faramir
      show aura at left with dissolve
      a "Kalau begitu, mungkin kita harus menjaga Rune lebih baik!"
      show gisha at right with dissolve
      g "Ya, kita akan tetap waspada. Hutan ini mungkin punya rahasia lain."

  # Melanjutkan cerita setelah pilihan
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Aura dan Gisha menyadari bahwa Rune mungkin memiliki hubungan khusus dengan Hutan Elir."

  # Mengakhiri bab kedua
  jump chapter_three

  # Label untuk bab ketiga
label chapter_three:
  # Menampilkan latar pagi hari di hutan
  scene forest3 with fade

  # Narasi awal dan dialog Rune tentang mimpinya
  s "Setelah kejadian di kolam kuno, Rune mulai bermimpi tentang kejadian-kejadian aneh di hutan Elir."
  s "Ia melihat bayangan-bayangan yang tampak mengawasi mereka, dan suara lembut yang memanggilnya dari dalam kegelapan."
  s "Pagi harinya, Rune membagikan mimpinya pada yang lain."

  show rune at center with dissolve
  r "Aku bermimpi tentang sosok-sosok gelap di hutan. Mereka seperti sedang menunggu kita…"

  # Reaksi Aura, Gisha, dan Faramir
  show rune at left with moveinleft
  show aura at right with dissolve
  a "(tertawa) Ah, itu cuma mimpi, Rune. Mungkin kamu terlalu banyak pikiran."

  show gisha at center with dissolve
  g "(serius) Tidak, Aura. Kita harus waspada. Mimpi bisa menjadi pertanda."

  hide rune
  hide aura
  show gisha at left with moveinleft
  show faramir at right with dissolve
  f "Gisha benar. Mimpi di hutan Elir seringkali menunjukkan masa depan. Tetap berhati-hatilah."

  hide rune 
  hide aura
  hide gisha
  hide faramir
  # Pilihan untuk Rune merespons reaksi teman-temannya
  menu:
    "Rune merasa takut dan bertanya lebih lanjut":
      show rune at center with dissolve
      r "Apakah ini berarti kita dalam bahaya, Paman Faramir?"
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Kita tidak bisa memastikan, Rune, tapi lebih baik kita tetap waspada. Hutan Elir selalu penuh misteri."

      # Reaksi Aura dan Gisha
      show aura at center with dissolve
      a "Hei, jangan takut, Rune! Aku ada di sini untuk melindungimu."
      hide rune 
      hide aura
      hide faramir
      show gisha at center with dissolve
      g "(mengangguk) Aura benar, tapi kita tetap harus hati-hati."

    "Rune merasa penasaran dan ingin tahu lebih banyak tentang mimpinya":
      show rune at center with dissolve
      r "Apakah mimpi-mimpi ini bisa menunjukkan sesuatu yang akan terjadi?"
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Terkadang, mimpi di hutan ini memang menyingkap masa depan."
      f "Jika mimpi itu terus berulang, mungkin hutan ini sedang berusaha memberimu pesan."

      # Reaksi Aura dan Gisha
      show aura at center with dissolve
      a "Pesan dari hutan? Kedengarannya menarik, ya, Rune?"
      hide rune 
      hide aura
      hide faramir
      show gisha at center with dissolve
      g "Menarik, tapi bisa juga berbahaya. Kita harus berhati-hati!"

    "Rune mencoba mengabaikan mimpinya":
      show rune at center with dissolve
      r "Mungkin kamu benar, Aura. Mungkin itu hanya mimpi biasa."
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Mungkin saja, Rune. Tapi tetaplah berhati-hati, karena hutan ini sering memberi tanda dalam berbagai cara."

      # Reaksi Gisha yang tetap waspada
      hide rune 
      hide aura
      hide faramir
      show gisha at center with dissolve
      g "Ya, lebih baik kita bersiap untuk apa pun. Hutan Elir tidak seperti hutan-hutan lainnya."

  # Melanjutkan cerita setelah pilihan
  hide rune 
  hide aura
  hide gisha
  hide faramir
  s "Aura mulai menyadari bahwa perjalanan mereka lebih dari sekadar petualangan biasa."
  s "Mereka memutuskan untuk melanjutkan dengan lebih waspada, sementara Rune semakin yakin ada sesuatu yang harus ia temukan di hutan ini."

  # Mengakhiri bab ketiga
  jump chapter_four

# Label untuk bab keempat
label chapter_four:
  # Menampilkan latar gelap di hutan
  scene forest4 with fade

  # Narasi awal tentang suasana hutan yang mulai menegangkan
  s "Dalam perjalanan mereka, suara gemerisik terdengar di sekitar mereka. Aura, yang biasanya berani, kini terlihat lebih hati-hati."
  s "Tiba-tiba, dari balik pepohonan, muncul makhluk aneh dengan mata merah menyala, mengintimidasi mereka."

  m "Grrrr... Hssssss..."
  # Dialog karakter saat makhluk muncul
  show aura at center with dissolve
  a "Apa-apaan itu?!"

  show aura at left with moveinleft
  show gisha at right with dissolve
  g "Jangan panik! Pegang senjata kalian!"

  show faramir at center with dissolve
  f "Tenang, ini makhluk penjaga hutan. Selama kita tidak mengganggu mereka, kita aman."

  # Makhluk mulai mendekat, dan Rune menjadi ketakutan
  hide aura
  hide gisha
  hide faramir
  show rune at center with dissolve
  r "Apa yang akan terjadi pada kita?"

  hide rune
  show aura at center with dissolve
  a "Aku tidak akan membiarkan mereka menyentuh Rune!"

  # Aura melindungi Rune, dan makhluk mundur
  hide rune
  hide aura
  hide gisha
  hide faramir
  show monster at center with dissolve
  s "Dengan keberanian dan tekad, Aura mengambil posisi bertahan, dan makhluk itu mundur setelah beberapa saat."
  s "Keberanian Aura membuat Rune merasa lebih aman, sementara Faramir dan Gisha menatap kagum pada tekad Aura."

  # Dialog Faramir setelah situasi mereda
  hide monster
  show faramir at center with dissolve
  f "Kalian sudah membuktikan diri sebagai teman yang setia. Itu yang terpenting."

  hide faramir
  # Menu pilihan untuk Rune
  menu:
    "Rune merasa kagum pada Aura":
      show rune at center with dissolve
      r "Terima kasih, Aura. Kau benar-benar luar biasa."
      show rune at left with moveinleft
      show aura at right with dissolve
      a "Itu sudah tugasku. Kita semua saling melindungi di sini."

    "Rune merasa ketakutan dan masih gemetar":
      show rune at center with dissolve
      r "(gemetar) Aku... masih takut..."
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Tidak apa-apa, Rune. Rasa takut adalah hal yang wajar. Kami semua di sini untuk menjaga satu sama lain."

    "Rune ingin belajar lebih banyak tentang makhluk hutan":
      show rune at center with dissolve
      r "(penasaran) Apa mereka sering muncul di hutan ini, Paman Faramir?"
      show rune at left with moveinleft
      show faramir at right with dissolve
      f "Ya, makhluk-makhluk ini adalah penjaga hutan. Mereka tidak akan menyakiti kita selama kita tidak menantang mereka."

  # Melanjutkan cerita setelah pilihan
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Setelah peristiwa itu, kelompok mereka melanjutkan perjalanan dengan hati-hati, masing-masing dari mereka menyadari pentingnya menjaga persahabatan dan keberanian dalam menghadapi bahaya."

  # Mengakhiri bab keempat
  jump chapter_five

# Label untuk bab kelima
label chapter_five:
  # Menampilkan latar altar di tengah hutan
  scene altar with fade

  # Narasi awal tentang altar kuno di hutan Elir
  s "Esok hari, setelah pengalaman mengerikan malam itu, mereka akhirnya tiba di pusat hutan Elir, di mana sebuah altar kuno berdiri di antara pepohonan yang rimbun."
  s "Altar itu dihiasi simbol-simbol yang memancarkan cahaya lembut, seolah menyambut kedatangan mereka. Rune merasa ada yang harus dia lakukan, seolah-olah ada kekuatan dalam dirinya yang ingin keluar."

  # Dialog Faramir yang mengarahkan Rune untuk mendengarkan pesan hutan
  show faramir at center with dissolve
  f "Rune, kamu sudah dipilih oleh hutan ini. Mungkin sekarang saatnya kamu mendengarkan apa yang ingin dikatakannya padamu."

  # Rune mendengarkan suara dalam dirinya dan merasakan tujuan mereka di hutan Elir
  hide faramir
  show rune at center with dissolve
  r "(menutup mata) Kita di sini untuk melindungi Hutan Elir... dan juga untuk menjaga agar makhluk-makhluk jahat tidak keluar dari dalamnya."

  # Reaksi dari Aura dan Gisha
  show rune at left with moveinleft
  show aura at right with dissolve
  a "(terkejut) Aku gak nyangka. Ternyata kita… punya takdir bersama di hutan ini."
  
  hide rune
  show aura at left with moveinleft
  show gisha at right with dissolve
  g "Jadi, kita memang sudah ditakdirkan untuk sampai di sini?!"

  # Faramir mengonfirmasi perasaan mereka dan menjelaskan takdir mereka sebagai penjaga hutan
  hide aura
  hide gisha
  show faramir at center with dissolve
  f "Ya. Takdir kalian sudah terikat dengan hutan Elir. Dan mulai sekarang, kalian adalah penjaga hutan ini."

  # Menu pilihan untuk respons Rune
  hide faramir
  menu:
    "Rune merasa bangga dan menerima tanggung jawab tersebut":
      show rune at center with dissolve
      r "(tersenyum bangga) Aku siap melindungi hutan ini. Ini adalah takdir yang harus kita jalani bersama."

    "Rune merasa takut akan tanggung jawab ini":
      show rune at center with dissolve
      r "(gemetar) Tapi... bagaimana jika aku gagal? Tanggung jawab ini terlalu besar untukku..."
      show faramir at center with dissolve
      f "Jangan khawatir, Rune. Kita adalah teman, semua ada di sini untuk saling mendukung."

    "Rune merasa terkejut tapi yakin pada teman-temannya":
      show rune at center with dissolve
      r "(terharu) Ini mengejutkan, tapi aku percaya pada kalian semua. Kita bisa lakukan ini bersama-sama."

  # Narasi akhir bab dan persiapan untuk petualangan mereka sebagai penjaga hutan
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Dengan penuh keyakinan, mereka berdiri di depan altar, menyatukan tangan."
  s "Dari sinilah petualangan mereka sebagai penjaga hutan Elir dimulai."
  s "Bersambung."

  # Mengakhiri bab kelima
  return