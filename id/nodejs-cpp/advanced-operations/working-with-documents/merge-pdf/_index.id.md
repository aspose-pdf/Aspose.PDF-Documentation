---
title: Cara Menggabungkan PDF di Node.js
linktitle: Menggabungkan file PDF
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menggabungkan atau mengombinasikan dua PDF menjadi satu PDF di Node.js

Menggabungkan dan mengombinasikan file adalah tugas yang sangat populer ketika bekerja dengan sejumlah besar dokumen. Terkadang, ketika bekerja dengan dokumen dan gambar, ketika mereka dipindai, diproses, dan diatur, beberapa file dibuat. Tetapi bagaimana jika Anda perlu menyimpan semuanya dalam satu file? Atau Anda tidak ingin mencetak beberapa dokumen? Gabungkan dua file PDF dengan Aspose.PDF untuk Node.js via C++.

Jika Anda ingin menggabungkan dua PDF, Anda dapat menggunakan fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/). Silakan periksa potongan kode berikut untuk menggabungkan dua file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan digabungkan.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk penggabungan. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Gabungkan dua file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultMerge.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Gabungkan dua file PDF dan simpan sebagai "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan digabungkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Gabungkan dua file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultMerge.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan ada dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Gabungkan dua file PDF dan simpan ke "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```