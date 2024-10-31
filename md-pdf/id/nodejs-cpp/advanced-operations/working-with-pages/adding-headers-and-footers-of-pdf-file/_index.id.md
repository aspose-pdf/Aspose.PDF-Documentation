---
title: Tambahkan Header dan Footer ke PDF di Node.js
linktitle: Tambahkan Header dan Footer ke PDF
type: docs
weight: 70
url: /nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk Node.js melalui C++ memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF untuk Node.js melalui C++** memungkinkan Anda menambahkan header dan footer dalam file PDF yang sudah ada.

Jika Anda ingin menambahkan header dan footer, Anda dapat menggunakan fungsi [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

Silakan periksa cuplikan kode berikut untuk menambahkan header dan footer ke file PDF dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan ditambahkan header dan footer.

1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk menambahkan header dan footer. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Tambahkan teks di Header dan Footer dari file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultAddHeaderFooter.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Tambahkan teks di Header/Footer dari file PDF dan simpan sebagai "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF untuk Node.js melalui C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF di mana header dan footer akan ditambahkan.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Tambahkan teks di Header dan Footer dari file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil dari operasi disimpan dalam "ResultAddHeaderFooter.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Tambahkan teks di Header/Footer dari file PDF dan simpan sebagai "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```