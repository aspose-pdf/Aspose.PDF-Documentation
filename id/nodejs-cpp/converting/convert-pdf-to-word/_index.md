---
title: Konversi PDF ke dokumen Word di Node.js
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: /id/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: Pelajari cara mengonversi PDF ke DOC(DOCX) dalam lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Untuk mengedit konten file PDF di Microsoft Word atau pengolah kata lain yang mendukung format DOC dan DOCX. File PDF dapat diedit, namun file DOC dan DOCX lebih fleksibel dan dapat disesuaikan.

{{% alert color="success" %}}
**Coba konversi PDF ke DOC secara daring**

Aspose.PDF for Node.js mempersembahkan aplikasi gratis daring untuk Anda ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi PDF ke DOC](/pdf/id/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOC

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) fungsi. 
Silakan periksa cuplikan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Mengonversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoDoc.doc". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Mengonversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoDoc.doc". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Coba konversi PDF ke DOCX secara online**

Aspose.PDF for Node.js mempersembahkan aplikasi gratis daring untuk Anda ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aplikasi Gratis Konversi PDF ke Word Aspose.PDF](/pdf/id/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Konversi PDF ke DOCX

Aspose.PDF for Node.js via C++ toolkit memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX. DOCX adalah format yang dikenal luas untuk dokumen Microsoft Word yang strukturnya diubah dari biner polos menjadi kombinasi file XML dan biner. File DOCX dapat dibuka dengan Word 2007 dan versi terbaru tetapi tidak dengan versi sebelumnya dari MS Word yang mendukung ekstensi file DOC.

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) fungsi. 
Silakan periksa cuplikan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoDocX.docx". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi error pada file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoDocX.docx". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi error pada file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


