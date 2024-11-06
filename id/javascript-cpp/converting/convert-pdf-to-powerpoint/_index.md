---
title: Mengubah PDF ke PPTX di JavaScript
linktitle: Mengubah PDF ke PowerPoint
type: docs
weight: 30
url: id/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF memungkinkan Anda untuk mengubah format PDF ke PPTX menggunakan JavaScript langsung di web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Operasi konversi bergantung pada jumlah halaman dalam dokumen dan dapat memakan waktu lama. Oleh karena itu, kami sangat menyarankan menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang membutuhkan sumber daya besar ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file yang telah dikonversi.

{{% alert color="success" %}}
**Coba mengubah PDF ke PowerPoint secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi online gratis ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas cara kerjanya.


[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Ubah PDF ke PPTX

```js

  /*Buat Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'termuat!' :
      (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

  /*Penanganan acara*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Mengonversi file PDF ke PptX dan menyimpan "ResultPDFtoPptX.pptx" - Minta Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF to PPTX files:

1. Pilih file PDF untuk konversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPDFtoPptX.pptx".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Konversi file PDF ke PptX dan simpan sebagai "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Buat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```