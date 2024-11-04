---
title: Tambahkan Stempel Gambar ke PDF di Node.js
linktitle: Stempel gambar dalam File PDF
type: docs
weight: 60
url: /nodejs-cpp/stamping/
description: Tambahkan Stempel Gambar dalam dokumen PDF Anda menggunakan AsposePdfAddStamp dengan alat Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Gambar dalam File PDF

Menyematkan dokumen PDF mirip dengan menyematkan dokumen kertas. Sebuah stempel dalam file PDF memberikan informasi tambahan pada file PDF, seperti melindungi file PDF agar tidak digunakan oleh orang lain dan mengkonfirmasi keamanan konten dari file PDF.
Anda dapat menggunakan fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) untuk menambahkan stempel gambar ke file PDF menggunakan Node.js.

Silakan periksa potongan kode berikut untuk menambahkan stempel gambar ke file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.

1. Tentukan nama file PDF di mana cap gambar akan ditambahkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan cap gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Tambahkan cap ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultImage.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Tambahkan cap ke file PDF dan simpan sebagai "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana stempel gambar akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Tambahkan stempel ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultImage.pdf". Jika parameter json.errorCode bukan 0 dan, oleh karena itu, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Tambahkan stempel ke file PDF dan simpan "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```