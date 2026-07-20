---
title: Ekstrak Teks dari PDF di Node.js
linktitle: Ekstrak Teks dari PDF
type: docs
weight: 10
url: /id/nodejs-cpp/extract-text/
description: Bagian ini menjelaskan cara mengekstrak teks dari dokumen PDF menggunakan toolkit Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks dari Semua Halaman Dokumen PDF

Mengekstrak teks dari PDF tidaklah mudah. Hanya beberapa pembaca PDF yang dapat mengekstrak teks dari gambar PDF atau PDF yang dipindai. Namun alat **Aspose.PDF for Node.js via C++** memungkinkan Anda dengan mudah mengekstrak teks dari semua file PDF di lingkungan Node.js. 

Kode ini menunjukkan cara menggunakan modul AsposePDFforNode.js untuk mengekstrak teks dari file PDF yang ditentukan dan mencatat baik teks yang diekstrak maupun kesalahan yang terjadi.

Periksa potongan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan diekstrak teksnya.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstrak teks. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstrak ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan berada dalam 'json.errorText'.

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
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstrak ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan berada dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
