---
title: Importer et exporter des annotations vers XFDF
linktitle: Importer et exporter des annotations vers XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/import-export-xfdf/
description: Vous pouvez importer et exporter des annotations au format XFDF avec C# et la bibliothèque Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Effortless XFDF Annotation Import and Export",
    "abstract": "La nouvelle fonctionnalité d'importation et d'exportation pour XFDF dans la bibliothèque Aspose.PDF for .NET améliore la gestion des documents PDF en permettant le transfert fluide des données d'annotations. Cette fonctionnalité permet aux utilisateurs d'intégrer facilement des annotations à partir de fichiers XFDF et de les exporter, favorisant ainsi un échange de données efficace et des capacités d'archivage pour les formulaires PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Annotations, Export Annotations, XFDF Format, Aspose.PDF for .NET, PdfAnnotationEditor, ImportAnnotationFromXfdf, ExportAnnotationsXfdf, PDF Forms Manipulation",
    "wordcount": "670",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Vous pouvez importer et exporter des annotations au format XFDF avec C# et la bibliothèque Aspose.PDF for .NET."
}
</script>

{{% alert color="primary" %}}

XFDF signifie XML Forms Data Format. C'est un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé à de nombreuses fins différentes, mais dans notre cas, il peut être utilisé pour envoyer ou recevoir des données de formulaire ou des annotations vers d'autres ordinateurs ou serveurs, etc., ou il peut être utilisé pour archiver les données de formulaire ou les annotations. Dans cet article, nous allons voir comment Aspose.Pdf.Facades a pris ce concept en considération et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** est un composant riche en fonctionnalités lorsqu'il s'agit d'éditer des documents PDF. Comme nous le savons, XFDF est un aspect important de la manipulation des formulaires PDF, l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF for .NET a bien pris cela en compte et a fourni des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF. La méthode [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) fournit la fonctionnalité pour exporter des annotations d'un document PDF vers un fichier XFDF, tandis que la méthode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) vous permet d'importer des annotations à partir d'un fichier XFDF existant. Pour importer ou exporter des annotations, nous devons spécifier les types d'annotations. Nous pouvons spécifier ces types sous forme d'énumération et ensuite passer cette énumération comme argument à l'une de ces méthodes. De cette manière, seules les annotations des types spécifiés seront importées ou exportées vers un fichier XFDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant vous montre comment exporter des annotations vers un fichier XFDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAnnotationsToXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationDemo1.pdf");

        // Define the annotation types to export
        var annotType = new Aspose.Pdf.Annotations.AnnotationType[] { Aspose.Pdf.Annotations.AnnotationType.Line, Aspose.Pdf.Annotations.AnnotationType.Square };

        // Export annotations to XFDF file
        using (var fileStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
        }
    }
}
```

Le code suivant décrit comment importer des annotations à partir d'un fichier XFDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Define the export file name
            var exportFileName = dataDir + "exportannotations.xfdf";

            // Import annotations from the XFDF file
            annotationEditor.ImportAnnotationsFromXfdf(exportFileName);

            // Save PDF document
            document.Save(dataDir + "ImportAnnotationFromXfdf_out.pdf");
        }
    }
}
```

## Une autre façon d'exporter/importer des annotations en une seule fois

Dans le code ci-dessous, une méthode ImportAnnotations permet d'importer des annotations directement à partir d'un autre document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var documentFrom = new Aspose.Pdf.Document(dataDir + "some_doc.pdf"))
    {
        // Create PDF document
        using (var documentTo = new Aspose.Pdf.Document())
        {
            // Add page
            var page = documentTo.Pages.Add();

            // Export/import
            using (var ms = new MemoryStream())
            {
                documentFrom.ExportAnnotationsToXfdf(ms);
                documentTo.ImportAnnotationsFromXfdf(ms);
            }

            // Save PDF document
            documentTo.Save(dataDir + "AnnotationDemo3_out.pdf");
        }
    }
}
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