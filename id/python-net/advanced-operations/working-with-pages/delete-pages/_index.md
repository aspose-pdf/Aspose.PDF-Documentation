---
title: Menghapus Halaman PDF secara Programatis dengan Python
linktitle: Menghapus Halaman PDF
type: docs
weight: 80
url: /id/python-net/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan pustaka Aspose.PDF untuk Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menghapus halaman dari PDF menggunakan Python
Abstract: Artikel ini memberikan panduan singkat tentang cara menghapus halaman dari file PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Artikel ini berfokus pada penggunaan kelas `PageCollection` untuk menghapus halaman tertentu. Prosesnya melibatkan pemanggilan metode `delete()` dengan indeks halaman yang akan dihapus, kemudian menyimpan dokumen yang diperbarui dengan metode `save()`. Selain itu, disediakan cuplikan kode untuk mendemonstrasikan penghapusan halaman dari file PDF, yang menggambarkan penggunaan pustaka Aspose.PDF dalam konteks praktis.
---

Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF untuk Python via .NET. Untuk menghapus halaman tertentu, gunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dari sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

## Hapus Halaman dari File PDF

Aspose.PDF untuk Python via .NET menghapus halaman 2 dari PDF masukan dan menyimpan dokumen yang diperbarui ke file baru. Fitur ini berguna untuk menghapus halaman yang tidak diinginkan atau sensitif tanpa mengubah bagian lain dari dokumen.

1. Muat PDF masukan sebagai sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hapus halaman menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Panggil metode [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) untuk menyimpan file PDF yang diperbarui.

Cuplikan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan Python.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## Hapus Banyak Halaman dari Dokumen PDF

Menghapus beberapa halaman memungkinkan Anda menghapus sekumpulan halaman yang ditentukan dalam satu operasi, yang lebih efisien dibandingkan menghapus halaman satu per satu. PDF yang dihasilkan disimpan ke file baru, menjaga dokumen asli.

1. Muat PDF masukan sebagai sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hapus halaman yang terdaftar dalam array pages menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang diperbarui ke file baru.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

