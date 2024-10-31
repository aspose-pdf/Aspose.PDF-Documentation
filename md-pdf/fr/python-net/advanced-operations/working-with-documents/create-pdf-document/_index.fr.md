---

title: Comment créer un PDF en utilisant Python  
linktitle: Créer un document PDF  
type: docs  
weight: 10  
url: /python-net/create-pdf-document/  
description: Créez et formatez le document PDF avec Aspose.PDF pour Python via .NET.  
lastmod: "2023-04-12"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  

<script type="application/ld+json">  
{  
    "@context": "https://schema.org",  
    "@type": "TechArticle",  
    "headline": "Comment créer un PDF en utilisant Python",  
    "alternativeHeadline": "Créer un document PDF à partir de zéro via Python",  
    "author": {  
        "@type": "Person",  
        "name":"Anastasiia Holub",  
        "givenName": "Anastasiia",  
        "familyName": "Holub",  
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"  
    },  
    "genre": "génération de document pdf",  
    "keywords": "pdf, python, dotnet, créer un document pdf",  
    "wordcount": "302",  
    "proficiencyLevel":"Débutant",  
    "publisher": {  
        "@type": "Organization",  
        "name": "Équipe de documentation Aspose.PDF",  
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
    "url": "/python-net/create-pdf-document/",  
    "mainEntityOfPage": {  
        "@type": "WebPage",  
        "@id": "/python-net/create-pdf-document/"  
    },  
    "dateModified": "2022-02-04",  
    "description": "Créez et formatez le document PDF avec Aspose.PDF pour Python via .NET."  
}  
</script>  


**Aspose.PDF pour Python via .NET** est une API de manipulation de PDF qui permet aux développeurs de créer, charger, modifier et convertir des fichiers PDF directement à partir d'applications Python pour .NET avec seulement quelques lignes de code.

## Comment créer un fichier PDF simple

Pour créer un PDF en utilisant Python via .NET avec Aspose.PDF, vous pouvez suivre ces étapes :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à la collection [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) de l'objet Document
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à la collection [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page
1. Enregistrez le document PDF résultant

```python

    import aspose.pdf as ap

    # Initialiser l'objet document
    document = ap.Document()
    # Ajouter une page
    page = document.pages.add()
    # Ajouter du texte à la nouvelle page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Enregistrer le PDF mis à jour
    document.save(output_pdf)
```