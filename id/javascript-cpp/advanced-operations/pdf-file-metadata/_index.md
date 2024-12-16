---
title: Bekerja dengan Metadata File PDF menggunakan JavaScript via C++
linktitle: Metadata File PDF
type: docs
weight: 130
url: /id/javascript-cpp/pdf-file-metadata/
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan metadata dari file PDF, mengatur Informasi File PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Informasi File PDF

1. Buat 'FileReader'.
1. Fungsi [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) dijalankan.
1. Metadata PDF yang dapat diperoleh:
- title - judul
- creator - pembuat
- author - penulis
- subject - subjek
- keywords - kata kunci
- creation - tanggal pembuatan
- mod - tanggal modifikasi
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda dapat mendapatkan daftar Info file PDF. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Mendapatkan info (metadata) dari file PDF.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - judul
      creator - pembuat
      author - penulis
      subject - subjek
      keywords - kata kunci
      format - format PDF
      version - versi PDF
      ispdfa - PDF adalah PDF/A
      ispdfua - PDF adalah PDF/UA
      islinearized - PDF terlinear
      isencrypted - PDF terenkripsi
      permission - izin PDF
      size - ukuran halaman PDF
      pagecount - Jumlah halaman
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - Jumlah anotasi
      bookmarkcount - Jumlah penanda buku
      attachmentcount - Jumlah lampiran
      metadatacount - Jumlah metadata
      javascriptcount - Jumlah JavaScript
      imagecount - Jumlah gambar
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Menggunakan Web Workers

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `info:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `Kesalahan: ${evt.data.json.errorText}`; 

    /*Pengendali acara*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Dapatkan info (metadata) dari file PDF - Tanyakan ke Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Dapatkan Semua Font

Mendapatkan font dari file PDF bisa menjadi cara yang berguna untuk menggunakan kembali font dalam dokumen atau aplikasi lain.
 
Dalam hal Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada menggunakan JavaScript via C++.

1. Buat 'FileReader'.
1. Fungsi [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) dijalankan.
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda dapat mendapatkan daftar font dari file PDF. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*dapatkan daftar font dari file PDF.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
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
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ?
          `font:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `Kesalahan: ${evt.data.json.errorText}`; 

    /*Penangan acara*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Dapatkan daftar font file PDF - Tanyakan Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## Mengatur Informasi File PDF

Aspose.PDF untuk JavaScript melalui C++ memungkinkan Anda mengatur informasi khusus file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul.
 Untuk mengatur informasi ini:

1. Buat 'FileReader'.
1. Jika tidak perlu mengatur nilai, gunakan undefined atau "" (string kosong).
1. Fungsi [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) dieksekusi.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultSetInfo.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan sebuah tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Mengatur info PDF: judul, pembuat, penulis, subjek, kata kunci, pembuatan (tanggal), mod (tanggal modifikasi)*/
        /*Jika tidak perlu mengatur nilai, gunakan undefined atau "" (string kosong)*/
        /*Mengatur info (metadata) dalam file PDF dan menyimpan "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Mengatur Informasi Dokumen PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Membuat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Menggunakan Web Workers

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Info PDF: judul, pembuat, penulis, subjek, kata kunci, pembuatan (tanggal), mod (tanggal modifikasi)*/
        const title = 'Mengatur Informasi Dokumen PDF';
        const creator = ''; /*jika tidak perlu mengatur nilai, gunakan: undefined atau ""/'' (string kosong)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*tanggal pembuatan*/
        const mod = '16/02/2023 11:55 PM'; /*tanggal modifikasi*/
        /*Atur info (metadata) dalam file PDF dan simpan "ResultSetInfo.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
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


## Hapus Informasi File PDF

Aspose.PDF untuk JavaScript melalui C++ memungkinkan Anda untuk menghapus Metadata file PDF:

1. Buat 'FileReader'.
1. Fungsi [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfRemoveMetadata.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Hapus metadata dari file PDF dan simpan sebagai "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Menggunakan Web Workers

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Hapus metadata dari file PDF dan simpan sebagai "ResultPdfRemoveMetadata.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Cuplikan Kode]

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