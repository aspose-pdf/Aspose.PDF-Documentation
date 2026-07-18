---
title: Hapus Gambar dari File PDF di Node.js
linktitle: Hapus Gambar
type: docs
weight: 20
url: /id/nodejs-cpp/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus Gambar dari File PDF menggunakan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---


Anda dapat menghapus gambar dari file PDF menggunakan Aspose.PDF for Node.js via C++.

Jika Anda ingin menghapus gambar dari PDF, Anda dapat menggunakan [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) fungsi. 
Silakan periksa potongan kode berikut untuk menghapus gambar di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF di mana gambar akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Hapus gambar dari PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteImages.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul error dalam file Anda, informasi error akan berada di 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF di mana gambar akan dihapus.
1. Inisialisasi modul AsposePdf. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Hapus gambar dari PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteImages.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul error dalam file Anda, informasi error akan berada di 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```