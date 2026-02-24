---
title: Mengekstrak Halaman secara Programatis dengan Python
linktitle: Mengekstrak Halaman PDF
type: docs
weight: 80
url: /id/python-net/extract-pages/
description: Anda dapat mengekstrak halaman dari file PDF Anda menggunakan Aspose.PDF untuk Python via .NET library.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengekstrak halaman PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara mengekstrak halaman dari dokumen PDF menggunakan perpustakaan Aspose.PDF untuk Python. Teknik-teknik ini mencakup ekstraksi satu halaman maupun beberapa halaman, memungkinkan pengembang membuat file PDF baru yang hanya berisi halaman yang dipilih. Contoh-contoh menggambarkan cara mengakses halaman tertentu dengan indeks berbasis 1, menyalinnya ke dokumen PDF baru, dan menyimpan hasilnya sambil menjaga dokumen asli tetap tidak berubah. Metode ini berguna untuk memecah dokumen besar, berbagi bagian tertentu, atau membuat subset PDF yang disesuaikan untuk distribusi atau analisis.
---

## Mengekstrak Satu Halaman dari PDF

Ekstrak halaman tertentu dari dokumen PDF dan simpan sebagai file baru. Menggunakan perpustakaan Aspose.PDF, skrip menyalin halaman yang diinginkan ke PDF baru, meninggalkan dokumen asli tidak berubah. Ini berguna untuk memecah PDF atau mengisolasi halaman penting untuk distribusi.

1. Muat PDF sumber menggunakan API [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Buat [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru untuk menampung halaman yang diekstrak.
1. Tambahkan [`Halaman`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) yang diinginkan dari dokumen sumber ke PDF baru menggunakan [`KoleksiHalaman`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
- Dalam contoh ini, halaman 2 diekstrak (indeks berbasis 1).
1. Simpan [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru dengan halaman yang diekstrak ke file output yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## Mengekstrak Beberapa Halaman dari PDF

Ekstrak beberapa halaman spesifik dari dokumen PDF dan simpan ke dalam file baru. Menggunakan perpustakaan Aspose.PDF, halaman yang dipilih disalin ke PDF baru sementara dokumen asli tetap utuh. Ini berguna untuk membuat PDF lebih kecil yang hanya berisi bagian relevan dari dokumen yang lebih besar.

1. Muat PDF sumber menggunakan API [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Buat [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru untuk menampung halaman-halaman yang diekstrak.
1. Pilih halaman yang akan diekstrak (dalam contoh ini, halaman 2 dan 3 menggunakan indeks berbasis 1).
1. Tambahkan setiap [`Halaman`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) yang dipilih dari dokumen sumber ke PDF baru menggunakan [`KoleksiHalaman`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru dengan halaman-halaman yang diekstrak ke file output yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
