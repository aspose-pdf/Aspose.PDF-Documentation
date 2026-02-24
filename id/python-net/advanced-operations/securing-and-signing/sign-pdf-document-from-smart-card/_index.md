---
title: Cara menambahkan tanda tangan Kartu Pintar ke PDF
linktitle: Penandatanganan PDF dengan Smart Card
type: docs
weight: 30
url: /id/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF untuk Python via .NET memungkinkan Anda menandatangani dokumen PDF menggunakan kartu pintar melalui bidang tanda tangan.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tanda tangani dokumen PDF dari Smart Card dengan Python
Abstract: Panduan ini menjelaskan cara menandatangani dokumen PDF secara digital menggunakan kartu pintar dengan Aspose.PDF untuk Python via .NET. Panduan ini menunjukkan cara mengakses sertifikat yang disimpan pada perangkat keras (seperti token USB atau kartu pintar) melalui Windows Certificate Store dan menggunakannya untuk menandatangani file PDF. Dokumentasi ini mencakup contoh kode yang menunjukkan cara menemukan sertifikat yang tepat, mengkonfigurasi properti tanda tangan, dan menyematkan tanda tangan digital ke dalam PDF. Ini memungkinkan penandatanganan yang aman dan berbasis perangkat keras sesuai dengan standar tanda tangan digital, cocok untuk alur kerja perusahaan dan hukum yang memerlukan kepercayaan tinggi.
---

Aspose.PDF menyediakan kemampuan kuat untuk mengintegrasikan komponen tanda tangan visual dan kriptografis, memastikan keaslian serta tampilan profesional dalam dokumen PDF yang ditandatangani secara digital.

## Tanda Tangan dengan Smart Card Menggunakan Bidang Tanda Tangan

Contoh ini menunjukkan cara menandatangani dokumen PDF secara digital menggunakan sertifikat eksternal dengan Aspose.PDF untuk Python dan menerapkan gambar tampilan tanda tangan khusus:

1. Membuka dokumen PDF.
1. Membuat objek PdfFileSignature dan mengaitkannya dengan dokumen.
1. Mengambil sertifikat digital lokal menggunakan metode khusus `get_local_certificate()`.
1. Menyiapkan ExternalSignature berdasarkan sertifikat yang dipilih.
1. Menerapkan gambar tampilan tanda tangan khusus (mis., logo perusahaan atau tanda tangan tulisan tangan).
1. Menandatangani secara digital halaman pertama dokumen dengan metadata yang ditentukan (alasan, kontak, lokasi).
1. Menyimpan dokumen yang ditandatangani ke file keluaran baru.

Metode ini ideal untuk situasi di mana tanda tangan harus diterapkan secara programatis menggunakan sertifikat eksternal—seperti token perangkat keras, penyimpanan sertifikat, atau penyedia tepercaya—dan ditampilkan dengan tata letak visual yang dipersonalisasi.

Berikut adalah contoh kode untuk menandatangani dokumen PDF dari kartu pintar:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## Verifikasi Tanda Tangan Digital

Potongan kode ini menunjukkan cara memverifikasi tanda tangan digital dalam dokumen PDF menggunakan Aspose.PDF untuk Python:

1. Membuka file PDF.
1. Membuat objek 'PdfFileSignature' dan mengaitkannya dengan dokumen.
1. Mengambil daftar semua nama bidang tanda tangan menggunakan 'get_signature_names()'.
1. Mengiterasi setiap tanda tangan dan memverifikasi keabsahannya dengan 'verify_signature()'.
1. Menaikkan pengecualian jika ada tanda tangan yang gagal verifikasi.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## Tanda Tangan dengan Sertifikat Eksternal

Potongan kode ini menunjukkan cara menambahkan dan menandatangani bidang tanda tangan digital dalam dokumen PDF menggunakan Aspose.PDF untuk Python dengan sertifikat eksternal:

1. Membuka file PDF sebagai aliran biner.
1. Membuat SignatureField dan menempatkannya pada halaman pertama dokumen di posisi yang ditentukan.
1. Mengambil sertifikat digital lokal menggunakan metode khusus `get_local_certificate()`.
1. Menyiapkan ExternalSignature dengan metadata seperti otoritas, alasan, dan informasi kontak.
1. Menetapkan nama bidang unik untuk bidang tanda tangan (partial_name = "sig1").
1. Menambahkan bidang tanda tangan ke bidang formulir PDF.
1. Menandatangani bidang tersebut dengan sertifikat eksternal.
1. Menyimpan dokumen yang ditandatangani ke file keluaran.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


