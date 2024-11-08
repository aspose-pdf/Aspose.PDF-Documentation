---
title: Mengatur warna latar belakang untuk PDF di Node.js
linktitle: Mengatur warna latar belakang
type: docs
weight: 80
url: /id/nodejs-cpp/set-background-color/
description: Mengatur warna latar belakang untuk file PDF Anda dengan Node.js melalui C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin mengatur warna latar belakang PDF, Anda dapat menggunakan fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

Silakan periksa cuplikan kode berikut untuk mengatur warna latar belakang PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama file PDF yang ingin Anda atur warna latar belakangnya.
3. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengatur warna latar belakang. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
2. Atur warna latar belakang untuk file PDF. Anda perlu melewatkan 3 argumen ke fungsi ini: nama file input, warna yang diinginkan dalam bentuk heksadesimal, dan nama file output. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengatur warna latar belakang untuk file PDF dan simpan sebagai "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang ingin Anda atur warna latar belakangnya.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Atur warna latar belakang untuk file PDF. Warna latar belakang diatur ke "#426bf4," yang merupakan kode warna heksadesimal yang mewakili warna biru. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultRotation.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Atur warna latar belakang untuk file PDF dan simpan "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```