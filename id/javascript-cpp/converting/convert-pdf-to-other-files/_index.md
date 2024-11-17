---
title: Mengonversi PDF ke EPUB, TeX, Teks, XPS dalam JavaScript
linktitle: Mengonversi PDF ke format lain
type: docs
weight: 90
url: /id/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan JavaScript atau JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Operasi konversi bergantung pada jumlah halaman dalam dokumen dan bisa memakan waktu yang sangat lama. Oleh karena itu, kami sangat menyarankan menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang membutuhkan sumber daya besar ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file yang telah dikonversi.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke EPUB secara online**


Aspose.PDF untuk JavaScript menghadirkan aplikasi online gratis ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Konversi PDF ke EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat mengalir ulang, artinya pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan penerbit dan rumah konversi untuk keperluan internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Handler acara*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke ePub dan simpan sebagai "ResultPDFtoEPUB.epub" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into EPUB files:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/) dieksekusi.
1. Nama file hasil ditentukan, dalam contoh ini "ResultPDFtoEPUB.epub".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
1. Sebagai hasil, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Konversi file PDF ke EPUB dan simpan sebagai "ResultPDFtoEPUB.epub"*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi online gratis ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke TeX

**Aspose.PDF untuk JavaScript** mendukung mengonversi PDF ke TeX.
Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penataan huruf berkualitas tinggi.

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Pengendali acara*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke TeX dan simpan sebagai "ResultPDFtoTeX.tex" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file TEX:

1. Pilih file PDF untuk diubah.
2. Buat 'FileReader'.
3. Fungsi [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/) dijalankan.
4. Nama file hasil ditetapkan, dalam contoh ini "ResultPDFtoTeX.tex".
5. Selanjutnya, jika 'json.errorCode' adalah 0, maka File hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
6. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Ubah file PDF menjadi TeX dan simpan sebagai "ResultPDFtoTeX.tex"*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke Teks secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi gratis online ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke TXT

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Konversi file PDF ke Teks dan simpan sebagai "ResultPDFtoTxt.txt" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
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


Berikut adalah potongan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file TXT:

1. Pilih file PDF untuk diubah.
2. Buat 'FileReader'.
3. Fungsi [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/) dijalankan.
4. Nama file hasil ditetapkan, dalam contoh ini "ResultPDFtoTxt.txt".
5. Selanjutnya, jika 'json.errorCode' adalah 0, maka file hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam file 'json.errorText'.
6. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Ubah file PDF ke Txt dan simpan sebagai "ResultPDFtoTxt.txt"*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Cobalah mengonversi PDF ke XPS secara online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi online gratis ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Konversi PDF ke XPS

Jenis file XPS terutama terkait dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya diberi nama kode Metro dan mencakup konsep pemasaran Jalur Cetak Generasi Berikutnya (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

**Aspose.PDF untuk JavaScript** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="Spesifikasi Kertas XML">XPS</abbr>. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan JavaScript.

```js

    /*Membuat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan peristiwa*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Mengonversi file PDF ke Xps dan menyimpan "ResultPDFtoXps.xps" - Meminta Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
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


Berikut adalah cuplikan kode JavaScript yang menunjukkan contoh sederhana mengubah halaman PDF menjadi file XPS:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/) dijalankan.
1. Nama file hasil ditentukan, dalam contoh ini "ResultPDFtoXps.xps".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka file hasil Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Konversi file PDF ke Xps dan simpan sebagai "ResultPDFtoXps.xps"*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Konversi PDF ke PDF Grayscale

Konversi PDF ke hitam putih dengan Aspose.PDF untuk JavaScript melalui toolkit Web C++. Mengapa saya harus mengonversi PDF ke Grayscale? Jika file PDF berisi banyak gambar berwarna dan ukuran file lebih penting daripada warna, konversi ini menghemat ruang. Jika Anda mencetak file PDF dalam hitam putih, mengonversinya akan memungkinkan Anda memeriksa secara visual seperti apa hasil akhirnya.

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Penangan acara*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*konversi file PDF ke grayscale dan simpan sebagai "ResultConvertToGrayscale.pdf" - Tanyakan kepada Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
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


Berikut adalah contoh kode JavaScript yang menunjukkan contoh sederhana dari mengonversi halaman PDF menjadi PDF Grayscale:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) dijalankan.
1. Nama dari file hasil ditetapkan, dalam contoh ini "ResultConvertToGrayscale.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*konversi file PDF menjadi grayscale dan simpan sebagai "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*buat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```