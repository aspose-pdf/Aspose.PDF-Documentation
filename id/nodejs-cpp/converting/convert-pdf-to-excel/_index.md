---
title: Konversi PDF ke Excel di Node.js
linktitle: Konversi PDF ke Excel
type: docs
weight: 20
url: /id/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js memungkinkan Anda mengonversi PDF ke format XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Membuat spreadsheet dari PDF menggunakan Node.js 

**Aspose.PDF for Node.js via C++** mendukung fitur mengonversi file PDF ke file Excel.

{{% alert color="success" %}}
**Coba mengonversi PDF ke Excel secara daring**

Aspose.PDF for Node.js mempersembahkan aplikasi gratis daring untuk Anda ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)**, di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.**

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Konversi PDF ke XLSX

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) fungsi. 
Silakan periksa cuplikan kode berikut untuk melakukan konversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Dapatkan objeknya jika berhasil.
1. Panggil fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

