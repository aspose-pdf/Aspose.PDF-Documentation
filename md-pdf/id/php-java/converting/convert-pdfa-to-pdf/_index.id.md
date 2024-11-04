---
title: Konversi PDF/A ke format PDF 
linktitle: Konversi PDF/A ke format PDF
type: docs
weight: 110
url: /php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF/A ke dokumen PDF dengan pustaka PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi dokumen PDF/A ke PDF

Mengonversi dokumen PDF/A ke PDF berarti menghapus pembatasan <abbr title="Portable Document Format Archive">PDF/A</abbr> dari dokumen asli. Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memiliki metode removePdfaCompliance(..) untuk menghapus informasi kepatuhan PDF dari file input/sumber.

```php
// Buat instance baru dari kelas Document dengan file input
$document = new Document($inputFile);

// Hapus kepatuhan PDF/A dari dokumen
$document->removePdfaCompliance();

// Simpan dokumen yang dimodifikasi ke file keluaran
$document->save($outputFile);
```

Informasi ini juga dihapus jika Anda membuat perubahan apa pun dalam dokumen (misalnya.
 add halaman). Dalam contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```php
// Buat instance baru dari kelas Document dengan file input
$document = new Document($inputFile);

// Hapus kepatuhan PDF/A dari dokumen
$document->getPages()->add();

// Simpan dokumen yang telah dimodifikasi ke file output
$document->save($outputFile);
```