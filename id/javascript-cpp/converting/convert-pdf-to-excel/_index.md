---
title: Mengonversi PDF ke Excel dalam JavaScript
linktitle: Mengonversi PDF ke Excel
type: docs
weight: 20
url: id/javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: mengonversi PDF ke Excel menggunakan javascript, mengonversi PDF ke XLSX, mengonversi PDF ke CSV.
description: Aspose.PDF untuk JavaScript memungkinkan Anda mengonversi PDF ke XLSX, dan format CSV.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Membuat spreadsheet dari PDF menggunakan JavaScript

**Aspose.PDF untuk JavaScript** mendukung fitur konversi file PDF ke format Excel, dan CSV.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke Excel secara online**

Aspose.PDF untuk JavaScript menyajikan aplikasi gratis online ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Operasi konversi tergantung pada jumlah halaman dalam dokumen dan bisa memakan waktu yang sangat lama.
 Oleh karena itu, kami sangat merekomendasikan menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang memakan sumber daya ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file yang telah dikonversi.

## Konversi PDF ke XLSX

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*konversi sebuah file PDF ke XlsX dan simpan sebagai "ResultPDFtoXlsX.xlsx" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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

Berikut adalah contoh kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file XlsX:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) dijalankan.
1. Nama dari file hasil ditetapkan, dalam contoh ini "ResultPDFtoXlsX.xlsx".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka file hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, oleh karena itu, akan ada kesalahan pada file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*mengonversi file PDF ke XlsX dan menyimpan "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*membuat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## Mengonversi PDF ke CSV

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah File(tabel): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Handler acara*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke CSV (ekstrak tabel) dengan template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), TAB sebagai pembatas dan simpan - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF into CSV:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) dieksekusi.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfTablesToCSV{0:D2}.csv".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan di file Anda, maka informasi tentang kesalahan tersebut akan ada dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Mengonversi file PDF menjadi CSV (ekstrak tabel) dengan template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), TAB sebagai pemisah*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Jumlah file(tabel): " + json.filesCount.toString();
          /*Buat tautan ke file hasil*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```