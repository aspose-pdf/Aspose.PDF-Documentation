---
title: Ekstrak Lampiran dari PDF
linktitle: Ekstrak Lampiran
type: docs
weight: 50
url: /id/python-net/extract-attachment/
description: Pelajari cara bekerja dengan lampiran PDF menggunakan Python dan Aspose.PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Panduan Lengkap Mengelola Lampiran PDF dalam Python: Menambah, Mengekstrak, dan Memproses Berkas Tersemat"
Abstract: Lampiran PDF banyak digunakan untuk menyimpan dokumen pendukung, laporan, gambar, dan sumber daya lainnya langsung di dalam file PDF. Artikel ini memberikan tinjauan lengkap tentang penanganan lampiran PDF dengan Python menggunakan Aspose.PDF. Artikel ini menjelaskan cara menyematkan file eksternal ke dalam PDF yang ada, mengekstrak lampiran tertentu atau semua lampiran, memeriksa metadata seperti ukuran file dan cap waktu, serta memulihkan file yang disimpan sebagai anotasi FileAttachment. Setiap contoh menunjukkan teknik praktis untuk mengotomatiskan alur kerja lampiran, meningkatkan portabilitas dokumen, dan menyederhanakan manajemen file. Baik membangun sistem dokumen perusahaan maupun skrip otomatisasi khusus, pengembang dapat menggunakan metode ini untuk mengelola file yang disematkan dalam dokumen PDF secara efisien.
---

## Ekstrak Lampiran Spesifik dari PDF

Ekstrak satu file tersemat dari dokumen PDF menggunakan Python dan Aspose.PDF. Ini mencari lampiran berdasarkan nama, mengambil isinya, dan menyimpannya sebagai file terpisah. Ini berguna untuk mengakses dokumen tersemat seperti laporan, log, atau file pendukung yang disimpan di dalam PDF.

1. Definisikan Fungsi 'extract_single_attachment()'.
1. Buka Dokumen PDF.
1. Cari Lampiran.
1. Ekstrak Konten Lampiran.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Tampilkan Metadata Lampiran File

Fungsi pembantu ini mencetak informasi metadata dari objek spesifikasi file. Ini biasanya digunakan saat bekerja dengan lampiran file tersemat dalam PDF menggunakan Aspose.PDF, memungkinkan pengembang untuk memeriksa detail seperti checksum, tanggal pembuatan, tanggal modifikasi, dan ukuran file.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Ekstrak dan Periksa Semua Lampiran PDF

Potongan kode ini menunjukkan cara mengekstrak semua file tersemat dari dokumen PDF menggunakan Python dan Aspose.PDF. Ini tidak hanya menyimpan setiap lampiran ke folder yang ditentukan tetapi juga mencetak metadata terperinci seperti nama file, deskripsi, tipe MIME, checksum, dan cap waktu. Ini berguna untuk audit, mengekspor, atau memproses konten tersemat dalam file PDF.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Ekstrak File dari Anotasi Lampiran PDF

Ekstrak file tersemat dari anotasi FileAttachment dalam PDF menggunakan Python dan Aspose.PDF. Ini mencari halaman pertama untuk anotasi lampiran pertama, mengambil file tersemat, dan menyimpannya ke direktori output yang dipilih. Ini berguna ketika PDF berisi ikon lampiran file yang dapat diklik alih-alih kumpulan file tersemat standar.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```