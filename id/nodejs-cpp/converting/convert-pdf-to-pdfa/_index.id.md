---
title: Mengonversi PDF ke format PDF/A di Node.js 
linktitle: Mengonversi PDF ke format PDF/A
type: docs
weight: 100
url: /nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF menjadi file PDF yang sesuai dengan PDF/A di lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk Node.js** memungkinkan Anda untuk mengonversi file PDF menjadi file PDF yang sesuai dengan <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr>. 

{{% alert color="success" %}}
**Coba mengonversi PDF ke PDF/A secara online**

Aspose.PDF untuk Node.js menyajikan aplikasi gratis online ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Mengonversi PDF ke format PDF/A

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
Silakan periksa cuplikan kode berikut untuk mengonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Perbaiki file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultConvertToPDFA.pdf". Selama proses konversi, validasi dilakukan, dan hasil validasi disimpan sebagai "ResultConvertToPDFALog.xml." Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengonversi file PDF ke PDF/A(1A) dan menyimpan "ResultConvertToPDFA.pdf"*/
      /*Selama proses konversi, validasi juga dilakukan, "ResultConvertToPDFALog.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Perbaiki file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultConvertToPDFA.pdf". Selama proses konversi, validasi dilakukan, dan hasil validasi disimpan sebagai "ResultConvertToPDFALog.xml." Jika parameter json.errorCode tidak 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke PDF/A(1A) dan simpan sebagai "ResultConvertToPDFA.pdf"*/
  /*Selama proses konversi, validasi juga dilakukan, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```