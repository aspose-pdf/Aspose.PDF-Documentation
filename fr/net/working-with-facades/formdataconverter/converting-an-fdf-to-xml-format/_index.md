---
title: Conversion d'un FDF au format XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/converting-an-fdf-to-xml-format/
description: Cette section explique comment vous pouvez convertir un FDF au format XML avec la classe FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Découvrez comment convertir efficacement des fichiers FDF au format XML en utilisant la classe FormDataConverter dans Aspose.PDF for .NET. Cette fonctionnalité simplifie la gestion des données en transformant les paires clé/valeur d'un FDF en une structure XML facilement lisible, améliorant ainsi l'interopérabilité et la gestion des données dans vos applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

Le [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace dans [Aspose.PDF for .NET](/pdf/net/) prend très bien en charge les AcroForms. Il prend également en charge l'importation et l'exportation de données de formulaire vers différents formats de fichiers comme FDF, XFDF et XML. Cependant, parfois, les développeurs peuvent avoir besoin de convertir un format en un autre. Cet article examine la fonctionnalité qui convertit FDF en XML.

{{% /alert %}}

## Détails de mise en œuvre

FDF signifie Forms Data Format, et un fichier FDF contient les valeurs de formulaire sous forme de paires clé/valeur. Nous savons également qu'un fichier XML contient les valeurs sous forme de balises. Où, principalement, la clé est représentée comme le nom de la balise et la valeur est représentée comme la valeur à l'intérieur de cette balise. Maintenant, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nous offre la flexibilité de convertir un format de fichier FDF en un format XML.

Nous pouvons utiliser la classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) à cet effet. Cette classe nous fournit différentes méthodes pour convertir un format de données en un autre format. Dans cet article, nous allons juste utiliser une méthode nommée [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Cette méthode prend un fichier FDF comme entrée ou flux source et l'enregistre au format XML.

Le code suivant vous montre comment convertir un fichier FDF en un fichier XML :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```