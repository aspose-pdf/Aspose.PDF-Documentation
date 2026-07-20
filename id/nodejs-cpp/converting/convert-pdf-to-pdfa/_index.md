---
title: Konversi PDF ke format PDF/A di Node.js
linktitle: Konversi PDF ke format PDF/A
type: docs
weight: 100
url: /id/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: Topik ini menunjukkan cara Aspose.PDF memungkinkan mengonversi file PDF menjadi file PDF yang mematuhi PDF/A dalam lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** memungkinkan Anda mengonversi file PDF menjadi <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> file PDF yang patuh. 

{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A secara online**

Aspose.PDF for Node.js mempersembahkan Anda aplikasi gratis daring ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Konversi PDF ke format PDF/A

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) fungsi. 
Silakan periksa cuplikan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Perbaiki file PDF. Jadi, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan di “ResultConvertToPDFA.pdf”. Selama proses konversi, validasi dilakukan, dan hasil validasi disimpan sebagai “ResultConvertToPDFALog.xml.” Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFALog.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Perbaiki file PDF. Jadi, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan di “ResultConvertToPDFA.pdf”. Selama proses konversi, validasi dilakukan, dan hasil validasi disimpan sebagai “ResultConvertToPDFALog.xml.” Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFALog.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





