---
title: Tambahkan tanda tangan digital atau tanda tangani PDF secara digital dengan Python
linktitle: Tanda tangani PDF secara digital
type: docs
weight: 10
url: /id/python-net/digitally-sign-pdf-file/
description: Tanda tangani dokumen PDF secara digital, verifikasi, atau validasi PDF yang ditandatangani secara digital menggunakan Python.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tanda tangani file PDF secara digital dengan Python
Abstract: Panduan ini menjelaskan cara menandatangani dokumen PDF secara digital menggunakan Aspose.PDF untuk Python via .NET. Panduan ini merinci proses penerapan tanda tangan digital standar dan lanjutan, menggunakan sertifikat (PFX dan PKCS#12), serta menyesuaikan tampilan dan perilaku tanda tangan. Dokumentasi mencakup contoh kode yang menunjukkan cara menandatangani PDF yang ada, menambahkan cap waktu, dan memverifikasi keabsahan tanda tangan. Hal ini memungkinkan pengembang memastikan keaslian, integritas, dan kepatuhan dokumen terhadap standar tanda tangan digital dalam Aplikasi Python mereka.
---

## Tanda Tangani PDF dengan Tanda Tangan Digital

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Sebuah **PKCS#7 detached signature** menambahkan tanda tangan digital ke sebuah dokumen tanpa menyematkan konten ke dalam blok tanda tangan.

Contoh berikut menandatangani dokumen PDF menggunakan tanda tangan digital PKCS#7 detached, menerapkan tanda tangan pada halaman pertama dalam area persegi panjang yang ditentukan.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Potongan kode Python ini memverifikasi tanda tangan digital dalam file PDF menggunakan metode 'file_sign.verify_signature()'.

1. Membuat instance PdfFileSignature yang memungkinkan Anda berinteraksi dengan tanda tangan dalam PDF.
1. Dapatkan daftar nama tanda tangan `get_signature_names(True)`.
1. Memeriksa tanda tangan pertama dalam daftar `verify_signature` untuk kepatuhan dengan sertifikat yang ditentukan.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## Tambahkan cap waktu ke tanda tangan digital

### Cara menandatangani PDF secara digital dengan cap waktu

Aspose.PDF untuk Python mendukung penandatanganan PDF secara digital dengan server cap waktu atau layanan Web.

Untuk memenuhi kebutuhan ini, kelas [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) telah ditambahkan ke namespace Aspose.PDF. Silakan lihat potongan kode berikut yang memperoleh cap waktu dan menambahkannya ke dokumen PDF:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## Menandatangani dokumen PDF menggunakan ECDSA

Menandatangani dokumen PDF menggunakan ECDSA (Elliptic Curve Digital Signature Algorithm) melibatkan penggunaan kriptografi kurva eliptik untuk menghasilkan tanda tangan digital.

Potongan kode di atas menunjukkan cara menerapkan tanda tangan digital PKCS#7 detached ke dokumen PDF menggunakan Aspose.PDF untuk Python. Dengan memuat dokumen, mengonfigurasi tampilan tanda tangan dan pengaturan keamanan, serta menyimpan hasilnya, contoh ini menampilkan alur kerja yang lengkap dan andal untuk menandatangani file PDF secara digital.

Metode ini memastikan keaslian dan integritas dokumen dengan menyematkan tanda tangan yang aman dan dapat diverifikasi pada halaman pertama. Penggunaan SHA-256 sebagai algoritma digest memenuhi standar kriptografi modern, sementara kemampuan mengontrol penempatan tanda tangan menawarkan fleksibilitas untuk tanda persetujuan yang terlihat.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
