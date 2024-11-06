---

title: Mengubah PDF ke Dokumen Word di Node.js  
linktitle: Mengubah PDF ke Word  
type: docs  
weight: 10  
url: id/nodejs-cpp/convert-pdf-to-doc/  
lastmod: "2023-11-16"  
description: Pelajari cara mengubah PDF ke DOC(DOCX) di lingkungan Node.js.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---

Untuk mengedit konten file PDF di Microsoft Word atau pengolah kata lainnya yang mendukung format DOC dan DOCX. File PDF dapat diedit, tetapi file DOC dan DOCX lebih fleksibel dan dapat disesuaikan.

{{% alert color="success" %}}  
**Cobalah untuk mengubah PDF ke DOC secara online**

Aspose.PDF untuk Node.js mempersembahkan kepada Anda aplikasi online gratis ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas yang dimilikinya.

[![Ubah PDF ke DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)  
{{% /alert %}}

## Mengubah PDF ke DOC

Jika Anda ingin mengubah dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
Silakan periksa potongan kode berikut untuk dikonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultPDFtoDoc.doc". Jika parameter json.errorCode bukan 0 dan, dengan demikian, ada kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengonversi file PDF ke Doc dan menyimpan "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Konversi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoDoc.doc". Jika parameter json.errorCode tidak 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke Doc dan simpan sebagai "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Coba konversi PDF ke DOCX online**


Aspose.PDF untuk Node.js menghadirkan aplikasi online gratis ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Word Aplikasi Gratis](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Konversi PDF ke DOCX

Aspose.PDF untuk Node.js melalui toolkit C++ memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX. DOCX adalah format yang dikenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi lateral tetapi tidak dengan versi sebelumnya dari MS Word yang mendukung ekstensi file DOC.

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/). Silakan periksa potongan kode berikut untuk mengonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPDFtoDocX.docx". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengonversi berkas PDF ke DocX dan menyimpan "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultPDFtoDocX.docx". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke DocX dan simpan sebagai "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```