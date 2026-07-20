---
title: Konversi PDF ke EPUB, TeX, Teks, XPS di Node.js
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Text, XPS, dll dalam lingkungan Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Coba konversi PDF ke EPUB secara online**

Aspose.PDF for Node.js mempersembahkan aplikasi daring gratis untuk Anda ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Ubah PDF menjadi EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat mengalir ulang, artinya pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan oleh penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Itu menggantikan standar Open eBook.

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Konversi file PDF. Oleh karena itu, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoEPUB.epub". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Konversi file PDF. Oleh karena itu, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoEPUB.epub". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan pada file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara daring**

Aspose.PDF for Node.js mempersembahkan aplikasi daring gratis untuk Anda ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke TeX

**Aspose.PDF for Node.js** mendukung mengonversi PDF ke TeX.
Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Konversikan file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoTeX.tex". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Konversikan file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoTeX.tex". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terdapat di 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba konversi PDF ke Teks secara daring**

Aspose.PDF for Node.js mempersembahkan aplikasi daring gratis untuk Anda ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke TXT

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Konversi file PDF. Jadi, bila 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoTxt.txt". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Konversi file PDF. Jadi, bila 'json.errorCode' adalah 0, hasil operasi disimpan di "ResultPDFtoTxt.txt". Jika parameter json.errorCode bukan 0 dan, akibatnya, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Coba konversi PDF ke XPS secara daring**

Aspose.PDF for Node.js mempersembahkan aplikasi daring gratis untuk Anda ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Konversi PDF ke XPS

Jenis file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya diberi kode nama Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), merupakan inisiatif Microsoft untuk mengintegrasikan pembuatan dan peninjauan dokumen ke dalam sistem operasi Windows.

**Aspose.PDF for Node.js** memberikan kemungkinan untuk mengonversi file PDF ke <abbr title="XML Paper Specification">XPS</abbr> format. Mari coba gunakan cuplikan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Node.js.

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoXps.xps". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' bernilai 0, hasil operasi disimpan dalam "ResultPDFtoXps.xps". Jika parameter json.errorCode tidak 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Konversi PDF ke PDF Grayscale

Ubah PDF menjadi hitam putih dengan Aspose.PDF for Node.js via C++ toolkit. 
Mengapa saya harus mengonversi PDF ke Grayscale? Jika file PDF berisi banyak gambar berwarna dan ukuran file penting dibandingkan warna, konversi akan menghemat ruang. Jika Anda mencetak file PDF dalam hitam putih, mengonversinya akan memungkinkan Anda memeriksa secara visual seperti apa hasil akhirnya. 

Jika Anda ingin mengonversi dokumen PDF, Anda dapat menggunakan [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) fungsi. 
Silakan periksa potongan kode berikut untuk mengonversi di lingkungan Node.js.

**CommonJS:**

1. Panggilan `require` dan impor `asposepdfnodejs` modul sebagai `AsposePdf` variabel.
1. Tentukan nama file PDF yang akan dikonversi.
1. Panggilan `AsposePdf` sebagai Promise dan lakukan operasi untuk mengonversi file. Dapatkan objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultConvertToGrayscale.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. Impor `asposepdfnodejs` modul.
1. Tentukan nama file PDF yang akan dikonversi.
1. Inisialisasi modul AsposePdf. Terima objek jika berhasil.
1. Panggil fungsi [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Konversi file PDF. Jadi, jika 'json.errorCode' adalah 0, hasil operasi disimpan dalam "ResultConvertToGrayscale.pdf". Jika parameter json.errorCode bukan 0 dan, sesuai, terjadi kesalahan dalam file Anda, informasi kesalahan akan terkandung dalam 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






