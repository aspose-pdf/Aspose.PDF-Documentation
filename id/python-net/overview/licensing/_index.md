---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
weight: 50
url: /id/python-net/licensing/
description: Aspose.PDF for Python mengundang pelanggannya untuk mendapatkan lisensi Classic. Selain itu, gunakan lisensi terbatas untuk lebih menjelajahi produk.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lisensi Aspose.PDF for Python
Abstract: Artikel ini membahas batasan dan opsi lisensi untuk Aspose.PDF for Python. Artikel ini menyoroti bahwa versi evaluasi memungkinkan pengujian fungsionalitas penuh tetapi menambahkan watermark pada PDF yang dihasilkan, menampilkan “Evaluation Only” bersama informasi hak cipta. Bagi pengguna yang ingin menguji tanpa batasan ini, tersedia Lisensi Sementara selama 30 hari. Artikel tersebut juga menjelaskan cara menerapkan lisensi Classic dengan memuatnya dari file atau aliran, merekomendasikan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan mengatur lisensi menggunakan kelas `Aspose.Pdf.License`. Cuplikan kode disediakan untuk mengilustrasikan proses lisensi.
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi dari Aspose.PDF for Python menyediakan fungsionalitas penuh produk, tetapi semua halaman dalam dokumen PDF yang dihasilkan memiliki watermark dengan "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" di bagian atas.

>Jika Anda ingin menguji Aspose.PDF tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara paling mudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan pada contoh di bawah.

Jika Anda menggunakan komponen Aspose for Python lainnya bersama dengan Aspose.PDF for Python, harap tentukan namespace untuk Lisensi seperti [kelas Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
