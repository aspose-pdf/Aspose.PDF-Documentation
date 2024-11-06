---
title: Bookmark di PDF di Node.js
linktitle: Bookmark di PDF
type: docs
weight: 10
url: id/nodejs-cpp/bookmark/
description: Anda dapat menambah atau menghapus bookmark di dokumen PDF dalam lingkungan Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hapus Bookmark Tertentu dari Dokumen PDF

Anda dapat menghapus bookmark dari file PDF menggunakan Aspose.PDF untuk Node.js melalui C++. Jika Anda ingin menghapus bookmark dari PDF, Anda dapat menggunakan fungsi [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
Silakan cek potongan kode berikut untuk menghapus bookmark dari file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama file PDF dari mana bookmark akan dihapus.
3. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus bookmark. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Hapus penanda buku. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteBookmarks.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Hapus penanda buku dari file PDF dan simpan sebagai "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana penanda buku akan dihapus.

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Hapus penanda buku. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteBookmarks.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan ada dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Hapus penanda buku dari file PDF dan simpan "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```