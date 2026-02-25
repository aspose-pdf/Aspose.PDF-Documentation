---
title: Menggunakan Anotasi Tautan dalam PDF
linktitle: Anotasi Tautan
type: docs
weight: 70
url: /id/python-net/link-annotations/
description: Aspose.PDF untuk Python via .NET memungkinkan Anda Menambahkan, Mengambil, dan Menghapus Anotasi Tautan dari dokumen PDF Anda.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## Tambahkan Anotasi Tautan ke file PDF yang ada

[Links](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) adalah anotasi yang membuka URL atau berpindah ke posisi tertentu dalam dokumen yang sama atau dokumen eksternal ketika Anda mengklik.

Anotasi Tautan adalah area persegi panjang yang dapat ditempatkan di mana saja pada halaman. Setiap tautan memiliki aksi PDF yang terkait dengannya. Aksi ini dijalankan ketika pengguna mengklik area tautan ini.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Tautan ke file PDF menggunakan contoh nomor telepon:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### Dapatkan Anotasi Tautan

Silakan coba menggunakan cuplikan kode berikut untuk Mendapatkan [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) dari dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Hapus Anotasi Tautan

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini kita perlu menemukan dan menghapus semua anotasi tautan pada halaman pertama. Setelah itu kami akan menyimpan dokumen dengan anotasi yang dihapus.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
