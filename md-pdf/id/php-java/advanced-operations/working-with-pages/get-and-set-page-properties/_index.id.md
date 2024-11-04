---
title: Mendapatkan dan Mengatur Properti Halaman
type: docs
weight: 30
url: /php-java/get-and-set-page-properties/
description: Topik ini menjelaskan cara mendapatkan angka dalam file PDF, mendapatkan properti halaman dan menentukan warna halaman menggunakan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
---

Aspose.PDF untuk PHP via Java memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi Java Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman.

## Mendapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Kemudian halaman dokumen diambil. Upaya dilakukan untuk mendapatkan jumlah halaman dari halaman yang diambil.

Cuplikan kode berikut menunjukkan cara mendapatkan jumlah halaman dari sebuah file PDF.


```php

    // Buka dokumen
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Dapatkan jumlah halaman
    $responseData = $responseData . "Jumlah Halaman : " + $pages->size();
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Kecuali file PDF disimpan dan semua elemen benar-benar ditempatkan di dalam file PDF, kita tidak dapat mendapatkan jumlah halaman untuk dokumen tertentu (karena kita tidak dapat memastikan tentang jumlah halaman di mana semua elemen akan ditempatkan). Namun dimulai dengan rilis Aspose.PDF untuk PHP via Java, kami telah memperkenalkan metode bernama [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) yang menyediakan fitur untuk mendapatkan jumlah halaman untuk dokumen PDF, tanpa menyimpan file. Jadi kita dapat mendapatkan informasi jumlah halaman secara langsung. Silakan coba menggunakan potongan kode berikut untuk memenuhi persyaratan ini.

```php

    // Buka dokumen
    $document = new Document($inputFile);      

    // tambahkan halaman ke koleksi halaman file PDF
    $page = $document->getPages()->add();
    
    // buat loop untuk menambahkan 300 instance TextFragment
    for ($i=0; $i < 300; $i++) { 
       // tambahkan TextFragment ke koleksi paragraf halaman pertama PDF
       $page->getParagraphs()->add(new TextFragment("Uji hitungan halaman"));
    }
    
    // proses paragraf untuk mendapatkan informasi jumlah halaman
    $document->processParagraphs();

    $pages = $document->getPages();

    // Dapatkan jumlah halaman
    $responseData = $responseData . "Jumlah Halaman : " + $pages->size();
```


## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti ini.

### **Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox dan Properti Rect**

- **Kotak media**: Kotak media adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, kotak media menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **Kotak bleed**: Jika dokumen memiliki bleed, PDF juga akan memiliki kotak bleed.
 Bleed adalah jumlah warna (atau karya seni) yang meluas melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("dipangkas"), tinta akan mencapai hingga ke tepi halaman. Bahkan jika halaman dipotong sedikit meleset dari tanda pemangkasan, tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Kotak trim menunjukkan ukuran akhir dari dokumen setelah dicetak dan dipangkas.
- **Art box**: Kotak seni adalah kotak yang digambar di sekitar konten aktual halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Kotak potong adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari kotak potong yang ditampilkan di Adobe Acrobat.
  Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Page Boundaries.
- **Page.Rect**: irisan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti-properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Mengakses Properti Halaman

Cuplikan kode berikut mendapatkan properti seperti ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Nomor Halaman, dan Rotate untuk halaman tertentu dalam dokumen. Kemudian menyimpan data yang diekstrak dalam variabel terpisah dan menggabungkannya menjadi string respons.

1. Buat objek Dokumen baru menggunakan variabel $inputFile.
1. Dapatkan koleksi halaman dari dokumen menggunakan metode getPages().
1. Dapatkan halaman tertentu dari koleksi halaman menggunakan metode get_Item().
1. Ekstrak berbagai properti (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Nomor Halaman, Rotate) dari objek halaman tertentu dan simpan dalam variabel terpisah.
1. Kode menggabungkan nilai properti yang diekstrak menjadi string respons terpisah ($responseData1, $responseData2, dll.).
1. Selanjutnya, ini mencoba untuk mengambil jumlah halaman menggunakan metode size() pada objek $pages, tetapi variabel $pages tidak terdefinisi.

Kode berikut menunjukkan cara mendapatkan properti halaman.

```php

   // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan koleksi halaman
    $pageCollection = $document->getPages();

    // Dapatkan halaman tertentu
    $page = $pageCollection->get_Item(1);

    // Dapatkan properti halaman
    $responseData1 = "ArtBox : Tinggi = " . $page->getArtBox()->getHeight()
        . ", Lebar = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Tinggi = " . $page->getBleedBox()->getHeight() . ", Lebar = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Tinggi = " . $page->getCropBox()->getHeight() . ", Lebar = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Tinggi = " . $page->getMediaBox()->getHeight() . ", Lebar = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Tinggi = " . $page->getTrimBox()->getHeight() . ", Lebar = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Tinggi = " . $page->getRect()->getHeight() . ", Lebar = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Nomor Halaman :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotasi :-" . $page->getRotate() . PHP_EOL;

    // Dapatkan jumlah halaman
    $responseData8 = $responseData8 . "Jumlah Halaman : " . $pages->size();
```


## Menentukan Warna Halaman

Kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) menyediakan properti yang terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna apa - RGB, hitam dan putih, skala abu-abu, atau tidak terdefinisi - yang digunakan halaman.

Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Properti [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) menentukan warna elemen pada halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) dari objek kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Cuplikan kode berikut menunjukkan cara mengiterasi melalui halaman individu dari file PDF untuk mendapatkan informasi warna.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Iterasi melalui semua halaman dari file PDF
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Dapatkan informasi jenis warna untuk halaman PDF tertentu
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Halaman # -" . $pageCount . " adalah Hitam dan putih..";
                break;
            case 1:
                $responseData ="Halaman # -" . $pageCount . " adalah Skala Abu-abu...";
                break;
            case 0:
                $responseData ="Halaman # -" . $pageCount . " adalah RGB..";
                break;
            case 3:
                $responseData ="Warna Halaman # -" . $pageCount . " tidak terdefinisi..";
                break;
        }
    }
```