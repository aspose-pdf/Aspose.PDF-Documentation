---
title: Ubah Kata Sandi dari File PDF
linktitle: Ubah Kata Sandi
type: docs
weight: 50
url: /javascript-cpp/change-password-pdf/
description: Ubah Kata Sandi dari File PDF dengan Aspose.PDF untuk JavaScript via C++.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ubah Kata Sandi dari File PDF

Jika Anda ingin mengubah kata sandi dari file PDF dari "owner" ke "newowner" coba cuplikan kode berikut:

1. Pilih file PDF.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/) dijalankan.
1. Nama file hasil diatur, dalam contoh ini "ResultPdfChangePassword.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, akibatnya, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.

1. Akibatnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Ubah kata sandi file PDF dari "owner" menjadi "newowner" dan simpan sebagai "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Menggunakan Web Workers

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*Kata sandi pemilik*/
        const newUserPassword = "newuser"; /*Kata sandi pengguna baru*/
        const newOwnerPassword = "newowner"; /*Kata sandi pemilik baru*/
        /*Ubah kata sandi file PDF dari "owner" menjadi "newowner" dan simpan sebagai "ResultPdfChangePassword.pdf" - Tanyakan ke Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Potongan kode]

    /*Buat tautan untuk mengunduh file hasil*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Klik di sini untuk mengunduh file " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```