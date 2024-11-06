---
title: Enkripsi PDF di Node.js
linktitle: Enkripsi Berkas PDF
type: docs
weight: 50
url: id/nodejs-cpp/encrypt-pdf/
description: Enkripsi Berkas PDF dengan Aspose.PDF untuk Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Enkripsi Berkas PDF menggunakan Kata Sandi Pengguna atau Pemilik

Jika Anda mengirim email kepada seseorang dengan lampiran PDF yang berisi informasi rahasia, Anda mungkin ingin menambahkan beberapa keamanan terlebih dahulu agar tidak jatuh ke tangan yang salah. Cara terbaik untuk membatasi akses tidak sah ke dokumen PDF adalah dengan melindunginya dengan kata sandi. Untuk mengenkripsi dokumen dengan mudah dan aman, Anda dapat menggunakan Aspose.PDF untuk Node.js via C++.

>Harap tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi berkas PDF.

- **Kata sandi Pengguna**, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi Pemilik**, jika diatur, mengontrol izin, seperti pencetakan, pengeditan, ekstraksi, pemberian komentar, dll.
 Acrobat/Reader akan menolak hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

Jika Anda ingin mengenkripsi file PDF, Anda dapat menggunakan fungsi [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). Jika Anda ingin mengenkripsi file PDF coba cuplikan kode berikut:

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dienkripsi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengenkripsi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Enkripsi file PDF dengan kata sandi "user" dan "owner".
1. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultEncrypt.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Enkripsi file PDF dengan kata sandi "user" dan "owner", dan simpan sebagai "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Ada berbagai [izin enkripsi](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Ada berbagai [algoritma enkripsi](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan diubah enkripsinya.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Dekripsi file PDF dengan kata sandi "user" dan "owner".

1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultEncrypt.pdf". Jika parameter json.errorCode tidak 0 dan, sesuai, terdapat kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Enkripsi file PDF dengan kata sandi "user" dan "owner", dan simpan sebagai "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```