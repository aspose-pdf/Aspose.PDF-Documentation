---
title: Ekstrak Teks Dari Stempel
type: docs
weight: 60
url: /id/php-java/extract-text-from-stamps/
---

## Ekstrak Teks dari Anotasi Stempel

Aspose.PDF untuk PHP via Java memungkinkan Anda mengekstrak teks dari anotasi stempel. Untuk mengekstrak teks dari Anotasi Stempel dalam PDF, langkah-langkah berikut dapat digunakan.

1. Muat dokumen PDF
1. Dapatkan halaman yang diinginkan dari dokumen
1. Buat instance baru dari kelas StampAnnotation
1. Buat instance baru dari kelas AnnotationSelector dan berikan anotasi stempel kepada itu
1. Terima pemilih anotasi pada halaman
1. Dapatkan anotasi stempel yang dipilih
1. Buat instance baru dari kelas TextAbsorber
1. Dapatkan anotasi stempel pertama
1. Dapatkan tampilan normal dari anotasi stempel
1. Kunjungi tampilan menggunakan penyerap teks
1. Dapatkan teks yang diekstrak dari penyerap teks
1. Tutup dokumen

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```