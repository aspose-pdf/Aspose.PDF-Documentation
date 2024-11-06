---
title: Mengonversi berbagai format file ke PDF 
linktitle: Mengonversi format file lain ke PDF 
type: docs
weight: 80
url: id/php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: Topik ini menunjukkan cara Aspose.PDF memungkinkan untuk mengonversi format file lain ke dokumen PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Mengonversi EPUB ke PDF

**Aspose.PDF untuk PHP** memungkinkan Anda dengan mudah mengonversi file EPUB ke format PDF.

<abbr title="electronic publication">EPUB</abbr> adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu.

Untuk mengonversi file EPUB ke format PDF, Aspose.PDF untuk PHP memiliki kelas bernama [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) yang digunakan untuk memuat file sumber EPUB.
 Setelah itu, objek diteruskan sebagai argumen ke inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), karena ini membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses konversi file EPUB ke format PDF.

1. Buat [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) EPUB.
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. Simpan dokumen PDF keluaran.

```php
// Buat instance baru dari EpubLoadOptions
$loadOption = new EpubLoadOptions();

// Buat objek Document baru dan muat file EPUB
$document = new Document($inputFile, $loadOption);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Coba ubah EPUB ke PDF secara online**

Aspose.PDF untuk PHP menyajikan aplikasi gratis online ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitasnya.
[![Aspose.PDF Konversi EPUB ke PDF dengan Aplikasi Gratis](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Konversi Markdown ke PDF

{{% alert color="success" %}}
**Coba untuk mengonversi Markdown ke PDF secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["Markdown ke PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi Markdown ke PDF dengan Aplikasi Gratis](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown adalah alat konversi teks ke HTML untuk penulis web. Markdown memungkinkan Anda menulis dalam format teks biasa yang mudah dibaca dan ditulis, lalu mengubahnya menjadi XHTML (atau HTML) yang secara struktural valid.

Cuplikan kode berikut menunjukkan cara menggunakan fungsi ini dengan Aspose.PDF untuk PHP:

```php
// Buat instance baru dari MdLoadOptions
$loadOption = new MdLoadOptions();

