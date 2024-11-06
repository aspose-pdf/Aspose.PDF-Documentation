---
title: Importer et exporter des annotations au format XFDF
linktitle: Importer et exporter des annotations au format XFDF
type: docs
weight: 40
url: fr/net/import-export-xfdf/
description: Vous pouvez importer et exporter des annotations au format XFDF avec C# et la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Importer et exporter des annotations au format XFDF",
    "alternativeHeadline": "Méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, import export vers XFDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez importer et exporter des annotations au format XFDF avec C# et la bibliothèque Aspose.PDF pour .NET."
}
</script>
{{% alert color="primary" %}}

XFDF signifie XML Forms Data Format. Il s'agit d'un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé à plusieurs fins, mais dans notre cas, il peut être utilisé pour envoyer ou recevoir des données de formulaire ou des annotations à d'autres ordinateurs ou serveurs, etc., ou pour archiver les données de formulaire ou les annotations. Dans cet article, nous verrons comment Aspose.Pdf.Facades a pris en compte ce concept et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

{{% /alert %}}

**Aspose.PDF pour .NET** est un composant riche en fonctionnalités en ce qui concerne l'édition des documents PDF. Comme nous le savons, XFDF est un aspect important de la manipulation des formulaires PDF, l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF pour .NET a très bien pris en compte cela et a fourni des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF.
La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code suivant vous montre comment exporter des annotations vers un fichier XFDF :

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // Le chemin vers le répertoire des documents.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// Importation d'annotations à partir d'un fichier XFDF
        /// Fichier au format XML Forms Data Format (XFDF) créé par Adobe Acrobat, une application d'auteur de PDF;
        /// stocke les descriptions des éléments de formulaire de page et leurs valeurs, telles que les noms et valeurs pour
        /// les champs de texte ; utilisé pour sauvegarder des données de formulaire qui peuvent être importées dans un document PDF.
        /// Vous pouvez importer des données d'annotation à partir du fichier XFDF vers PDF en utilisant
        /// la méthode ImportAnnotationsFromXfdf dans la classe PdfAnnotationEditor.
        /// </summary>       
   
        public static void ExportAnnotationXFDF()
        {
            // Créer un objet PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // Lier le document PDF à l'éditeur d'annotations
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));
           
            // Exporter les annotations
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
Le prochain extrait de code décrit comment importer des annotations dans un fichier XFDF :

```csharp
public static void ImportAnnotationXFDF()
{
    // Créer un objet PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Créer un nouveau document PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importer l'annotation
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Sauvegarder le PDF de sortie
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Encore une autre façon d'exporter/importer les annotations en une seule fois

Dans le code ci-dessous, une méthode ImportAnnotations permet d'importer des annotations directement depuis un autre document PDF.

```csharp
        /// <summary>
        /// La méthode ImportAnnotations permet d'importer des annotations directement d'un autre document PDF
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // Créer un objet PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // Créer un nouveau document PDF
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // L'éditeur d'annotations permet d'importer des annotations de plusieurs documents PDF,
            // mais dans cet exemple, nous utilisons seulement un.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // Sauvegarder le PDF de sortie
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```

