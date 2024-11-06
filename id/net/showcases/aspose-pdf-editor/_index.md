---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
weight: 10
url: id/net/aspose-pdf-editor/
description: Aspose.PDF untuk .NET menunjukkan HTML5 PDF Editor adalah editor PDF berbasis web sumber terbuka.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Apa itu Html5 PDF Editor oleh Aspose.PDF untuk .NET?

HTML5 PDF Editor oleh Aspose.PDF untuk .NET adalah editor PDF berbasis web sumber terbuka yang memungkinkan pengguna untuk membuat, mengedit, dan mengonversi file PDF secara online serta pengguna dapat dengan mudah menyematkan editor tersebut dalam aplikasi web mereka sendiri untuk melihat dan mengedit file PDF. HTML5 PDF Editor dikembangkan menggunakan HTML5, jQuery Ajax, ASP.NET, Bootstrap dan backend didukung oleh Aspose.PDF untuk .NET. Antarmuka pengguna dari editor ini sangat sederhana untuk pemahaman yang mudah dan peningkatan fitur sesuai kebutuhan pengguna.

![Image](../images/aspose-pdf-editor.png)

## Fitur

Saat ini, ia mendukung fitur-fitur berikut:

- Membuat file PDF baru
- Memuat dan Melihat file PDF
- Memuat file PDF dan Gambar dari Dropbox
- Memuat file PDF dan gambar dari Dropbox
- Mengekspor file PDF ke berbagai format file
- Menambahkan atau Menggabungkan file PDF
- Menyisipkan Halaman Baru
- Menghapus Halaman
- Memindahkan Halaman dalam file PDF
- Menyisipkan Teks dalam PDF
- Menyorot Teks dalam PDF
- Memutar Teks yang Disisipkan dalam PDF
- Mencari Teks dalam PDF
- Mengganti Teks dalam PDF
- Menyisipkan Gambar
- Mengubah Ukuran Tanda Tangan dan Gambar
- Menyeret dan Menempatkan item yang disisipkan
- Memuat file PDF dengan bidang formulir
- Mengisi bidang formulir menggunakan Editor
- Menyimpan dan Mengekspor PDF dengan data bidang formulir
- Menyoroti bidang formulir yang diperlukan
- Menambah Lampiran ke file PDF
- Memuat Lampiran dari file PDF masukan
- Mengunduh file Lampiran
- Menghapus file Lampiran
- Menandatangani PDF menggunakan Gambar Tangan Bebas

## Persyaratan Sistem

Sebagai aplikasi Web .NET, HTML5 PDF Editor dikembangkan menggunakan ASP.NET, C#, HTML5, jQuery, Javascript. Anda akan memerlukan lingkungan sistem berikut untuk mengatur HTML5 PDF Editor di pihak Anda.

- Visual Studio 2010 (atau lebih tinggi)
- .NET Framework 3.5 (atau lebih tinggi)
- Aspose.PDF untuk .NET
- Aspose.PDF untuk .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

Anda dapat menggunakan salah satu browser berikut untuk menjalankan aplikasi di ujung Anda:

- Mozilla Firefox (disarankan)
- Internet Explorer (versi 9 atau lebih baru)
- Google Chrome
- Apple Safari

## Dukungan

Kami, di Aspose, memastikan untuk memberikan dukungan terbaik kepada pelanggan / pengguna kami untuk pertanyaan mereka dalam segala hal, baik teknis maupun penjualan. Silakan gunakan tautan di bawah ini untuk setiap pertanyaan terkait lisensi dan penjualan atau pertanyaan teknis.

# Panduan Pengembang Editor PDF

## Membuat File PDF Baru

Selain mengedit dokumen PDF yang ada, Editor PDF Html5 juga mendukung pembuatan file PDF baru dari awal yang dapat Anda lakukan dengan menggunakan opsi Buat File Baru dari bilah menu. Dengan menggunakan fitur ini, Anda dapat membuat PDF kosong di editor, menambahkan beberapa teks/gambar ke dalamnya dan menyimpannya dalam format yang diinginkan. Di bagian berikutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Buat File Baru" diklik pada halaman**

Ketika Anda mengklik item menu "Buat File Baru", metode onNewFileClicked dipanggil dalam file Editor.js.
Ketika Anda mengklik item menu "Buat File Baru", metode onNewFileClicked dipanggil di file Editor.js.

**jQuery - Mengirim permintaan Ajax ke server untuk metode CreateNewFile.**

Lihat tab Editor.js di bawah ini untuk kode sumber metode onNewFileClicked, itu memanggil metode CreateNewFile di file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini dengan kode sumber metode CreateNewFile. Ini menghapus semua data yang ada mengenai file yang sebelumnya dimuat menggunakan metode ResetData.

