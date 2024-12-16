---
title: Tambahkan Header dan Footer ke PDF melalui JavaScript via C++ 
linktitle: Tambahkan Header dan Footer ke PDF
type: docs
weight: 70
url: /id/javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk JavaScript via C++ memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan AsposePdfAddTextHeaderFooter.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF untuk JavaScript via C++** memungkinkan Anda menambahkan header dan footer dalam file PDF yang sudah ada.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/) dieksekusi.
1. Nama file yang dihasilkan ditetapkan, dalam contoh ini "ResultAddHeader.pdf".

1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.  
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan sebuah tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

Potongan kode berikut menunjukkan kepada Anda bagaimana menambahkan teks di header file PDF dengan JavaScript.

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*menambahkan header halaman ke file PDF dan menyimpan "ResultAddHeader.pdf"*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*buat tautan untuk mengunduh file hasil*/
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

    /*Pengendali acara*/
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF untuk JavaScript via C++';
        const footer = 'ASPOSE';
        /*Tambahkan teks di Header/Footer dari file PDF dan simpan sebagai "ResultAddHeaderFooter.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddTextHeaderFooter',
            "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] },
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