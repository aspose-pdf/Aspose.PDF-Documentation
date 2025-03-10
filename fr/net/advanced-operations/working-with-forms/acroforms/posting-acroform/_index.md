---
title: Publication des données AcroForm
linktitle: Publication des AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/posting-acroform-data/
description: Vous pouvez importer et exporter des données de formulaire vers un fichier XML avec l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Posting AcroForm Data",
    "alternativeHeadline": "Post AcroForm Data",
    "abstract": "Présentation d'une nouvelle fonctionnalité puissante dans Aspose.PDF for .NET, la capacité de publier des données AcroForm. Cette fonctionnalité permet aux développeurs non seulement de créer et d'éditer des AcroForms, mais aussi d'importer et d'exporter sans effort des données de formulaire vers des fichiers XML, améliorant ainsi les capacités de traitement et de stockage des données au sein des applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Posting AcroForm Data, Import and Export Form Data, Aspose.PDF for .NET, AcroForm Fields, Submit Button, External Web Page Integration, Form Data Posting, XML File Handling, FieldType.Text, Database Saving",
    "wordcount": "400",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Vous pouvez importer et exporter des données de formulaire vers un fichier XML avec l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF for .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm est un type important de document PDF. Vous pouvez non seulement créer et éditer un AcroForm en utilisant [l'espace de noms Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), mais aussi importer et exporter des données de formulaire vers un fichier XML. L'espace de noms Aspose.Pdf.Facades dans Aspose.PDF for .NET vous permet de mettre en œuvre une autre fonctionnalité d'AcroForm, qui vous aide à publier des données AcroForm sur une page Web externe. Cette page Web lit ensuite les variables de publication et utilise ces données pour un traitement ultérieur. Cette fonctionnalité est utile dans les cas où vous ne souhaitez pas seulement conserver les données dans le fichier PDF, mais que vous souhaitez les envoyer à votre serveur et ensuite les sauvegarder dans une base de données, etc.

{{% /alert %}}

## Détails de mise en œuvre

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Dans cet article, nous avons essayé de créer un AcroForm en utilisant [l'espace de noms Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace). Nous avons également ajouté un bouton de soumission et défini son URL cible. Les extraits de code suivants vous montrent comment créer le formulaire et ensuite recevoir les données publiées sur la page Web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAcroFormWithFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create an instance of FormEditor class and bind input and output pdf files
    using (var editor = new Aspose.Pdf.Facades.FormEditor(dataDir + "input.pdf", dataDir + "output.pdf"))
    {
        // Create AcroForm fields - I have created only two fields for simplicity
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

        // Add a submit button and set target URL
        editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

        // Save PDF document
        editor.Save();
    }
}
```

{{% alert color="primary" %}}

L'extrait de code suivant vous montre comment recevoir les valeurs publiées sur la page Web cible. Dans cet exemple, j'ai utilisé une page nommée Show.aspx, et j'ai ajouté une simple ligne de code dans la méthode de chargement de la page.

{{% /alert %}}

```csharp
// Show the posted values on the target web page
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>