---
title: Bookmark dalam PDF di Node.js
linktitle: Bookmark dalam PDF
type: docs
weight: 10
url: /id/nodejs-cpp/bookmark/
description: Anda dapat menambah atau menghapus bookmark dalam dokumen PDF di lingkungan Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hapus Bookmark Tertentu dari Dokumen PDF

Anda dapat menghapus bookmark dari file PDF menggunakan Aspose.PDF untuk Node.js via C++. Jika Anda ingin menghapus bookmark dari PDF, Anda dapat menggunakan [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) fungsi. 
Silakan periksa potongan kode berikut untuk menghapus bookmark dari file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang bookmark-nya akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus bookmark. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Hapus bookmark. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteBookmarks.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, sebuah kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang bookmark-nya akan dihapus.
1. Inisialisasi modul AsposePdf. Dapatkan objeknya jika berhasil.
1. Panggil fungsi [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Hapus bookmark. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteBookmarks.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, sebuah kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```