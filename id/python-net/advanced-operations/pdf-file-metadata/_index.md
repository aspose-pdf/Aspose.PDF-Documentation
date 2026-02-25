---
title: Bekerja dengan Metadata File PDF di Python
linktitle: Metadata File PDF
type: docs
weight: 200
url: /id/python-net/pdf-file-metadata/
description: Jelajahi cara mengekstrak dan mengelola metadata PDF, seperti penulis dan judul, dalam Python menggunakan Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan dan Atur Metadata dalam PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang memanipulasi metadata PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini menjelaskan metode untuk mengekstrak dan mengatur properti metadata, termasuk penulis, tanggal pembuatan, kata kunci, dan lainnya, yang penting untuk katalogisasi dokumen, optimasi pencarian, atau validasi. Potongan kode menunjukkan cara mengambil metadata dari PDF menggunakan kelas `Document` dan properti `info`, mengatur metadata baru menggunakan objek `DocumentInfo`, dan menyimpan perubahan. Selain itu, artikel ini menunjukkan cara memperbarui metadata XMP secara programatik, yang meningkatkan organisasi dan ketercarian dokumen. Artikel juga menjelaskan cara menyisipkan metadata dengan prefiks khusus dengan mendaftarkan URI namespace. Fungsionalitas ini penting bagi pengembang yang ingin mengelola informasi dokumen PDF secara efektif dalam aplikasi.
---

## Dapatkan Informasi File PDF

Potongan kode ini menunjukkan cara mengekstrak metadata dari dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan mengakses properti info dari objek Document, ia mengambil informasi penting seperti penulis, tanggal pembuatan, kata kunci, tanggal modifikasi, subjek, dan judul. Fungsionalitas ini penting bagi aplikasi yang memerlukan katalogisasi dokumen, optimasi pencarian, atau validasi properti dokumen.

1. Buka file PDF menggunakan kelas Document
1. Ambil metadata dokumen melalui properti info
1. Tampilkan Informasi Metadata. Cetak bidang metadata yang diinginkan

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

        # Get document information
        doc_info = document.info

        # Display document information
        print(f"Author: {doc_info.author}")
        print(f"Creation Date: {doc_info.creation_date}")
        print(f"Keywords: {doc_info.keywords}")
        print(f"Modify Date: {doc_info.mod_date}")
        print(f"Subject: {doc_info.subject}")
        print(f"Title: {doc_info.title}")
```

## Atur Informasi File PDF

Aspose.PDF untuk Python via .NET memungkinkan Anda mengatur informasi khusus file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul. Untuk mengatur informasi ini:

1. Buka file PDF menggunakan kelas Document.
1. Buat objek [DocumentInfo]() dan atur properti metadata yang diinginkan.
1. Simpan perubahan ke file PDF baru menggunakan metode save.

Potongan kode berikut menunjukkan cara mengatur informasi file PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

        # Specify document information
        doc_info = ap.DocumentInfo(document)
        doc_info.author = "Aspose"
        doc_info.creation_date = datetime.datetime.now()
        doc_info.keywords = "Aspose.Pdf, DOM, API"
        doc_info.mod_date = datetime.datetime.now()
        doc_info.subject = "PDF Information"
        doc_info.title = "Setting PDF Document Information"
        doc_info.producer = "Custom producer"
        doc_info.creator = "Custom creator"

        # Save PDF document
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## Atur Metadata XMP dalam File PDF

Potongan kode ini menunjukkan cara secara programatik mengatur atau memperbarui metadata XMP dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan memodifikasi properti seperti xmp:CreateDate, xmp:Nickname, dan bidang yang didefinisikan secara khusus, Anda dapat menyematkan metadata standar ke dalam file PDF Anda. Pendekatan ini sangat berguna untuk meningkatkan organisasi dokumen, memfasilitasi ketercarian, dan menyematkan informasi penting langsung ke dalam file.

Aspose.PDF memungkinkan Anda mengatur metadata dalam file PDF. Untuk mengatur metadata:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Modifikasi metadata XMP dengan menetapkan nilai ke kunci tertentu.
1. Simpan Dokumen PDF yang Diperbarui.

Potongan kode berikut menunjukkan cara mengatur metadata dalam file PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## Sisipkan Metadata dengan Prefiks

Beberapa pengembang perlu membuat namespace metadata baru dengan prefiks. Potongan kode berikut menunjukkan cara menyisipkan metadata dengan prefiks.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
