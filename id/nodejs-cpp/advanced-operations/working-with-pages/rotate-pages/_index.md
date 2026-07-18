---
title: Putar Halaman PDF di Node.js
linktitle: Putar Halaman PDF
type: docs
weight: 50
url: /id/nodejs-cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara programatik di lingkungan Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Bagian ini menjelaskan cara memutar halaman dalam file PDF yang ada menggunakan Aspose.PDF for Node.js via C++.

Jika Anda ingin memutar halaman PDF, Anda dapat menggunakan [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) fungsi. Fungsi ini menggunakan parameter khusus 'AsposePdfModule.Rotation' untuk nilai rotasi. Dengan parameter ini Anda dapat mengatur berapa derajat yang perlu diputar PDF. Ada variasi: None, 90, 180, atau 270 derajat.

Silakan periksa potongan kode berikut untuk memutar halaman PDF di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan diputar.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk memutar halaman. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Putar semua file PDF. Rotasi diatur ke 270 derajat (on270). Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error di file Anda, informasi error akan berada dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan diputar.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Putar semua file PDF. Rotasi diatur ke 270 derajat (on270). Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error di file Anda, informasi error akan berada dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```