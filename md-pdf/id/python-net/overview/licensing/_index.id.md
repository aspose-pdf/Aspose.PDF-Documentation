---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /python-net/licensing/
description: Aspose. PDF untuk Python mengundang pelanggannya untuk mendapatkan lisensi Klasik. Serta menggunakan lisensi terbatas untuk lebih mengeksplorasi produk.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF dibuat dengan tanda air evaluasi.** Versi evaluasi dari Aspose.PDF untuk Python menyediakan fungsi produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi tanda air dengan "Evaluasi Saja. Dibuat dengan Aspose.PDF. Hak Cipta 2002-2020 Aspose Pty Ltd" di bagian atas.

>Jika Anda ingin menguji Aspose.PDF tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari.
 Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk mengatur lisensi adalah dengan meletakkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah ini.

Jika Anda menggunakan komponen Aspose untuk Python lainnya bersama dengan Aspose.PDF untuk Python, harap tentukan namespace untuk Lisensi seperti [kelas Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```