---
title: Menghapus lampiran dari PDF di Node.js
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 10
url: /id/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan lingkungan Node.js untuk menghapus lampiran dalam file PDF dengan Aspose.PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus lampiran dari file PDF menggunakan Aspose.PDF for Node.js via C++. Jika Anda ingin menghapus lampiran dari PDF, Anda dapat menggunakan [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) fungsi. 
Silakan periksa cuplikan kode berikut untuk menghapus lampiran dari file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang lampirannya akan dihapus.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus lampiran. Terima objek jika berhasil.
1. Panggil fungsi tersebut [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Hapus lampiran. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPdfDeleteAttachments.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang lampirannya akan dihapus.
1. Inisialisasi modul AsposePdf. Dapatkan objek jika berhasil.
1. Panggil fungsi tersebut [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Hapus lampiran. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPdfDeleteAttachments.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```