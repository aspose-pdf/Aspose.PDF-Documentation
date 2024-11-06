---
title: Dapatkan info tentang Produk menggunakan JavaScript
linktitle: Dapatkan info tentang Produk
type: docs
weight: 70
url: id/javascript-cpp/get-info-about-product/
description: Topik ini menunjukkan cara mendapatkan info tentang Produk dengan Aspose.PDF untuk JavaScript via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Topik ini menjelaskan cara mendapatkan info tentang Produk menggunakan JavaScript.

```js

    /*Buat Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Kesalahan dari Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode !== 0) ? `Kesalahan: ${evt.data.json.errorText}` :
                          "Produk       : " + evt.data.json.product
                      + "\nKeluarga     : " + evt.data.json.family
                      + "\nVersi        : " + evt.data.json.version
                      + "\nTanggal rilis: " + evt.data.json.releasedate
                      + "\nProdusen     : " + evt.data.json.producer
                      + "\nBerlisensi   : " + evt.data.json.islicensed;

    /*Penangan acara*/
    const onAsposePdfAbout = e => {
      /*Dapatkan info tentang Produk - Tanyakan pada Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


Berikut cuplikan kode JavaScript menunjukkan contoh sederhana mendapatkan info tentang Produk:

1. Fungsi [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) dijalankan.
1. Informasi Produk yang dapat diperoleh:
- Nama produk
- Keluarga produk
- Versi produk
- Tanggal rilis
- Nama lengkap/produser
- Produk berlisensi
1. Selanjutnya, jika 'json.errorCode' adalah 0, maka Anda dapat mendapatkan informasi tentang Produk. Jika parameter 'json.errorCode' tidak sama dengan 0 dan, sesuai, akan ada kesalahan di file Anda, maka informasi tentang kesalahan tersebut akan terdapat dalam file 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*Dapatkan info tentang Produk*/
    const json = AsposePdfAbout();
    /* JSON
    Nama produk       : json.product
    Keluarga produk   : json.family
    Versi produk      : json.version
    Tanggal rilis     : json.releasedate
    Nama lengkap/produser : json.producer
    Produk berlisensi : json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Product      : " + json.product
                + "\nFamily       : " + json.family
                + "\nVersion      : " + json.version
                + "\nRelease date : " + json.releasedate
                + "\nProducer     : " + json.producer
                + "\nIs licensed  : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```