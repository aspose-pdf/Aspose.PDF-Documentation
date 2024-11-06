---
title: Cara menandatangani PDF secara digital
linktitle: Tanda tangan digital PDF
type: docs
weight: 10
url: id/php-java/digitally-sign-pdf-file/
description: Tandatangani dokumen PDF secara digital menggunakan Java. Verifikasi, atau validasi PDF yang ditandatangani secara digital dengan aplikasi berbasis Java menggunakan PDF Library. Anda dapat mengesahkan file PDF dengan Sertifikat PKCS1.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Saat menandatangani dokumen PDF menggunakan tanda tangan, Anda pada dasarnya mengonfirmasi bahwa isinya harus tetap "seperti adanya". Akibatnya, setiap perubahan yang dilakukan setelahnya akan membatalkan tanda tangan dan dengan demikian, Anda tahu apakah dokumen telah diubah. Mengesahkan dokumen terlebih dahulu memungkinkan Anda menentukan perubahan yang dapat dilakukan pengguna pada dokumen tanpa membatalkan sertifikasi.

Dengan kata lain, dokumen tersebut masih dianggap mempertahankan integritasnya dan penerima masih dapat mempercayai dokumen tersebut. Untuk detail lebih lanjut, silakan kunjungi Mengautentikasi dan menandatangani PDF.

## Tanda tangani PDF dengan tanda tangan digital

```php

    // Buka dokumen
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // Gunakan PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // Simpan file PDF keluaran
    $signature->save($outputFile);    
    $document->close();
```