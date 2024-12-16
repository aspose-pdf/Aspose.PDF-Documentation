---
title: Tambahkan latar belakang ke PDF di Node.js
linktitle: Tambahkan latar belakang
type: docs
weight: 10
url: /id/nodejs-cpp/add-background/
description: Tambahkan gambar latar belakang ke file PDF Anda di Node.js 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan fungsi [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) di Node.js.

Silakan periksa cuplikan kode berikut untuk menambahkan gambar latar belakang dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF di mana gambar latar belakang akan ditambahkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan gambar latar belakang. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. Tambahkan gambar latar belakang ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultAddBackgroundImage.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Tambahkan gambar latar belakang ke file PDF dan simpan sebagai "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana gambar latar belakang akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Tambahkan gambar latar belakang ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddBackgroundImage.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Tambahkan gambar latar belakang ke file PDF dan simpan sebagai "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```