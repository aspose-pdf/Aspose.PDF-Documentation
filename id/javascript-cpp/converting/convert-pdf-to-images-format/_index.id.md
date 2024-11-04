---
title: Konversi PDF ke Format Gambar dalam JavaScript
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, JPEG, PNG, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript Mengonversi PDF ke Gambar

Dalam artikel ini, kami akan menunjukkan pilihan untuk mengonversi PDF ke format gambar.

Dokumen yang dipindai sebelumnya sering disimpan dalam format file PDF. Namun, apakah Anda perlu mengeditnya di editor grafis atau mengirimkannya lebih lanjut dalam format gambar? Kami memiliki alat universal untuk Anda untuk mengonversi PDF ke gambar menggunakan
Tugas yang paling umum adalah ketika Anda perlu menyimpan seluruh dokumen PDF atau beberapa halaman tertentu dari dokumen sebagai satu set gambar. **Aspose untuk JavaScript melalui C++** memungkinkan Anda mengonversi PDF ke format JPG dan PNG untuk menyederhanakan langkah-langkah yang diperlukan untuk mendapatkan gambar Anda dari file PDF tertentu.

**Aspose.PDF untuk JavaScript melalui C++** mendukung berbagai konversi format PDF ke gambar.
 Silakan periksa bagian [Format File yang Didukung Aspose.PDF](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

Operasi konversi tergantung pada jumlah halaman dalam dokumen dan dapat memakan waktu yang sangat lama. Oleh karena itu, kami sangat merekomendasikan menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang membutuhkan banyak sumber daya ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file yang telah dikonversi.

{{% alert color="success" %}}
**Coba konversi PDF ke JPEG online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi gratis online ["PDF ke JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF conversion PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Konversi PDF ke JPEG

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah file(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Error: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*mengkonversi file PDF ke file jpg dengan template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
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

Berikut adalah potongan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file Jpeg:

1. Pilih file PDF untuk mengonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfToJpg{0:D2}.jpg".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*mengonversi file PDF ke file jpg dengan template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
        /*buat tautan ke file hasil*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Coba konversi PDF ke TIFF online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi online gratis ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF konversi PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF ke TIFF

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah berkas(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi berkas PDF ke TIFF dengan template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Buat tautan untuk mengunduh berkas hasil*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Klik di sini untuk mengunduh berkas " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into Tiff files:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) dijalankan.
1. Nama file hasil ditentukan, dalam contoh ini "ResultPdfToTiff{0:D2}.tiff".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda akan diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan pada file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Konversi file PDF ke TIFF dengan template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
          /*Buat tautan ke file hasil*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk JavaScript menyajikan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF ke PNG

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'termuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah berkas(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*konversi berkas PDF ke berkas-berkas png dengan template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Cuplikan kode]

    /*buat tautan untuk mengunduh berkas hasil*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Klik di sini untuk mengunduh berkas " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


Berikut adalah potongan kode JavaScript yang menunjukkan contoh sederhana untuk mengonversi halaman PDF menjadi file PNG:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) dijalankan.
1. Nama file hasil diatur, dalam contoh ini "ResultPdfToPng{0:D2}.png".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat di file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*mengonversi file PDF ke file png dengan template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
        /*buat tautan ke file hasil*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

## Konversi PDF ke SVG

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah file(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke SVG - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file SVG:

1. Pilih file PDF untuk diubah.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfToSvg.svg".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda akan diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Ubah file PDF menjadi SVG*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
          /*Buat tautan ke file hasil*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### Konversi PDF ke SVG yang di-zip

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke SVG(zip) dan simpan "ResultPdfToSvgZip.zip" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengkonversi halaman PDF menjadi file SVG(zip):

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) dijalankan.
1. Nama file yang dihasilkan ditetapkan, dalam contoh ini "ResultPdfToSvgZip.zip".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Konversi file PDF menjadi SVG(zip) dan simpan sebagai "ResultPdfToSvgZip.zip"*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Konversi PDF ke DICOM

```js

  /*Buat Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'termuat!' :
      (evt.data.json.errorCode == 0) ?
        `Jumlah file(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `Kesalahan: ${evt.data.json.errorText}`;

  /*Penanganan acara*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Konversi file PDF ke DICOM dengan template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan - Minta Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
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


Berikut adalah contoh kode JavaScript yang menunjukkan contoh sederhana mengonversi halaman PDF menjadi file DICOM:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfToDICOM{0:D2}.dcm".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan pada file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Mengonversi file PDF ke DICOM dengan template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
        /*Buat tautan ke file hasil*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Mengonversi PDF ke BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? 
          `Jumlah File(halaman): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Mengonversi file PDF ke BMP dengan templat "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan - Tanya Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Membuat tautan untuk mengunduh file hasil*/
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengkonversi halaman PDF menjadi file BMP:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultPdfToBmp{0:D2}.bmp".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file yang dihasilkan ke sistem operasi pengguna.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Konversi file PDF ke BMP dengan template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Jumlah file(halaman): " + json.filesCount.toString();
          /*Buat tautan ke file hasil*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```