---
title: Convert XFA Form ke AcroForm
linktitle: Convert XFA Form
type: docs
weight: 10
url: id/php-java/convert-form/
description: Bagian ini menjelaskan bagaimana mengkonversi Formulir XFA ke AcroForm dengan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengkonversi Formulir XFA Dinamis ke AcroForm Standar

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, “XML Forms Architecture”. Ini juga dapat mengkonversi formulir XFA dinamis ke Acroform standar. Informasi tentang formulir (sejauh menyangkut PDF) sangat samar – ini menentukan bahwa bidang ada, dengan properti, dan peristiwa JavaScript, tetapi tidak menentukan rendering apa pun. Objek formulir XFA digambar pada saat memuat dokumen.

Saat ini PDF mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF:

- AcroForms (juga dikenal sebagai formulir Acrobat), diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.

- Adobe XML Forms Architecture (XFA) forms, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional. (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.)

Tidak mungkin untuk mengekstrak atau memanipulasi halaman dari Formulir XFA, karena konten formulir dihasilkan saat runtime (selama penayangan formulir XFA) dalam aplikasi yang mencoba menampilkan atau merender formulir XFA. Aspose.PDF memiliki fitur yang memungkinkan pengembang untuk mengonversi formulir XFA ke AcroForms standar.

```php

        // Muat formulir XFA
        $document = new Document($inputFile);
        
        // Setel jenis bidang formulir sebagai AcroForm standar
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // Simpan dokumen yang diperbarui
        $document->save($outputFile);
        
        // Simpan PDF yang dimodifikasi    
        $document->close();
```