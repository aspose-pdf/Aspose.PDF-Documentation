---
title: Bekerja dengan Formulir XFA
linktitle: Formulir XFA
type: docs
weight: 20
url: /id/python-net/xfa-forms/
description: Aspose.PDF untuk Python melalui .NET API memungkinkan Anda bekerja dengan bidang XFA dan XFA Acroform dalam dokumen PDF.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Konversi XFA-ke-Acroform

{{% alert color="primary" %}}

Coba online
Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Potongan kode berikut menunjukkan cara mengonversi formulir XFA dinamis (XML Forms Architecture) menjadi AcroForm standar.

**Langkah utama meliputi:**

1. Memuat dokumen PDF masukan.
1. Mengubah jenis formulir menjadi STANDARD.
1. Menyimpan PDF yang sudah dikonversi ke file baru.

Konversi ini memungkinkan kompatibilitas yang lebih baik dan penanganan formulir yang konsisten di berbagai pembaca PDF dan aplikasi.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Penggunaan IgnoreNeedsRendering

Contoh ini menunjukkan cara mengonversi formulir XFA dinamis menjadi AcroForm standar menggunakan Aspose.PDF untuk Python. Kode memeriksa apakah PDF masukan berisi formulir XFA dan mengabaikan rendering jika diperlukan. Kemudian jenis formulir diatur ke STANDARD dan PDF yang diperbarui disimpan.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

