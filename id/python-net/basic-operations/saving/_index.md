---
title: Simpan dokumen PDF secara programatis
linktitle: Simpan PDF
type: docs
weight: 30
url: /id/python-net/save-pdf-document/
description: Pelajari cara menyimpan file PDF di Python menggunakan Aspose.PDF untuk Python via .NET library. Simpan dokumen PDF ke sistem file, ke aliran, dan di aplikasi web.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menyimpan dokumen PDF menggunakan pustaka Aspose.PDF di Python
Abstract: Artikel ini memberikan panduan tentang menyimpan dokumen PDF menggunakan pustaka Aspose.PDF di Python. Artikel ini menjelaskan tiga metode utama untuk menyimpan PDF - ke sistem file, ke aliran, dan dalam format tertentu seperti PDF/A atau PDF/X. Metode `save()` dari kelas `Document` menjadi pusat operasi ini. Untuk menyimpan PDF ke sistem file, dokumen dapat dibuat atau dimanipulasi, seperti menambahkan halaman baru, dan kemudian disimpan langsung ke path. Untuk menyimpan ke aliran, overload metode `Save` memungkinkan menulis dokumen ke objek aliran. Selain itu, artikel ini menjelaskan cara menyimpan dokumen dalam format PDF/A atau PDF/X, yang merupakan standar untuk pengarsipan jangka panjang dan pertukaran grafik, masing-masing. Proses ini memerlukan persiapan dokumen dengan metode `convert` sebelum disimpan. Potongan kode Python yang disediakan mendemonstrasikan setiap pendekatan, menggambarkan penerapan praktis dari metode-metode ini.
---

## Simpan dokumen PDF ke sistem file

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem file menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Simpan dokumen PDF ke aliran

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke aliran dengan menggunakan overload metode `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Simpan format PDF/A atau PDF/X

PDF/A adalah versi PDF (Portable Document Format) yang distandarisasi ISO untuk penggunaan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik.
PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti linking font (berlawanan dengan embedding font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font tersemat, dan antarmuka pengguna untuk membaca anotasi tersemat.

PDF/X adalah subset dari standar ISO PDF. Tujuan PDF/X adalah memfasilitasi pertukaran grafik, sehingga memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku pada file PDF standar.

Dalam kedua kasus, metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan metode [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

