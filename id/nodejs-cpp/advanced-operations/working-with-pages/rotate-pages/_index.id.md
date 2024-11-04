---
title: Memutar Halaman PDF di Node.js
linktitle: Memutar Halaman PDF
type: docs
weight: 50
url: /nodejs-cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara terprogram di lingkungan Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Bagian ini menjelaskan cara memutar halaman dalam file PDF yang ada menggunakan Aspose.PDF untuk Node.js melalui C++.

Jika Anda ingin memutar halaman PDF, Anda dapat menggunakan fungsi [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). Fungsi ini menggunakan parameter khusus 'AsposePdfModule.Rotation' untuk nilai rotasi. Dengan ini Anda dapat mengatur berapa derajat Anda perlu memutar PDF. Ada varian: Tidak Ada, 90, 180, atau 270 derajat.

Silakan periksa potongan kode berikut untuk memutar halaman PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.

1. Tentukan nama file PDF yang akan diputar.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk memutar halaman. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Putar semua file PDF. Rotasi diatur ke 270 derajat (on270). Jadi, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Putar halaman PDF dan simpan di "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan diputar.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Putar semua file PDF. Rotasi diatur ke 270 derajat (on270). Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Putar halaman PDF dan simpan "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```