// Buat instance baru dari Document dan muat file Markdown input
$document = new Document($inputFile, $loadOption);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```


## Mengubah PCL ke PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer Hewlett-Packard yang dikembangkan untuk mengakses fitur standar printer. PCL tingkat 1 hingga 5e/5c adalah bahasa berbasis perintah yang menggunakan urutan kontrol yang diproses dan diinterpretasikan sesuai urutan penerimaan. Pada tingkat konsumen, aliran data PCL dihasilkan oleh driver cetak. Output PCL juga dapat dengan mudah dihasilkan oleh aplikasi khusus.

{{% alert color="success" %}}
**Cobalah mengubah PCL ke PDF secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["PCL ke PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PCL ke PDF dengan Aplikasi Gratis](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Saat ini, hanya PCL5 dan versi yang lebih lama yang didukung.**

|**Set Perintah**|**Dukungan**|**Pengecualian**|**Deskripsi**|

| :- | :- | :- | :- |
|Perintah kontrol pekerjaan|+|Mode pencetakan dupleks|Mengontrol proses cetak: jumlah salinan, tempat keluaran, pencetakan simplex/dupleks, offset kiri dan atas, dll.|
|Perintah kontrol halaman|+|Perintah Lewati Perforasi|Menentukan ukuran halaman, margin, orientasi halaman antar-baris, jarak antar-karakter, dll.|
|Perintah Pemposisian Kursor|+| |Menentukan posisi kursor dan, dengan demikian, asal usul teks, gambar raster atau vektor dan detail lainnya.|

|Perintah pemilihan font|+|<p>1. Perintah Data Cetak Transparan.</p><p>2. Font lunak tersemat. Dalam versi saat ini, alih-alih membuat font lunak, pustaka kami memilih font yang sesuai dari font TrueType "keras" yang ada yang diinstal pada mesin target. <br>   Kesesuaian ditentukan oleh rasio lebar/tinggi. <br>   Fitur ini hanya berfungsi untuk font Bitmap dan TrueType dan tidak menjamin bahwa teks yang dicetak dengan font lunak akan relevan dengan yang ada di file sumber. <br>   Karena kode karakter dalam font lunak dapat tidak sesuai dengan yang default.</p><p>3. Set Simbol yang Ditentukan Pengguna.</p>|Mengizinkan pemuatan font lunak (tersemat) dari file PCL dan mengelolanya dalam memori.|
|Perintah grafik raster|+|Hanya hitam & putih|Mengizinkan pemuatan gambar raster dari file PCL ke memori, menentukan parameter raster <br>seperti lebar, tinggi, jenis kompresi, resolusi, dll.|
|Perintah warna|+| |Mengizinkan pewarnaan untuk semua objek yang dapat dicetak.|
|Perintah Model Cetak|+| |Mengizinkan pengisian teks, gambar raster, dan area persegi panjang dengan pola raster yang telah ditentukan dan yang ditentukan pengguna, menentukan mode transparansi untuk pola dan gambar raster sumber.
 <br>Polanya yang telah ditentukan sebelumnya adalah arsir, arsir silang, dan bayangan.|
|Perintah pengisian area persegi panjang|+| |Memungkinkan pembuatan dan pengisian area persegi panjang dengan pola.|
|Perintah Grafik Vektor HP-GL/2|+|Perintah Vektor Layar (SV), Perintah Mode Transparansi (TR), Perintah Data Transparan (TD), RO (Memutar Sistem Koordinat), Perintah Font Skala atau Bitmap (SB), Perintah Kemiringan Karakter (SL) dan Ruang Ekstra (ES) tidak diimplementasikan dan perintah DV (Mendefinisikan Jalur Teks Variabel) direalisasikan dalam versi beta.|<p>- Memungkinkan memuat gambar vektor HP-GL/2 dari file PCL ke dalam memori. Vector gambar memiliki titik asal di sudut kiri bawah area cetak, dapat diskalakan, diterjemahkan, diputar, dan dipotong.</p><p>- Sebuah gambar vektor dapat berisi teks, sebagai label, dan bentuk geometris seperti persegi panjang, lingkaran, elips, garis, busur, kurva bezier dan bentuk kompleks yang terdiri dari bentuk sederhana.</p><p>- Bentuk tertutup termasuk huruf dari label dapat diisi dengan isian solid atau pola vektor.</p><p>- Pola dapat berupa hatching, cross-hatch, shading, raster yang ditentukan pengguna, PCL hatching atau cross-hatch dan PCL yang ditentukan pengguna. Pola PCL adalah raster. Label dapat diputar, diskalakan, dan diarahkan secara individual dalam empat arah: atas, bawah, kiri, dan kanan. Arah Kiri dan Kanan melibatkan pengaturan huruf satu demi satu. Arah Atas dan Bawah melibatkan pengaturan huruf satu di bawah lainnya.</p>|
|Macross|―| |Memungkinkan memuat urutan perintah PCL ke dalam memori dan menggunakan urutan ini berkali-kali, misalnya, untuk mencetak header halaman atau mengatur satu format untuk satu set halaman.|
|Unicode text|―| |Memungkinkan pencetakan karakter non-ASCII. Tidak diimplementasikan karena kurangnya file sampel dengan teks Unicode  
PCL6 (PCL-XL) | Direalisasikan hanya dalam versi Beta karena kekurangan file uji. Font yang tersemat juga tidak didukung. Ekstensi JetReady tidak didukung karena tidak mungkin memiliki spesifikasi JetReady. | Format file biner.

### Mengkonversi file PCL menjadi format PDF

Untuk memungkinkan konversi dari PCL ke PDF, [Aspose.PDF untuk PHP](https://products.aspose.com/pdf/php-java) memiliki kelas [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Objek ini kemudian diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin perender PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses mengkonversi file PCL menjadi format PDF.

```php
// Membuat instance baru dari PclLoadOptions
$loadOption = new PclLoadOptions();

// Membuat instance baru dari Document dan memuat file PCL
$document = new Document($inputFile, $loadOption);

