---
title: Optimalkan Sumber Daya PDF di Node.js
linktitle: Optimalkan Sumber Daya PDF
type: docs
weight: 15
url: /nodejs-cpp/optimize-pdf-resources/
description: Optimalkan Sumber Daya dari file PDF untuk tampilan web cepat menggunakan alat Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimalkan Sumber Daya PDF

Optimalkan sumber daya di dokumen:

1. Sumber daya yang tidak digunakan pada halaman dokumen dihapus
1. Sumber daya yang sama digabungkan menjadi satu objek
1. Objek yang tidak digunakan dihapus
 

Jika Anda ingin mengoptimalkan sumber daya PDF, Anda dapat menggunakan fungsi [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). Silakan periksa cuplikan kode berikut untuk mengoptimalkan sumber daya PDF di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang sumber dayanya akan dioptimalkan.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengoptimalkan file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimalkan sumber daya PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfOptimizeResource.pdf". Jika parameter json.errorCode bukan 0 dan, dengan demikian, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimalkan sumber daya file PDF dan simpan sebagai "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang sumber dayanya akan dioptimalkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimalkan sumber daya PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfOptimizeResource.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terdapat kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimalkan sumber daya file PDF dan simpan dalam "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```