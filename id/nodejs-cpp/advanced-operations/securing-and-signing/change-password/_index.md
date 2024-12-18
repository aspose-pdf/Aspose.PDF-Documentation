---
title: Ubah Kata Sandi dari File PDF di Node.js
linktitle: Ubah Kata Sandi
type: docs
weight: 50
url: /id/nodejs-cpp/change-password-pdf/
description: Ubah Kata Sandi dari File PDF dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ubah Kata Sandi dari File PDF

Jika Anda ingin mengubah kata sandi PDF, Anda dapat menggunakan fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). Fungsi ini mengubah kata sandi pengguna dan kata sandi pemilik dengan kata sandi pemilik, sambil mempertahankan pengaturan keamanan asli. Jika Anda ingin mengubah kata sandi file PDF dari "owner" menjadi "newowner" atau "newuser" coba cuplikan kode berikut:

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan diubah kata sandinya.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengubah kata sandi. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Ubah Kata Sandi. Kata sandi pemilik yang ada diatur ke "owner," dan diubah menjadi "newowner" dengan kata sandi pengguna baru "newuser".
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfChangePassword.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ubah kata sandi file PDF dari "owner" menjadi "newowner" dan simpan sebagai "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


Silakan perhatikan bahwa jika kata sandi adalah string kosong:

1. Jika kata sandi pengguna kosong - PDF terbuka tanpa meminta kata sandi (tetapi tetap terenkripsi).
1. Jika kata sandi pemilik kosong, PDF terbuka dengan permintaan kata sandi pengguna.
1. Jika keduanya kosong - PDF terbuka tanpa meminta kata sandi (tetapi tetap terenkripsi).

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan mengganti kata sandi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Ganti Kata Sandi. Kata sandi pemilik yang ada diatur ke "owner," dan diubah menjadi "newowner" dengan kata sandi pengguna baru "newuser".

1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfChangePassword.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Ubah kata sandi file PDF dari "owner" ke "newowner" dan simpan "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```