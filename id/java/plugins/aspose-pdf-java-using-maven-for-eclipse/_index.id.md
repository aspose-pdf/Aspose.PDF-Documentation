---
title: Aspose.PDF Java menggunakan Maven untuk Eclipse
type: docs
weight: 80
url: /java/aspose-pdf-java-using-maven-for-eclipse/
lastmod: "2021-06-05"
---

## Pengantar

### Eclipse IDE

Eclipse IDE adalah Lingkungan Pengembangan Terpadu Java (IDE) yang terkenal. IDE ini adalah produk paling dikenal dari proyek Eclipse Open Source. Saat ini, ini adalah lingkungan pengembangan terkemuka untuk Java dengan pangsa pasar sekitar 60%.

Eclipse IDE dapat diperluas dengan komponen perangkat lunak tambahan. Eclipse menyebut komponen perangkat lunak ini sebagai Plug-in. Beberapa proyek Open Source dan perusahaan telah memperluas Eclipse IDE atau membuat aplikasi mandiri (Eclipse RCP) di atas kerangka kerja Eclipse.

### Aspose.PDF untuk Java

[Aspose.PDF untuk Java](https://products.aspose.com/pdf/java/) adalah API pembuatan dokumen PDF yang kuat yang memungkinkan aplikasi Java Anda untuk membaca, menulis, dan memanipulasi dokumen PDF tanpa menggunakan Adobe Acrobat.

Aspose.PDF untuk Java menawarkan kekayaan fitur yang luar biasa, termasuk opsi kompresi PDF, pembuatan dan manipulasi tabel, dukungan grafik, fungsi gambar, fungsionalitas hyperlink yang luas, kontrol keamanan yang diperluas, dan penanganan font kustom.

### Aspose.PDF Java (Maven) untuk Eclipse

- Aspose.PDF Java (Maven) untuk Eclipse adalah Plugin untuk **Eclipse IDE** oleh **Aspose.** Plugin ini ditujukan untuk pengembang yang menggunakan platform Maven untuk pengembangan Java dan ingin menggunakan Aspose.PDF untuk Java dalam proyek mereka. Plugin ini memungkinkan Anda membuat proyek maven untuk menggunakan Aspose.PDF untuk Java API dan juga mengunduh [Contoh Kode](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) dari API.
- Plugin ini menyediakan fitur-fitur berikut untuk bekerja dengan Aspose.PDF untuk Java API dalam **Eclipse IDE** dengan nyaman:

![todo:image_alt_text](https://i.imgur.com/KWKGljg.png)

**WIZARD**:
Plugin ini berisi dua wizard

**Proyek Aspose.PDF Maven (wizard)**

- Wizard Proyek Baru ini memungkinkan pengembang membuat proyek **Maven** untuk menggunakan Aspose.PDF untuk Java dari Baru -> Proyek -> Maven-> Proyek Aspose.PDF Maven.

- Referensi dari ketergantungan maven Aspose.PDF untuk Java API secara otomatis diambil dari [Repositori Maven Aspose Cloud](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo) dan ditambahkan di pom.xml.
- Proyek yang dibuat akan selalu mengandung versi terbaru yang tersedia dari **Maven** Dependency untuk Aspose.PDF for Java API.
- Langkah-langkah wizard juga hadir dengan opsi untuk mengunduh [Contoh Kode](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) untuk menggunakan Aspose.PDF for Java API.
Contoh Kode Aspose.PDF (wizard)

- Wizard File Baru ini memungkinkan Anda untuk menyalin [Contoh Kode](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) yang telah diunduh ke dalam proyek Anda untuk menggunakan Aspose.PDF for Java dari New -> Other -> Java -> Aspose.PDF Code Example.
- Contoh yang tersedia ditampilkan dalam format pohon di mana pengguna dapat memilihnya secara kategoris.
- Semua contoh dalam kategori yang dipilih akan disalin ke folder paket proyek "**com.aspose.pdf.examples**" bersama dengan sumber daya yang dibutuhkan dalam folder "**src/main/resources**" yang diperlukan untuk menjalankan contoh-contoh tersebut.
- Contoh Kode Aspose.PDF for Java API dimaksudkan untuk mendemonstrasikan berbagai fungsi dari API tersebut.

- Wizard juga akan mencari dan memperbarui Contoh Kode baru yang tersedia dari repositori contoh Aspose.PDF for Java.

## Persyaratan Sistem dan Platform yang Didukung

### Persyaratan Sistem

- **Memori Sistem:** 2 GB atau lebih (Direkomendasikan)
- **OS:** Sistem operasi apa pun yang mendukung Java VM (Virtual Machine)
- **Koneksi Internet:** 2 MB atau lebih cepat (Direkomendasikan)

### Platform yang Didukung

- Eclipse Mars.1 (4.5.1) - Direkomendasikan
- Eclipse Juno atau yang lebih baru.

## Mengunduh

### Mengunduh Eclipse IDE

Anda perlu menginstal Eclipse IDE terlebih dahulu sebelum mengunduh plugin Aspose.PDF Java (Maven) untuk Eclipse.

Untuk mengunduh Eclipse IDE

1. Pergi ke [https://eclipse.org](https://eclipse.org/).
1. Unduh dan instal Eclipse IDE yang direkomendasikan untuk pengembang Java SE / EE.

### Mengunduh Aspose.PDF Java (Maven) untuk Eclipse

Berikut adalah tiga metode yang direkomendasikan untuk pengunduhan dan instalasi plugin Aspose.PDF Java (Maven) untuk Eclipse yang berhasil:

- Instalasi drag and drop dari [Eclipse Marketplace](https://marketplace.eclipse.org/content/asposepdf-java-maven-eclipse) ke ruang kerja Eclipse Anda.

- Atau pergi ke **Help** > **Install New Software...** > Masukkan URL situs pembaruan berikut di **Work with
Kemudian pilih "Aspose.PDF Java (Maven) untuk Eclipse" dan **Finish**. Terima Perjanjian Lisensi dan Instal plugin.

## Menginstal

Menginstal Aspose.PDF Java (Maven) untuk Eclipse

## Menggunakan Plugin

Menggunakan Aspose.PDF Java (Maven) untuk Eclipse

### Bagaimana cara menerapkan Lisensi Aspose?

Plugin ini menggunakan versi evaluasi dari Aspose.PDF. Setelah Anda puas dengan evaluasi Anda, Anda dapat membeli lisensi di [situs web Aspose](https://purchase.aspose.com/buy). Untuk menghapus pesan evaluasi dan batasan fitur, lisensi produk harus diterapkan. Anda akan menerima file lisensi setelah Anda membeli produk. Silakan ikuti langkah-langkah di bawah ini untuk menerapkan lisensi

- Pastikan file lisensi dinamai sebagai Aspose.PDF.Java.lic
- Letakkan file **Aspose.PDF.Java.lic** di folder yang berisi Aspose.PDF.jar
- Gunakan kode berikut untuk mengaktifkan lisensi:

{{< highlight java >}}

License license = new License();

license.setLicense("Aspose.PDF.Java.lic");

{{< /highlight >}}

## Dukungan, Perluasan, dan Kontribusi

### Dukungan

- Jika Anda ingin melihat masalah yang diketahui/dilaporkan (oleh pengguna atau tim Q.A) dalam plugin.
- Atau Anda ingin melaporkan masalah yang Anda temukan dalam plugin
- Memiliki saran peningkatan atau ingin membuat permintaan fitur

Silakan ikuti [**Pelacak Masalah GitHub**](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues) untuk mencatat masalah yang ditemukan dalam plugin.

### Perluas dan Berkontribusi

Aspose.PDF Java (Maven) untuk Eclipse bersifat open source dan kode sumbernya tersedia di situs web pengkodean sosial utama yang terdaftar di bawah ini. Pengembang didorong untuk mengunduh kode sumber dan berkontribusi dengan menyarankan atau menambahkan fitur baru atau meningkatkan yang sudah ada sehingga orang lain juga dapat mengambil manfaat darinya. Pengembang juga dapat belajar darinya untuk membuat plugin mereka sendiri.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_Maven_for_Eclipse)

### Cara mengkonfigurasi kode sumber Aspose.PDF Java (Maven) untuk Eclipse

Langkah-langkah sederhana di bawah ini akan dengan lancar mengarahkan ke konfigurasi yang berhasil dari kode sumber plugin **"Aspose.PDF Java (Maven) untuk Eclipse"** di Eclipse IDE

1. Unduh / Klon kode sumber.
1. Pilih **File** > Import > General > Existing Projects into Workspace
1. Telusuri ke sumber proyek terbaru yang telah Anda unduh
1. Pilih Proyek Eclipse yang ingin Anda impor
1. Klik Selesai
1. Kode plugin Aspose.PDF Java untuk Eclipse sekarang siap untuk ditingkatkan.