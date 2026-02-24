---
title: Buat AcroForm - Buat PDF yang Dapat Diisi dengan Python
linktitle: Buat AcroForm
type: docs
weight: 10
url: /id/python-net/create-form/
description: Dengan Aspose.PDF untuk Python Anda dapat membuat formulir dari awal di file PDF Anda
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara membuat AcroForm dalam PDF menggunakan Python
Abstract: Artikel ini memberikan panduan cara membuat field formulir dalam dokumen PDF menggunakan library Aspose.PDF untuk Python. Ini memperkenalkan kelas `Document`, yang berisi koleksi `Form` untuk mengelola field formulir. Proses menambahkan field formulir melibatkan pembuatan field yang diinginkan dan menggunakan metode `add` dari koleksi `Form`. Contoh spesifik disediakan untuk menggambarkan penambahan `TextBoxField` ke dokumen PDF. Contoh tersebut mencakup kode terperinci yang menunjukkan pembuatan `TextBoxField`, penetapan propertinya seperti posisi, nama, nilai, border, dan warna, dan kemudian menambahkannya ke dokumen. PDF yang dimodifikasi kemudian disimpan dengan field formulir yang baru ditambahkan.
---

## Buat formulir dari awal

### Tambahkan Field Formulir dalam Dokumen PDF

Kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menyediakan koleksi bernama [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) yang membantu Anda mengelola field formulir dalam dokumen PDF.

Untuk menambahkan field formulir:

1. Buat field formulir yang ingin Anda tambahkan.
1. Panggil metode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) dari koleksi Form.

### Menambahkan TextBoxField

Contoh di bawah menunjukkan cara menambahkan [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


