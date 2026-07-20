---
title: Konversi PDF ke PPTX di Node.js
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-18"
description: Aspose.PDF memungkinkan Anda mengonversi PDF ke format PPTX menggunakan Node.js secara langsung di lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Coba mengonversi PDF ke PowerPoint secara online**

Aspose.PDF for Node.js mempersembahkan aplikasi gratis online ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Konversi PDF ke PPTX

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) fungsi. 
Silakan periksa cuplikan kode berikut untuk melakukan konversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoPptX.pptx". Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul error dalam file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoPptX.pptx". Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul error dalam file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```