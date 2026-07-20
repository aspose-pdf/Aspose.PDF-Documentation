---
title: Ubah Kata Sandi File PDF di Node.js
linktitle: Ubah Kata Sandi
type: docs
weight: 50
url: /id/nodejs-cpp/change-password-pdf/
description: Ubah Kata Sandi File PDF dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ubah Kata Sandi File PDF

Jika Anda ingin mengubah kata sandi PDF, Anda dapat menggunakan [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) fungsi. Ini mengubah password pengguna dan password pemilik dengan password pemilik, sambil mempertahankan pengaturan keamanan asli.
Jika Anda ingin mengubah password file PDF dari “owner” menjadi “newowner” atau “newuser”, coba potongan kode berikut:

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan mengubah password.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengubah kata sandi. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Ubah Kata Sandi. Kata sandi pemilik yang ada disetel ke "owner," dan diubah menjadi "newowner" dengan kata sandi pengguna baru "newuser".
1. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfChangePassword.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Harap dicatat bahwa jika kata sandi berupa string kosong:

1. Jika kata sandi pengguna kosong - PDF akan terbuka tanpa meminta kata sandi (tetapi tetap terenkripsi).
1. Jika kata sandi pemilik kosong, PDF akan terbuka dengan permintaan kata sandi pengguna.
1. Jika keduanya kosong  - PDF terbuka tanpa meminta kata sandi (tetapi tetap terenkripsi).


**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan mengubah password.
1. Inisialisasi modul AsposePdf. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Ubah Kata Sandi. Kata sandi pemilik yang ada disetel ke "owner," dan diubah menjadi "newowner" dengan kata sandi pengguna baru "newuser".
1. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfChangePassword.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```