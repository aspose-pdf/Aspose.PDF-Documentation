---
title: Ekstrak Gambar dari PDF di Node.js
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: /id/nodejs-cpp/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian gambar dari PDF menggunakan Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak gambar dari file PDF dalam lingkungan Node.js

Jika Anda ingin mengekstrak gambar dari dokumen PDF, Anda dapat menggunakan [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) fungsi. 
Kita harus mengirim tiga argumen ke fungsi ini: nama file input dan output serta resolusi.
Silakan periksa potongan kode berikut untuk mengekstrak gambar dari file PDF menggunakan Node.js.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan diekstrak gambarnya.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstrak gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Ekstrak gambar dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfExtractImage{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error pada file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan diekstrak gambarnya.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Ekstrak gambar dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfExtractImage{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error pada file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
