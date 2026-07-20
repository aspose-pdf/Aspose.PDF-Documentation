---
title: Cara Menggabungkan PDF di Node.js
linktitle: Gabungkan file PDF
type: docs
weight: 20
url: /id/nodejs-cpp/merge-pdf/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Gabungkan atau kombinasikan dua PDF menjadi satu PDF di Node.js

Menggabungkan dan mengkombinasikan file merupakan tugas yang sangat populer selama bekerja dengan sejumlah besar dokumen. Terkadang, saat bekerja dengan dokumen dan gambar, ketika mereka dipindai, diproses, dan diorganisir, beberapa file dibuat.
Tapi bagaimana jika Anda perlu menyimpan semuanya dalam satu file? Atau Anda tidak ingin mencetak beberapa dokumen? Gabungkan dua file PDF dengan Aspose.PDF for Node.js via C++.

Jika Anda ingin menggabungkan dua PDF, Anda dapat menggunakan [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) fungsi. 
Silakan periksa cuplikan kode berikut untuk menggabungkan dua file PDF di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan digabungkan.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk penggabungan. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Gabungkan dua file PDF. Jadi, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan dalam “ResultMerge.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan digabungkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Gabungkan dua file PDF. Jadi, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan dalam “ResultMerge.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```