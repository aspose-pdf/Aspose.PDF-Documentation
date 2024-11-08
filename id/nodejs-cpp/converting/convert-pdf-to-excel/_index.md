---
title: Mengonversi PDF ke Excel di Node.js
linktitle: Mengonversi PDF ke Excel
type: docs
weight: 20
url: /id/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
keywords: mengonversi PDF ke Excel menggunakan node.js, mengonversi PDF ke XLSX.
description: Aspose.PDF untuk Node.js memungkinkan Anda mengonversi PDF ke format XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Membuat spreadsheet dari PDF menggunakan Node.js

**Aspose.PDF untuk Node.js via C++** mendukung fitur konversi file PDF ke file Excel.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke Excel secara online**

Aspose.PDF untuk Node.js menghadirkan aplikasi online gratis ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba mengeksplorasi fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Mengonversi PDF ke XLSX

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
 
Silakan periksa cuplikan kode berikut untuk dikonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke XlsX dan simpan sebagai "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke XlsX dan simpan sebagai "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```