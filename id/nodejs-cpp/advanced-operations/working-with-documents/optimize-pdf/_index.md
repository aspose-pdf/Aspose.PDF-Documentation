---
title: Optimalkan PDF menggunakan Aspose.PDF untuk Node.js via C++
linktitle: Optimalkan File PDF
type: docs
weight: 10
url: id/nodejs-cpp/optimize-pdf/
description: Optimalkan dan kompres file PDF untuk tampilan web cepat menggunakan lingkungan Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimalkan Dokumen PDF

Toolkit oleh Aspose.PDF untuk Node.js via C++ memungkinkan Anda untuk mengoptimalkan konten PDF untuk lingkungan Node.js.

Optimalisasi, atau linearisasi mengacu pada proses membuat file PDF cocok untuk penelusuran online menggunakan browser web.

Jika Anda ingin mengoptimalkan PDF, Anda dapat menggunakan fungsi [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
Silakan periksa cuplikan kode berikut untuk mengoptimalkan file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dioptimalkan.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengoptimalkan file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimalkan file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultOptimize.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimalkan file PDF dan simpan sebagai "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dioptimalkan.

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.  
1. Panggil fungsi [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).  
1. Optimalkan file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultOptimize.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimalkan file PDF dan simpan sebagai "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```