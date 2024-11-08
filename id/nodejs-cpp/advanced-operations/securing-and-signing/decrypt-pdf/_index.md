---
title: Dekripsi PDF di Node.js
linktitle: Dekripsi File PDF
type: docs
weight: 40
url: /id/nodejs-cpp/decrypt-pdf/
description: Dekripsi File PDF dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Baru-baru ini, semakin banyak pengguna bertukar dokumen terenkripsi untuk menghindari menjadi korban penipuan Internet dan melindungi dokumen mereka. Dalam hal ini, menjadi perlu untuk mengakses file PDF terenkripsi, karena akses semacam itu hanya dapat diperoleh oleh pengguna yang berwenang. Selain itu, orang mencari berbagai solusi untuk mendekripsi file PDF.

Jika Anda ingin mendekripsi file PDF, Anda dapat menggunakan fungsi [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/). Jika Anda ingin mendekripsi file PDF, coba potongan kode berikut:

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan diubah menjadi terdekripsi.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mendekripsi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Dekripsi file PDF dengan kata sandi adalah "owner".
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultDecrypt.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Dekripsi file PDF dengan kata sandi adalah "owner" dan simpan sebagai "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan diubah menjadi didekripsi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Dekripsi file PDF dengan kata sandi "owner".
1. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultDecrypt.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan ada dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Dekripsi file PDF dengan kata sandi "owner" dan simpan sebagai "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```