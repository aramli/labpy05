# Praktikum5
Tugas Pemrograman Dasar Pertemuan Ke 10 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Tugas Praktikum
<ul>
  <li>Flowchart</li>
  <img src="https://github.com/aramli/labpy05/raw/main/img/flowchart.png" width="700"/>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy05/raw/main/img/1.png" width="700"/>
  <img src="https://github.com/aramli/labpy05/raw/main/img/2.png" width="700"/>
  <li>Hasil Program</li>
    1. Lihat Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/11.png" width="600"/><br>
    2. Menambahkan Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/12.png" width="600"/><br>
    3. Mengubah Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/13.png" width="600"/><br>
    4. Menghapus Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/14.png" width="600"/><br>
    5. Mencari Data Mahasiswa & Keluar Program<br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/15.png" width="600"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy05/raw/main/img/3.png" width="700"/><br>
  1. Pertama-tama, Program dimulai dengan mencetak judul “PROGRAM INPUT NILAI MAHASISWA” ke layar, agar pengguna memahami konteks aplikasi. Setelah itu, dibuat sebuah dictionary kosong bernama data_mahasiswa yang akan berfungsi sebagai tempat penyimpanan seluruh data mahasiswa, dengan NIM sebagai kunci dan detail nilai sebagai nilai.
<br><br>
 <img src="https://github.com/aramli/labpy05/raw/main/img/4.png" width="700"/><br>
  2. Selanjutnya, Program masuk ke perulangan tak terbatas menggunakan while True. Di dalam loop ini, pengguna diminta memilih opsi melalui input menu. Nilai input kemudian diubah ke huruf kecil dengan .lower() sehingga perbandingan opsi menjadi konsisten, apa pun kapitalisasi yang dimasukkan pengguna.
<br><br>
<img src="https://github.com/aramli/labpy05/raw/main/img/5.png" width="700"/><br>
  3. Jika pengguna memilih opsi ‘k’, program mencetak pesan “Terima kasih telah menggunakan program ini.” dan menjalankan break untuk menghentikan loop. Ini menutup aplikasi dan mengakhiri interaksi.
<br><br>
<img src="https://github.com/aramli/labpy05/raw/main/img/6.png" width="700"/><br>
  4. Ketika opsi ‘t’ dipilih, program meminta pengguna mengisi NIM, nama, serta nilai tugas, UTS, dan UAS. Nilai-nilai yang diinput untuk tugas, UTS, dan UAS dikonversi ke tipe float. Program kemudian menghitung nilai akhir menggunakan bobot: tugas 30%, UTS 35%, dan UAS 35%. Semua data disimpan ke dalam data_mahasiswa dengan NIM sebagai kunci dan sebuah dictionary yang memuat nama dan seluruh komponen nilai sebagai nilai.
<br><br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/7.png" width="700"/><br>
  5. Saat opsi ‘l’ dipilih, program mencetak header tabel dan garis pembatas untuk menampilkan data secara rapi. Jika data_mahasiswa kosong, program menampilkan pesan bahwa tidak ada data. Jika ada data, program menginisialisasi nomor urut no = 1, lalu melakukan iterasi atas setiap pasangan (nim, mhs) dari dictionary. Setiap baris dicetak menggunakan f-string dengan pengaturan alignment: nomor dan angka rata tengah, nama rata kiri, serta angka ditampilkan satu digit desimal. Setelah mencetak satu baris, nomor urut ditingkatkan satu.
<br><br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/8.png" width="700"/><br>
  6. Dengan opsi ‘u’, pengguna diminta mengisi NIM yang akan diubah. Program memeriksa apakah NIM tersebut ada dalam data_mahasiswa. Jika ditemukan, pengguna diminta mengisi ulang nama dan nilai-nilai, lalu nilai akhir dihitung kembali. Data lama diganti dengan data baru pada kunci NIM tersebut. Jika NIM tidak ditemukan, program memberi pesan agar pengguna memeriksa kembali NIM yang dimasukkan.
<br><br>
  <img src="https://github.com/aramli/labpy05/raw/main/img/9.png" width="700"/><br>
  7. Ketika opsi ‘h’ dipilih, program meminta NIM yang akan dihapus. Jika NIM tersebut ada dalam dictionary, data dihapus menggunakan del data_mahasiswa[nim], dan program menginformasikan bahwa data berhasil dihapus. Jika NIM tidak ditemukan, program menampilkan pesan bahwa data tidak tersedia untuk NIM tersebut.
<br><br>
<img src="https://github.com/aramli/labpy05/raw/main/img/10.png" width="700"/><br>
  8. Dengan opsi ‘c’, program meminta NIM yang ingin dicari. Jika kunci NIM ditemukan, program mengambil dictionary data mahasiswa terkait dan mencetak detail lengkapnya, termasuk nama, nilai tugas, UTS, UAS, serta nilai akhir yang ditampilkan dengan satu angka di belakang koma. Jika tidak ditemukan, program menampilkan pesan bahwa data untuk NIM tersebut tidak ada.
<br><br>
</ul>
