---
title: Konversi PDF ke Format Gambar di Node.js
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /id/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, JPEG, PNG, SVG dengan beberapa baris kode di lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Mengonversi PDF ke Gambar

Dalam artikel ini, kami akan menunjukkan kepada Anda opsi untuk mengonversi PDF ke format gambar.

Dokumen yang dipindai sebelumnya sering disimpan dalam format file PDF. Namun, apakah Anda perlu mengeditnya di editor grafis atau mengirimnya lebih lanjut dalam format gambar? Kami memiliki alat universal untuk Anda mengkonversi PDF ke gambar menggunakan 
Tugas paling umum adalah ketika Anda perlu menyimpan seluruh dokumen PDF atau beberapa halaman tertentu dari dokumen sebagai sekumpulan gambar. **Aspose for Node.js via C++** memungkinkan Anda mengonversi PDF ke format JPG dan PNG untuk menyederhanakan langkah-langkah yang diperlukan guna mendapatkan gambar Anda dari file PDF tertentu.

**Aspose.PDF for Node.js via C++** mendukung berbagai konversi format PDF ke gambar. Harap periksa bagian tersebut. [Format File yang Didukung Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Coba mengonversi PDF ke JPEG secara daring**

Aspose.PDF for Node.js menyajikan Anda aplikasi gratis secara online ["PDF ke JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya dalam beroperasi.

[![Konversi Aspose.PDF PDF ke JPEG dengan Aplikasi Gratis](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Ubah PDF ke JPEG

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Ubah file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToJpg{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Ubah file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToJpg{0:D2}.jpg". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke TIFF secara daring**

Aspose.PDF for Node.js menyajikan Anda aplikasi gratis secara online ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya dalam beroperasi.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF ke TIFF

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Mengonversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToTiff{0:D2}.tiff". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Mengonversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToTiff{0:D2}.tiff". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, akibatnya, muncul kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikutnya.

Aspose.PDF for Node.js menyajikan Anda aplikasi gratis secara online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya dalam beroperasi.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF ke PNG

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToPng{0:D2}.png". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToPng{0:D2}.png". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF for Node.js menyajikan Anda aplikasi gratis secara online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya dalam beroperasi.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah sekumpulan spesifikasi format berkas berbasis XML untuk grafis vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG merupakan standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

## Konversi PDF ke SVG

### Konversi PDF ke SVG klasik

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Konversi file PDF. Dengan demikian, bila 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToSvg.svg". Jika parameter json.errorCode tidak bernilai 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan berada dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Konversi file PDF. Dengan demikian, bila 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPdfToSvg.svg". Jika parameter json.errorCode tidak bernilai 0 dan, sesuai, muncul kesalahan pada file Anda, informasi kesalahan akan berada dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Ubah PDF menjadi SVG terkompresi

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToSvgZip.zip". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToSvgZip.zip". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Konversi PDF ke DICOM

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToDICOM{0:D2}.dcm". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan berada di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToDICOM{0:D2}.dcm". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan berada di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## Ubah PDF menjadi BMP

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToBmp{0:D2}.bmp". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultPdfToBmp{0:D2}.bmp". Di mana {0:D2} mewakili nomor halaman dengan format dua digit. Gambar disimpan dengan resolusi 150 DPI. Jika parameter json.errorCode tidak 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





