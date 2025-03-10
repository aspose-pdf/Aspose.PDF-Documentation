---
title: Extraire des données d'AcroForm en utilisant C#
linktitle: Extraire des données d'AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données des champs de formulaire à partir de fichiers PDF. Apprenez à extraire des données d'AcroForms et à les enregistrer au format JSON, XML ou FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "Découvrez la nouvelle fonctionnalité dans Aspose.PDF for .NET qui simplifie l'extraction des données des champs de formulaire à partir des AcroForms dans les documents PDF. Avec la possibilité d'exporter des données au format JSON, XML, FDF et XFDF, les utilisateurs peuvent gérer efficacement les données de formulaire tout en tirant parti d'exemples de code concis pour une intégration transparente dans les applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Extraire les champs de formulaire d'un document PDF

Tout en vous permettant de générer des champs de formulaire et de remplir des champs de formulaire, Aspose.PDF for .NET facilite l'extraction des données des champs de formulaire ou des informations sur les champs de formulaire à partir de fichiers PDF.

Dans le code d'exemple ci-dessous, nous démontrons comment itérer à travers chaque page d'un PDF pour extraire des informations sur tous les AcroForms dans le PDF ainsi que les valeurs des champs de formulaire. Ce code d'exemple suppose que vous ne connaissez pas le nom des champs de formulaire à l'avance.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données. Consultez le bas de cet article pour un code d'exemple sur la façon d'utiliser cette fonction.

## Récupérer la valeur du champ de formulaire par titre

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire de la collection Form de l'objet Document. Cet exemple sélectionne un TextBoxField et récupère sa valeur en utilisant la propriété Value.

## Extraire les champs de formulaire d'un document PDF vers JSON

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## Extraire des données au format XML d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données au format XML, vous devez créer un objet de la classe Form, puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et disposer de l'objet Form. Le code suivant vous montre comment exporter des données vers un fichier XML.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## Exporter des données vers FDF à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier FDF à partir du fichier PDF en utilisant la méthode ExportFdf. Pour exporter des données au format FDF, vous devez créer un objet de la classe Form, puis appeler la méthode ExportFdf en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form. Le code suivant vous montre comment exporter des données vers un fichier FDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## Exporter des données vers XFDF à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XFDF à partir du fichier PDF en utilisant la méthode ExportXfdf. Pour exporter des données au format XFDF, vous devez créer un objet de la classe Form, puis appeler la méthode ExportXfdf en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form. Le code suivant vous montre comment exporter des données vers un fichier XFDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```