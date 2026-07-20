---
title: Membagi PDF di Node.js
linktitle: Membagi file PDF
type: docs
weight: 30
url: /id/nodejs-cpp/split-pdf/
description: Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF terpisah dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Membagi PDF menjadi dua file menggunakan Node.js

Jika Anda ingin membagi satu PDF menjadi bagian-bagian, Anda dapat menggunakan [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) fungsi. 
Silakan periksa cuplikan kode berikut untuk memisahkan dua PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dipisahkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk membagi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Membagi dua file PDF. Ini menetapkan variabel pageToSplit ke 1, menunjukkan bahwa file PDF akan dibagi pada halaman 1. 
1. Dengan demikian, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultSplit1.pdf”, dan “ResultSplit2.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat di ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dipisahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Membagi dua file PDF. Ini menetapkan variabel pageToSplit ke 1, menunjukkan bahwa file PDF akan dibagi pada halaman 1. 
1. Dengan demikian, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultSplit1.pdf”, dan “ResultSplit2.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat di ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```