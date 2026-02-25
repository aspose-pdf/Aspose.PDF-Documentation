---
title: Memodifikasi AcroForm
linktitle: Memodifikasi AcroForm
type: docs
weight: 45
url: /id/python-net/modifying-form/
description: Memodifikasi formulir dalam file PDF Anda dengan perpustakaan Aspose.PDF untuk Python via .NET. Anda dapat menambahkan atau menghapus bidang dalam formulir yang ada, mendapatkan dan mengatur batas bidang, dan lain-lain.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengelola dan Menyesuaikan Bidang Formulir PDF
Abstract: Koleksi contoh ini menampilkan berbagai teknik untuk mengelola dan menyesuaikan bidang formulir PDF menggunakan Aspose.PDF untuk Python via .NET. Ini mencakup metode untuk membersihkan teks dari bidang formulir gaya Pengetik menggunakan TextFragmentAbsorber, mengatur dan mengambil batas karakter dengan FormEditor, menerapkan font khusus dan gaya pada bidang kotak teks, serta menghapus bidang formulir tertentu berdasarkan nama. Operasi ini memungkinkan pengembang untuk membersihkan, memformat, dan menyesuaikan formulir PDF untuk distribusi ulang, branding, atau tujuan validasi data, mendukung penyempurnaan estetika dan fungsional dalam alur kerja dokumen otomatis.
---

## Bersihkan Teks dalam Formulir

Contoh ini menunjukkan cara membersihkan teks dari bidang formulir Typewriter dalam PDF menggunakan Aspose.PDF untuk Python via .NET. Ini memindai halaman pertama PDF, mengidentifikasi formulir Typewriter, menghapus kontennya, dan menyimpan dokumen yang telah diperbarui. Pendekatan ini berguna untuk mengatur ulang atau membersihkan bidang formulir sebelum mendistribusikan kembali PDF.

1. Muat dokumen PDF input.
1. Akses formulir pada halaman pertama.
1. Iterasi setiap formulir dan periksa apakah itu formulir `Typewriter`.
1. Gunakan TextFragmentAbsorber untuk menemukan fragmen teks dalam formulir.
1. Bersihkan teks setiap fragmen.
1. Simpan PDF yang dimodifikasi ke file output.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## Dapatkan atau Atur Batas Bidang

Metode set_field_limit(field, limit) pada kelas FormEditor memungkinkan Anda mengatur batas bidang, yaitu jumlah maksimum karakter yang dapat dimasukkan ke dalam sebuah bidang.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

Demikian pula, Aspose.PDF memiliki metode yang mengambil batas bidang.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## Atur Font Kustom untuk Bidang Formulir

Bidang formulir dalam file PDF Adobe dapat dikonfigurasi untuk menggunakan font default tertentu. Pada versi awal Aspose.PDF, hanya 14 font default yang didukung. Rilis selanjutnya memungkinkan pengembang menerapkan font apa pun.

Kode ini memperbarui tampilan bidang kotak teks dalam formulir PDF dengan mengatur font kustom, ukuran, dan warna, kemudian menyimpan dokumen yang telah dimodifikasi menggunakan Aspose.PDF untuk Python via .NET.

Cuplikan kode berikut menunjukkan cara mengatur font default untuk bidang formulir PDF.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## Hapus bidang dalam formulir yang ada

Kode ini menghapus bidang formulir tertentu (berdasarkan namanya) dari dokumen PDF dan menyimpan file yang telah diperbarui menggunakan Aspose.PDF untuk Python via .NET.

1. Muat dokumen PDF.
1. Hapus bidang formulir berdasarkan nama.
1. Simpan PDF yang diperbarui.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

