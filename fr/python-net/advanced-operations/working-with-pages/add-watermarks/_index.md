---
title: Ajouter un filigrane à un PDF en utilisant Python
linktitle: Ajouter un filigrane
type: docs
weight: 40
url: fr/python-net/add-watermarks/
description: Cet article explique les fonctionnalités de travail avec les artefacts et l'obtention de filigranes dans les PDFs en utilisant Python de manière programmatique.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un filigrane à un PDF en utilisant Python",
    "alternativeHeadline": "Comment ajouter un filigrane à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf,python, ajouter un filigrane",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
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
    "description": "Cet article explique les fonctionnalités de travail avec les artefacts et l'obtention de filigranes dans les PDFs en utilisant Python."
}
</script>


**Aspose.PDF for Python via .NET** permet d'ajouter des filigranes à votre document PDF en utilisant des artefacts. Veuillez consulter cet article pour résoudre votre tâche.

Pour travailler avec les artefacts, Aspose.PDF dispose de deux classes : [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) et [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

Pour obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la propriété Artifacts. Ce sujet explique comment travailler avec les artefacts dans les fichiers PDF.

## Travailler avec les artefacts

La classe [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) contient les propriétés suivantes :

**contents** – Obtient une collection d'opérateurs internes d'artefact. Son type pris en charge est System.Collections.ICollection.
**form** – Obtient le XForm d'un artefact (si XForm est utilisé). Les filigranes, en-têtes et pieds de page contiennent un XForm qui montre tous les contenus d'artefact.

**image** – Obtient l'image d'un artefact (si une image est présente, sinon null).
**text** – Obtient le texte d'un artefact.  
**rectangle** – Obtient la position d'un artefact sur la page.  
**rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens antihoraire).  
**opacity** – Obtient l'opacité d'un artefact. Les valeurs possibles sont dans la plage 0…1, où 1 est complètement opaque.

## Exemples de Programmation : Comment Ajouter un Filigrane sur des Fichiers PDF

L'extrait de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec Python.

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
    "name": "Aspose.PDF pour Python via .NET Library",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour Python",
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