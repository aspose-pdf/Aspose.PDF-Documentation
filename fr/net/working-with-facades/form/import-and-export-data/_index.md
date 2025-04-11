---
title: Importer et Exporter des Données
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/import-and-export-data/
description: Cette section explique comment importer et exporter des données avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "La fonctionnalité d'importation et d'exportation de données dans Aspose.PDF for .NET permet une intégration transparente de la gestion des données documentaires en permettant aux utilisateurs d'importer et d'exporter des données de formulaires PDF en utilisant les formats XML, FDF, XFDF et JSON. Cette fonctionnalité améliore les capacités de gestion des données, facilitant l'automatisation des flux de travail et le maintien de dossiers précis directement à partir de documents PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

[Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) la classe vous permet d'importer des données à partir d'un fichier XML vers le fichier PDF en utilisant la méthode [ImportXml](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.form/importxml/methods/1). Afin d'importer des données à partir de XML, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ImportXml](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/importxml/index) en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/save) de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form). Le code suivant montre comment importer des données à partir d'un fichier XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## Exporter des Données vers XML à partir d'un Fichier PDF

La classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) vous permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode [ExportXml](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportxml). Afin d'exporter des données vers XML, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ExportXml](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportxml) en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et disposer de l'objet Form. Le code suivant montre comment exporter des données vers un fichier XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## Importer des Données à partir de FDF dans un Fichier PDF

La classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) vous permet d'importer des données à partir d'un fichier FDF vers le fichier PDF en utilisant la méthode [ImportFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/importfdf). Afin d'importer des données à partir de FDF, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ImportFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/importfdf) en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/save) de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form). Le code suivant montre comment importer des données à partir d'un fichier FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## Exporter des Données vers FDF à partir d'un Fichier PDF

La classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) vous permet d'exporter des données vers un fichier FDF à partir du fichier PDF en utilisant la méthode [ExportFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportfdf). Afin d'exporter des données vers FDF, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ExportFdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportfdf) en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/save) de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form). Le code suivant montre comment exporter des données vers un fichier FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## Importer des Données à partir de XFDF dans un Fichier PDF

La classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) vous permet d'importer des données à partir d'un fichier XFDF vers le fichier PDF en utilisant la méthode [ImportXfdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/importxfdf). Afin d'importer des données à partir de XFDF, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ImportXfdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/importxfdf) en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/save) de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form). Le code suivant montre comment importer des données à partir d'un fichier XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## Exporter des Données vers XFDF à partir d'un Fichier PDF

La classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) vous permet d'exporter des données vers un fichier XFDF à partir du fichier PDF en utilisant la méthode [ExportXfdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportxfdf). Afin d'exporter des données vers XFDF, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form) puis appeler la méthode [ExportXfdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/exportxfdf) en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/save) de la classe [Form](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/form). Le code suivant montre comment exporter des données vers un fichier XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## Exporter des valeurs des champs vers le fichier JSON

Aspose.Pdf.Facades fournit une API alternative pour travailler avec les champs de formulaire. Ce snippet démontre comment exporter et importer des valeurs de champ en utilisant cette API.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## Importer des valeurs dans les champs à partir du fichier JSON

Ce code snippet démontre comment importer des valeurs dans les champs de formulaire d'un document PDF à partir d'un fichier JSON en utilisant l'API Aspose.Pdf.Facades. L'objet FileStream est utilisé pour gérer le fichier JSON.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```