// Menyimpan dokumen sebagai file PDF
$document->save($outputFile);
```

### Masalah yang Diketahui

1. Asal dari string teks dan gambar dapat sedikit berbeda dari yang ada di file PCL sumber jika arah cetak tidak 0º. Hal yang sama berlaku untuk gambar vektor jika sistem koordinat plot vektor diputar (perintah RO mendahului).
2. Asal label dalam gambar vektor dapat berbeda dari yang ada di file PCL sumber jika label dipengaruhi oleh rangkaian perintah: Label Origin (LO), Define Variable Text Path (DV), Absolute Direction (DI) atau Relative Direction (DR).
3. Teks dapat dibaca dengan tidak benar jika harus dirender dengan font Bitmap atau TrueType soft (tertanam), karena saat ini font ini hanya sebagian didukung (lihat pengecualian dalam "Tabel fitur yang didukung"). Dalam situasi ini, teks hanya dapat dibaca dengan benar jika kode karakter dalam font soft sesuai dengan yang default. Gaya teks yang dibaca juga dapat berbeda dari yang ada di file PCL sumber karena tidak perlu mengatur gaya di header font soft.

1. Jika file PCL yang diurai berisi font Intellifont atau Universal, sebuah pengecualian akan dilemparkan, karena font Intellifont dan Universal sama sekali tidak didukung.
1. Jika file PCL yang diurai berisi perintah makro, hasil penguraian akan sangat berbeda dari file sumbernya, karena perintah makro tidak didukung.

## Konversi Teks ke PDF

**Aspose.PDF untuk PHP** menyediakan kemampuan untuk mengonversi file Teks ke format PDF. Dalam artikel ini, kami menunjukkan betapa mudah dan efisiennya kami dapat mengonversi file teks ke PDF menggunakan Aspose.PDF.

Ketika Anda perlu mengonversi file Teks ke PDF, mulailah dengan membaca file teks sumber dalam pembaca tertentu. Kami telah menggunakan StringBuilder untuk membaca konten file Teks. Instansiasi objek Document dan tambahkan halaman baru dalam koleksi Pages. Buat objek baru dari TextFragment dan berikan objek StringBuilder ke konstruktor. Tambahkan paragraf baru dalam koleksi Paragraphs menggunakan objek TextFragment dan simpan file PDF yang dihasilkan menggunakan metode Save dari kelas Document.
**Coba ubah TEKS ke PDF secara online**
{{% alert color="primary" %}}

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["Teks ke PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF TEKS ke PDF dengan Aplikasi Gratis](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Ubah file teks biasa menjadi PDF

```php
// Buat objek Dokumen baru.
$document = new Document();

// Tambahkan halaman baru ke dokumen.
$page = $document->getPages()->add();

// Baca konten dari file teks input.
$text = file_get_contents($inputFile);

// Buat objek FontRepository baru.
$fontRepository = new FontRepository();

// Temukan font "Courier" di repository.
$font = $fontRepository->findFont("Courier");

// Buat objek TextFragment baru dengan teks input.
$textFragment = new TextFragment($text);

// Atur font dari fragmen teks ke "Courier".
$textFragment->getTextState()->setFont($font);

// Tambahkan fragmen teks ke halaman.
$page->getParagraphs()->add($textFragment);

// Simpan dokumen ke file output.
$document->save($outputFile);
```


## Convert XPS ke PDF

**Aspose.PDF untuk PHP** mendukung fitur konversi file <abbr title="XML Paper Specification">XPS</abbr> ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

XPS, XML Paper Specification, adalah format file Microsoft yang digunakan untuk mengintegrasikan pembuatan dan melihat dokumen ke dalam Windows. Dengan Aspose.PDF untuk PHP, dimungkinkan untuk mengonversi file XPS ke PDF, format file portabel dari Adobe.

Format file ini pada dasarnya adalah file XML yang di-zip, terutama digunakan untuk distribusi dan penyimpanan. Sangat sulit untuk diedit dan sebagian besar diimplementasikan oleh Microsoft.

Untuk mengonversi file XPS ke PDF menggunakan [Aspose.PDF untuk PHP](https://products.aspose.com/pdf/php-java), gunakan kelas [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Ini digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Nantinya, objek ini diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses konversi file XPS ke format PDF.

```php
// Membuat instance baru dari kelas XpsLoadOptions
$loadOption = new XpsLoadOptions();

