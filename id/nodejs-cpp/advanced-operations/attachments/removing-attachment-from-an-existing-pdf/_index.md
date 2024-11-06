---
title: Menghapus lampiran dari PDF di Node.js
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 10
url: id/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan lingkungan Node.js untuk menghapus lampiran dalam file PDF dengan Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus lampiran dari file PDF menggunakan Aspose.PDF untuk Node.js melalui C++. Jika Anda ingin menghapus lampiran dari PDF, Anda dapat menggunakan fungsi [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/). Silakan periksa potongan kode berikut untuk menghapus lampiran dari file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF dari mana lampiran akan dihapus.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menghapus lampiran. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Hapus lampiran. Jadi, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultPdfDeleteAttachments.pdf". Jika parameter json.errorCode bukan 0 dan, dengan demikian, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Hapus lampiran dari file PDF dan simpan sebagai "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana lampiran akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Hapus lampiran. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfDeleteAttachments.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Hapus lampiran dari file PDF dan simpan "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```