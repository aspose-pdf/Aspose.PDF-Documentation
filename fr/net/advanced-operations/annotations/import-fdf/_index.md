---
title: Importer des annotations au format FDF dans un PDF via C#
linktitle: Importer des annotations au format FDF dans un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/import-fdf/
description: Utilisez les méthodes existantes Form.ImportFdf() ou PdfAnnotationEditor.ImportAnnotationsFromFdf() pour importer des annotations au format FDF dans un PDF avec Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Importez des annotations au format FDF dans des fichiers PDF sans effort en utilisant Aspose.PDF for .NET, améliorant vos capacités de gestion de PDF. Avec les méthodes Form.ImportFdf() et PdfAnnotationEditor.ImportAnnotationsFromFdf(), vous pouvez intégrer sans effort les données de formulaire et les commentaires provenant de fichiers FDF légers dans vos documents PDF, rationalisant ainsi les processus de soumission de données et d'annotation.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

FDF (Forms Data Format) est un format de fichier qui stocke et transmet des données de formulaire et des annotations dans des documents PDF. C'est une version PDF légère qui contient uniquement les valeurs des champs de formulaire ou des commentaires, sans le contenu complet du fichier PDF original. Les fichiers FDF sont souvent utilisés lors de la soumission de données de formulaire à un serveur, ou lors de l'échange d'annotations sans avoir besoin d'envoyer l'intégralité du fichier PDF. Ils peuvent être importés dans un PDF pour remplir des champs de formulaire ou appliquer des commentaires.

{{% /alert %}}

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfannotationeditor/) contient des méthodes pour travailler avec l'importation d'annotations depuis un fichier FDF. La méthode [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) fournit la fonctionnalité pour importer des annotations d'un document FDF dans un fichier PDF.

De plus, la [classe Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/) inclut la méthode [Form.ImportFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/importfdf/) - importe le contenu des champs du fichier FDF et les place dans le nouveau PDF.

Le code suivant montre comment importer des annotations au format FDF dans un PDF avec la méthode Form.ImportFdf() :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

Le code suivant montre comment importer des annotations au format FDF dans un PDF avec la méthode PdfAnnotationEditor.ImportAnnotationsFromFdf() :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```