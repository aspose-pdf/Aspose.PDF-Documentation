---
title: Buat Portofolio PDF di Python
linktitle: Portofolio
type: docs
weight: 20
url: /id/python-net/portfolio/
description: Pelajari cara membuat dan mengelola portofolio PDF di Python dengan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bangun dan edit portofolio PDF dengan file tersemat di Python
Abstract: Artikel ini menjelaskan cara membuat dan mengelola portofolio PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menggabungkan berbagai jenis file ke dalam satu portofolio PDF, menambahkan file ke koleksi dokumen, dan menghapus item portofolio secara programatik dengan Python.
---

Membuat portofolio PDF memungkinkan pengkonsolidasian dan pengarsipan berbagai jenis file ke dalam satu dokumen yang konsisten. Dokumen semacam itu dapat mencakup file teks, gambar, spreadsheet, presentasi, dan materi lainnya, serta memastikan semua materi yang relevan disimpan dan diatur di satu lokasi.

Portofolio PDF akan membantu menampilkan presentasi Anda dengan cara berkualitas tinggi, di mana pun Anda menggunakannya. Secara umum, membuat portofolio PDF adalah tugas yang sangat terkini dan modern.

Gunakan portofolio PDF ketika Anda ingin mendistribusikan kumpulan file terkait sekaligus sambil mempertahankan setiap file dalam format aslinya di dalam satu wadah PDF.

## Cara Membuat Portofolio PDF

Aspose.PDF for Python via .NET memungkinkan pembuatan dokumen Portofolio PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Tambahkan file ke dalam a document.collection object setelah mendapatkannya dengan the [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) class. Ketika file telah ditambahkan, gunakan the Document class' [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat PDF Portfolio.

Kode di bawah ini menghasilkan portofolio berikut.

### PDF Portfolio yang dibuat dengan Aspose.PDF for Python

![PDF Portfolio yang dibuat dengan Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Hapus file dari PDF Portfolio

Untuk menghapus/mengeluarkan file dari PDF portfolio, coba gunakan baris kode berikut.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Topik Lampiran Terkait

- [Bekerja dengan lampiran PDF di Python](/pdf/id/python-net/attachments/)
- [Tambahkan Lampiran ke PDF dengan Python](/pdf/id/python-net/add-attachment-to-pdf-document/)
- [Hapus lampiran dari PDF di Python](/pdf/id/python-net/removing-attachment-from-an-existing-pdf/)