**Pembuatan file PDF baru menggunakan Aspose.PDF untuk .NET**

Setelah menghapus data menggunakan metode ResetData, metode CreateNewFile membuat file PDF baru menggunakan kelas Document dari Aspose.PDF untuk .NET.
Seperti yang Anda lihat di tab di bawah ini, objek Document sedang menghasilkan file dengan satu halaman kosong. Setelah file dihasilkan di server, file tersebut dikonversi menjadi gambar menggunakan metode ImageConverter untuk dimuat di kanvas.

**Memuat file hasil ke kanvas.**

Setelah file dikonversi menjadi gambar di sisi server, kontrol dikembalikan ke metode onNewFileClicked di Editor.js.
Setelah file dikonversi menjadi gambar di sisi server, kontrol dikembalikan ke metode onNewFileClicked di Editor.js.

## Mengekspor PDF ke Berbagai Format File

HTML5 PDF Editor mendukung ekspor file PDF ke berbagai format file yang dapat Anda lakukan dengan menggunakan opsi Export File dari menu bar. Dengan menggunakan fitur ini, Anda dapat mengekspor file PDF ke format yang Anda inginkan. Di bagian berikutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Export File" diklik di halaman.**

Ketika Anda mengklik item menu "Export File", Anda dapat memilih format ekspor dari daftar. Setelah memilih format ekspor, metode "ExportFile" dipanggil di file Editor.js.

**jQuery - Mengirim permintaan server Ajax untuk metode btnFileExport_Click**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode "ExportFile". Ini mengirim permintaan ke metode server btnFileExport_Click dengan parameter format file di file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini.
Lihat tab Canvas.aspx.cs di bawah ini.

**Ekspor file untuk diunduh di browser klien**

Setelah file dihasilkan di server, kontrol dikembalikan ke metode ExportFile di Editor.js dari mana file dikirim ke browser untuk pengguna mengunduh menggunakan metode ExportToBrowser.

## Menambahkan atau Menggabungkan File PDF

Html5 PDF Editor mendukung penambahan atau penggabungan file PDF yang dapat Anda lakukan dengan menggunakan opsi Append File dari menu bar. Dengan menggunakan fitur ini, Anda dapat menambahkan file PDF ke file input Anda. Di bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Append File" diklik di halaman.**

Ketika Anda mengklik item menu "Append File", Anda dapat mengunggah file menggunakan dialog unggah file. Setelah file diunggah, metode "fileSelected" dipanggil di file Editor.js.

**jQuery - Kirim permintaan server untuk metode ProcessRequest**

Lihat tab Editor.js di bawah ini untuk kode sumber metode "fileSelected".
Lihat tab Editor.js di bawah ini untuk kode sumber dari metode "fileSelected".

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini. Berdasarkan parameter formulir yang diberikan, file yang akan ditambahkan disimpan di server dan metode "AppendFile" dipanggil. Metode AppendFile, menambahkan file yang diunggah menggunakan Aspose.PDF untuk .NET, mengonversi file hasil ke gambar dan mengembalikan kontrol kembali ke metode "fileSelected" di Editor.js

**Perbarui konten kanvas setelah menambahkan file**

Setelah file dihasilkan di server, kontrol dikembalikan ke metode "fileSeleceted" di Editor.js yang memperbarui konten editor.

## Unggah File PDF Lokal

Editor PDF HTML5 mendukung pengunggahan file PDF dari mesin lokal menggunakan opsi Buka Dari Komputer dari bilah menu. Dengan menggunakan fitur ini, Anda dapat membuka file PDF yang ada dan melakukan pengeditan pada file PDF Anda. Di bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Buka Dari Komputer" diklik pada halaman.**
**HTML - "Buka Dari Komputer" item menu diklik pada halaman.**

Ketika Anda mengklik item menu "Buka Dari Komputer", Anda dapat mengunggah file input menggunakan dialog unggah file. Setelah file diunggah, metode "fileSelected" dipanggil di file Editor.js.

**jQuery - Mengirim permintaan server untuk metode ProcessRequest**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode "fileSelected". File diposting ke server dan metode "ProcessRequest" dipanggil di file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini. Berdasarkan parameter formulir yang dilewatkan, file yang akan diunggah disimpan di server, mengatur ulang data menggunakan metode "ResetData" dan metode "ImageConverter" dipanggil. Metode ImageConverter, mengonversi file yang diunggah menjadi gambar menggunakan Aspose.PDF untuk .NET dan mengembalikan kontrol kembali ke metode "fileSelected" di Editor.js

