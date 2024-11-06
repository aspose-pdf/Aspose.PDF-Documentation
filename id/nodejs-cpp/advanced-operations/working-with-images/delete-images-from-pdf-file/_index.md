---
title: Hapus Gambar dari File PDF di Node.js
linktitle: Hapus Gambar
type: docs
weight: 20
url: id/nodejs-cpp/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus gambar dari file PDF menggunakan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
---

Anda dapat menghapus gambar dari file PDF menggunakan Aspose.PDF untuk Node.js via C++.

Jika Anda ingin menghapus gambar dari PDF, Anda dapat menggunakan fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/). Silakan periksa cuplikan kode berikut untuk menghapus gambar dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF di mana gambar akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. Hapus gambar dari PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteImages.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Hapus gambar dari file PDF dan simpan sebagai "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana gambar akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Hapus gambar dari PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteImages.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Hapus gambar dari file PDF dan simpan sebagai "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```