---
title: Ekstrak Tabel dari PDF di Node.js
linktitle: Ekstrak Tabel dari PDF
type: docs
weight: 10
url: /id/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Cara mengonversi PDF ke CSV menggunakan Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak tabel saat mengonversi PDF ke file CSV

### Konversi PDF ke CSV

Jika ada tabel dalam PDF maka tabel tersebut akan disimpan dalam file CSV terpisah. Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) fungsi. 
Silakan periksa cuplikan kode berikut untuk mengonversi file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Konversi file PDF. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultPDFtoXlsX.xlsx”. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Konversi file PDF. Jadi, jika ‘json.errorCode’ adalah 0, hasil operasi disimpan dalam “ResultPDFtoXlsX.xlsx”. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```