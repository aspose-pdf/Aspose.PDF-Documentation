---
title: Hapus Gambar dari File PDF melalui JavaScript
linktitle: Hapus Gambar
type: docs
weight: 20
url: id/javascript-cpp/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus gambar dari file PDF menggunakan Aspose.PDF untuk JavaScript.
lastmod: "2022-02-17"
---

Anda dapat menghapus gambar dari file PDF menggunakan Aspose.PDF untuk JavaScript melalui C++. Anda dapat mendapatkan hasilnya langsung di browser Anda.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfDeleteImages.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan di file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.

1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan sebuah tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Hapus gambar dari file PDF dan simpan sebagai "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Penanganan event*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Hapus gambar dari file PDF dan simpan sebagai "ResultPdfDeleteImages.pdf" - Tanyakan ke Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
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