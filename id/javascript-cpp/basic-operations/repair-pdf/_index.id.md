---
title: Memperbaiki PDF dengan JavaScript melalui C++
linktitle: Memperbaiki PDF
type: docs
weight: 10
url: /javascript-cpp/repair-pdf/
description: Topik ini menjelaskan cara Memperbaiki PDF melalui JavaScript melalui C++
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF untuk JavaScript memungkinkan perbaikan PDF berkualitas tinggi. File PDF mungkin tidak terbuka karena alasan apa pun, terlepas dari program atau browsernya. Dalam beberapa kasus, dokumen dapat dipulihkan, coba kode berikut dan lihat sendiri.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfRepair.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda dapat memperoleh tautan ke file hasil. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.

1. Akibatnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Memperbaiki file PDF dan menyimpan "ResultPdfRepair.pdf"*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Membuat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Menggunakan Web Workers

```js

    /*Membuat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Memperbaiki file PDF dan menyimpan "ResultPdfRepair.pdf" - Tanya Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Cuplikan kode]

    /*Membuat tautan untuk mengunduh file hasil*/
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