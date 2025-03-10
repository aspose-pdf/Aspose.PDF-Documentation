---
title: Importer et Exporter des Annotations vers XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/import-export-annotations/
description: Cette section explique comment importer et exporter des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante pour importer et exporter des annotations vers XFDF, améliorant les capacités de manipulation des PDF. Cette fonctionnalité permet aux utilisateurs de transférer sélectivement des données d'annotation au format XML Forms Data Format, permettant une intégration et un archivage sans faille pour une meilleure gestion des documents. Avec des méthodes dédiées pour spécifier les types d'annotations, les utilisateurs peuvent gérer efficacement leurs annotations PDF avec précision.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

XFDF signifie XML Forms Data Format. C'est un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé à de nombreuses fins différentes, mais dans notre cas, il peut être utilisé pour envoyer ou recevoir des données de formulaire ou des annotations vers d'autres ordinateurs ou serveurs, etc., ou il peut être utilisé pour archiver les données de formulaire ou les annotations. Dans cet article, nous allons voir comment Aspose.Pdf.Facades a pris ce concept en considération et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

## Importation et Exportation des Annotations vers XFDF

[Aspose.PDF for .NET](/pdf/net/) est un composant riche en fonctionnalités lorsqu'il s'agit d'éditer des documents PDF. Comme nous le savons, XFDF est un aspect important de la manipulation des formulaires PDF, le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) a très bien pris cela en compte et a fourni des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF. La méthode [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) fournit la fonctionnalité pour exporter des annotations d'un document PDF vers un fichier XFDF, tandis que la méthode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) vous permet d'importer des annotations à partir d'un fichier XFDF existant. Pour importer ou exporter des annotations, nous devons spécifier les types d'annotations. Nous pouvons spécifier ces types sous forme d'énumération et ensuite passer cette énumération comme argument à l'une de ces méthodes. De cette manière, seules les annotations des types spécifiés seront importées ou exportées vers un fichier XFDF.

Le code suivant montre comment importer des annotations dans un fichier XFDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

Le code suivant décrit comment importer/exporter des annotations vers un fichier XFDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

De cette manière, seules les annotations des types spécifiés seront importées ou exportées vers un fichier XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```