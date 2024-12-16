---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /id/cpp/licensing/
description: Aspose. PDF untuk C++ mengundang pelanggannya untuk mendapatkan lisensi Klasik dan Lisensi Meteran. Serta menggunakan lisensi terbatas untuk lebih mengeksplorasi produk.
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Keterbatasan Versi Evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli, jadi versi evaluasi memungkinkan Anda menggunakannya seperti biasanya. Namun, akan ada batasan berikut saat menggunakan versi evaluasi dari API:

**PDF dibuat dengan tanda air evaluasi** Versi evaluasi dari Aspose.PDF untuk C++ menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi tanda air dengan "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd" di bagian atas.

**Batas Jumlah Item Koleksi yang dapat Diproses**

Dalam versi evaluasi, hanya empat item yang dapat diproses dari koleksi apa pun (misalnya, hanya empat halaman, empat bidang formulir, dll.).

## Menerapkan Lisensi menggunakan File atau Objek Stream

Lisensi dapat dimuat dari file atau objek stream. Aspose.PDF untuk C++ akan mencoba menemukan lisensi di lokasi berikut:

1. Jalur eksplisit.
1. Folder yang berisi Aspose.PDF.dll.
1. Folder yang berisi assembly yang memanggil Aspose.PDF.dll.
1. Folder yang berisi assembly entri (file .exe Anda).
1. Sumber daya tertanam dalam assembly yang memanggil Aspose.PDF.dll.

Cara termudah untuk mengatur lisensi adalah dengan meletakkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file, tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah ini.

### Memuat Lisensi dari File

Cara termudah untuk menerapkan lisensi adalah dengan meletakkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan hanya menentukan nama file tanpa jalur.

{{% alert color="primary" %}}

Ketika Anda memanggil metode SetLicense, nama lisensi yang Anda berikan haruslah nama dari file lisensi. For example, jika Anda mengubah nama file lisensi menjadi "Aspose.PDF.lic.xml" berikan nama file tersebut ke metode Pdf->SetLicense(…).

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### Memuat Lisensi dari Objek Stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## Lisensi Meteran

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci meteran. Ini adalah mekanisme lisensi baru. Mekanisme lisensi baru ini akan digunakan bersama dengan metode lisensi yang sudah ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi meteran. Untuk detail lebih lanjut, silakan merujuk ke bagian FAQ Lisensi Meteran.

Kelas baru Metered telah diperkenalkan untuk menerapkan kunci meteran. Berikut adalah contoh kode yang menunjukkan cara mengatur kunci publik dan privat berbayar.

Untuk informasi lebih lanjut, silakan merujuk ke bagian [FAQ Lisensi Berbayar](https://purchase.aspose.com/faqs/licensing/metered).