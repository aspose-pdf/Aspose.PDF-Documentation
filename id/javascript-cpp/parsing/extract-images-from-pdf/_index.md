---
title: Ekstrak Gambar dari PDF JavaScript
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: id/javascript-cpp/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian dari gambar dari PDF menggunakan toolkit Aspose.PDF untuk JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Toolkit web dari Aspose.PDF memungkinkan Anda untuk dengan mudah mengekstrak gambar dari file PDF.

Jika Anda ingin mengekstrak gambar dari dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/). Silakan periksa cuplikan kode berikut untuk mengekstrak gambar dari file PDF menggunakan JavaScript melalui C++.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) dijalankan.
1. Nama file hasil ditentukan, dalam contoh ini "ResultPdfExtractImage{0:D2}.jpg".

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda dapat mendapatkan tautan ke file hasil. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Ekstrak gambar dari file PDF dengan templat "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Jumlah file(gambar): " + json.filesCount.toString();
        /*Buat tautan ke file hasil*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Menggunakan Web Workers

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah File(gambar): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Ekstrak gambar dari file PDF dengan template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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