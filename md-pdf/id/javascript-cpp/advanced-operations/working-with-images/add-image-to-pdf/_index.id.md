---
title: Tambahkan Gambar ke PDF menggunakan JavaScript via C++
linktitle: Tambahkan Gambar
type: docs
weight: 10
url: /javascript-cpp/add-image-to-pdf/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan Aspose.PDF untuk JavaScript via C++.
lastmod: "2023-12-15"
---

## Tambahkan Gambar di File PDF yang Ada

Apakah Anda perlu melampirkan gambar ke PDF? Ingin meningkatkan keterbacaan PDF Anda? Tambahkan gambar ke PDF Anda dan presentasi atau resume Anda akan terlihat lebih menarik.

Umumnya diyakini bahwa menambahkan gambar ke file PDF memerlukan alat khusus yang kompleks. Namun, dengan Aspose.PDF untuk JavaScript Anda dapat dengan cepat dan mudah menambahkan gambar yang Anda butuhkan ke PDF menggunakan JavaScript langsung di browser Anda.

Untuk menambahkan gambar ke file PDF yang ada:

1. Atur nama file gambar default.
1. Buat 'FileReader'.
1. Atur nama file gambar.
1. Siapkan file gambar dari BLOB.
1. Fungsi [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) dieksekusi.

1. Tambahkan file gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file yang dihasilkan ke sistem operasi pengguna.

Cuplikan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```js

  /*atur nama file gambar default*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*atur nama file gambar*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*siapkan(simpan) file gambar dari BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

Dalam contoh berikut, kami memilih gambar untuk ditangani:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*tambahkan file gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'gambar disiapkan!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Setel nama file gambar default: 'Aspose.jpg' sudah dimuat, lihat pengaturan di 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Penangan acara*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Tambahkan gambar ke akhir file PDF dan simpan sebagai "ResultImage.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Setel nama file gambar*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Simpan BLOB di Memori FS untuk pemrosesan*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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