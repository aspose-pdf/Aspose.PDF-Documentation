---
title: Simpan dokumen PDF secara programatis
linktitle: Simpan PDF
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Pelajari cara menyimpan file PDF di Python Aspose.PDF untuk perpustakaan Python via .NET. Simpan dokumen PDF ke sistem file, ke aliran, dan dalam aplikasi Web.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Simpan dokumen PDF ke sistem file

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem file menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
    document.pages.add()
    document.save(output_pdf)
```

## Simpan dokumen PDF ke aliran

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke aliran dengan menggunakan overload dari metode `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## Simpan format PDF/A atau PDF/X

PDF/A adalah versi ISO-standar dari Portable Document Format (PDF) untuk digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik. PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti penghubungan font (berbeda dengan penyematan font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font yang disematkan, dan antarmuka pengguna untuk membaca anotasi yang disematkan.

PDF/X adalah subset dari standar ISO PDF. Tujuan PDF/X adalah untuk memfasilitasi pertukaran grafis, dan oleh karena itu memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku untuk file PDF standar.

Dalam kedua kasus, metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan metode [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```