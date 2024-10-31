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
define anon = Character("???")

image bg forest = "images/backgrounds/forest.png"

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# The game starts here.

# Mulai permainan
label start:
  play music gamemusic

  # Menampilkan latar belakang hutan
  scene bg forest with fade

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
  anon "Ah, lihat siapa yang kita temui! Rune, bukan? Senang bertemu denganmu."
  anon "Jangan takut pada Aura dan Gisha, mereka memang suka bercanda dan galak."

  # Rune tersenyum tipis
  show rune at right with dissolve
  show faramir at left with moveinleft
  r "(tersenyum tipis) Terima kasih, Paman…"

  # Melanjutkan ke pilihan respons terhadap Faramir
  menu:
    "Bertanya tentang hutan pada Faramir":
      hide faramir
      show rune at center with dissolve
      r "Paman Faramir, apa ada sesuatu yang istimewa di hutan ini?"
      hide rune
      show faramir at center with dissolve
      f "Ah, banyak sekali cerita tentang hutan Elir ini."
      f "Banyak misteri dan juga keajaiban yang tersembunyi. Suatu hari, kamu mungkin akan mengetahuinya sendiri."

    "Meminta Faramir untuk menemani":
      hide faramir
      show rune at center with dissolve
      r "Paman Faramir, bisakah Paman menemani aku ke dalam?"
      hide rune
      show faramir at center with dissolve
      f "(tersenyum) Tentu, Rune. Tapi ingat, hutan ini juga punya banyak rahasia. Kita harus berhati-hati."

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

  # Menampilkan latar pohon besar
  scene forest3 with dissolve

  # Dialog saat mereka tiba di pohon tua
  s "Mereka tiba di sebuah pohon besar dengan akar yang menjalar ke mana-mana. Rune tiba-tiba merasakan sesuatu yang aneh dan mendekati pohon itu."

  show rune at center
  r "(sambil menyentuh kulit pohon) Seperti… ada yang memanggilku…"

  # Reaksi Aura dan Gisha
  hide rune
  show aura at left
  a "(bingung) Apa maksudmu, Rune?"
  show gisha at right
  g "Apa yang kamu rasakan, Rune?"

  # Faramir memberikan petunjuk tentang pohon tua
  show faramir at center
  f "Instingmu benar, Rune. Pohon ini berbeda dari yang lain."

  # Rune mengalami kejadian ajaib dengan pohon
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Tiba-tiba, cahaya lembut muncul dari pohon itu saat Rune menyentuh batangnya. Cahaya itu seperti menelusuri tubuh Rune, dan semua yang ada di situ melihatnya dengan terkejut."

  # Pilihan untuk Rune merespons kejadian ajaib tersebut
  menu:
    "Rune merasa takut dan mundur":
      r "(terkejut) Aku… aku tidak tahu mengapa ini terjadi! Aku merasa takut!"
      show faramir at center
      f "Tidak perlu takut, Rune. Pohon ini hanya menunjukkan siapa dirimu yang sebenarnya."

      # Reaksi Aura dan Gisha yang mencoba menenangkan Rune
      show aura at left
      a "Aku yakin kamu akan baik-baik saja, Rune. Kami di sini bersamamu!"
      show gisha at right
      g "(mencoba tersenyum) Benar, kamu tidak sendirian, Rune."

    "Rune merasa penasaran dan bertanya pada Faramir":
      r "(penasaran) Paman Faramir, mengapa pohon ini bereaksi padaku?"
      show faramir at center
      f "(tersenyum samar) Sepertinya pohon ini menyimpan kekuatan yang hanya bisa dibangkitkan olehmu, Rune. Mungkin, hutan ini telah memilihmu untuk suatu alasan yang akan kita ketahui nanti."

      # Reaksi Aura yang penuh antusiasme
      show aura at left
      a "Keren! Mungkin Rune punya kekuatan khusus yang bisa bantu kita!"

    "Rune mencoba menyembunyikan rasa terkejutnya":
      r "(berusaha tenang) Mungkin hanya kebetulan… aku tidak tahu apa yang terjadi."
      show faramir at center
      f "(tersenyum) Terkadang, kebetulan adalah petunjuk dari hutan ini. Kamu akan memahami ini lebih baik seiring berjalannya waktu."

      # Reaksi Aura dan Gisha yang sedikit bingung
      show aura at left
      a "Kalau begitu, mungkin kita harus menjaga Rune lebih baik!"
      show gisha at right
      g "Ya, kita akan tetap waspada. Hutan ini mungkin punya rahasia lain."

  # Melanjutkan cerita setelah pilihan
  hide rune
  hide aura
  hide gisha
  hide faramir
  s "Aura dan Gisha menyadari bahwa Rune mungkin memiliki hubungan khusus dengan Hutan Elir."

  # Mengakhiri bab kedua
  return

  # Label untuk bab ketiga
