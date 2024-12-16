---
title: Advanced operations using JavaScript via C++
linktitle: Advanced operations
type: docs
weight: 60
url: /id/javascript-cpp/advanced-operations/
description: Aspose.PDF untuk JavaScript via C++ dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga mengatasi tujuan yang lebih kompleks. Periksa bagian berikutnya untuk pengguna dan pengembang lanjutan.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Operasi Lanjutan** adalah bagian tentang cara menangani file PDF yang ada secara programatis, baik dokumen yang dibuat dengan Aspose.PDF seperti yang dibahas di [Operasi Dasar](/pdf/id/javascript-cpp/basic-operations/), atau PDF yang dibuat dengan Adobe Acrobat, Google Docs, Microsoft Office, Open Office, atau produsen PDF lainnya.

## Menggunakan Web Workers

Versi 23.6 menambahkan kemampuan untuk menggunakan Web Workers:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

Penggunaan Web Workers dari JavaScript via C++, memungkinkan Anda melakukan operasi tanpa memblokir antarmuka, dalam thread pekerja terpisah.

Web Workers adalah alat sederhana untuk menjalankan skrip di latar belakang. Yang memungkinkan Anda melakukan tugas tanpa mengganggu antarmuka pengguna, dalam thread pekerja terpisah.

Anda akan mempelajari berbagai cara untuk:

- [Bekerja dengan Dokumen](/pdf/id/javascript-cpp/working-with-documents/) - kompres, pisah, dan gabungkan dokumen dan lakukan operasi lain dengan seluruh dokumen.
- [Bekerja dengan Halaman](/pdf/id/javascript-cpp/working-with-pages/) - tambahkan, pindahkan atau hapus, potong halaman, stempel.
- [Metadata dalam PDF](/pdf/id/javascript-cpp/pdf-file-metadata/) - dapatkan atau atur metadata dalam dokumen.
- [Bekerja dengan Gambar](/pdf/id/javascript-cpp/working-with-images/) - sisipkan, hapus, ekstrak gambar dalam dokumen
- [Navigasi dan Interaksi](/pdf/id/javascript-cpp/navigation-and-interaction/) - mengelola tindakan, penanda, navigasi halaman
- [Anotasi](/pdf/id/javascript-cpp/annotations/) - Anotasi memungkinkan pengguna untuk menambahkan konten kustom pada halaman PDF. Anda dapat menambahkan, menghapus, dan memodifikasi anotasi dari dokumen PDF.

- [Mengamankan dan Menandatangani](/pdf/id/javascript-cpp/securing-and-signing/) - lindungi dan tandatangani dokumen PDF Anda secara programatis
- [Attachments](/pdf/id/javascript-cpp/attachments/) - Dokumen PDF dapat berisi lampiran file. Lampiran ini dapat berupa dokumen PDF lain, atau jenis file apa pun, seperti file audio, dokumen Microsoft Office, dll. Anda akan belajar cara menambahkan lampiran ke pdf, mendapatkan informasi dari lampiran, dan menyimpannya ke file, menghapus lampiran dari PDF secara programatis dengan JavaScript.