**Perbarui konten kanvas setelah mengunggah file**

Setelah file dihasilkan di server, kontrol dikembalikan ke metode "fileSeleceted" di Editor.js yang memperbarui isi editor yaitu.
## Menambah Halaman dalam File PDF

Menggunakan Html5 PDF Editor, Anda dapat menambah halaman baru ke dalam file PDF menggunakan opsi Tambah Halaman dari menu bar. Dengan fitur ini, Anda dapat menambahkan halaman kosong ke file PDF Anda. Pada bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Tambah Halaman" diklik pada halaman**

Ketika Anda mengklik item menu "Tambah Halaman", metode "AddPage" dipanggil dalam file Editor.js.

**jQuery - Mengirim permintaan Ajax ke server untuk metode AddPage_Click.**

Lihat tab Editor.js di bawah ini untuk kode sumber metode AddPage, itu memanggil metode AddPage_Click dalam file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini dengan kode sumber metode AddPage_Click.
## Menghapus Halaman dari File PDF

Menggunakan Html5 PDF Editor, Anda dapat menghapus halaman dari file PDF menggunakan opsi Hapus Halaman dari bilah menu. Pada bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Hapus Halaman" diklik di halaman**

Ketika Anda mengklik item menu "Hapus Halaman", metode DeletePage dipanggil di file Editor.js.

**jQuery - Mengirim permintaan Ajax ke server untuk metode DeletePage_Click.**

Lihat tab Editor.js di bawah ini untuk kode sumber metode DeletePage, itu memanggil metode DeletePage_Click di file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini dengan kode sumber metode DeletePage_Click. Ini menghapus halaman yang dipilih dari file PDF menggunakan metode Hapus dari koleksi Aspose.PDF.Document.Page.

**Memperbarui konten pengeditan**

Setelah menghapus halaman dari file PDF, kontrol kemudian dikembalikan ke metode DeletePage di file Editor.js yang memperbarui penomoran halaman, menghapus koleksi apa pun yang terkait dengan halaman yang dihapus menggunakan metode updateIndexesDelete.
Setelah menghapus halaman dari file PDF, kontrol kemudian dikembalikan ke metode DeletePage di file Editor.js yang memperbarui penomoran halaman, menghapus koleksi apa pun yang terkait dengan halaman yang dihapus menggunakan metode updateIndexesDelete.

## Memindahkan Halaman dalam File PDF

Menggunakan Html5 PDF Editor, Anda dapat memindahkan halaman dalam file PDF menggunakan opsi Move Page dari menu bar. Setelah Anda menekan item menu Move Page, Anda akan disajikan dengan dialog input untuk menentukan lokasi baru halaman yang dipilih. Di bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Move Page" diklik di halaman**

Ketika Anda mengklik item menu "Move Page", dialog input ditampilkan untuk mendapatkan lokasi baru halaman yang dipilih. Setelah memberikan nomor halaman dan menekan tombol "Move", metode "Move" dipanggil di file Editor.js.

**jQuery - Mengirim permintaan Ajax ke server untuk metode MovePages.**

Lihat tab Editor.js di bawah ini untuk kode sumber metode Move, yang memanggil metode MovePage dan mengirimkan detail seperti bergerak dari, bergerak ke, daftar halaman ke metode MovePages di file CanvasSave.aspx.cs.
**Metode ASP.NET untuk menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini dengan kode sumber dari metode MovePages. Metode ini menggunakan koleksi Aspose.PDF.Document.Pages untuk memindahkan halaman.

**Memperbarui konten yang sedang diedit**

Setelah halaman dipindahkan, kontrol kemudian dikembalikan ke metode MovePage di file Editor.js yang memperbarui indeks halaman dan informasi terkait koleksi yang berbeda di editor menggunakan metode MoveUpdate.

## Menyisipkan Teks dalam Berkas PDF

Menggunakan Html5 PDF Editor, Anda dapat menyisipkan teks dalam berkas PDF menggunakan opsi Text Mode dari menu bar. Setelah Anda memilih item menu Text Mode dan mengklik lokasi mana pun pada editor di mana Anda ingin menambahkan teks, Anda akan disajikan dengan dialog input untuk memasukkan dan memformat teks yang diinginkan seperti yang ditunjukkan di bawah ini:

Pada bagian selanjutnya, kita akan membahas detail teknis di balik fitur ini.
Dalam bagian berikutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - "Text Mode" menu item dipilih di halaman**

