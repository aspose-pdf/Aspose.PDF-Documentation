---
title: Mengonversi PDF ke Dokumen Word dalam JavaScript
linktitle: Mengonversi PDF ke Word
type: docs
weight: 10
url: /id/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Pelajari cara menulis kode JavaScript untuk konversi PDF ke DOC(DOCX) langsung di Web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Operasi konversi tergantung pada jumlah halaman dalam dokumen dan dapat memakan waktu yang sangat lama. Oleh karena itu, kami sangat menyarankan untuk menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang memakan banyak sumber daya ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file yang telah dikonversi.

Untuk mengedit konten file PDF di Microsoft Word atau pengolah kata lainnya yang mendukung format DOC dan DOCX. File PDF dapat diedit, tetapi file DOC dan DOCX lebih fleksibel dan dapat disesuaikan.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke DOC secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi gratis online ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi PDF ke DOC](/pdf/id/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOC

```js

  /*Buat Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'dimuat!' :
      (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

  /*Penangan peristiwa*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Konversi file PDF ke Doc dan simpan sebagai "ResultPDFtoDoc.doc" - Minta ke Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file DOC:

1. Pilih file PDF untuk diubah.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) dijalankan.
1. Nama dari file hasil ditetapkan, dalam contoh ini "ResultPDFtoDoc.doc".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka file hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan di file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Mengonversi file PDF ke Doc dan menyimpan "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Membuat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**Coba ubah PDF ke DOCX secara online**

Aspose.PDF untuk JavaScript menyajikan aplikasi online gratis ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aplikasi Gratis Aspose.PDF Konversi PDF ke Word](/pdf/id/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Ubah PDF ke DOCX

Aspose.PDF untuk JavaScript API memungkinkan Anda membaca dan mengkonversi dokumen PDF ke DOCX. DOCX adalah format terkenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi lateral tetapi tidak dengan versi MS Word sebelumnya yang mendukung ekstensi file DOC.

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Penangan kejadian*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*mengkonversi file PDF ke DocX dan menyimpan "ResultPDFtoDocX.docx" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Cuplikan kode]

    /*buat tautan untuk mengunduh file hasil*/
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


The following JavaScript code snippet shows simple example of coverting PDF pages into DOCX files:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPDFtoDocX.docx".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*konversi file PDF ke DocX dan simpan sebagai "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*buat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```