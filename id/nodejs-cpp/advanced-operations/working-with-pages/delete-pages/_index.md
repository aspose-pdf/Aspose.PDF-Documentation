---
title: Hapus Halaman di PDF dalam Node.js
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: id/nodejs-cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan Aspose.PDF untuk Node.js melalui C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin menghapus halaman PDF, Anda dapat menggunakan fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).

Salah satu fitur dari fungsi ini adalah dapat menerima beberapa jenis sebagai parameter numPages:

- string: dalam hal ini, kita dapat menyebutkan serangkaian halaman menggunakan halaman tertentu atau interval. Misalnya, string "7, 20, 30-32, 34" berarti kita ingin menghapus halaman 7, 20, dari 30 hingga 32 dan 34.
- array: dalam hal ini, kita hanya dapat menyebutkan halaman. Array [3,7] berarti kita ingin menghapus halaman 3 dan 7.
- int: nomor halaman tunggal.

Silakan periksa cuplikan kode berikut untuk menghapus halaman PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF dari mana halaman akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus halaman. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. Menghapus halaman tertentu dari file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultDeletePages.pdf". Jika parameter json.errorCode bukan 0 dan, oleh karena itu, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, termasuk nomor halaman dengan interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array dari nomor halaman*/
      /*const numPages = [1,3];*/
      /*number, nomor halaman*/
      const numPages = 1;
      /*Hapus halaman dari file PDF dan simpan sebagai "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana halaman akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Fungsi ini membantu menghapus halaman yang ditentukan dari file PDF. Operasi ditentukan oleh variabel numPages, yang dapat berupa string dengan interval halaman (misalnya, "7, 20, 22, 30-32, 33, 36-40, 46"), array nomor halaman, atau satu nomor halaman.
1. Menghapus halaman tertentu dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultDeletePages.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, termasuk nomor halaman dengan interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array nomor halaman*/
  /*const numPages = [1,3];*/
  /*number, nomor halaman*/
  const numPages = 1;
  /*Hapus halaman dari file PDF dan simpan "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```