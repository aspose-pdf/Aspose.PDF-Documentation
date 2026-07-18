---
title: Perbaiki PDF di Node.js
linktitle: Perbaiki PDF
type: docs
weight: 10
url: /id/nodejs-cpp/repair-pdf/
description: Topik ini menjelaskan cara memperbaiki PDF di lingkungan Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js memungkinkan perbaikan PDF berkualitas tinggi. File PDF mungkin tidak dapat dibuka karena alasan apa pun, terlepas dari program atau browser yang digunakan. Dalam beberapa kasus dokumen dapat dipulihkan, coba kode berikut dan lihat sendiri.
Jika Anda ingin memperbaiki dokumen PDF, Anda dapat menggunakan [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) fungsi. 
Silakan periksa potongan kode berikut untuk memperbaiki file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan diperbaiki.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk memperbaiki file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Perbaiki file PDF. Jadi, jika \u0027json.errorCode\u0027 adalah 0, hasil operasi disimpan dalam \u0022ResultPdfRepair.pdf\u0022. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan berada dalam \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan diperbaiki.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Perbaiki file PDF. Jadi, jika \u0027json.errorCode\u0027 adalah 0, hasil operasi disimpan dalam \u0022ResultPdfRepair.pdf\u0022. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan berada dalam \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```