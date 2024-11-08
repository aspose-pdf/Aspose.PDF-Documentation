---
title: Hapus Anotasi di Node.js
linktitle: Hapus Anotasi
type: docs
weight: 10
url: /id/nodejs-cpp/delete-annotation/
description: Dengan Aspose.PDF untuk Node.js Anda dapat menghapus anotasi dari file PDF Anda.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Anda dapat menghapus anotasi dari file PDF menggunakan Aspose.PDF untuk Node.js via C++. Jika Anda ingin menghapus anotasi dari PDF, Anda dapat menggunakan fungsi [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). Silakan periksa cuplikan kode berikut untuk menghapus anotasi dari file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF dari mana anotasi akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus anotasi. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Hapus anotasi. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteAnnotations.pdf". Jika parameter json.errorCode bukan 0 dan, oleh karena itu, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Hapus anotasi dari file PDF dan simpan sebagai "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana anotasi akan dihapus.

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Hapus anotasi. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteAnnotations.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Hapus anotasi dari file PDF dan simpan sebagai "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```