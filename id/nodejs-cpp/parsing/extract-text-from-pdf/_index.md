---
title: Ekstrak Teks dari PDF di Node.js
linktitle: Ekstrak teks dari PDF
type: docs
weight: 30
url: /id/nodejs-cpp/extract-text-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF untuk Node.js via C++. 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah tugas yang sangat umum dan berguna. 
Mengekstrak teks dari PDF melayani berbagai tujuan, mulai dari meningkatkan pencarian dan ketersediaan hingga memungkinkan analisis dan otomatisasi data di berbagai bidang seperti bisnis, penelitian, dan manajemen informasi.

Jika Anda ingin mengekstrak teks dari dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/). 
Silakan periksa potongan kode berikut untuk mengekstrak teks dari file PDF menggunakan Node.js via C++.

Periksa potongan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:


**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama untuk file PDF dari mana teks akan diekstraksi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstraksi teks. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstraksi ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, oleh karena itu, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ekstrak teks dari file PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama untuk file PDF dari mana teks akan diekstraksi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstraksi akan ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Ekstrak teks dari file PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```