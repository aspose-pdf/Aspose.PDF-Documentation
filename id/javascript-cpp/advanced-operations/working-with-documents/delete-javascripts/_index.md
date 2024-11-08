---
title: Hapus kode JavaScript dari file PDF
linktitle: Hapus JavaScripts
type: docs
weight: 50
url: /id/javascript-cpp/delete-javascripts/
description: Hapus makro JavaScript dari file PDF langsung di Web dengan Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Menghapus JavaScript dalam file PDF mungkin diperlukan untuk alasan keamanan dan privasi. JavaScript dalam file PDF terkadang dapat digunakan secara jahat atau untuk fungsi yang tidak diinginkan. Anda dapat mendapatkan hasilnya langsung di browser Anda.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/) dijalankan.
1. Nama file hasil diatur, dalam contoh ini "ResultPdfDeleteJavaScripts.pdf".

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Hapus JavaScript dari file PDF dan simpan sebagai "ResultPdfDeleteJavaScripts.pdf"*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
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
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Hapus JavaScripts dari file PDF dan simpan "ResultPdfDeleteJavaScripts.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
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