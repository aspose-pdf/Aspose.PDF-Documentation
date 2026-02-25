---
title: Ekstrak Tautan dari File PDF menggunakan Python
linktitle: Ekstrak Tautan
type: docs
weight: 30
url: /id/python-net/extract-links/
description: Temukan cara mengekstrak hyperlink dari dokumen PDF menggunakan Python dengan Aspose.PDF untuk manajemen konten dan analisis tautan.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengekstrak Tautan dari PDF
Abstract: Panduan Aspose.PDF untuk Python via .NET tentang mengekstrak tautan menjelaskan cara secara programatik mengambil anotasi hyperlink dari dokumen PDF menggunakan Python. Dokumentasi mencakup contoh kode praktis dan menyoroti bagaimana fungsi ini dapat digunakan untuk tugas seperti audit tautan, analisis navigasi, atau membangun fitur dokumen interaktif. Baik Anda bekerja dengan PDF satu halaman maupun memproses batch besar, panduan ini menawarkan pendekatan yang jelas dan efisien untuk ekstraksi hyperlink.
---

## Ekstrak Tautan dari File PDF

Contoh ini menunjukkan cara mengiterasi semua anotasi tautan pada halaman pertama PDF menggunakan Aspose.PDF untuk Python. Ini memfilter anotasi untuk mengidentifikasi yang berjenis LinkAnnotation, mengcastingnya secara aman, dan kemudian mencetak indeks halaman serta posisi persegi panjangnya pada halaman.

Ini dapat digunakan untuk debugging, analitik, atau pembaruan otomatis pada anotasi tautan yang ada dalam PDF.

1. Muat dokumen PDF. Gunakan ap.Document(path_infile) untuk membuka file.
1. Akses anotasi dari halaman pertama. Gunakan document.pages[1].annotations untuk mengambil semua anotasi.
1. Filter hanya untuk tipe LinkAnnotation. Periksa annotation_type setiap anotasi.
1. Cast dan proses LinkAnnotation. Gunakan is_assignable() dan cast() untuk memastikan akses aman ke properti LinkAnnotation.
1. Cetak detail anotasi. Output indeks halaman dan persegi panjang (lokasi) setiap tautan.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Ekstrak Hyperlink dari File PDF

Kode ini menunjukkan cara mengekstrak semua objek LinkAnnotation dari halaman pertama dokumen PDF menggunakan Aspose.PDF untuk Python, dan kemudian mengidentifikasi yang mengandung GoToURIAction. Untuk setiap tautan tersebut, kode mencetak indeks halaman dan URI target.

Ini berguna untuk tugas seperti:

- Audit tautan eksternal dalam PDF
- Mengekstrak URL dokumentasi atau dukungan
- Mendeteksi hyperlink yang rusak atau kedaluwarsa

1. Muat dokumen PDF. Buka file menggunakan ap.Document.
1. Dapatkan semua anotasi tautan dari halaman pertama. Filter anotasi untuk hanya menyertakan yang berjenis AnnotationType.LINK.
1. Periksa tipe dan cast ke LinkAnnotation. Pastikan setiap anotasi memang LinkAnnotation sebelum mengakses propertinya.
1. Periksa tipe aksi tautan. Filter tautan yang menggunakan GoToURIAction (yaitu, tautan ke URL web).
1. Ekstrak dan cetak URI serta indeks halaman. Gunakan .uri untuk mendapatkan tautan eksternal dan .page_index untuk konteks.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
