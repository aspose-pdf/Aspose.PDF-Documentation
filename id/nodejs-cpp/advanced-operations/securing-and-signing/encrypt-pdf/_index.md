---
title:  Enkripsi PDF di Node.js
linktitle: Enkripsi File PDF
type: docs
weight: 50
url: /id/nodejs-cpp/encrypt-pdf/
description: Enkripsi File PDF dengan Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Enkripsi File PDF menggunakan menggunakan Kata Sandi Pengguna atau Pemilik

Jika Anda mengirim email kepada seseorang dengan lampiran PDF yang berisi informasi rahasia, Anda mungkin ingin menambahkan beberapa keamanan terlebih dahulu agar tidak jatuh ke tangan yang salah. Cara terbaik untuk membatasi akses tidak sah ke dokumen PDF adalah melindunginya dengan kata sandi. Untuk mengenkripsi dokumen dengan mudah dan aman, Anda dapat menggunakan Aspose.PDF for Node.js via C++.

>Silakan tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

- Password **User password**, jika diatur, adalah apa yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna memasukkan password pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- Password **Owner password**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, memberi komentar, dll. Acrobat/Reader akan melarang hal‑hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan password ini jika Anda ingin mengatur/mengubah izin.

Jika Anda ingin mengenkripsi file PDF, Anda dapat menggunakan [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fungsi. 
Jika Anda ingin mengenkripsi file PDF, coba potongan kode berikut:

**CommonJS:**

1. Panggil `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dienkripsi.
1. Panggil `AsposePdf` sebagai Promise dan melakukan operasi untuk mengenkripsi file. Terima objek jika berhasil.
1. Panggil [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fungsi. 
1. Enkripsi file PDF dengan kata sandi “user” dan “owner”.
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultEncrypt.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error dalam file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Ada yang berbeda [izin enkripsi](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Modul.Izin.EkstrakKonten
- Modul.Izin.UbahTeksAnotasi
- Modul.Izin.IsiFormulir
- Modul.Izin.EkstrakKontenDenganDisabilitas
- Modul.Izin.SusunDokumen
- Modul.Izin.KualitasCetak

Ada berbagai [algoritma enkripsi](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan mengubah enkripsi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fungsi. 
1. Dekripsi file PDF dengan password "user" dan "owner".
1. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultEncrypt.pdf". Jika parameter json.errorCode bukan 0 dan, akibatnya, muncul error dalam file Anda, informasi error akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```