---
title:  Ekstrak data dari AcroForm 
linktitle:  Ekstrak data dari AcroForm
type: docs
weight: 50
url: id/php-java/extract-data-from-acroform/
description: AcroForms ada di banyak dokumen PDF. Artikel ini bertujuan untuk membantu Anda memahami cara mengekstrak data dari AcroForms menggunakan PHP dan Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Aspose.PDF untuk PHP tidak hanya memungkinkan Anda membuat dan mengisi bidang formulir, tetapi juga memudahkan untuk mengekstrak data bidang formulir atau informasi bidang formulir dari file PDF.

Misalkan kita tidak tahu nama-nama bidang formulir sebelumnya. Maka kita harus mengiterasi setiap halaman dalam PDF untuk mengekstrak informasi tentang semua AcroForms dalam PDF serta nilai-nilai dari bidang formulir. Untuk mendapatkan akses ke formulir, kita perlu menggunakan metode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```php

    // Membuat instance baru dari kelas License dan mengatur file lisensi
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Mengatur jalur ke direktori yang berisi dokumen PDF
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Mengatur jalur ke file PDF input
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Mengatur header respons untuk menunjukkan bahwa respons akan dalam format JSON
    header('Content-Type: application/json; charset=utf-8');

    // Inisialisasi variabel data respons
    $responseData = "";

    try {
        // Membuat instance baru dari kelas Document dan memuat file PDF input
        $document = new Document($inputFile);

        // Mendapatkan bidang formulir dari dokumen dan mengonversinya ke nilai PHP
        $fields = java_values($document->getForm()->getFields());

        // Melakukan iterasi pada setiap bidang formulir dan mengekstrak nama dan nilai bidang
        foreach ($fields as $formField) {
            // Menggabungkan nama dan nilai bidang ke data respons
            $responseData = $responseData . "(Nama Bidang: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Nilai: " . $formField->getValue() . "),";
        }

        // Menutup dokumen
        $document->close();
    }
```


Jika Anda mengetahui nama dari kolom formulir yang ingin Anda ekstrak nilainya, maka Anda dapat menggunakan indexer dalam koleksi Documents.Form untuk dengan cepat mengambil data ini.

## Ekstrak Data ke XML dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang objek Form. Cuplikan kode berikut menunjukkan cara mengekspor data ke file XML.

```php

    // Buka dokumen
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Buat objek FileOutputStream untuk menulis file font.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Ekspor data
    $form->exportXml($xmlOutputStream);

    // Tutup aliran file
    $xmlOutputStream->close();

    // Tutup dokumen
    $form->close();
```

## Ekspor Data ke FDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Harap dicatat, bahwa ini adalah kelas dari `com.aspose.pdf.facades`. Meskipun namanya mirip, kelas ini memiliki tujuan yang sedikit berbeda.

Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`. Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara mengekspor data ke file XFDF.

```php

    // Buka dokumen
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Buat objek FileOutputStream untuk menulis file font.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Ekspor data
    $form->exportFdf($xmlOutputStream);

    // Tutup file stream
    $xmlOutputStream->close();

    // Tutup dokumen
    $form->close();
```

## Ekspor Data ke XFDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`. 
Cuplikan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```php

    // Buka dokumen
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Buat objek FileOutputStream untuk menulis file font.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Ekspor data
    $form->exportXfdf($xmlOutputStream);

    // Tutup file stream
    $xmlOutputStream->close();

    // Tutup dokumen
    $form->close();
```