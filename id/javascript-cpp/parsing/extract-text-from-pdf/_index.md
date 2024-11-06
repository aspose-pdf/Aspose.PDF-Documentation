---
title: Ekstrak Teks dari PDF menggunakan JavaScript
linktitle: Ekstrak teks dari PDF
type: docs
weight: 30
url: id/javascript-cpp/extract-text-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF untuk JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah tugas yang sangat umum dan berguna. Mengekstrak teks dari PDF memiliki berbagai tujuan, mulai dari meningkatkan pencarian dan ketersediaan hingga memungkinkan analisis dan otomatisasi data di berbagai bidang seperti bisnis, penelitian, dan manajemen informasi.

Jika Anda ingin mengekstrak teks dari dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/). Silakan periksa potongan kode berikut untuk mengekstrak teks dari file PDF menggunakan JavaScript melalui C++.

1. Buat 'FileReader'.

1. Fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) dijalankan.
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda bisa mendapatkan tautan ke file hasil. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.

```js

    var ffileExtract = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Ekstrak teks dari file PDF*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
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
        (evt.data.json.errorCode == 0) ?
            evt.data.json.extractText :
            `Kesalahan: ${evt.data.json.errorText}`; 

    /*Event handler*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Ekstrak teks dari file PDF - Tanyakan Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```