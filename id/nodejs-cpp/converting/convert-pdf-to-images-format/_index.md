---
title: Convert PDF ke Format Gambar di Node.js
linktitle: Convert PDF ke Gambar
type: docs
weight: 70
url: id/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, JPEG, PNG, SVG dengan beberapa baris kode di lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convert PDF ke Gambar

Dalam artikel ini, kami akan menunjukkan kepada Anda opsi untuk mengonversi PDF ke format gambar.

Dokumen yang sebelumnya dipindai sering disimpan dalam format file PDF. Namun, apakah Anda perlu mengeditnya di editor grafis atau mengirimkannya lebih lanjut dalam format gambar? Kami memiliki alat universal untuk Anda untuk mengonversi PDF ke gambar menggunakan 
Tugas yang paling umum adalah ketika Anda perlu menyimpan seluruh dokumen PDF atau beberapa halaman spesifik dari dokumen sebagai serangkaian gambar.
 **Aspose untuk Node.js via C++** memungkinkan Anda mengkonversi PDF ke format JPG dan PNG untuk menyederhanakan langkah-langkah yang diperlukan untuk mendapatkan gambar Anda dari file PDF tertentu.

**Aspose.PDF untuk Node.js via C++** mendukung berbagai konversi format gambar dari PDF. Silakan periksa bagian [Format File yang Didukung Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Coba konversi PDF ke JPEG secara online**

Aspose.PDF untuk Node.js menghadirkan aplikasi gratis online ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF konversi PDF ke JPEG dengan Aplikasi Gratis](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Konversi PDF ke JPEG

Jika Anda ingin mengkonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).

Silakan periksa cuplikan kode berikut untuk melakukan konversi di lingkungan Node.js.
**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToJpg{0:D2}.jpg". Dimana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversikan file PDF ke JPG dengan template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToJpg{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, muncul kesalahan di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke JPG dengan template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Coba konversi PDF ke TIFF secara online**

Aspose.PDF untuk Node.js menyajikan aplikasi gratis online ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF conversion PDF to TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF ke TIFF

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/). Silakan periksa cuplikan kode berikut untuk mengonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama file PDF yang akan dikonversi.
3. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToTiff{0:D2}.tiff". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Mengonversi file PDF ke TIFF dengan template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToTiff{0:D2}.tiff". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar-gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke TIFF dengan template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk Node.js mempersembahkan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF ke PNG

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
Silakan periksa cuplikan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
2. Tentukan nama file PDF yang akan dikonversi.
3. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.

1. Panggil fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToPng{0:D2}.png". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan ada di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke PNG dengan template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToPng{0:D2}.png". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke PNG dengan template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Coba ubah PDF menjadi SVG secara online**

Aspose.PDF untuk Node.js menghadirkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

## Konversi PDF ke SVG

### Mengubah PDF ke SVG klasik

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/). 
Silakan periksa cuplikan kode berikut untuk mengonversi di lingkungan Node.js.


**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPdfToSvg.svg". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke SVG dan simpan sebagai "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan diubah
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToSvg.svg". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Mengonversi file PDF ke SVG dan simpan sebagai "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Mengonversi PDF ke SVG yang di-zip

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
 
Silakan periksa potongan kode berikut untuk dikonversi di lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToSvgZip.zip". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke SVG(zip) dan simpan sebagai "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Konversi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToSvgZip.zip". Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*konversi file PDF ke SVG zip dan simpan "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Mengonversi PDF ke DICOM

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
 
Silakan periksa potongan kode berikut untuk dikonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Konversi file PDF. Dengan demikian, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToDICOM{0:D2}.dcm". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke DICOM dengan template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToDICOM{0:D2}.dcm". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, kesalahan muncul di file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke DICOM dengan template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## Konversi PDF ke BMP

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/). Silakan periksa potongan kode berikut untuk mengonversi dalam lingkungan Node.js.

**CommonJS:**

1. Panggil `require` dan impor modul `asposepdfnodejs` sebagai variabel `AsposePdf`.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggil `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).

1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToBmp{0:D2}.bmp". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, muncul kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Konversi file PDF ke BMP dengan template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor modul `asposepdfnodejs`.
1. Tentukan nama file PDF yang akan dikonversi.

1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToBmp{0:D2}.bmp". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Konversi file PDF ke BMP dengan template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format nomor halaman), resolusi 150 DPI dan simpan*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```