// Membuat instance baru dari kelas Document dan memuat file XPS
$document = new Document($inputFile, $loadOption);

// Menyimpan dokumen sebagai file PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi format XPS ke PDF secara online**

Aspose.PDF untuk PHP menyajikan aplikasi gratis online ["XPS ke PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi XPS ke PDF dengan Aplikasi Gratis](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## Konversi PostScript ke PDF

**Aspose.PDF untuk PHP** mendukung fitur konversi file PostScript ke format PDF. Salah satu fitur dari Aspose.PDF adalah bahwa Anda dapat mengatur sekumpulan folder font yang akan digunakan selama konversi.

Untuk mengonversi file PostScript ke format PDF, Aspose.PDF untuk PHP menawarkan kelas [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) yang digunakan untuk menginisialisasi objek LoadOptions. Kemudian objek ini dapat diteruskan sebagai argumen ke konstruktor objek Document, yang akan membantu Mesin Rendering PDF menentukan format dokumen sumber.

Cuplikan kode berikut dapat digunakan untuk mengonversi file PostScript menjadi format PDF:

```php
// Buat objek PsLoadOptions baru.
$loadOption = new PsLoadOptions();

// Buat objek Document baru dan muat file PS input.
$document = new Document($inputFile, $loadOption);

// Simpan dokumen sebagai file PDF.
$document->save($outputFile);
```

## Konversi XML ke PDF

Format XML digunakan untuk menyimpan data terstruktur.
 Ada beberapa cara untuk mengonversi <abbr title="Extensible Markup Language">XML</abbr> ke PDF di Aspose.PDF.

{{% alert color="success" %}}
**Coba mengonversi XML ke PDF secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi XML ke PDF dengan Aplikasi Gratis](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Pertimbangkan opsi menggunakan dokumen XML berdasarkan standar XSL-FO.

### Mengonversi XSL-FO ke PDF

Konversi file XSL-FO ke PDF dapat diimplementasikan dengan menggunakan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) dengan [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// Tetapkan path ke file sampel
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// Buat instance baru dari kelas XslFoLoadOptions dan masukkan path file XSL-FO
$loadOption = new XslFoLoadOptions($inputFoFile);

// Buat instance baru dari kelas Document dan masukkan file XML dan opsi pemuatan XSL-FO
$document = new Document($inputFile, $loadOption);

// Simpan dokumen PDF yang dikonversi ke path file keluaran
$document->save($outputFile);
```

## Mengonversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX adalah format turunan dari sistem TeX. LaTeX (ˈleɪtɛk/ lay-tek atau lah-tek) adalah sistem persiapan dokumen dan bahasa markup dokumen. Ini banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ini juga memiliki peran penting dalam persiapan dan publikasi buku dan artikel yang mengandung materi multibahasa yang kompleks, seperti Sanskerta dan Arab, termasuk edisi kritis. LaTeX menggunakan program penyusunan huruf TeX untuk memformat keluarannya dan dirinya sendiri ditulis dalam bahasa makro TeX.

**Aspose.PDF untuk PHP** mendukung fitur untuk mengonversi file TeX ke format PDF dan untuk memenuhi persyaratan ini, paket com.aspose.pdf memiliki kelas bernama [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) yang menyediakan kemampuan untuk memuat file LaTex dan merender keluaran dalam format PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 Cuplikan kode berikut menunjukkan proses konversi file LaTex ke format PDF.

```php
// Buat instance baru dari kelas LatexLoadOptions
$loadOption = new LatexLoadOptions();

// Buat instance baru dari kelas Document dan muat file TeX menggunakan TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Coba konversi LaTeX/TeX ke PDF secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi online gratis ["LaTex ke PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi LaTeX/TeX ke PDF dengan Aplikasi Gratis](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}