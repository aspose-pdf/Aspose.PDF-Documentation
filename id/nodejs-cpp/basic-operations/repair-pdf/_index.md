---
title: Memperbaiki PDF di Node.js 
linktitle: Memperbaiki PDF
type: docs
weight: 10
url: id/nodejs-cpp/repair-pdf/
description: Topik ini menjelaskan cara Memperbaiki PDF di lingkungan Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF untuk Node.js memungkinkan perbaikan PDF berkualitas tinggi. File PDF mungkin tidak terbuka karena alasan apapun, terlepas dari program atau browser. Dalam beberapa kasus, dokumen dapat dipulihkan, coba kode berikut dan lihat sendiri.
Jika Anda ingin memperbaiki dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
Silakan cek potongan kode berikut untuk memperbaiki file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan diperbaiki.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk memperbaiki file. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Perbaiki file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfRepair.pdf". Jika parameter json.errorCode bukan 0 dan, dengan demikian, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Perbaiki file PDF dan simpan sebagai "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan diperbaiki.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Perbaiki file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfRepair.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, sebuah kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Memperbaiki file PDF dan simpan sebagai "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```