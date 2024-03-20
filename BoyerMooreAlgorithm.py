UKURAN_ABJAD = 256


def heuristikKarakterBuruk(string, ukuran):
	'''
	Fungsi pra-pemrosesan untuk
	heuristik karakter buruk Boyer Moore
	'''

	# Inisialisasi semua kemunculan sebagai -1
	karakterBuruk = [-1]*UKURAN_ABJAD

	# Isi nilai aktual kemunculan terakhir
	for i in range(ukuran):
		karakterBuruk[ord(string[i])] = i

	# kembalikan list yang diinisialisasi
	return karakterBuruk


def pencarian(teks, pola):
	'''
	Fungsi pencarian pola yang menggunakan Heuristik Karakter Buruk
	dari Algoritma Boyer Moore
	'''
	m = len(pola)
	n = len(teks)

	# buat list karakter buruk dengan memanggil
	# fungsi pra-pemrosesan heuristikKarakterBuruk()
	# untuk pola yang diberikan
	karakterBuruk = heuristikKarakterBuruk(pola, m)

	# s adalah pergeseran pola terhadap teks
	s = 0
	while(s <= n-m):
		j = m-1

		# Terus kurangi indeks j dari pola saat
		# karakter pola dan teks cocok
		# pada pergeseran s ini
		while j >= 0 and pola[j] == teks[s+j]:
			j -= 1

		# Jika pola hadir pada pergeseran saat ini,
		# maka indeks j akan menjadi -1 setelah loop di atas
		if j < 0:
			print("Pola ditemukan pada pergeseran = {}".format(s))

			''' 
				Pergeseran pola sehingga karakter berikutnya dalam teks
				selaras dengan kemunculan terakhirnya di dalam pola.
				Kondisi s+m < n diperlukan untuk kasus ketika
				pola terjadi di akhir teks
			'''
			s += (m-karakterBuruk[ord(teks[s+m])] if s+m < n else 1)
		else:
			'''
			Pergeseran pola sehingga karakter buruk dalam teks
			selaras dengan kemunculan terakhirnya di dalam pola. Fungsi
			maksimum digunakan untuk memastikan bahwa kita mendapatkan
			pergeseran positif. Kita mungkin mendapatkan pergeseran negatif
			jika kemunculan terakhir karakter buruk dalam pola ada di sebelah kanan
			karakter saat ini.
			'''
			s += max(1, j-karakterBuruk[ord(teks[s+j])])


# Program utama untuk menguji fungsi di atas
def utama():
	teks = "ABAAABCD"
	pola = "ABC"
	pencarian(teks, pola)


if __name__ == '__main__':
	utama()
