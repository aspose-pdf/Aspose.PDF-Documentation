---
title: Tambahkan Stempel Gambar dalam PDF menggunakan JavaScript via C++ 
linktitle: Stempel gambar dalam File PDF
type: docs
weight: 60
url: /javascript-cpp/stamping/
description: Tambahkan Stempel Gambar ke dokumen PDF Anda menggunakan fungsi AsposePdfAddStamp dengan toolkit JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Gambar dalam File PDF

Menyegel dokumen PDF mirip dengan menyegel dokumen kertas. Stempel dalam file PDF memberikan informasi tambahan pada file PDF, seperti melindungi file PDF agar tidak digunakan oleh orang lain dan mengonfirmasi keamanan konten file PDF.
Anda dapat menggunakan fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) untuk menambahkan stempel gambar ke file PDF menggunakan JavaScript.

Untuk menambahkan stempel gambar:

1. Atur nama file gambar default.
1. Buat 'FileReader'.
1. Atur nama file gambar.
1. Siapkan file stempel dari BLOB.

Cuplikan kode berikut menunjukkan cara menambahkan stempel gambar dalam file PDF.

```js

  /*atur nama file stempel default*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*atur nama file stempel*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*siapkan(simpan) file stempel dari BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. Buat 'FileReader'.
1. Fungsi [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) dijalankan.
1. Tambahkan file gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda akan diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, oleh karena itu, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*masukkan file stempel ke file PDF dan simpan sebagai "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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
            'gambar disiapkan!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Setel nama file stempel default: 'Aspose.jpg' sudah dimuat, lihat pengaturan di 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Penangan acara*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*Tambahkan stempel ke file PDF dan simpan sebagai "ResultStamp.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*Setel nama file stempel*/
      fileStamp = e.target.files[0].name;
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