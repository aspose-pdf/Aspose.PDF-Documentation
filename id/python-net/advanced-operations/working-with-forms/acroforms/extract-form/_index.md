---
title: Ekstrak AcroForm - Ekstrak Data Formulir dari PDF dalam Python
linktitle: Ekstrak AcroForm
type: docs
weight: 30
url: /id/python-net/extract-form/
keywords: ekstrak data formulir dari pdf python
description: Ekstrak formulir dari dokumen PDF Anda dengan pustaka Aspose.PDF untuk Python. Dapatkan nilai dari bidang individu dari file PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ekstrak AcroForm",
    "alternativeHeadline": "Cara mengekstrak AcroForm dari PDF dalam Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, ekstrak acroform",
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
            "https://www.youtube.com/@AsposePDF",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Ekstrak formulir dari dokumen PDF Anda dengan pustaka Aspose.PDF untuk Python. Dapatkan nilai dari bidang individu dari file PDF."
}
</script>


## Ekstrak data dari formulir

### Dapatkan Nilai dari Semua Bidang Dokumen PDF

Untuk mendapatkan nilai dari semua bidang dalam dokumen PDF, Anda perlu menavigasi melalui semua bidang formulir dan kemudian mendapatkan nilainya menggunakan properti Value. Dapatkan setiap bidang dari koleksi Form, dalam tipe bidang dasar yang disebut [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) dan akses ke properti [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Potongan kode Python berikut menunjukkan cara mendapatkan nilai dari semua bidang dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    pdfDocument = ap.Document(input_file)

    # Dapatkan nilai dari semua bidang
    for formField in pdfDocument.form.fields:
        # Analisis nama dan nilai jika perlu
        print("Nama Bidang : " + formField.partial_name)
        print("Nilai : " + str(formField.value))