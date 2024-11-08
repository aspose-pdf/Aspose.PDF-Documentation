---
title: Menghapus lampiran dari PDF dengan JavaScript
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 10
url: /id/javascript-cpp/menghapus-lampiran-dari-pdf-yang-ada/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan toolkit Web JavaScript untuk menghapus lampiran dalam file PDF menggunakan Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus lampiran dari file PDF menggunakan Aspose.PDF untuk JavaScript melalui C++. Anda dapat memperoleh hasilnya langsung di browser Anda.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfDeleteAttachments.pdf".

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Hapus lampiran dari file PDF dan simpan "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
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
        (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Hapus lampiran dari file PDF dan simpan sebagai "ResultPdfDeleteAttachments.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
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