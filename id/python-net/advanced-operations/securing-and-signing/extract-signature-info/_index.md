---
title: Ekstrak detail dari Tanda Tangan
linktitle: Ekstrak detail dari Tanda Tangan
type: docs
weight: 20
url: /id/python-net/extract-image-and-signature-information/
description: Cara mengekstrak gambar dari tanda tangan digital pada dokumen PDF menggunakan Aspose.PDF untuk Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan detail Tanda Tangan dalam PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara mengekstrak gambar dan informasi tanda tangan digital dari dokumen PDF menggunakan Aspose.PDF untuk Python. Artikel ini menyediakan panduan langkah demi langkah dan contoh kode untuk mengidentifikasi, mengakses, dan menyimpan gambar yang disematkan, serta mengambil metadata dan status validasi tanda tangan digital.
---

## Mengekstrak Gambar dari Kolom Tanda Tangan

Aspose.PDF untuk Python via .NET mendukung fitur menandatangani file PDF secara digital menggunakan kelas [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/).

Potongan kode ini menunjukkan cara mengekstrak gambar tanda tangan digital dari dokumen PDF menggunakan Aspose.PDF untuk Python.

Langkah-langkah:

1. Membuka dokumen PDF.
1. Mengiterasi bidang formulir untuk menemukan objek SignatureField.
1. Mengekstrak gambar yang terkait dengan setiap tanda tangan (jika tersedia).
1. Menyimpan gambar tanda tangan yang diekstrak sebagai file JPEG.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## Ekstrak Informasi Tanda Tangan

Aspose.PDF untuk Python via .NET mendukung fitur menandatangani file PDF secara digital menggunakan kelas SignatureField. Saat ini, kami juga dapat menentukan keabsahan sertifikat namun tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstrak meliputi kunci publik, sidik jari, penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) ke kelas [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek SignatureField:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

Anda dapat memperoleh informasi tentang algoritma tanda tangan dokumen.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## Memeriksa tanda tangan untuk kompromi

Potongan kode ini menunjukkan cara mendeteksi tanda tangan digital yang dikompromikan dalam dokumen PDF menggunakan Aspose.PDF untuk Python.

Langkah-langkah meliputi:

1. Membuka dokumen PDF.
1. Membuat instance 'SignaturesCompromiseDetector' untuk menganalisis dokumen.
1. Memeriksa adanya tanda tangan digital yang dikompromikan (tidak valid atau diubah).
1. Mencetak nama-nama tanda tangan yang dikompromikan yang ditemukan.
1. Melaporkan cakupan tanda tangan—menunjukkan seberapa banyak dokumen yang dilindungi oleh tanda tangan yang valid.

Fitur ini penting dalam penggunaan dimana keaslian dan integritas dokumen harus diverifikasi, seperti lingkungan hukum, keuangan, dan yang berorientasi pada kepatuhan. Fitur ini memungkinkan pengembang secara otomatis mendeteksi pemalsuan atau kerusakan pada PDF yang ditandatangani.

Aspose.PDF menawarkan rangkaian lengkap alat untuk validasi tanda tangan digital, memudahkan pembuatan aplikasi yang aman dan sadar tanda tangan yang menjaga kepercayaan dokumen.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

