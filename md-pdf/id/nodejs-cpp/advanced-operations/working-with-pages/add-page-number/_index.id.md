---
title: Tambahkan penomoran halaman ke PDF di Node.js
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: /nodejs-cpp/add-page-number/
description: Aspose.PDF untuk Node.js melalui C++ memungkinkan Anda menambahkan Cap Nomor Halaman ke file PDF Anda menggunakan AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian yang berbeda dari dokumen. Cuplikan kode berikut menunjukkan cara menambahkan nomor halaman ke halaman PDF menggunakan fungsi [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) di Node.js.

Silakan periksa cuplikan kode berikut untuk menambahkan nomor halaman ke dalam PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama file PDF di mana nomor halaman akan ditambahkan.
3. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan nomor halaman. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Tambahkan nomor halaman ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddPageNum.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Tambahkan nomor halaman ke file PDF dan simpan sebagai "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana nomor halaman akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Tambahkan nomor halaman ke file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddPageNum.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Tambahkan nomor halaman ke file PDF dan simpan "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```