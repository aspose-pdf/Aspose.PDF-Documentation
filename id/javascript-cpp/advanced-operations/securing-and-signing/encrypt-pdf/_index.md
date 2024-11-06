---
title: Mengenkripsi PDF menggunakan JavaScript
linktitle: Mengenkripsi Berkas PDF
type: docs
weight: 50
url: id/javascript-cpp/encrypt-pdf/
description: Mengenkripsi Berkas PDF dengan Aspose.PDF untuk JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mengenkripsi Berkas PDF menggunakan Kata Sandi Pengguna atau Pemilik

Jika Anda mengirim email kepada seseorang dengan lampiran PDF yang berisi informasi rahasia, Anda mungkin ingin menambahkan beberapa keamanan terlebih dahulu untuk menghindari jatuh ke tangan yang salah. Cara terbaik untuk membatasi akses tidak sah ke dokumen PDF adalah dengan melindunginya dengan kata sandi. Untuk mengenkripsi dokumen dengan mudah dan aman, Anda dapat menggunakan Aspose.PDF untuk JavaScript via C++.

>Harap tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi berkas PDF.

- **Kata sandi Pengguna**, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi Pemilik**, jika diatur, mengontrol izin, seperti pencetakan, pengeditan, ekstraksi, komentar, dll.
 Acrobat/Reader akan menonaktifkan hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

Cuplikan kode berikut menunjukkan cara mengenkripsi file PDF.

1. Pilih file PDF untuk dienkripsi.
1. Buat 'FileReader'.
1. Fungsi [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) dijalankan.
1. Nama file hasil ditetapkan, dalam contoh ini "ResultEncrypt.pdf".
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka DownloadFile Anda diberi nama yang Anda tentukan sebelumnya. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, oleh karena itu, akan ada kesalahan dalam file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.
1. Sebagai hasilnya, fungsi [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) menghasilkan tautan dan memungkinkan Anda mengunduh file hasil ke sistem operasi pengguna.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*mengenkripsi file PDF dengan kata sandi "user" dan "owner", dan simpan sebagai "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*buat tautan untuk mengunduh file hasil*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Menggunakan Web Workers

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'dimuat!' :
        (evt.data.json.errorCode == 0) ?
          `Hasil:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Enkripsi file PDF dengan kata sandi "user" dan "owner", dan simpan sebagai "ResultEncrypt.pdf" - Minta Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
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