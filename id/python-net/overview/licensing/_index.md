---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
weight: 50
url: /id/python-net/licensing/
description: Aspose.PDF untuk Python mengundang pelanggannya untuk mendapatkan lisensi Klasik. Serta menggunakan lisensi terbatas untuk menjelajahi produk dengan lebih baik.
lastmod: "2025-02-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lisensi Aspose.PDF untuk Python
Abstract: Artikel ini membahas batasan dan opsi lisensi untuk Aspose.PDF untuk Python. Artikel menyoroti bahwa versi evaluasi memungkinkan pengujian fungsi penuh namun menambahkan watermark pada PDF yang dihasilkan, menyatakan "Evaluation Only" bersama dengan informasi hak cipta. Bagi pengguna yang ingin menguji tanpa batasan ini, tersedia Lisensi Sementara selama 30 hari. Artikel selanjutnya menjelaskan cara menerapkan lisensi klasik dengan memuatnya dari file atau stream, merekomendasikan menempatkan file lisensi di direktori yang sama dengan file Aspose.PDF.dll dan mengatur lisensi menggunakan kelas `Aspose.Pdf.License`. Potongan kode disediakan untuk mengilustrasikan proses lisensi.
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF yang dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF untuk Python menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi watermark dengan "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" di bagian atas.

>Jika Anda ingin menguji Aspose.PDF tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk menetapkan lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan pada contoh di bawah.

Jika Anda menggunakan komponen Aspose untuk Python lainnya bersama dengan Aspose.PDF untuk Python, harap tentukan namespace untuk Lisensi seperti [kelas Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```

