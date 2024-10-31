---
title: Tambahkan watermark ke PDF menggunakan Python
linktitle: Tambahkan watermark
type: docs
weight: 40
url: /python-net/add-watermarks/
description: Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan Python secara programatis.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan watermark ke PDF menggunakan Python",
    "alternativeHeadline": "Cara menambahkan watermark ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf,python, tambahkan watermark",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "AS",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan Python."
}
</script>


**Aspose.PDF untuk Python via .NET** memungkinkan penambahan watermark ke dokumen PDF Anda menggunakan Artifacts. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Untuk bekerja dengan artifacts, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) dan [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

Untuk mendapatkan semua artifacts pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) memiliki properti Artifacts. Topik ini menjelaskan cara bekerja dengan artifacts dalam file PDF.

## Bekerja dengan Artifacts

Kelas [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) memiliki properti berikut:

**contents** – Mendapatkan koleksi operator internal artifact. Jenis yang didukung adalah System.Collections.ICollection.
**form** – Mendapatkan XForm dari artifact (jika XForm digunakan). Watermark, header, dan footer artifacts mengandung XForm yang menunjukkan semua konten artifact.

**image** – Mendapatkan gambar dari artifact (jika ada gambar, jika tidak null).
**text** – Mendapatkan teks dari sebuah artefak.  
**rectangle** – Mendapatkan posisi sebuah artefak pada halaman.  
**rotation** – Mendapatkan rotasi sebuah artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).  
**opacity** – Mendapatkan opasitas sebuah artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 sepenuhnya tidak transparan.

## Contoh Pemrograman: Cara Menambahkan Tanda Air Pada File PDF

Cuplikan kode berikut menunjukkan cara mendapatkan setiap tanda air pada halaman pertama dari sebuah file PDF dengan Python.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>