---
title: Tambahkan tanda tangan digital dalam PDF di Node.js
linktitle: Tanda tangan digital PDF
type: docs
weight: 70
url: /id/nodejs-cpp/sign-pdf/
description: Tandatangani dokumen PDF secara digital dalam lingkungan Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tanda tangan digital dalam dokumen PDF adalah cara untuk memverifikasi keaslian dan integritas dokumen. Ini adalah proses tanda tangan elektronik dari dokumen PDF menggunakan kunci pribadi dan sertifikat digital. Tanda tangan ini menjamin pemegang bahwa dokumen tersebut tidak diubah atau dimodifikasi sejak penandatanganan dan bahwa penandatangan adalah orang yang disetujui. Untuk menandatangani PDF dengan Node.js, gunakan alat Aspose.PDF.

Jika Anda ingin menandatangani file PDF, Anda dapat menggunakan fungsi [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

Dimungkinkan untuk menggunakan **parameter** terkait tanda tangan:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- lokasi
- isVisible
- signatureAppearance
- fileNameResult 

Cuplikan kode ini menggunakan modul AsposePDFforNode.js di lingkungan Node.js untuk menandatangani file PDF secara digital menggunakan tanda tangan PKCS7.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan ditandatangani, file kunci PKCS7, dan file gambar tampilan tanda tangan. Sertifikat dan gambar dapat ditempatkan di mana saja pada sistem file Anda dari mana Anda mengunggahnya untuk penandatanganan PDF.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menandatangani file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/). 
1. Tandatangani file PDF dengan tanda tangan digital. Parameter terkait tanda tangan (seperti file kunci, kata sandi, koordinat, alasan, kontak, lokasi, dll).

1. Oleh karena itu, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSignPKCS7.pdf". Jika parameter json.errorCode bukan 0 dan, oleh karena itu, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Kunci PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Penampilan tanda tangan*/
      const sign_img_file = 'Aspose.jpg';
      /*Menandatangani file PDF dengan tanda tangan digital dan simpan sebagai "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.

1. Tentukan nama file PDF yang akan ditandatangani, file kunci PKCS7, dan file gambar penampilan tanda tangan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Tandatangani file PDF dengan tanda tangan digital. Parameter terkait tanda tangan (seperti file kunci, kata sandi, koordinat, alasan, kontak, lokasi, dll).
1. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultSignPKCS7.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Kunci PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Penampilan tanda tangan*/
  const sign_img_file = 'Aspose.jpg';
  /*Tandatangani file PDF dengan tanda tangan digital dan simpan "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```