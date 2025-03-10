---
title: Convertir des fichiers PDF en formats PDF/A
linktitle: Convertir des fichiers PDF en formats PDF/A
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /fr/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Apprenez à convertir un fichier PDF au format PDF/A à des fins d'archivage en utilisant Aspose.PDF dans .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PDF/A formats",
    "alternativeHeadline": "Effortless PDF to PDF/A Conversion with Validation in C#",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET permet une conversion transparente de fichiers PDF standards en divers formats conformes à PDF/A, y compris PDF/A-1b, PDF/A-2u et PDF/A-3a. Cette fonctionnalité garantit non seulement la conformité aux normes PDF/A grâce à une validation complète, mais permet également l'attachement de fichiers supplémentaires et la substitution de polices manquantes, améliorant ainsi l'intégrité et l'accessibilité des documents. Explorez les capacités robustes d'Aspose.PDF pour des conversions PDF/A efficaces et fiables.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1064",
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
    "url": "/net/convert-pdf-to-pdfa/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-pdfa/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

**Aspose.PDF for .NET** vous permet de convertir un fichier PDF en un fichier PDF conforme à <abbr title="Portable Document Format / A">PDF/A</abbr>. Avant de le faire, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous suivons Adobe Preflight et veraPDF pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre « représentation » de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF car Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier en utilisant la méthode Convert de la classe Document. Avant de convertir le PDF en fichier conforme à PDF/A, validez le PDF en utilisant la méthode Validate. Le résultat de la validation est stocké dans un fichier XML et ce résultat est également passé à la méthode Convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération ConvertErrorAction.

{{% alert color="success" %}}
**Essayez de convertir PDF en PDF/A en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to PDF/A avec l'application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Normes prises en charge
Nous prenons en charge les normes suivantes : PDF/A-1b, PDF/A-1a, PDF/A-2b, PDF/A-2u, PDF/A-2a, PDF/A-3b, PDF/A-3u, PDF/A-3a, PDF/A-4, PDF/A-4e, PDF/A-4f.

## Convertir un fichier PDF en PDF/A-1b

Le code suivant montre comment convertir des fichiers PDF en PDF conforme à PDF/A-1b.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
    
    // Save PDF document
    document.Save(dataDir + "PDFToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf");

    // Validate PDF for PDF/A-1a
    document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
}
```
{{< /tab >}}
{{< /tabs >}}

## Convertir un fichier PDF en PDF/A-3b

Aspose.PDF for .NET prend également en charge la fonctionnalité de conversion d'un fichier PDF en format PDF/A-3b.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document, log file is omitted
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA3b_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document, log file is omitted
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA3b_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Convertir un fichier PDF en PDF/A-4

Aspose.PDF for .NET prend également en charge la fonctionnalité de conversion d'un fichier PDF en format PDF/A-4.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);
    
        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

    // Convert to the PDF/A-4 format
    document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA4_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ajouter une pièce jointe à un fichier PDF/A

Si vous avez besoin d'attacher des fichiers à un document conforme à PDF/A, nous vous recommandons d'utiliser une valeur PDF_A_3A de l'énumération Aspose.PDF.PdfFormat.
PDF/A-3a est le format qui offre la fonctionnalité d'attacher n'importe quel format de fichier en tant que pièce jointe à un fichier conforme à PDF/A.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Setup new file to be added as attachment
        using (var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file"))
        {
            // Add attachment to document's attachment collection
            document.EmbeddedFiles.Add(fileSpecification);

            // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
            document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

            // Save PDF document
            document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Setup new file to be added as attachment
    using var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file");

    // Add attachment to document's attachment collection
    document.EmbeddedFiles.Add(fileSpecification);

    // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
    document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Remplacer les polices manquantes par des polices alternatives

Selon les normes PDF/A, les polices doivent être intégrées dans un document PDF/A. Cependant, si les polices ne sont pas intégrées dans le document source et n'existent pas sur la machine, la conversion PDF/A échoue. Dans ce cas, il est nécessaire de substituer les polices manquantes par des polices alternatives existant sur la machine. Les polices manquantes peuvent être substituées en utilisant la classe SimpleFontSubsitution lors de la conversion de PDF en PDF/A.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // During the conversion, the missing font will be replaced with the substitution one
        document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // During the conversion, the missing font will be replaced with the substitution one
    document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}