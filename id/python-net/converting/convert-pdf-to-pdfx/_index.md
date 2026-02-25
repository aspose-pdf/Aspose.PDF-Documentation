---
title: Konversi PDF ke format PDF/x dalam Python
linktitle: Konversi PDF ke format PDF/x
type: docs
weight: 120
url: /id/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: Topik ini menunjukkan cara mengonversi PDF ke format PDF/x menggunakan Aspose.PDF for Python melalui .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengonversi PDF ke format PDF/x
Abstract: Artikel ini memberikan panduan komprehensif tentang mengonversi PDF ke format PDF/A, PDF/E, dan PDF/X menggunakan Aspose.PDF untuk Python.
---

**Format PDF ke PDF/x berarti kemampuan untuk mengonversi PDF ke format tambahan, yaitu PDF/A, PDF/E, dan PDF/X.**

## Konversi PDF ke PDF/A

**Aspose.PDF for Python** memungkinkan Anda mengonversi file PDF ke file PDF yang mematuhi <abbr title="Portable Document Format / A">PDF/A</abbr>. Sebelum melakukannya, file harus divalidasi. Topik ini menjelaskan caranya.

{{% alert color="primary" %}}

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasar memiliki “representasi” masing-masing tentang kepatuhan PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A untuk referensi. Kami memilih produk Adobe untuk memverifikasi cara Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat semua hal yang terkait dengan PDF.

{{% /alert %}}

Konversi file menggunakan metode Convert pada kelas Document. Sebelum mengonversi PDF ke file yang mematuhi PDF/A, validasi PDF menggunakan metode Validate. Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode Convert. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan enumerasi ConvertErrorAction.

{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi gratis online ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Metode 'document.validate()' memvalidasi apakah file PDF mematuhi standar PDF/A-1B (versi PDF yang distandarisasi ISO untuk arsip jangka panjang). Hasil validasi disimpan dalam file log.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil metode validate dengan tingkat kepatuhan target (ap.PdfFormat.PDF_A_1B).
1. Hasil validasi ditulis ke file log yang ditentukan.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Konversi PDF ke PDF/A-1B

Potongan kode berikut menunjukkan cara mengonversi file PDF ke format PDF/A-1B:

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil metode convert dengan parameter berikut:
- Jalur file log - menyimpan detail proses konversi dan pemeriksaan kepatuhan.
- Format target - 'ap.PdfFormat.PDF_A_1B' (standar arsip).
- Tindakan error - 'ap.ConvertErrorAction.DELETE' — secara otomatis menghapus elemen yang menghalangi kepatuhan.
1. Simpan file PDF/A yang telah dikonversi ke jalur output.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PDF 2.0 dan PDF/A-4

Contoh ini menunjukkan cara mengonversi dokumen PDF ke format standar yang lebih baru: PDF 2.0 dan PDF/A-4.
Kedua konversi membantu memastikan kepatuhan dengan spesifikasi modern dan persyaratan arsip.

1. Muat dokumen input menggunakan ap.Document.
1. Lakukan konversi pertama ke PDF 2.0 dengan memanggil document.convert dengan:
- Jalur file log untuk detail konversi.
- Format target - 'ap.PdfFormat.V_2_0'.
- Tindakan error - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Lakukan konversi kedua ke PDF/A-4 menggunakan metode yang sama, memastikan file juga mematuhi standar arsip.
1. Simpan dokumen hasil di jalur output yang ditentukan.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PDF/A-3A dengan File Tersemat

Potongan kode berikut menunjukkan cara menyematkan file eksternal ke dalam PDF dan kemudian mengonversi PDF ke format PDF/A-3A, yang mendukung lampiran dan cocok untuk arsip jangka panjang dengan konten tersemat.

1. Muat PDF input menggunakan 'ap.Document'.
1. Buat objek 'FileSpecification' yang menunjuk ke file yang akan disematkan (misalnya, "aspose-logo.jpg") dengan deskripsi.
1. Tambahkan spesifikasi file ke koleksi 'embedded_files' PDF.
1. Konversi dokumen ke PDF/A-3A menggunakan 'document.convert', dengan menentukan:
- Jalur file log.
- Format target - 'ap.PdfFormat.PDF_A_3A'.
- Aksi kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PDF/A-1B dengan Substitusi Font

Fungsi ini mengonversi PDF ke format PDF/A-1B sambil menangani font yang hilang dengan menggantinya dengan font yang tersedia. Hal ini memastikan PDF yang dikonversi tetap konsisten secara visual dan mematuhi standar arsip.

1. Muat PDF menggunakan 'ap.Document'.
1. Konversi PDF ke PDF/A-1B menggunakan 'document.convert', dengan menentukan:
- Jalur file log.
- Format target - 'ap.PdfFormat.PDF_A_1B'.
- Aksi kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PDF/A-1B dengan Penandaan Otomatis

Fungsi ini mengonversi dokumen PDF ke format PDF/A-1B sambil secara otomatis menandai konten untuk aksesibilitas dan konsistensi struktural. Penandaan otomatis meningkatkan kegunaan dokumen untuk pembaca layar dan memastikan struktur semantik yang tepat.

1. Muat PDF menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
- Jalur file log.
- Format target - 'ap.PdfFormat.PDF_A_1B'.
- Aksi kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Konfigurasikan 'AutoTaggingSettings':
- Aktifkan 'enable_auto_tagging = True'.
- Atur 'heading_recognition_strategy = AUTO' untuk mendeteksi heading secara otomatis.
1. Tetapkan pengaturan penandaan otomatis ke opsi konversi.
1. Konversi PDF menggunakan 'document.convert(options)'.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Konversi PDF ke PDF/E

Potongan kode ini memvalidasi apakah dokumen PDF mematuhi standar PDF/E-1, yang merupakan standar ISO khusus untuk dokumen teknik dan teknis. Hasil validasi disimpan ke file log.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil metode validate, dengan menentukan:
- Jalur file log untuk menyimpan hasil validasi.
- Format target - 'ap.PdfFormat.PDF_E_1'.
1. Hasil validasi disimpan dalam file log untuk ditinjau.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

Contoh berikut menunjukkan cara mengonversi PDF ke format PDF/E-1, yang merupakan standar ISO khusus untuk dokumentasi teknik dan teknis. Format ini mempertahankan tata letak yang tepat, grafis, dan metadata yang diperlukan untuk alur kerja teknik.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
- Jalur file log untuk melacak masalah konversi.
- Format target - 'ap.PdfFormat.PDF_E_1'.
- Aksi kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Konversi PDF menggunakan 'document.convert(options)'.
1. Simpan PDF yang telah dikonversi ke jalur output yang ditentukan.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Konversi PDF ke PDF/X

Potongan kode berikut mengonversi dokumen PDF ke format PDF/X-4, yang merupakan standar ISO yang umum digunakan dalam industri percetakan dan penerbitan. PDF/X-4 memastikan akurasi warna, mempertahankan transparansi, dan menyematkan profil ICC untuk output yang konsisten di berbagai perangkat.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
- Jalur file log.
- Format target - 'ap.PdfFormat.PDF_X_4'.
- Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Sediakan **berkas profil ICC** untuk manajemen warna melalui 'icc_profile_file_name'.
1. Tentukan **OutputIntent** dengan identifier kondisi (misalnya "FOGRA39") untuk kebutuhan pencetakan.
1. Konversi PDF menggunakan 'document.convert()'.
1. Simpan PDF yang telah dikonversi ke jalur output yang ditentukan.
1. Tampilkan pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
