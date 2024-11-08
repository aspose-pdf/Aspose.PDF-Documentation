---
title: Manipulasi Dokumen PDF 
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 30
url: /id/php-java/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan cara menentukan Kemajuan pembuatan file PDF.
lastmod: "2024-06-05"
---

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF untuk kompatibilitas PDF/A-1a atau PDF/A-1b, gunakan metode [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Metode ini memungkinkan Anda untuk menentukan nama file di mana hasilnya akan disimpan dan jenis validasi yang diperlukan [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) enumerasi: PDF_A_1A atau PDF_A_1B.

Format XML output adalah format khusus Aspose.
 The XML berisi kumpulan tag dengan nama Problem; setiap tag berisi detail dari masalah tertentu. Atribut ObjectID dari tag Problem mewakili ID dari objek tertentu yang terkait dengan masalah ini. Atribut Clause mewakili aturan yang sesuai dalam spesifikasi PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Validasi PDF untuk PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Bekerja dengan TOC

### Menambahkan TOC ke PDF yang Ada

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dalam paket com.aspose.pdf. Paket com.aspose.pdf dapat membuat baru dan memanipulasi file PDF yang ada. Untuk menambahkan TOC ke PDF yang ada, gunakan paket com.aspose.pdf.

Cuplikan kode PHP ini menggunakan Aspose.PDF untuk menambahkan Daftar Isi (TOC) ke dokumen PDF yang ada:

```php
    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan akses ke halaman pertama file PDF
    $tocPage = $document->getPages()->insert(1);

    // Buat objek untuk merepresentasikan informasi TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Daftar Isi");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Tetapkan judul untuk TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Buat objek string yang akan digunakan sebagai elemen TOC
    $titles = ["Halaman pertama", "Halaman kedua", "Halaman ketiga", "Halaman keempat"];

    for ($i = 0; $i < 4; $i++) {
        // Buat objek Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Tentukan halaman tujuan untuk objek heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Halaman tujuan
        $heading2->setTop($page->getRect()->getHeight());

        // Koordinat tujuan
        $segment2->setText($titles[$i]);

        // Tambahkan heading ke halaman yang berisi TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```

### Atur TabLeaderType yang berbeda untuk Level TOC yang berbeda

Aspose.PDF juga memungkinkan pengaturan TabLeaderType yang berbeda untuk level TOC yang berbeda. Anda perlu mengatur properti LineDash dari FormatArray dengan nilai yang sesuai dari enum TabLeaderType seperti berikut.

```php
    // Buka dokumen
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // atur LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Daftar Isi");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definisikan format dari daftar empat tingkat dengan mengatur margin kiri dan
    // pengaturan format teks dari setiap tingkat
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Buat bagian dalam dokumen Pdf
    $page = $document->getPages()->add();

    // Tambahkan empat heading dalam bagian
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Contoh Heading" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Tambahkan heading ke Daftar Isi.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```


### Sembunyikan Nomor Halaman dalam TOC

Jika Anda tidak ingin menampilkan nomor halaman, bersama dengan judul dalam TOC, Anda dapat menggunakan properti [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) dari Kelas [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) sebagai false. Silakan periksa potongan kode berikut untuk menyembunyikan nomor halaman dalam daftar isi:

```php
    // Buka dokumen
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Buat objek untuk merepresentasikan informasi TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Daftar Isi");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Tetapkan judul untuk TOC
    $tocInfo->setTitle($title);

    // Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definisikan format dari daftar empat tingkat dengan mengatur margin kiri dan
    // pengaturan format teks dari setiap tingkat

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Tambahkan empat judul dalam bagian
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("ini adalah judul dari tingkat " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```


### Sesuaikan Nomor Halaman saat menambahkan TOC

Umumnya untuk menyesuaikan penomoran halaman dalam TOC saat menambahkan TOC dalam dokumen PDF. Sebagai contoh, kita mungkin perlu menambahkan beberapa awalan sebelum nomor halaman seperti P1, P2, P3 dan seterusnya. Dalam kasus seperti itu, Aspose.PDF untuk PHP via Java menyediakan properti PageNumbersPrefix dari kelas TocInfo yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan akses ke halaman pertama file PDF
    $tocPage = $document->getPages()->insert(1);

    // Buat objek untuk mewakili informasi TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Daftar Isi");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Tetapkan judul untuk TOC
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Buat objek string yang akan digunakan sebagai elemen TOC
    $titles = ["Halaman pertama", "Halaman kedua", "Halaman ketiga", "Halaman keempat"];

    for ($i = 0; $i < 4; $i++) {
        // Buat objek Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Tentukan halaman tujuan untuk objek heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Halaman tujuan
        $heading2->setTop($page->getRect()->getHeight());

        // Koordinat tujuan
        $segment2->setText($titles[$i]);

        // Tambahkan heading ke halaman yang berisi TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```


## Tambahkan Lapisan ke File PDF

Lapisan dapat digunakan dalam dokumen PDF dengan berbagai cara. Anda mungkin memiliki file multi-bahasa yang ingin Anda distribusikan dan menginginkan teks dalam setiap bahasa muncul pada lapisan yang berbeda, dengan desain latar belakang muncul pada lapisan terpisah. Anda mungkin juga membuat dokumen dengan animasi yang muncul pada lapisan terpisah. Salah satu contohnya bisa menambahkan perjanjian lisensi ke file Anda, dan Anda tidak ingin pengguna melihat kontennya sampai mereka menyetujui ketentuan perjanjian tersebut.

Aspose.PDF untuk PHP melalui Java mendukung penambahan lapisan ke file PDF.

Untuk bekerja dengan lapisan dalam file PDF, gunakan anggota API berikut.

Kelas [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) mewakili sebuah lapisan dan berisi properti berikut:

- **Name** – nama lapisan.
- **Id** – ID lapisan.
- **Contents** – daftar operator lapisan.

Setelah objek [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) telah ditentukan, tambahkan ke koleksi Lapisan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Kode di bawah ini menunjukkan cara menambahkan lapisan ke dokumen PDF.

```php
    // Buka dokumen
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Garis Merah");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Garis Hijau");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Garis Biru");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Atur Kedaluwarsa PDF

Fitur kedaluwarsa PDF mengatur berapa lama sebuah file PDF berlaku. Pada tanggal tertentu, jika seseorang mencoba mengaksesnya, sebuah pop-up ditampilkan, menjelaskan bahwa file tersebut telah kedaluwarsa dan bahwa mereka memerlukan yang baru.

Aspose.PDF memungkinkan Anda untuk mengatur kedaluwarsa saat membuat dan mengedit file PDF.

Cuplikan kode di bawah ini menunjukkan cara mengatur tanggal kedaluwarsa untuk sebuah file PDF. Anda perlu menggunakan JavaScript karena file yang disimpan oleh komponen pihak ketiga (misalnya OwnerGuard) tidak dapat dilihat di workstation lain tanpa utilitas tersebut.

File PDF dapat dibuat menggunakan PDF OwnerGuard menggunakan file yang sudah ada dengan tanggal kedaluwarsa. Namun file baru hanya dapat dibuka di workstation yang memiliki PDF OwnerGuard terinstal. Workstation tanpa PDF OwnerGuard akan memberikan ExpirationFeatureError. Sebagai contoh, PDF Reader membuka file jika OwnerGuard terinstal, tetapi Adobe Acrobat mengembalikan kesalahan.

```php

    // Buka dokumen
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('File ini telah kedaluwarsa. Anda memerlukan yang baru.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```