Ketika Anda memilih menu item "Text Mode" dan mengklik lokasi yang diinginkan pada editor untuk memasukkan teks dalam file PDF, dialog input ditampilkan untuk mendapatkan teks yang Anda butuhkan untuk dimasukkan di halaman. Setelah memberikan teks dan menekan tombol "OK", metode "saveTextFromArea" dipanggil di file Editor.js.

**Javascript - Dapatkan teks input dari dialog input dan tampilkan di editor.**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode saveTextFromArea, yang mendapatkan teks dari dialog input dan menampilkannya di editor. Juga, menyimpan data dalam koleksi bentuk yang kemudian digunakan di sisi server untuk memasukkan teks ke dalam file PDF. Anda dapat memeriksa kode sumber dari metode saveFile yang dipanggil ketika file disimpan.

**Metode web ASP.NET menangani permintaan server**

Seperti disebutkan di atas, teks akan benar-benar dimasukkan ke dalam file PDF sumber kami ketika kita melakukan operasi simpan yang menggunakan metode GetTextStamp untuk membuat cap teks untuk dimasukkan dalam file PDF.
Seperti yang disebutkan di atas, teks sebenarnya akan dimasukkan ke dalam file PDF sumber kita ketika kita melakukan operasi penyimpanan yang menggunakan metode GetTextStamp untuk membuat cap teks yang akan dimasukkan dalam file PDF.

## Sorot Teks dalam File PDF

Menggunakan Html5 PDF Editor, Anda dapat menyorot teks dalam file PDF menggunakan opsi Mode Sorot dari bilah menu. Setelah Anda memilih item menu Mode Sorot, Anda dapat menyorot teks dan area apa pun menggunakan alat penyorot persegi panjang. Pada bagian selanjutnya, kita akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Mode Sorot" dipilih di halaman**

Ketika Anda memilih item menu "Mode Sorot", Anda dapat menggambar sorotan persegi panjang di sekitar teks atau item apa pun dalam file PDF Anda. Implementasi dari proses ini dapat dilihat pada metode "tools.rect" dalam file Editor.js.

**Javascript - Gambar persegi penyorotan pada editor.**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode tool.rect, yang memungkinkan pengguna untuk menggambar persegi penyorotan di lokasi mana pun pada editor.
Lihat tab Editor.js di bawah ini untuk kode sumber dari metode tool.rect, yang memungkinkan pengguna untuk menggambar persegi panjang penyorot di lokasi mana pun pada editor.

**Metode web ASP.NET menangani permintaan server**

Seperti yang disebutkan di atas, penyorotan sebenarnya dimasukkan ke dalam file PDF sumber kita ketika kita melakukan operasi simpan yang menggunakan metode GetImageStamp untuk memasukkan cap gambar di file PDF sumber di lokasi yang ditentukan pada editor. Lihat tab Canvas.aspx.cs di bawah ini dengan kode sumber dari metode GetImageStamp. Ini menggunakan kelas Aspose.PDF.ImageStamp untuk memasukkan persegi panjang penyorotan ke dalam file PDF.

## Mencari Teks dalam File PDF

Menggunakan Html5 PDF Editor, Anda dapat mencari teks dalam file PDF menggunakan opsi Cari Teks dari bilah menu. Setelah Anda mengklik item menu Cari Teks, Anda akan disajikan dengan kotak dialog untuk memasukkan teks yang akan dicari seperti yang ditunjukkan di bawah ini:

Setelah menyediakan teks dan menekan pencarian, semua instansi kata yang dicari akan disorot seperti yang ditunjukkan di bawah ini:

### Bagaimana cara kerjanya?

**HTML - Item menu "Cari Teks" diklik di halaman**
**HTML - "Menu Item Cari Teks" diklik pada halaman**

Ketika Anda mengklik item menu "Cari Teks", Anda akan disajikan dengan dialog input untuk memasukkan teks yang ingin Anda cari. Setelah memasukkan teks dan menekan tombol cari, metode "Pindah" dipanggil yang memeriksa apakah operasi pindah halaman dilakukan atau operasi pencarian dilakukan kemudian memanggil metode performSearch dalam file Editor.js.

**jQuery - Mengirim permintaan server Ajax untuk metode SearchData**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode performSearch, yang mendapatkan teks input dan permintaan ke metode server SearchData di file _CanvasSave.aspx.cs_.

**Metode web ASP.NET menangani permintaan server**

Lihat tab _Canvas.aspx.cs_ di bawah ini.
Lihat tab _Canvas.aspx.cs_ di bawah ini.

## Mengganti Teks dalam Berkas PDF

