---  
title: Extract Text from PDF in Node.js  
linktitle: Extract Text from PDF  
type: docs  
weight: 10  
url: id/nodejs-cpp/extract-text/  
description: Bagian ini menjelaskan cara mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF untuk Node.js melalui toolkit C++.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari PDF tidaklah mudah. Hanya beberapa pembaca PDF yang dapat mengekstrak teks dari gambar PDF atau PDF yang dipindai. Tetapi alat **Aspose.PDF untuk Node.js melalui C++** memungkinkan Anda dengan mudah mengekstrak teks dari semua file PDF di lingkungan Node.js.

Kode ini menunjukkan cara menggunakan modul AsposePDFforNode.js untuk mengekstrak teks dari file PDF yang ditentukan dan mencatat teks yang diekstrak atau kesalahan yang ditemukan.

Periksa cuplikan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.

1. Tentukan nama untuk file PDF dari mana teks akan diekstraksi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstraksi teks. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Teks yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstraksi ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

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
1. Teks yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, teks yang diekstraksi ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, dengan demikian, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Ekstrak teks dari file PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```