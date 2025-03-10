---
title: Conversion d'un XML au format FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/converting-an-xml-to-fdf-format/
description: Cette section explique comment vous pouvez convertir un XML au format FDF avec FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "La fonctionnalité permet aux développeurs de convertir sans effort des fichiers XML au format FDF en utilisant la classe FormDataConverter dans Aspose.PDF for .NET. Cette fonctionnalité améliore l'échange de données entre les formats de documents, facilitant la gestion efficace des données de formulaire dans les applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) prend très bien en charge les AcroForms. Il prend également en charge l'importation et l'exportation de données de formulaire vers différents formats de fichiers comme FDF, XFDF et XML. Cependant, parfois un développeur doit convertir un format en un autre. Dans cet article, nous examinerons la fonctionnalité qui nous permet de convertir un format FDF en XML.

{{% /alert %}}

## Détails de mise en œuvre

FDF signifie Forms Data Format, et un fichier FDF contient les valeurs de formulaire sous forme de paires clé/valeur. Nous savons également qu'un fichier XML contient les valeurs sous forme de balises. Où, principalement la clé est représentée comme le nom de la balise et la valeur est représentée comme la valeur à l'intérieur de cette balise. Maintenant, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre la flexibilité de convertir un format de fichier XML en format FDF.

Utilisez la classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) à cet effet. Cette classe fournit différentes méthodes pour convertir un format de données en un autre. Cet article montre comment utiliser une méthode, ConvertXmlToFdf(..), qui prend un fichier FDF comme entrée ou flux source et l'enregistre au format XML. Le code suivant montre comment convertir un fichier FDF en un fichier XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```