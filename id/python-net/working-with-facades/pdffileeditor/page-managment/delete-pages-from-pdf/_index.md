---
title: Hapus Halaman dari PDF
linktitle: Hapus Halaman dari PDF
type: docs
weight: 20
url: /id/python-net/delete-pages-from-pdf/
description: Hapus halaman yang dipilih dari dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Halaman Tertentu dari Dokumen PDF dalam Python
Abstract: Pelajari cara menghapus halaman yang dipilih dari dokumen PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menghapus halaman tertentu dari file PDF yang ada secara programatis, membuat dokumen baru tanpa halaman yang dihapus.
---

Kadang-kadang dokumen PDF berisi halaman yang tidak diperlukan atau sensitif yang perlu dihapus. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menghapus halaman tertentu dari PDF tanpa harus mengedit file secara manual.

Contoh kami menunjukkan cara menggunakan metode delete dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk menghapus halaman dari dokumen PDF. Dengan menentukan nomor halaman yang akan dihapus, Anda dapat membuat PDF baru yang tidak menyertakan halaman yang tidak diinginkan. Fungsionalitas ini berguna untuk membersihkan laporan, menghapus informasi rahasia, atau menyiapkan ekstrak dokumen khusus.

1. Buat Objek PdfFileEditor.
1. Tentukan Halaman yang Akan Dihapus.
1. Hapus Halaman.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```