---
title: Membagi PDF di Node.js
linktitle: Membagi file PDF
type: docs
weight: 30
url: /id/nodejs-cpp/split-pdf/
description: Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individu dengan Aspose.PDF untuk Node.js melalui C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Membagi PDF menjadi dua file menggunakan Node.js

Jika Anda ingin membagi satu PDF menjadi beberapa bagian, Anda dapat menggunakan fungsi [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
Silakan periksa cuplikan kode berikut untuk membagi dua PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dibagi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi pembagian file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. Pisahkan dua file PDF. Ini menetapkan variabel pageToSplit ke 1, menunjukkan bahwa file PDF akan dipisahkan pada halaman 1. 
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSplit1.pdf", dan "ResultSplit2.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Tetapkan nomor halaman untuk dipisahkan*/
      const pageToSplit = 1;
      /*Pisahkan ke dua file PDF dan simpan "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.

1. Tentukan nama file PDF yang akan dipisahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Pisahkan dua file PDF. Ini mengatur variabel pageToSplit ke 1, menunjukkan bahwa file PDF akan dipisahkan pada halaman 1.
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSplit1.pdf", dan "ResultSplit2.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Tetapkan nomor halaman untuk dipisahkan*/
  const pageToSplit = 1;
  /*Pisahkan menjadi dua file PDF dan simpan "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```