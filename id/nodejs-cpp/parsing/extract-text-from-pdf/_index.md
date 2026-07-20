---
title: Mengurai Teks dari PDF di Node.js
linktitle: Mengurai teks dari PDF
type: docs
weight: 30
url: /id/nodejs-cpp/extract-text-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengurai teks dari dokumen PDF menggunakan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengurai Teks Dari Dokumen PDF

Mengurai teks dari dokumen PDF adalah tugas yang sangat umum dan berguna. 
Mengekstrak teks dari PDF melayani berbagai tujuan, mulai dari meningkatkan pencarian dan ketersediaan hingga memungkinkan analisis dan otomatisasi data di berbagai bidang seperti bisnis, penelitian, dan manajemen informasi.

Jika Anda ingin mengekstrak teks dari dokumen PDF, Anda dapat menggunakan [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) function. 
Silakan periksa potongan kode berikut untuk mengekstrak teks dari file PDF menggunakan Node.js via C++.

Periksa potongan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan diekstrak teksnya.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk mengekstrak teks. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstrak akan ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan berada di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan diekstrak teksnya.
1. Inisialisasi modul AsposePdf. Terima objeknya jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstrak akan ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan berada di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```