label chapter_three:
  # Menampilkan latar pagi hari di hutan
  scene bg forest_day with fade

  # Narasi awal dan dialog Rune tentang mimpinya
  s "Setelah kejadian di pohon, Rune mulai bermimpi tentang kejadian-kejadian aneh di hutan Elir. Ia melihat bayangan-bayangan yang tampak mengawasi mereka, dan suara lembut yang memanggilnya dari dalam kegelapan."
  s "Esok harinya, Rune membagikan mimpinya pada yang lain."

  show rune worried at left
  r "Aku bermimpi tentang sosok-sosok gelap di hutan. Mereka seperti sedang menunggu kita…"

  # Reaksi Aura, Gisha, dan Faramir
  show aura laugh at right
  a "(tertawa) Ah, itu cuma mimpi, Rune. Mungkin kamu terlalu banyak pikiran."

  show gisha serious at center
  g "(serius) Tidak, Aura. Kita harus waspada. Mimpi bisa menjadi pertanda."

  show faramir calm at left
  f "Gisha benar. Mimpi di hutan Elir seringkali menunjukkan masa depan. Tetap berhati-hatilah."

  # Pilihan untuk Rune merespons reaksi teman-temannya
  menu:
    "Rune merasa takut dan bertanya lebih lanjut":
      r "(ketakutan) Apakah ini berarti kita dalam bahaya, Paman Faramir?"
      show faramir calm at center
      f "Kita tidak bisa memastikan, Rune, tapi lebih baik kita tetap waspada. Hutan Elir selalu penuh misteri."

      # Reaksi Aura dan Gisha
      show aura laugh at right
      a "Hei, jangan takut, Rune! Aku ada di sini untuk melindungimu."
      show gisha serious at left
      g "(mengangguk) Aura benar, tapi kita tetap harus hati-hati."

    "Rune merasa penasaran dan ingin tahu lebih banyak tentang mimpinya":
      r "(penasaran) Apakah mimpi-mimpi ini bisa menunjukkan sesuatu yang akan terjadi?"
      show faramir calm at center
      f "Terkadang, mimpi di hutan ini memang menyingkap masa depan. Jika mimpi itu terus berulang, mungkin hutan ini sedang berusaha memberimu pesan."

      # Reaksi Aura dan Gisha
      show aura laugh at right
      a "Pesan dari hutan? Kedengarannya menarik, ya, Rune?"
      show gisha serious at left
      g "(serius) Menarik, tapi bisa juga berbahaya. Kita harus berhati-hati."

    "Rune mencoba mengabaikan mimpinya":
      r "(tersenyum tipis) Mungkin kamu benar, Aura. Mungkin itu hanya mimpi biasa."
      show faramir calm at center
      f "Mungkin saja, Rune. Tapi tetaplah berhati-hati, karena hutan ini sering memberi tanda dalam berbagai cara."

      # Reaksi Gisha yang tetap waspada
      show gisha serious at right
      g "Ya, lebih baik kita bersiap untuk apa pun. Hutan Elir tidak seperti hutan-hutan lainnya."

  # Melanjutkan cerita setelah pilihan
  s "Aura mulai menyadari bahwa perjalanan mereka lebih dari sekadar petualangan biasa. Mereka memutuskan untuk melanjutkan dengan lebih waspada, sementara Rune semakin yakin ada sesuatu yang harus ia temukan di hutan ini."

  # Mengakhiri bab ketiga
  return

