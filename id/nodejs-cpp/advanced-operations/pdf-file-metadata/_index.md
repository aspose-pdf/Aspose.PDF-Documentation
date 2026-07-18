---
title: Bekerja dengan Metadata File PDF di Node.js
linktitle: Metadata File PDF
type: docs
weight: 130
url: /id/nodejs-cpp/pdf-file-metadata/
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan metadata dari file PDF, mengatur Informasi File PDF di Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Informasi File PDF

Jika Anda ingin mendapatkan informasi file PDF, Anda dapat menggunakan [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) fungsi. 
Silakan periksa potongan kode berikut untuk mendapatkan informasi file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang informasinya akan diekstrak.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstrak info. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Metadata yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' bernilai 0, metadata yang diekstrak ditampilkan menggunakan console.log. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang informasinya akan diekstrak.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Metadata yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' bernilai 0, metadata yang diekstrak ditampilkan menggunakan console.log. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## Dapatkan Semua Font

Mengambil font dari file PDF dapat menjadi cara yang berguna untuk menggunakan kembali font dalam dokumen atau aplikasi lain. 

Jika Anda ingin mengambil font dari sebuah file PDF, Anda dapat menggunakan [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) fungsi. 
Silakan periksa potongan kode berikut untuk mendapatkan font dari file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF dari mana font akan diekstrak.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstrak font. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Font yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, ia menampilkan array detail font, termasuk nama font, apakah font tersebut ter-embed, dan status aksesibilitasnya menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF dari mana font akan diekstrak.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Font yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, ia menampilkan array detail font, termasuk nama font, apakah font tersebut ter-embed, dan status aksesibilitasnya menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Atur Informasi File PDF

Aspose.PDF for Node.js via C++ memungkinkan Anda mengatur informasi khusus file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul. Untuk mengatur informasi ini:

Jika Anda ingin mengatur informasi khusus file, Anda dapat menggunakan [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) fungsi. 
Silakan periksa potongan kode berikut untuk mengatur informasi file di lingkungan Node.js.

Mungkin diatur: 
- judul
- pencipta
- penulis
- subjek
- daftar kata kunci
- tanggal pembuatan
- ubah tanggal
- nama file hasil

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF tempat informasi akan diatur.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Setel informasi file PDF. Informasi seperti judul, pembuat, penulis, subjek, kata kunci, tanggal pembuatan, dan tanggal modifikasi disediakan sebagai parameter. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSetInfo.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF tempat informasi akan diatur.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Setel informasi file PDF. Informasi seperti judul, pembuat, penulis, subjek, kata kunci, tanggal pembuatan, dan tanggal modifikasi disediakan sebagai parameter. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSetInfo.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Hapus Informasi File PDF

Aspose.PDF for Node.js via C++ memungkinkan Anda menghapus Metadata file PDF:

Jika Anda ingin menghapus metadata dari PDF, Anda dapat menggunakan [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) fungsi. 
Harap periksa cuplikan kode berikut untuk menghapus metadata dari PDF di lingkungan Node.js.

**CommonJS:**

1. Minta modul AsposePDFforNode.js.
1. Tentukan nama file PDF dari mana informasi akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Hapus informasi file PDF. Jadi, jika \u0027json.errorCode\u0027 adalah 0, hasil operasi disimpan dalam \u0022ResultPdfRemoveMetadata.pdf\u0022. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan terdapat dalam \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF dari mana informasi akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Hapus informasi file PDF. Jadi, jika \u0027json.errorCode\u0027 adalah 0, hasil operasi disimpan dalam \u0022ResultPdfRemoveMetadata.pdf\u0022. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan terdapat dalam \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```