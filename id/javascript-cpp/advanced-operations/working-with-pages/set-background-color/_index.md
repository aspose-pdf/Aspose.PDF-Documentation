---
title: Mengatur warna latar belakang untuk PDF dengan JavaScript melalui C++
linktitle: Mengatur warna latar belakang
type: docs
weight: 80
url: /id/javascript-cpp/set-background-color/
description: Mengatur warna latar belakang untuk file PDF Anda dengan JavaScript melalui C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cuplikan kode berikut menunjukkan cara mengatur warna latar belakang halaman PDF menggunakan fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) dengan JavaScript.

Dalam contoh berikut, kita memilih file PDF untuk ditangani.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) dieksekusi (format heksadesimal “#RRGGBB”, di mana RR-merah, GG-hijau dan BB-biru bilangan bulat heksadesimal).
1. Atur warna latar belakang untuk file PDF dan simpan sebagai "ResultPdfSetBackgroundColor.pdf"

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffilePdfSetBackgroundColor = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Setel warna latar belakang untuk file PDF dan simpan sebagai "ResultPdfSetBackgroundColor.pdf"*/
        const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
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
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*Atur warna latar belakang untuk file PDF dan simpan "ResultPdfSetBackgroundColor.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
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