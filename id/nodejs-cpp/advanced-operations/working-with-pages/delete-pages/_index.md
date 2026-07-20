---
title: Hapus Halaman dalam PDF di Node.js
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: /id/nodejs-cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin menghapus halaman PDF, Anda dapat menggunakan [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) fungsi. 

Fitur dari fungsi ini adalah dapat menerima beberapa tipe sebagai parameter numPages:

- string: dalam kasus ini, kita dapat menyebutkan satu set halaman menggunakan halaman tertentu atau interval. Misalnya, string '7, 20, 30-32, 34' berarti kita ingin menghapus halaman 7, 20, dari 30 sampai 32, dan 34.
- array: dalam kasus ini, kita hanya dapat menyebutkan halaman. Array [3,7] berarti kita ingin menghapus halaman 3 dan 7.
- int: satu nomor halaman.

Silakan periksa cuplikan kode berikut untuk menghapus halaman PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang halaman‑halamannya akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk menghapus halaman. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Menghapus halaman‑halaman tertentu dari file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan di "ResultDeletePages.pdf". Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan pada file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang halaman‑halamannya akan dihapus.
1. Inisialisasi modul AsposePdf. Dapatkan objeknya jika berhasil.
1. Panggil fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Fungsi ini membantu menghapus halaman yang ditentukan dari file PDF. Operasi ditentukan oleh variabel numPages, yang dapat berupa string dengan interval halaman (misalnya “7, 20, 22, 30-32, 33, 36-40, 46”), array nomor halaman, atau satu nomor halaman.
1. Menghapus halaman‑halaman tertentu dari file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan di "ResultDeletePages.pdf". Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan pada file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```