# Label untuk bab keempat
label chapter_four:
  # Menampilkan latar gelap di hutan
  scene bg forest_dark with fade

  # Narasi awal tentang suasana hutan yang mulai menegangkan
  s "Dalam perjalanan mereka, suara gemerisik terdengar di sekitar mereka. Aura, yang biasanya berani, kini terlihat lebih hati-hati."
  s "Tiba-tiba, dari balik pepohonan, muncul makhluk aneh dengan mata merah menyala, mengintimidasi mereka."

  # Dialog karakter saat makhluk muncul
  show aura brave at left
  a "Apa-apaan itu?!"

  show gisha serious at right
  g "(serius) Jangan panik! Pegang senjata kalian dan jangan bergerak."

  show faramir calm at center
  f "Tenang, ini makhluk penjaga hutan. Selama kita tidak mengganggu mereka, kita aman."

  # Makhluk mulai mendekat, dan Rune menjadi ketakutan
  show monster at center with dissolve
  show rune scared at left
  r "(ketakutan) Apa yang akan terjadi pada kita?"

  show aura brave at right
  a "(berani) Aku tidak akan membiarkan mereka menyentuh Rune!"

  # Aura melindungi Rune, dan makhluk mundur
  show monster with dissolve
  s "Dengan keberanian dan tekad, Aura mengambil posisi bertahan, dan makhluk itu mundur setelah beberapa saat. Keberanian Aura membuat Rune merasa lebih aman, sementara Faramir dan Gisha menatap kagum pada tekad Aura."

  # Dialog Faramir setelah situasi mereda
  show faramir calm at center
  f "Kalian sudah membuktikan diri sebagai teman yang setia. Itu yang terpenting."

  # Menu pilihan untuk Rune
  menu:
    "Rune merasa kagum pada Aura":
      r "(terharu) Terima kasih, Aura. Kau benar-benar teman yang luar biasa."
      show aura brave at right
      a "(tersenyum) Itu sudah tugasku. Kita semua saling melindungi di sini."

    "Rune merasa ketakutan dan masih gemetar":
      r "(gemetar) Aku... masih takut..."
      show faramir calm at center
      f "Tidak apa-apa, Rune. Rasa takut adalah hal yang wajar. Kami semua di sini untuk menjaga satu sama lain."

    "Rune ingin belajar lebih banyak tentang makhluk hutan":
      r "(penasaran) Apa mereka sering muncul di hutan ini, Paman Faramir?"
      show faramir calm at left
      f "Ya, makhluk-makhluk ini adalah penjaga hutan. Mereka tidak akan menyakiti kita selama kita tidak menantang mereka."

  # Melanjutkan cerita setelah pilihan
  s "Setelah peristiwa itu, kelompok mereka melanjutkan perjalanan dengan hati-hati, masing-masing dari mereka menyadari pentingnya menjaga persahabatan dan keberanian dalam menghadapi bahaya."

  # Mengakhiri bab keempat
  return

# Label untuk bab kelima
label chapter_five:
  # Menampilkan latar altar di tengah hutan
  scene bg altar_forest with fade

  # Narasi awal tentang altar kuno di hutan Elir
  s "Pagi hari, setelah pengalaman mengerikan malam itu, mereka akhirnya tiba di pusat hutan Elir, di mana sebuah altar kuno berdiri di antara pepohonan yang rimbun."
  s "Altar itu dihiasi simbol-simbol yang memancarkan cahaya lembut, seolah menyambut kedatangan mereka. Rune merasa ada yang harus dia lakukan, seolah-olah ada kekuatan dalam dirinya yang ingin keluar."

  # Dialog Faramir yang mengarahkan Rune untuk mendengarkan pesan hutan
  show faramir wise at left
  f "Rune, kamu sudah dipilih oleh hutan ini. Mungkin sekarang saatnya kamu mendengarkan apa yang ingin dikatakannya padamu."

  # Rune mendengarkan suara dalam dirinya dan merasakan tujuan mereka di hutan Elir
  show rune determined at center
  r "(menutup mata) Kita di sini untuk melindungi Hutan Elir... dan juga untuk menjaga agar makhluk-makhluk jahat tidak keluar dari dalamnya."

  # Reaksi dari Aura dan Gisha
  show aura surprised at left
  a "(terkejut) Aku gak nyangka. Ternyata kita… punya takdir bersama di hutan ini."

  show gisha curious at right
  g "(penasaran) Jadi, kita memang sudah ditakdirkan untuk sampai di sini?"

  # Faramir mengonfirmasi perasaan mereka dan menjelaskan takdir mereka sebagai penjaga hutan
  show faramir wise at left
  f "Ya. Takdir kalian sudah terikat dengan hutan Elir. Dan mulai sekarang, kalian adalah penjaga hutan ini."

  # Menu pilihan untuk respons Rune
  menu:
    "Rune merasa bangga dan menerima tanggung jawab sebagai penjaga":
      r "(tersenyum bangga) Aku siap melindungi hutan ini. Ini adalah takdir yang harus kita jalani bersama."

    "Rune merasa takut akan tanggung jawab ini":
      r "(gemetar) Tapi... bagaimana jika aku gagal? Tanggung jawab ini terlalu besar untukku..."
      show faramir wise at left
      f "Jangan khawatir, Rune. Kami semua ada di sini untuk saling mendukung."

    "Rune merasa terkejut tapi yakin pada teman-temannya":
      r "(terharu) Ini mengejutkan, tapi aku percaya pada kalian semua. Kita bisa lakukan ini bersama-sama."

  # Narasi akhir bab dan persiapan untuk petualangan mereka sebagai penjaga hutan
  s "Dengan penuh keyakinan, mereka berdiri di depan altar, menyatukan tangan. Dari sinilah petualangan mereka sebagai penjaga hutan Elir dimulai, dengan tekad untuk melindungi rahasia-rahasia hutan dari ancaman apa pun yang datang."

  # Mengakhiri bab kelima
  return