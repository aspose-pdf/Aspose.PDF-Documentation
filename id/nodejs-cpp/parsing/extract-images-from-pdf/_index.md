---
title: Ekstrak Gambar dari PDF di Node.js
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: id/nodejs-cpp/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian dari gambar dari PDF menggunakan Aspose.PDF untuk Node.js melalui toolkit C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak gambar dari file PDF di lingkungan Node.js

Jika Anda ingin mengekstrak gambar dari dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/). Kita harus memberikan tiga argumen untuk fungsi ini: nama file input dan output serta resolusi.
Silakan periksa cuplikan kode berikut untuk mengekstrak gambar dari file PDF menggunakan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama untuk file PDF dari mana gambar akan diekstrak.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengekstraksi gambar. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Ekstrak gambar dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfExtractImage{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ekstrak gambar dari file PDF dengan template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama untuk file PDF dari mana gambar akan diekstraksi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Ekstrak gambar dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfExtractImage{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, dengan demikian, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Ekstrak gambar dari file PDF dengan template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```