---
title: Tambahkan penomoran halaman ke PDF di Node.js
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: /id/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ memungkinkan Anda menambahkan Page Number Stamp ke file PDF Anda menggunakan AsposePdfAddPageNum.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen. Potongan kode berikut menunjukkan cara menambahkan nomor halaman ke halaman PDF menggunakan [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) fungsi di Node.js.

Silakan periksa potongan kode berikut untuk menambahkan nomor halaman ke PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF di mana nomor halaman akan ditambahkan.
1. Panggilan `AsposePdf` sebagai Promise dan melakukan operasi untuk menambahkan nomor halaman. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Tambahkan nomor halaman ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddPageNum.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan ada di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF di mana nomor halaman akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Tambahkan nomor halaman ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddPageNum.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan ada di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```