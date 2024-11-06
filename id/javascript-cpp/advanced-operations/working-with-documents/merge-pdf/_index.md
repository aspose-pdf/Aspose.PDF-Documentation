---
title: Cara Menggabungkan PDF menggunakan JavaScript melalui C++
linktitle: Menggabungkan file PDF
type: docs
weight: 20
url: id/javascript-cpp/merge-pdf/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Aspose.PDF untuk JavaScript melalui C++
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menggabungkan atau mengkombinasikan dua PDF menjadi satu PDF dalam JavaScript

Menggabungkan dan mengkombinasikan file adalah tugas yang sangat populer saat bekerja dengan sejumlah besar dokumen. Terkadang, saat bekerja dengan dokumen dan gambar, ketika mereka dipindai, diproses, dan diatur, beberapa file dibuat. Tetapi bagaimana jika Anda perlu menyimpan semuanya dalam satu file? Atau apakah Anda tidak ingin mencetak beberapa dokumen? Gabungkan dua file PDF dengan Aspose.PDF untuk JavaScript melalui C++.

Alat JavaScript ini memungkinkan untuk menggabungkan dua file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk JavaScript melalui C++. Contoh ini ditulis dalam JavaScript.

1. Pilih file PDF untuk digabungkan.
1. Buat sebuah 'FileReader'.

1. Fungsi [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) dieksekusi.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultMerge.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, karenanya, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*hanya dua file*/
      if (index >= e.target.files.length || index >= 2) {
        /*gabungkan dua file PDF dan simpan sebagai "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*siapkan(simpan) file dari BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Menggunakan Web Workers

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Hasil:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'tunggu sebentar...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara. Hanya dua file yang digabungkan. Jika hanya satu file yang dipilih, maka gunakan file tersebut. Untuk file kedua Anda perlu melakukan AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Tanyakan Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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