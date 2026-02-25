---
title: Perbarui Tautan di PDF menggunakan Python
linktitle: Perbarui Tautan
type: docs
weight: 20
url: /id/python-net/update-links/
description: Perbarui tautan dalam PDF secara programatis. Panduan ini membahas cara memperbarui tautan dalam PDF dengan bahasa Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara memperbarui Tautan di PDF
Abstract: Panduan Aspose.PDF untuk Python via .NET tentang memperbarui tautan membimbing pengembang melalui proses memodifikasi perilaku hyperlink dalam dokumen PDF menggunakan Python. Panduan ini menjelaskan cara mengubah tujuan tautan agar mengarah ke halaman tertentu, situs web eksternal, atau bahkan file PDF lain. Dokumentasi juga mencakup cara menyesuaikan tampilan anotasi tautan, termasuk warna teks, dan menyediakan contoh kode praktis untuk setiap skenario. Baik Anda memperbaiki URL yang sudah usang atau meningkatkan navigasi, sumber daya ini menawarkan pendekatan yang jelas dan efisien untuk mengelola tautan secara programatis.
---

## Perbarui Warna Teks LinkAnnotation

Contoh ini menunjukkan cara mendeteksi semua anotasi tautan pada halaman pertama PDF menggunakan Aspose.PDF untuk Python, kemudian menyorot teks di sekitar setiap tautan dengan mengubah warna font menjadi merah. Ini menggunakan TextFragmentAbsorber dengan area yang sedikit diperluas di sekitar persegi panjang tautan untuk menemukan dan memodifikasi teks terdekat.

Ini dapat digunakan untuk:

- Menandai tautan secara visual dalam dokumen
- Meningkatkan aksesibilitas dengan menekankan konten yang ditautkan
- Praproses file PDF sebelum peninjauan atau ekspor

Untuk masing-masing anotasi tautan ini, skrip mengambil batas persegi panjangnya dan sedikit memperluas wilayah tersebut untuk mencakup teks di sekitarnya, memungkinkan identifikasi visual yang lebih luas. Kemudian skrip menerapkan TextFragmentAbsorber pada area yang diperluas itu untuk mengekstrak fragmen teks apa pun yang berada di dalamnya. Fragmen yang terdeteksi diubah warna fontnya menjadi merah, sehingga menandai teks di sekitarnya untuk penekanan dan peninjauan. Setelah semua pembaruan diterapkan, dokumen yang telah dimodifikasi disimpan ke jalur keluaran, mempertahankan anotasi yang disorot dan teks yang terkait.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Perbarui Border

Skrip fokus pada halaman pertama dokumen dan menyaring semua anotasi, memilih hanya yang berjenis LINK—biasanya mewakili elemen interaktif, seperti hyperlink atau pemicu navigasi. Untuk tiap anotasi tautan ini, kode mengubahnya menjadi tipe LinkAnnotation dan memperbarui properti warnanya menjadi merah, secara visual menyorotnya agar menonjol dari konten lainnya. Setelah semua anotasi tautan dimodifikasi, dokumen yang diperbarui disimpan ke lokasi keluaran yang ditentukan, mempertahankan gaya baru.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Perbarui Tujuan Web

Setelah jalur-jalur ditetapkan, dokumen asli dimuat menggunakan pustaka Aspose.PDF, membuat isinya dapat diakses untuk dimodifikasi. Skrip kemudian fokus pada halaman pertama dokumen, menyaring semua anotasi dan memilih hanya yang berjenis tautan, biasanya mewakili area yang dapat diklik atau hyperlink. Untuk menghindari kesalahan tipe dan memastikan penanganan yang aman, setiap anotasi diperiksa dengan is_assignable dan kemudian diubah menjadi tipe LinkAnnotation yang sesuai. Jika tautan terkait dengan GoToURIAction, yang berarti mengarah ke alamat web, skrip memperbarui URI tersebut untuk mengarahkan pengguna ke "https://www.google.com". Akhirnya, setelah semua perubahan yang diinginkan diterapkan, dokumen yang dimodifikasi disimpan ke jalur keluaran yang ditentukan.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
