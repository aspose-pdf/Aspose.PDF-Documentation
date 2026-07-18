---
title: Tambahkan cap Gambar ke PDF dalam Node.js
linktitle: Cap Gambar dalam File PDF
type: docs
weight: 60
url: /id/nodejs-cpp/stamping/
description: Tambahkan Cap Gambar ke dokumen PDF Anda menggunakan AsposePdfAddStamp dengan alat Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Cap Gambar dalam File PDF

Menstempel dokumen PDF mirip dengan menstempel dokumen kertas. Sebuah cap dalam file PDF memberikan informasi tambahan ke file PDF, seperti melindungi file PDF agar tidak digunakan oleh orang lain dan mengonfirmasi keamanan isi file PDF.
Anda dapat menggunakan [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) fungsi untuk menambahkan stempel gambar ke file PDF menggunakan Node.js.

Silakan periksa cuplikan kode berikut untuk menambahkan stempel gambar ke file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF di mana stempel gambar akan ditambahkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan cap gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Tambahkan stempel ke file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultImage.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi error pada file Anda, informasi error akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF di mana stempel gambar akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Tambahkan stempel ke file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultImage.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi error pada file Anda, informasi error akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```