Menggunakan Html5 PDF Editor, Anda dapat mengganti teks yang ada dalam berkas PDF menggunakan opsi Ganti Teks dari bilah menu. Setelah Anda mengklik item menu Ganti Teks, Anda akan diberikan kotak dialog untuk memasukkan teks yang akan dicari dan diganti.

### Bagaimana cara kerjanya?

**HTML - Item menu "Ganti Teks" diklik pada halaman**

Ketika Anda mengklik item menu "Ganti Teks", Anda akan diberikan dialog input untuk memasukkan teks yang akan dicari dan diganti. Setelah memasukkan teks dan menekan tombol Ganti, metode "ReplaceText" dipanggil di file Editor.js.

**jQuery - Mengirim permintaan server Ajax untuk metode ReplaceText**

Lihat tab Editor.js di bawah ini untuk kode sumber dari metode ReplaceText, yang mendapatkan teks input dari dialog teks input dan permintaan ke metode server ReplaceText di file CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini.
## Memuat Berkas PDF dengan Form Fields

Menggunakan Html5 PDF Editor, Anda dapat memuat dan bekerja dengan berkas PDF yang mengandung form fields. Setelah berkas dengan form fields dimuat dalam editor, semua form fields dimuat untuk diedit. Pada bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Buka Dari Komputer" diklik pada halaman.**

Ketika Anda mengklik item menu "Buka Dari Komputer", Anda dapat mengunggah berkas masukan yang mengandung form fields menggunakan dialog unggah berkas. Setelah berkas diunggah, metode "fileSelected" dipanggil dalam berkas Editor.js.

**jQuery - Mengirim permintaan server untuk metode ProcessRequest**

Berkas diposting ke server dan metode "ProcessRequest" dipanggil dalam berkas CanvasSave.aspx.cs.

**Metode web ASP.NET menangani permintaan server**

Lihat tab Canvas.aspx.cs di bawah.
Lihat tab Canvas.aspx.cs di bawah ini.

**Memuat kolom formulir di kanvas**

Lihat tab Editor.js di bawah ini, metode manageFields dalam Editor.js digunakan untuk menghasilkan semua kolom di kanvas berdasarkan informasi yang dikirimkan dari sisi server. Ini menggambar kontrol kolom HTML menggunakan jenis dan informasi lokasi dari sisi server ke kanvas.

## Menyoroti Kolom Formulir yang Diperlukan

Menggunakan Html5 PDF Editor, Anda dapat menyoroti kolom formulir yang diperlukan dalam editor. Setelah file dengan kolom formulir dimuat dalam editor, semua kolom formulir yang diperlukan disorot untuk pengguna guna membantu dalam pengeditan. Di bagian selanjutnya, kami akan membahas detail teknis di balik fitur ini.

### Bagaimana cara kerjanya?

**HTML - Item menu "Buka Dari Komputer" diklik di halaman.**

Ketika Anda mengklik item menu "Buka Dari Komputer", Anda dapat mengunggah file input yang mengandung kolom formulir menggunakan dialog unggah file. Setelah file diunggah, metode "fileSelected" dipanggil dalam file Editor.js.

**jQuery - Mengirim permintaan server untuk metode ProcessRequest**
**jQuery - Mengirim permintaan server untuk metode ProcessRequest**

File dikirim ke server dan metode "ProcessRequest" dipanggil dalam file CanvasSave.aspx.cs.

**Metode web ASP.NET mengelola permintaan server**

Lihat tab Canvas.aspx.cs di bawah ini. Berdasarkan parameter formulir yang diberikan, file yang akan diunggah disimpan di server, metode ImageConverter mengonversi file yang diunggah menjadi gambar dan metode "CheckFields" dipanggil yang menggunakan kelas Aspose.PDF.InteractiveFeatures.Forms untuk memeriksa semua bidang formulir dan mengumpulkan informasi mengenai bidang tersebut yaitu. FieldType, Lokasi, dll. Setelah mendapatkan detail dari semua bidang formulir, kita mendapatkan informasi apakah sebuah bidang formulir diperlukan menggunakan metode Aspose.PDF.Facades.IsRequiredField dan mengembalikan koleksi bidang kembali ke metode ImageConverter. Metode ImageConverter mengembalikan kontrol kembali ke metode "fileSelected" di Editor.js

**Memuat bidang formulir di kanvas**

Lihat tab Editor.js di bawah ini, metode manageFields di Editor.js digunakan untuk menghasilkan semua bidang di kanvas berdasarkan informasi yang dikirim kembali dari sisi server.
Lihat tab Editor.js di bawah, metode manageFields dalam Editor.js digunakan untuk menghasilkan semua bidang di kanvas berdasarkan informasi yang dikirim kembali dari sisi server.
