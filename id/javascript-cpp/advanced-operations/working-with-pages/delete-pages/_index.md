---
title: Hapus Halaman PDF dengan JavaScript melalui C++ 
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: /id/javascript-cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan Aspose.PDF untuk JavaScript melalui C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF untuk JavaScript melalui C++. Anda dapat mendapatkan hasilnya langsung di browser Anda.

1. Buat 'FileReader'.
1. Tentukan nomor halaman yang akan dihapus.
1. Fungsi [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) dieksekusi.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultDeletePages.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.

1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan sebuah tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*string, termasuk nomor halaman dengan interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*array, array dari nomor halaman*/
      /*const numPages = [1,3];*/
      /*number, nomor halaman*/
      /*const numPages = 1;*/
      /*menghapus halaman 1-3 dari file PDF dan menyimpan "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
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
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*string, termasuk nomor halaman dengan interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*array, array dari nomor halaman*/
        /*const numPages = [1,3];*/
        /*nomor, nomor halaman*/
        /*const numPages = 1;*/
        /*Hapus halaman dari file PDF dan simpan sebagai "ResultDeletePages.pdf - Minta Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
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