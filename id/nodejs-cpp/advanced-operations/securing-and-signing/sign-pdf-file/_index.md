---
title: Tambahkan tanda tangan digital di PDF di Node.js
linktitle: Tandatangani PDF secara digital
type: docs
weight: 70
url: /id/nodejs-cpp/sign-pdf/
description: Tandatangani dokumen PDF secara digital di lingkungan Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


Tanda tangan digital dalam dokumen PDF adalah cara untuk memverifikasi keaslian dan integritas dokumen. Ini adalah proses penandatanganan elektronik dokumen PDF menggunakan kunci pribadi dan sertifikat digital. Tanda tangan ini menjamin kepada pemegangnya bahwa dokumen tidak diubah atau dimodifikasi sejak penandatanganan dan bahwa penandatangan adalah orang yang menyetujuinya. Untuk menandatangani PDF dengan Node.js, gunakan alat Aspose.PDF.

Jika Anda ingin menandatangani file PDF, Anda dapat menggunakan [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fungsi.

Dimungkinkan untuk menggunakan **parameters** terkait dengan tanda tangan:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- alasan
- kontak
- lokasi
- isVisible
- signatureAppearance
- fileNameResult 

Potongan kode ini menggunakan modul AsposePDFforNode.js dalam lingkungan Node.js untuk menandatangani secara digital file PDF menggunakan tanda tangan PKCS7.

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan ditandatangani, file kunci PKCS7, dan file gambar tampilan tanda tangan. Sertifikat dan gambar dapat ditempatkan di mana saja di sistem file Anda dari mana Anda mengunggahnya untuk penandatanganan PDF.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menandatangani file. Terima objek jika berhasil.
1. Panggil [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fungsi. 
1. Tandatangani file PDF dengan tanda tangan digital. Parameter yang terkait dengan tanda tangan (seperti file kunci, kata sandi, koordinat, alasan, kontak, lokasi, dll). 
1. Dengan demikian, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan dalam “ResultSignPKCS7.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan ditandatangani, file kunci PKCS7, dan file gambar tampilan tanda tangan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fungsi. 
1. Tandatangani file PDF dengan tanda tangan digital. Parameter yang terkait dengan tanda tangan (seperti file kunci, kata sandi, koordinat, alasan, kontak, lokasi, dll). 
1. Dengan demikian, jika ‘json.errorCode’ bernilai 0, hasil operasi disimpan dalam “ResultSignPKCS7.pdf”. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```