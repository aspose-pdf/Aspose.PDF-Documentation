---

title: Bekerja dengan Metadata File PDF di Node.js  
linktitle: Metadata File PDF  
type: docs  
weight: 130  
url: /id/nodejs-cpp/pdf-file-metadata/  
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan metadata dari file PDF, mengatur Informasi File PDF di Node.js.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  

---

## Mendapatkan Informasi File PDF

Jika Anda ingin mendapatkan informasi file PDF, Anda dapat menggunakan fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/). Silakan periksa cuplikan kode berikut untuk mendapatkan informasi file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF dari mana informasi akan diekstraksi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstraksi info. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Metadata yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, metadata yang diekstrak ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Dapatkan info (metadata) dari file PDF*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Judul             : json.title
        Pembuat           : json.creator
        Penulis           : json.author
        Subjek            : json.subject
        Kata Kunci        : json.keywords
        Tanggal Pembuatan : json.creation
        Tanggal Modifikasi: json.mod
        Format PDF        : json.format
        Versi PDF         : json.version
        PDF adalah PDF/A  : json.ispdfa
        PDF adalah PDF/UA : json.ispdfua
        PDF terlinearasi  : json.islinearized
        PDF terenkripsi   : json.isencrypted
        Izin PDF          : json.permission
        Ukuran halaman PDF: json.size
        Jumlah halaman    : json.pagecount
        Jumlah anotasi    : json.annotationcount
        Jumlah penanda    : json.bookmarkcount
        Jumlah lampiran   : json.attachmentcount
        Jumlah metadata   : json.metadatacount
        Jumlah JavaScript : json.javascriptcount
        Jumlah gambar     : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Judul: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana informasi akan diekstraksi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Metadata yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, metadata yang diekstraksi ditampilkan menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Dapatkan info (metadata) dari file PDF*/
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

Mendapatkan font dari file PDF bisa menjadi cara yang berguna untuk menggunakan kembali font dalam dokumen atau aplikasi lain.

Jika Anda ingin mendapatkan font dari file PDF, Anda dapat menggunakan fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/). Silakan periksa cuplikan kode berikut untuk mendapatkan font dari file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF dari mana font akan diekstraksi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstraksi font. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. Font yang diekstrak disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, itu menampilkan array detail font, termasuk nama font, apakah itu tersemat, dan status aksesibilitasnya menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Dapatkan daftar font dari file PDF*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array dari font: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana font akan diekstraksi.

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Font yang diekstraksi disimpan dalam objek JSON. Jadi, jika 'json.errorCode' adalah 0, ia menampilkan array detail font, termasuk nama font, apakah itu tertanam, dan status aksesibilitasnya menggunakan console.log. Jika parameter json.errorCode bukan 0 dan, sesuai, sebuah kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Dapatkan daftar font dari file PDF*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Atur Informasi File PDF


Aspose.PDF untuk Node.js via C++ memungkinkan Anda untuk mengatur informasi spesifik file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul. Untuk mengatur informasi ini:

Jika Anda ingin mengatur informasi spesifik file, Anda dapat menggunakan fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
Silakan periksa potongan kode berikut untuk mengatur informasi file dalam lingkungan Node.js.

Dapat diatur:
- judul
- pembuat
- penulis
- subjek
- daftar kata kunci
- tanggal pembuatan
- tanggal modifikasi
- nama file hasil

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF di mana informasi akan diatur.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. Tetapkan informasi file PDF. Informasi seperti judul, pembuat, penulis, subjek, kata kunci, tanggal pembuatan, dan tanggal modifikasi disediakan sebagai parameter. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSetInfo.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Tetapkan info PDF: judul, pembuat, penulis, subjek, kata kunci, pembuatan (tanggal), mod (tanggal modifikasi)*/
      /*Jika tidak perlu menetapkan nilai, gunakan undefined atau "" (string kosong)*/
      /*Tetapkan info (metadata) dalam file PDF dan simpan sebagai "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Menetapkan Informasi Dokumen PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF tempat informasi akan diatur.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Atur informasi file PDF. Informasi seperti judul, pembuat, penulis, subjek, kata kunci, tanggal pembuatan, dan tanggal modifikasi diberikan sebagai parameter. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSetInfo.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*Jika tidak perlu mengatur nilai, gunakan undefined atau "" (string kosong)*/
  /*Atur info (metadata) dalam file PDF dan simpan sebagai "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## Menghapus Informasi File PDF

Aspose.PDF untuk Node.js melalui C++ memungkinkan Anda untuk menghapus Metadata file PDF:

Jika Anda ingin menghapus metadata dari PDF, Anda dapat menggunakan fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). Silakan periksa potongan kode berikut untuk menghapus metadata dari PDF di lingkungan Node.js.

**CommonJS:**

1. Memerlukan modul AsposePDFforNode.js.
1. Tentukan nama file PDF dari mana informasi akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Hapus informasi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfRemoveMetadata.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Menghapus metadata dari file PDF dan menyimpan "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF dari mana informasi akan dihapus.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Hapus informasi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfRemoveMetadata.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai dengan itu, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Hapus metadata dari file PDF dan simpan "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```