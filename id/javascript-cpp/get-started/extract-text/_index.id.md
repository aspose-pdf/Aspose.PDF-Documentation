---
title: Ekstrak Teks dari PDF menggunakan JavaScript
linktitle: Ekstrak Teks dari PDF
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: Bagian ini menjelaskan cara mengekstrak teks dari dokumen PDF menggunakan toolkit JavaScript.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari PDF tidaklah mudah. Tidak banyak pembaca PDF yang dapat mengekstrak teks dari gambar PDF atau PDF yang dipindai. Namun, alat **Aspose.PDF for JavaScript via C++** memungkinkan Anda dengan mudah mengekstrak teks dari semua file PDF.

Periksa cuplikan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:

1. Pilih file PDF untuk mengekstrak teks.
1. Buat 'FileReader' untuk membaca teks.
1. Fungsi [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) dijalankan.

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka 'json.extractText' akan berisi konten yang diekstrak. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, file Anda akan memiliki kesalahan, maka informasi tentang kesalahan tersebut akan terkandung dalam 'json.errorText'.
1. Sebagai hasilnya, Anda akan menerima string dengan teks yang diekstrak dari PDF Anda.

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

    /*Penangani peristiwa*/
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