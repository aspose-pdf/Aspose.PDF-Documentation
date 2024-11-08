---
title: Ekstraksi Tabel dari PDF di Node.js
linktitle: Ekstraksi Tabel dari PDF
type: docs
weight: 10
url: /id/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Cara mengonversi PDF ke CSV menggunakan Aspose.PDF untuk Node.js via toolkit C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstraksi tabel saat mengonversi PDF ke file CSV

### Konversi PDF ke CSV

Jika ada tabel dalam PDF maka mereka akan disimpan dalam file CSV terpisah. Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). 
Silakan periksa cuplikan kode berikut untuk mengonversi file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode bukan 0 dan, sesuai dengan itu, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengonversi file PDF ke CSV (ekstrak tabel) dengan template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), TAB sebagai pembatas, dan simpan*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.

1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Konversi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoXlsX.xlsx". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke CSV (ekstrak tabel) dengan template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), TAB sebagai pemisah dan simpan*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```