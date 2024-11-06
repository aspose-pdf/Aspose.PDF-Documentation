---

title: Bekerja dengan Judul di PDF  
type: docs  
weight: 70  
url: id/php-java/working-with-headings/  
lastmod: "2024-06-05"  
description: Buat penomoran pada judul dokumen PDF Anda menggunakan PHP. Aspose.PDF untuk PHP via Java menawarkan berbagai macam gaya penomoran.  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---
## Terapkan Gaya Penomoran pada Judul

Judul adalah bagian penting dari setiap dokumen. Penulis selalu berusaha membuat judul lebih menonjol dan bermakna bagi pembacanya. Jika ada lebih dari satu judul dalam sebuah dokumen, seorang penulis memiliki beberapa opsi untuk mengatur judul-judul ini. Salah satu pendekatan yang paling umum untuk mengatur judul adalah menulis judul dalam Gaya Penomoran.

Aspose.PDF untuk PHP via Java menawarkan banyak gaya penomoran yang sudah ditentukan sebelumnya. Gaya penomoran yang sudah ditentukan ini disimpan dalam enumerasi, NumberingStyle. Nilai-nilai yang sudah ditentukan dari enumerasi NumberingStyle dan deskripsinya diberikan di bawah ini:

|**Jenis Judul**|**Deskripsi**|  
| :- | :- |  

|NumeralsArabic|Tipe Arab, misalnya, 1,1.1,...|
|NumeralsRomanUppercase|Tipe Romawi atas, misalnya, I,I.II, ...|
|NumeralsRomanLowercase|Tipe Romawi bawah, misalnya, i,i.ii, ...|
|LettersUppercase|Tipe Inggris atas, misalnya, A,A.B, ...|
|LettersLowercase|Tipe Inggris bawah, misalnya, a,a.b, ...|
Properti [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dari kelas [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) digunakan untuk mengatur gaya penomoran dari judul.


Kode sumber, untuk mendapatkan output yang ditunjukkan pada gambar di atas, diberikan di bawah dalam contoh.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("Daftar 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("Daftar 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("nilai, pada tanggal efektif rencana, dari properti yang akan didistribusikan di bawah rencana untuk setiap yang diizinkan");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```