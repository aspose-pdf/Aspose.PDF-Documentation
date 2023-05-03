---
title: Add watermark to PDF using Python
linktitle: Add watermark
type: docs
weight: 40
url: /python-net/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using Python",
    "alternativeHeadline": "How to add watermark to PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf,python, add watermark",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "This article explains the features of working with artifacts and getting watermarks in PDFs using Python."
}
</script>

**Aspose.PDF for Python via .NET** allows adding watermarks to your PDF document using Artifacts. Please check this article to resolve your task.

In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) and [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

In order to get all artifacts on a particular page, the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) class contains following properties:

**contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
**form** – Gets an artifact’s XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
**image** – Gets an artifact’s image (if an image is presents, else null).
**text** – Gets an artifact’s text.
**rectangle** – Gets an position of an artifact on the page.
**rotation** – Gets an artifact’s rotation (in degrees, positive value indicates counter-clockwise rotation).
**opacity** – Gets an artifact’s opacity. Possible values are in the range 0…1, where 1 is completely opaque.

## Programming Samples: How To Add Watermark On PDF Files

The following code snippet shows how to get each watermark on the first page of a PDF file with Python.

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
    "name": "Aspose.PDF for Python via .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
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
