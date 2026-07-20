---
title: Konversi PDF/A ke format PDF di Node.js
linktitle: Konversi PDF/A ke format PDF
type: docs
weight: 110
url: /id/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: Topik ini menunjukkan cara Aspose.PDF memungkinkan mengonversi file PDF/A menjadi dokumen PDF dalam lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Konversi PDF/A ke format PDF

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultConvertToPDF.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF/A yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultConvertToPDF.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```