---
title: Bekerja dengan Portofolio di PDF menggunakan Python
linktitle: Portofolio
type: docs
weight: 20
url: /id/python-net/portfolio/
description: Cara Membuat Portofolio PDF dengan Python. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara bekerja dengan Portofolio di PDF dengan Python
Abstract: Artikel ini membahas pembuatan dan pengelolaan portofolio PDF menggunakan Aspose.PDF untuk Python via .NET. Sebuah portofolio PDF memfasilitasi konsolidasi berbagai jenis file—seperti file teks, gambar, spreadsheet, dan presentasi—ke dalam satu dokumen teratur, memastikan semua materi yang relevan disimpan secara kolektif. Artikel ini menjelaskan proses pembuatan portofolio PDF, menyoroti penggunaan kelas `Document` dan kelas `FileSpecification` untuk menambahkan file ke koleksi dokumen. Contoh disediakan, yang menunjukkan penyertaan file Microsoft Excel, dokumen Word, dan file gambar ke dalam portofolio PDF. Selain itu, artikel ini menyertakan potongan kode untuk membuat portofolio serta menghapus file darinya, menggambarkan kesederhanaan dan efisiensi mengelola portofolio PDF dengan Aspose.PDF untuk Python.
---

Membuat portofolio PDF memungkinkan konsolidasi dan pengarsipan berbagai jenis file ke dalam satu dokumen yang konsisten. Dokumen semacam itu dapat mencakup file teks, gambar, spreadsheet, presentasi, dan materi lainnya, serta memastikan semua materi relevan disimpan dan diatur dalam satu tempat.

Portofolio PDF akan membantu menampilkan presentasi Anda dengan kualitas tinggi, di mana pun Anda menggunakannya. Secara umum, membuat portofolio PDF adalah tugas yang sangat terkini dan modern.

## Cara Membuat Portofolio PDF

Aspose.PDF untuk Python via .NET memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Tambahkan file ke objek document.collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . Setelah file ditambahkan, gunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas Document untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.

Kode di bawah ini menghasilkan portofolio berikut.

### Portofolio PDF yang dibuat dengan Aspose.PDF untuk Python

![Portofolio PDF yang dibuat dengan Aspose.PDF untuk Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Hapus File dari Portofolio PDF

Untuk menghapus file dari portofolio PDF, coba gunakan baris kode berikut.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


