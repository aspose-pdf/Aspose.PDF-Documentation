---
title: Membuat AcroForms - Membuat PDF Isian di PHP
linktitle: Membuat AcroForms
type: docs
weight: 10
url: /php-java/create-forms/
description: Bagian ini menjelaskan cara membuat AcroForms dari awal dalam dokumen PDF Anda dengan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Menambahkan Form Field dalam Dokumen PDF

Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) menyediakan koleksi bernama Form yang membantu mengelola field formulir dalam dokumen PDF.

Untuk menambahkan field formulir:

1. Buat field formulir yang ingin Anda tambahkan.
2. Panggil metode tambah koleksi [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Contoh ini menunjukkan cara menambahkan TextBoxField. Anda dapat menambahkan field formulir apa pun menggunakan pendekatan yang sama:

1. Pertama, buat objek field dan atur propertinya.
2. Kemudian, tambahkan field ke koleksi Form.

### Menambahkan TextBoxField

Field teks adalah elemen formulir yang memungkinkan penerima memasukkan teks ke dalam formulir Anda.
 Dokumen ini akan digunakan kapan saja Anda ingin memberikan kebebasan kepada pengguna untuk mengetik apa yang mereka inginkan.

Cuplikan kode berikut menunjukkan cara menambahkan TextBoxField ke dokumen PDF.

```php

    // Buka dokumen
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Buat bidang
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Beberapa nilai dalam Kotak Teks");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Tambahkan bidang ke dokumen
    $document->getForm()->add($textBoxField, 1);

    // Simpan PDF yang dimodifikasi
    $document->save($outputFile);
    $document->close();
```

## Menambahkan RadioButtonField

Tombol Radio paling sering digunakan untuk pertanyaan pilihan ganda, dalam skenario di mana hanya satu jawaban yang dapat dipilih.
Cuplikan kode berikut menunjukkan cara menambahkan [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dalam dokumen PDF.

```php

    // Buka dokumen            
    $document = new Document($inputFile);

    // tambahkan halaman ke file PDF
    $page = $document->getPages()->get_Item(1);

    // buat objek RadioButtonField dengan nomor halaman sebagai argumen
    $radio = new RadioButtonField($page);

    // tambahkan opsi tombol radio pertama dan juga tentukan asalnya 
    // menggunakan objek Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // tambahkan opsi tombol radio kedua
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // tambahkan tombol radio ke objek form dari objek Document
    $document->getForm()->add($radio);

    // simpan file PDF
    $document->save($outputFile);
    $document->close();
```

Cuplikan kode berikut menunjukkan langkah-langkah untuk menambahkan [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dengan tiga opsi dan menempatkannya di dalam sel Tabel.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("Item1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("Item2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("Item3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## Menambahkan field ComboBox

Kotak Kombo adalah field formulir yang akan menambahkan menu dropdown ke dokumen Anda.

Cuplikan kode berikut menunjukkan cara menambahkan field [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) dalam dokumen PDF.

```php

        $document = new Document($inputFile);

        // membuat objek ComboBox Field
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // menambahkan opsi ke ComboBox
        $combo->addOption("Merah");
        $combo->addOption("Kuning");
        $combo->addOption("Hijau");
        $combo->addOption("Biru");

        // menambahkan objek combo box ke koleksi field formulir dari objek dokumen
        $document->getForm()->add($combo);

        // menyimpan dokumen PDF
        $document->save($outputFile);
        $document->close();
```

## Menambahkan Tooltip ke Formulir

Kelas Document menyediakan koleksi yang disebut Form yang mengelola field formulir dalam dokumen PDF.
 Untuk menambahkan tooltip ke bidang formulir, gunakan kelas Field AlternateName. Adobe Acrobat menggunakan 'nama alternatif' sebagai tooltip bidang.

Potongan kode berikut menunjukkan cara menambahkan tooltip ke bidang formulir dengan PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Tetapkan tooltip untuk textfield
    $textBoxField->setAlternateName("Petunjuk kotak teks");

    // simpan dokumen PDF
    $document->save($outputFile);
    $document->close();
```