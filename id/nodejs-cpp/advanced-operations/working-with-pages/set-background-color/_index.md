---
title: Atur warna latar belakang untuk PDF di Node.js
linktitle: Atur warna latar belakang
type: docs
weight: 80
url: /id/nodejs-cpp/set-background-color/
description: Atur warna latar belakang untuk file PDF Anda dengan Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin mengatur warna latar belakang PDF, Anda dapat menggunakan [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) fungsi. 

Silakan periksa cuplikan kode berikut untuk mengatur warna latar belakang PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang ingin Anda atur warna latar belakangnya.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengatur warna latar belakang. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Setel warna latar belakang untuk file PDF. Anda harus mengirimkan 3 argumen ke fungsi ini: nama file input, warna yang diinginkan dalam format heksadesimal, dan nama file output. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan berada di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang ingin Anda atur warna latar belakangnya.
1. Inisialisasi modul AsposePdf. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Atur warna latar belakang untuk file PDF. Warna latar belakang diatur menjadi "#426bf4," yang merupakan kode warna heksadesimal yang merepresentasikan warna biru. Oleh karena itu, jika `json.errorCode` bernilai 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter `json.errorCode` tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam `json.errorText`.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```