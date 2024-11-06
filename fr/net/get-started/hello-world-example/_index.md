---
title: Exemple de Hello World en utilisant le langage C#
linktitle: Exemple Hello World
type: docs
weight: 40
url: fr/net/hello-world-example/
description: Cet échantillon démontre comment créer un document PDF simple avec le texte Hello World en utilisant Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exemple de Hello World en utilisant le langage C#",
    "alternativeHeadline": "Exemple Aspose.PDF en C#",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, génération de documents",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet échantillon démontre comment créer un document PDF simple avec le texte Hello World en utilisant Aspose.PDF",
    "articleBody": "Un exemple de \"Hello World\" est traditionnellement utilisé pour introduire les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.\nAspose.PDF pour .NET est une API PDF riche en fonctionnalités qui permet aux développeurs d'intégrer la création, la manipulation et la conversion de documents PDF dans leurs applications .NET. Elle prend en charge le travail avec de nombreux formats de fichiers populaires, y compris PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et les formats de fichiers image. Dans cet article, nous créons un document PDF contenant le texte \"Hello World !\". Après avoir installé Aspose.PDF pour .NET dans votre environnement, vous pouvez exécuter l'échantillon de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.\nLe fragment de code suivant suit ces étapes :\n1. Instancier un objet Document\n2. Ajouter une Page à l'objet document\n3. Créer un TextFragment\n4. Ajouter TextFragment à la collection de Paragraphes de la page\n5. Sauvegarder le document PDF résultant\nLe fragment de code suivant est un programme Hello World pour montrer le fonctionnement de l'API Aspose.PDF pour .NET."
}
</script>
Un exemple "Hello World" est traditionnellement utilisé pour présenter les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF pour .NET est une API PDF riche en fonctionnalités qui permet aux développeurs d'intégrer la création, la manipulation et la conversion de documents PDF dans leurs applications .NET. Elle prend en charge de nombreux formats de fichiers populaires incluant PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et les formats de fichiers image. Dans cet article, nous créons un document PDF contenant le texte "Hello World!". Après avoir installé Aspose.PDF pour .NET dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Ce fragment de code suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à l'objet document
1.
1. Ajoutez TextFragment à la collection [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page
1. [Enregistrez](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) le document PDF résultant

Le code suivant est un programme Hello World pour montrer le fonctionnement de l'API Aspose.PDF pour .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Initialise l'objet document
            Document document = new Document();
            // Ajoute une page
            Page page = document.Pages.Add();
            // Ajoute du texte à la nouvelle page
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Enregistre le PDF mis à jour
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
