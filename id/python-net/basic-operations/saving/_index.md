---
title: Simpan dokumen PDF secara programatik
linktitle: Simpan PDF
type: docs
weight: 30
url: /id/python-net/save-pdf-document/
description: Pelajari cara menyimpan file PDF dalam Python menggunakan perpustakaan Aspose.PDF for Python via .NET. Simpan dokumen PDF ke sistem file, ke aliran, dan dalam aplikasi Web.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menyimpan dokumen PDF menggunakan perpustakaan Aspose.PDF di Python
Abstract: Artikel ini memberikan panduan tentang menyimpan dokumen PDF menggunakan pustaka Aspose.PDF dalam Python. Artikel ini menguraikan tiga metode utama untuk menyimpan PDF - ke sistem file, ke stream, dan dalam format khusus seperti PDF/A atau PDF/X. Metode `save()` dari kelas `Document` menjadi pusat dalam operasi ini. Untuk menyimpan PDF ke sistem file, sebuah dokumen dapat dibuat atau dimanipulasi, misalnya menambahkan halaman baru, dan kemudian disimpan langsung ke path. Untuk menyimpan ke stream, overload metode `Save` memungkinkan menulis dokumen ke objek stream. Selain itu, artikel ini menjelaskan cara menyimpan dokumen dalam format PDF/A atau PDF/X, yang merupakan standar untuk pengarsipan jangka panjang dan pertukaran grafis, masing-masing. Proses ini memerlukan persiapan dokumen dengan metode `convert` sebelum menyimpannya. Potongan kode Python yang disediakan menunjukkan masing-masing pendekatan, menggambarkan penerapan praktis dari metode-metode tersebut.
---

## Simpan dokumen PDF ke sistem berkas

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem berkas menggunakan [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## Simpan dokumen PDF ke aliran

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke stream dengan menggunakan overloads of `Save` metode.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## Simpan format PDF/A atau PDF/X

Anda dapat dengan mudah menyimpan dokumen dalam versi PDF tertentu, seperti PDF/A atau PDF/X. Dalam kasus ini, kita perlu memanggil metode convert sebelum menyimpan dokumen.

PDF/A adalah versi Portable Document Format (PDF) yang distandarisasi oleh ISO untuk digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik.
PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti pengaitan font (berlawanan dengan penyematan font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font yang disematkan, dan antarmuka pengguna untuk membaca anotasi yang disematkan.

PDF/X adalah subset dari standar ISO PDF. Tujuan PDF/X adalah memfasilitasi pertukaran grafis, sehingga ia memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku pada file PDF standar.

Dalam kedua kasus, yang [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan yang [konversi](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
