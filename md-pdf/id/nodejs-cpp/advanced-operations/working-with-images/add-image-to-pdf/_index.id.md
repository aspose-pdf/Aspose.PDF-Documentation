---
title: Tambahkan Gambar ke PDF di Node.js 
linktitle: Tambahkan Gambar
type: docs
weight: 10
url: /nodejs-cpp/add-image-to-pdf/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
---

## Tambahkan gambar ke file PDF yang ada

Umumnya diyakini bahwa menambahkan gambar ke file PDF memerlukan alat khusus yang kompleks. Namun, dengan Aspose.PDF untuk Node.js Anda dapat dengan cepat dan mudah menambahkan gambar yang Anda butuhkan ke PDF di lingkungan Node.js.

Kita hanya dapat menambahkan gambar ke akhir file, oleh karena itu contoh yang tepat adalah kita memiliki beberapa halaman dokumen hasil pemindaian dan mengonversinya menjadi satu PDF.

Jika Anda ingin menambahkan gambar, Anda dapat menggunakan fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/). Silakan cek cuplikan kode berikut untuk menambahkan gambar di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.

1. Tentukan nama file PDF di mana gambar akan ditambahkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Tambahkan gambar ke akhir PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddImage.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Tambahkan gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana gambar akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Tambahkan gambar ke akhir PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddImage.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Tambahkan sebuah gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```