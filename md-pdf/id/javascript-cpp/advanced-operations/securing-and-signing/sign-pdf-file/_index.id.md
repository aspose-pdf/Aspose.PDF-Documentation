---
title: Tambahkan tanda tangan digital atau tandatangani PDF secara digital dalam JavaScript melalui C++
linktitle: Tandatangani PDF secara digital
type: docs
weight: 70
url: /javascript-cpp/sign-pdf/
description: Tandatangani dokumen PDF secara digital menggunakan JavaScript melalui C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tanda tangan digital dalam dokumen PDF adalah cara untuk memverifikasi keaslian dan integritas dokumen. Ini adalah proses tanda tangan elektronik dari dokumen PDF menggunakan kunci pribadi dan sertifikat digital. Tanda tangan ini menjamin pemegang bahwa dokumen tidak diubah atau dimodifikasi sejak penandatanganan dan bahwa penanda tangan adalah pihak yang menyetujuinya. Untuk menandatangani PDF dengan JavaScript, gunakan alat Aspose.PDF.

Aspose.PDF untuk JavaScript melalui C++ mendukung fitur untuk menandatangani file PDF secara digital menggunakan [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Tandatangani PDF dengan tanda tangan digital

```js

    /*Atur nama file kunci PKCS7 default*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*Atur nama file kunci PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Simpan BLOB di Memori FS untuk pemrosesan*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Atur nama file gambar (Tampilan Tanda Tangan) default*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*Atur nama file gambar*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Simpan BLOB di Memori FS untuk pemrosesan*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*Tandatangani file PDF dengan tanda tangan digital dan simpan sebagai "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
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
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'file disiapkan!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Atur nama file kunci PKCS7 default*/
    var fileSign = "test.pfx";
    /*Atur nama file gambar (Penampilan Tanda Tangan) default: 'Aspose.jpg' sudah dimuat, lihat pengaturan di 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*Penangan acara*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'Alasan';
        const contact = 'contact@test.com';
        const location = 'Lokasi';
        const isVisible = 1;
        /*Tandatangani file PDF dengan tanda tangan digital dan simpan sebagai "ResultSignPKCS7.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*Atur nama file kunci PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*Simpan BLOB di Memori FS untuk pemrosesan*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Atur nama file gambar*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*Simpan BLOB di Memori FS untuk pemrosesan*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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