---
title: Tambahkan Gambar ke PDF di Node.js
linktitle: Tambahkan Gambar
type: docs
weight: 10
url: /id/nodejs-cpp/add-image-to-pdf/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan Aspose.PDF for Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
---

## Tambahkan gambar ke file PDF yang ada

Umumnya diyakini bahwa menambahkan gambar ke file PDF memerlukan alat khusus yang kompleks. Namun, dengan Aspose.PDF for Node.js Anda dapat dengan cepat dan mudah menambahkan gambar yang Anda perlukan ke PDF dalam lingkungan Node.js.

Kami hanya dapat menambahkan gambar ke akhir file, sehingga contoh yang tepat adalah kami memiliki beberapa halaman dokumen yang dipindai dan mengonversinya menjadi satu PDF.

Jika Anda ingin menambahkan gambar, Anda dapat menggunakan [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) fungsi. 
Silakan periksa cuplikan kode berikut untuk menambahkan gambar di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF di mana gambar akan ditambahkan.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk menambahkan gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Tambahkan gambar ke akhir PDF. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultAddImage.pdf”. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF di mana gambar akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Tambahkan gambar ke akhir PDF. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultAddImage.pdf”. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```