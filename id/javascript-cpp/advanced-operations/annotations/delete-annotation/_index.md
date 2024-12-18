---
title: Hapus Anotasi menggunakan JavaScript
linktitle: Hapus Anotasi
type: docs
weight: 10
url: /id/javascript-cpp/delete-annotation/
description: Dengan Aspose.PDF untuk JavaScript Anda dapat menghapus anotasi dari file PDF Anda.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Anda dapat menghapus anotasi dari file PDF menggunakan Aspose.PDF untuk JavaScript melalui C++. Anda dapat mendapatkan hasilnya langsung di browser Anda.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/) dijalankan.
1. Nama dari file hasil ditetapkan, dalam contoh ini "ResultPdfDeleteAnnotations.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, oleh karena itu, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.

1. Akibatnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Hapus anotasi dari file PDF dan simpan sebagai "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
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
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Hapus anotasi dari file PDF dan simpan sebagai "ResultPdfDeleteAnnotations.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
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