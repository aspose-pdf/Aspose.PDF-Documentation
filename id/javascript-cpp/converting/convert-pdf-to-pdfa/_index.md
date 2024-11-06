---
title: Mengonversi PDF ke format PDF/A
linktitle: Mengonversi PDF ke format PDF/A
type: docs
weight: 100
url: id/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk JavaScript** memungkinkan Anda untuk mengonversi file PDF ke file PDF yang sesuai dengan <abbr title="Portable Document Format / A">PDF/A</abbr>.

Operasi konversi bergantung pada jumlah halaman dalam dokumen dan bisa sangat memakan waktu. Oleh karena itu, kami sangat menyarankan menggunakan Web Workers.

Kode ini menunjukkan cara untuk memindahkan tugas konversi file PDF yang membutuhkan banyak sumber daya ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara ramah pengguna untuk mengunduh file yang telah dikonversi.

{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A online**

Aspose.PDF untuk JavaScript menghadirkan aplikasi gratis online ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Konversi PDF ke format PDF/A

```js

  /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `Kesalahan: ${evt.data.json.errorText}`;

    /*Handler acara*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*mengonversi file PDF ke PDF/A(1A) dan menyimpan "ResultConvertToPDFA.pdf"*/
        /*selama proses konversi, validasi juga dilakukan, "ResultConvertToPDFA.xml"- Tanyakan Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

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


Berikut ini adalah potongan kode JavaScript yang menunjukkan contoh sederhana dari mengkonversi file PDF ke file PDF/A:

1. Pilih file PDF untuk dikonversi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) dieksekusi.
1. Nama dari file hasil ditetapkan, dalam contoh ini "ResultConvertToPDFA.pdf". Selama proses konversi, validasi juga dilakukan, "ResultConvertToPDFA.xml".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberikan nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, karenanya, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda untuk mengunduh file hasil, dan tautan untuk mengunduh file Log (xml) ke sistem operasi pengguna.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*mengkonversi file PDF ke PDF/A(1A) dan menyimpan "ResultConvertToPDFA.pdf"*/
      /*selama proses konversi, validasi juga dilakukan, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nFile Log (format xml): " + json.fileNameLogResult;
        /*buat tautan untuk mengunduh file hasil*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nFile Log (format xml): " + json.fileNameLogResult;
      /*buat tautan untuk mengunduh Log (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```