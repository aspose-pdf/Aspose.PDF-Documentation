---
title: Dekripsi PDF menggunakan JavaScript
linktitle: Dekripsi File PDF
type: docs
weight: 40
url: /javascript-cpp/decrypt-pdf/
description: Dekripsi File PDF dengan Aspose.PDF untuk JavaScript melalui C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Baru-baru ini, semakin banyak pengguna bertukar dokumen terenkripsi agar tidak menjadi korban penipuan Internet dan melindungi dokumen mereka. Dalam hal ini, menjadi perlu untuk mengakses file PDF terenkripsi, karena akses semacam itu hanya dapat diperoleh oleh pengguna yang berwenang. Juga, orang mencari berbagai solusi untuk mendekripsi file PDF.

Lebih baik menyelesaikan masalah ini sekali dengan menggunakan Aspose.PDF untuk JavaScript melalui C++ langsung di browser web Anda. Cuplikan kode berikut menunjukkan cara mendekripsi file PDF.

1. Pilih file PDF untuk didekripsi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) dijalankan.

1. Nama file hasil diatur, dalam contoh ini "ResultDecrypt.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Akibatnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Mendekripsi file PDF dengan kata sandi "owner" dan simpan sebagai "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
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

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*Dekripsi file PDF dengan kata sandi "owner" dan simpan sebagai "ResultDecrypt.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
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