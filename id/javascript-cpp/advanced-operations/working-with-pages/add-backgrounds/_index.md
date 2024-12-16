---
title: Tambahkan latar belakang ke PDF dengan JavaScript melalui C++
linktitle: Tambahkan latar belakang
type: docs
weight: 10
url: /id/javascript-cpp/add-backgrounds/
description: Tambahkan gambar latar belakang ke file PDF Anda dengan JavaScript melalui C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan fungsi [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) dengan JavaScript.

Dalam cuplikan kode berikutnya, kita mengunggah gambar untuk pekerjaan lebih lanjut dalam sistem file internal:

1. Buat 'FileReader'.
1. Tetapkan nama file gambar.
1. Siapkan file gambar dari BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*tetapkan nama file gambar*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*siapkan(simpan) file gambar dari BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


Dalam contoh berikut, kita memilih file PDF untuk ditangani.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) dijalankan.
1. Tambahkan file gambar ke dalam PDF dan simpan sebagai "ResultBackgroundImage.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*tambahkan file gambar latar ke dalam PDF dan simpan sebagai "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*buat tautan untuk mengunduh file hasil*/
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
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Hasil:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'gambar siap!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Tetapkan nama file gambar default: 'Aspose.jpg' sudah dimuat, lihat pengaturan di 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*Penangan acara*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Tambahkan gambar latar belakang ke file PDF dan simpan sebagai "ResultBackgroundImage.pdf" - Tanyakan ke Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Tetapkan nama file gambar*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Simpan BLOB di Memory FS untuk pemrosesan*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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