---
title: Dekripsi PDF di Node.js
linktitle: Dekripsi File PDF
type: docs
weight: 40
url: /id/nodejs-cpp/decrypt-pdf/
description: Dekripsi File PDF dengan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dekripsi File PDF menggunakan Owner Password

Baru-baru ini, semakin banyak pengguna bertukar dokumen terenkripsi untuk tidak menjadi korban penipuan Internet dan melindungi dokumen mereka.
Sehubungan dengan itu, menjadi diperlukan untuk mengakses file PDF yang terenkripsi, karena akses tersebut hanya dapat diperoleh oleh pengguna yang berwenang. Selain itu, orang‑orang mencari berbagai solusi untuk mendekripsi file PDF. 

Jika Anda ingin mendekripsi file PDF, Anda dapat menggunakan [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fungsi. 
Jika Anda ingin mendekripsi file PDF, coba potongan kode berikut:

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan mengubah yang didekripsi.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk mendekripsi file. Terima objek jika berhasil.
1. Panggil [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fungsi.
1. Dekripsi file PDF dengan kata sandi "owner".
1. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultDecrypt.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan mengubah yang didekripsi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fungsi.
1. Dekripsi file PDF dengan kata sandi "owner".
1. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultDecrypt.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```