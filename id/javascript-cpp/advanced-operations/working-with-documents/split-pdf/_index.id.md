---
title: Memisahkan PDF menggunakan JavaScript
linktitle: Memisahkan file PDF
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individual dengan Aspose.PDF untuk JavaScript melalui C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memisahkan PDF menjadi dua file menggunakan JavaScript

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individual menggunakan JavaScript. Saat ini, kami mendukung pemisahan menjadi dua bagian. Ini berarti bahwa `pageToSplit` adalah penanda untuk pembagian. File pertama akan berisi semua halaman dari 1 hingga `pageToSplit` secara inklusif, dan file kedua akan memiliki sisa halaman.

Operasi pemisahan bergantung pada jumlah halaman dalam dokumen dan dapat memakan waktu yang sangat lama. Oleh karena itu, kami sangat merekomendasikan menggunakan Web Workers.

Potongan kode yang disediakan adalah contoh penggunaan Web Worker dalam JavaScript untuk memisahkan file PDF menjadi dua file PDF terpisah dan menawarkan pengguna opsi untuk mengunduh file hasilnya.
 Here's a steps of the code:

1. Membuat Web Worker. Sebuah web worker diinisialisasi menggunakan file skrip "AsposePDFforJS.js". Web worker ini akan menangani tugas pemisahan file PDF di latar belakang. Dalam contoh kami, setiap kesalahan yang terjadi di worker ditangkap dan dicatat ke dalam konsol.
1. Penanganan Pesan. Web worker diatur untuk mendengarkan pesan menggunakan event handler onmessage. Ketika menerima pesan dari halaman web, ia memproses permintaan dan mengirimkan respons kembali ke thread utama.
1. Penanganan Acara Pemisahan File. Ada penangan acara ffileSplit yang dipicu ketika pengguna memilih file PDF untuk dipisah. Ia membaca file PDF yang dipilih menggunakan FileReader dan mengirimkan konten file serta parameter yang relevan (seperti jumlah halaman yang akan dipisah dan nama file keluaran) ke web worker melalui panggilan postMessage.
1. Fungsi Unduh File. Fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) bertanggung jawab untuk menghasilkan tautan yang memungkinkan pengguna mengunduh file. Fungsi ini menerima nama file, jenis MIME, dan konten file. Fungsi ini membuat tautan unduhan, mengasosiasikan konten file dengannya, menetapkan nama file, dan menambahkannya ke dokumen. Ini memungkinkan pengguna untuk mengunduh file PDF yang dihasilkan.

1. Penanganan Pesan di Web Worker. Selanjutnya, jika 'json.errorCode' adalah 0, maka json.fileNameResult akan berisi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, karenanya, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam properti 'json.errorText'.

1. Tampilan Hasil. Halaman utama mencakup elemen dengan ID 'output'. Ketika web worker mengirim pesan dengan hasil, elemen 'output' diperbarui. Jika operasi berhasil, ia menampilkan tautan unduh untuk dua file PDF yang telah dipisah. Jika ada kesalahan, ia menampilkan pesan kesalahan.

Kode ini menunjukkan cara untuk memindahkan tugas pemisahan file PDF yang memakan banyak sumber daya ke web worker untuk mencegah pemblokiran thread UI utama. Ini juga menawarkan cara yang ramah pengguna untuk mengunduh file PDF yang telah dipisah.

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Kesalahan: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Tetapkan nomor halaman untuk dipisah*/
        const pageToSplit = 1;
        /*Pisah menjadi dua file PDF dan simpan sebagai "ResultSplit1.pdf", "ResultSplit2.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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

The following JavaScript code snippet shows simple example of splitting PDF pages into individual PDF files:

1. Pilih file PDF untuk dipecah.
1. Buat objek 'FileReader' dalam handler.
1. Tetapkan nomor halaman untuk dipecah.
1. Panggil [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) di handler terakhir.
1. Analisis hasilnya. Nama file hasil ditetapkan, dalam contoh ini "ResultSplit2.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka json.fileNameResult akan berisi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, dengan demikian, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terkandung dalam properti 'json.errorText'.
1. Anda dapat menggunakan fungsi pembantu [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Tetapkan nomor halaman untuk dipecah*/
      const pageToSplit = 1;
      /*Pecah menjadi dua file PDF dan simpan "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Buat tautan untuk mengunduh file hasil pertama*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Buat tautan untuk mengunduh file hasil kedua*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```