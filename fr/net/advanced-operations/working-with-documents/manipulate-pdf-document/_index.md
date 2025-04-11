---
title: Manipuler un document PDF en C#
linktitle: Manipuler un document PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/manipulate-pdf-document/
description: Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A, comment travailler avec la table des matières, comment définir la date d'expiration d'un PDF, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document in C#",
    "alternativeHeadline": "Enhanced PDF Manipulation Features in C# Library",
    "abstract": "Découvrez les puissantes capacités de manipulation des documents PDF en C#, y compris la validation pour les normes PDF/A, la possibilité de créer et de personnaliser des tables des matières, et de définir des dates d'expiration pour les documents. Cette fonctionnalité améliore non seulement la gestion des documents, mais garantit également la conformité aux normes de l'industrie, ce qui est essentiel pour les développeurs à la recherche de solutions robustes de gestion des PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "manipulate PDF, C#, validate PDF/A, TOC, set PDF expiry date, flatten fillable PDF, Aspose.PDF, PDF generation progress, customize page numbers, PDF encryption",
    "wordcount": "2736",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2025-04-04",
    "description": "Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A, comment travailler avec la table des matières, comment définir la date d'expiration d'un PDF, etc."
}
</script>

## **Manipuler un document PDF en C#**

## Valider un document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A-1a ou PDF/A-1b, utilisez la méthode Validate de la classe [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis de l'énumération [PdfFormat](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pdfformat) : PDF_A_1A ou PDF_A_1B.

{{% alert color="primary" %}}

Le format XML de sortie est un format personnalisé d'Aspose. L'XML contient une collection de balises nommées Problème ; chaque balise contient les détails d'un problème particulier. L'attribut ObjectID de la balise Problème représente l'ID de l'objet particulier auquel ce problème est lié. L'attribut Clause représente une règle correspondante dans la spécification PDF.

{{% /alert %}}

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant vous montre comment valider un document PDF pour PDF/A-1A.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1aStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "validation-result-A1A.xml", Aspose.Pdf.PdfFormat.PDF_A_1A);
    }
}
```

Le code suivant vous montre comment valider un document PDF pour PDF/A-1b.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1bStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1b
        document.Validate(dataDir + "validation-result-A1B.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```

{{% alert color="primary" %}}

Aspose.PDF for .NET peut être utilisé pour déterminer si le document chargé est un PDF valide et aussi [s'il est crypté ou non](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Afin d'étendre davantage les capacités de la classe Document, la propriété *IsPdfaCompliant* a été ajoutée pour déterminer si le fichier d'entrée est conforme au PDF/A et une propriété nommée *PdfaFormat* pour identifier le format PDF/A a été introduite.

{{% /alert %}}

## Travailler avec la table des matières

### Ajouter une table des matières à un PDF existant

L'API Aspose.PDF vous permet d'ajouter une table des matières soit lors de la création d'un PDF, soit à un fichier existant. La classe ListSection dans l'espace de noms Aspose.Pdf.Generator vous permet de créer une table des matières lors de la création d'un PDF à partir de zéro. Pour ajouter des titres, qui sont des éléments de la table des matières, utilisez la classe Aspose.Pdf.Generator.Heading.

Pour ajouter une table des matières à un fichier PDF existant, utilisez la classe Heading dans l'espace de noms Aspose.PDF. L'espace de noms Aspose.Pdf peut à la fois créer de nouveaux fichiers PDF et manipuler des fichiers PDF existants. Pour ajouter une table des matières à un PDF existant, utilisez l'espace de noms Aspose.PDF. Le code suivant montre comment créer une table des matières à l'intérieur d'un fichier PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTOCToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Get access to the first page of PDF file
        var tocPage = document.Pages.Insert(1);

        // Create an object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocPage.TocInfo = tocInfo;

        // Create string objects which will be used as TOC elements
        string[] titles = { "First page", "Second page", "Third page", "Fourth page" };

        for (int i = 0; i < 2; i++)
        {
            // Create Heading object
            var heading = new Aspose.Pdf.Heading(1);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);

            // Specify the destination page for the heading object
            heading.DestinationPage = document.Pages[i + 2];

            // Destination page
            heading.Top = document.Pages[i + 2].Rect.Height;

            // Destination coordinate
            segment.Text = titles[i];

            // Add heading to the page containing TOC
            tocPage.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Définir un TabLeaderType différent pour différents niveaux de table des matières

Aspose.PDF permet également de définir un TabLeaderType différent pour différents niveaux de table des matières. Vous devez définir la propriété LineDash de FormatArray avec la valeur appropriée de l'énumération TabLeaderType comme suit.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithCustomFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set LeaderType
        tocInfo.LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 30;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Define the format of the four levels list by setting the left margins
        // and text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Left = 0;
        tocInfo.FormatArray[0].Margin.Right = 30;
        tocInfo.FormatArray[0].LineDash = Aspose.Pdf.Text.TabLeaderType.Dot;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 10;
        tocInfo.FormatArray[1].Margin.Right = 30;
        tocInfo.FormatArray[1].LineDash = Aspose.Pdf.Text.TabLeaderType.None;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].Margin.Left = 20;
        tocInfo.FormatArray[2].Margin.Right = 30;
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;
        tocInfo.FormatArray[3].Margin.Left = 30;
        tocInfo.FormatArray[3].Margin.Right = 30;
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            heading.TocPage = tocPage;
            segment.Text = "Sample Heading " + level;
            heading.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial Unicode MS");

            // Add the heading into Table Of Contents.
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Masquer les numéros de page dans la table des matières

Si vous ne souhaitez pas afficher les numéros de page, avec les titres dans la table des matières, vous pouvez utiliser la propriété [IsShowPageNumbers](https://reference.aspose.com/pdf/fr/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) de la classe [TOCInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf/tocinfo) comme faux. Veuillez consulter le code suivant pour masquer les numéros de page dans la table des matières :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithHiddenPageNumbers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Hide page numbers in TOC
        tocInfo.IsShowPageNumbers = false;

        // Define the format of the four levels list by setting the left margins and
        // text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Right = 0;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 30;
        tocInfo.FormatArray[1].TextState.Underline = true;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            segment.Text = "this is heading of level " + level;
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Personnaliser les numéros de page lors de l'ajout de la table des matières

Il est courant de personnaliser la numérotation des pages dans la table des matières lors de l'ajout de la table des matières dans un document PDF. Par exemple, nous pouvons avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans ce cas, Aspose.PDF for .NET fournit la propriété PageNumbersPrefix de la classe TocInfo qui peut être utilisée pour personnaliser les numéros de page comme montré dans l'exemple de code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizePageNumbersAddingToC()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CustomizePageNumbersAddingToC.pdf"))
    {
        // Get access to first page of PDF file
        Page tocPage = document.Pages.Insert(1);

        // Create object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocInfo.PageNumbersPrefix = "P";
        tocPage.TocInfo = tocInfo;

        // Loop through the pages to create TOC entries
        for (int i = 1; i < document.Pages.Count; i++)
        {
            // Create Heading object
            var heading2 = new Aspose.Pdf.Heading(1);
            var segment2 = new Aspose.Pdf.Text.TextSegment();
            heading2.TocPage = tocPage;
            heading2.Segments.Add(segment2);

            // Specify the destination page for heading object
            heading2.DestinationPage = document.Pages[i + 1];

            // Destination page
            heading2.Top = document.Pages[i + 1].Rect.Height;

            // Destination coordinate
            segment2.Text = "Page " + i.ToString();

            // Add heading to page containing TOC
            tocPage.Paragraphs.Add(heading2);
        }

        // Save PDF document
        document.Save(dataDir + "CustomizePageNumbersAddingToC_out.pdf");
    }
}
```

## Comment définir la date d'expiration d'un PDF

Nous appliquons des privilèges d'accès sur les fichiers PDF afin qu'un certain groupe d'utilisateurs puisse accéder à des fonctionnalités/objets particuliers des documents PDF. Afin de restreindre l'accès au fichier PDF, nous appliquons généralement un cryptage et nous pouvons avoir besoin de définir une expiration du fichier PDF, afin que l'utilisateur accédant/visualisant le document reçoive un message valide concernant l'expiration du fichier PDF.

Pour accomplir l'exigence ci-dessus, nous pouvons utiliser l'objet *JavascriptAction*. Veuillez jeter un œil au code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add text fragment to paragraphs collection of page object
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World..."));

        // Create JavaScript object to set PDF expiry date
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(
            "var year=2017;" +
            "var month=5;" +
            "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
            "expiry = new Date(year, month);" +
            "if (today.getTime() > expiry.getTime())" +
            "app.alert('The file is expired. You need a new one.');"
        );

        // Set JavaScript as PDF open action
        document.OpenAction = javaScript;

        // Save PDF Document
        document.Save(dataDir + "SetExpiryDate_out.pdf");
    }
}
```

## Déterminer la progression de la génération de fichiers PDF

Un client nous a demandé d'ajouter une fonctionnalité qui permet aux développeurs de déterminer la progression de la génération de fichiers PDF. Voici la réponse à cette demande.

Le champ [CustomerProgressHandler](https://reference.aspose.com/pdf/fr/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) de la classe [DocSaveOptions](https://reference.aspose.com/pdf/fr/net/aspose.pdf/docsaveoptions) vous permet de déterminer comment se déroule la génération du PDF. Le gestionnaire a les types suivants :

- DocSaveOptions.ConversionProgessEventHandler.
- DocSaveOptions.ProgressEventHandlerInfo.
- DocSaveOptions.ProgressEventType.

Les extraits de code ci-dessous montrent comment utiliser CustomerProgressHandler.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineProgress()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Create DocSaveOptions instance and set custom progress handler
        var saveOptions = new Aspose.Pdf.DocSaveOptions();
        saveOptions.CustomProgressHandler = new Aspose.Pdf.UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

        // Save PDF Document
        document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
    }
}

// Method to handle progress and display it on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## Aplatir un PDF remplissable

Les documents PDF incluent souvent des formulaires avec des widgets remplissables interactifs tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour les rendre non modifiables à des fins d'application diverses, nous devons aplatir le fichier PDF. Aspose.PDF fournit la fonction d'aplatir votre PDF en C# avec juste quelques lignes de code :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Fillable PDF
        if (document.Form.Fields.Count() > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

## Analyser un document PDF pour des mises à jour incrémentielles
Pour vérifier si un document a été mis à jour de manière incrémentielle, utilisez la méthode `HasIncrementalUpdate` de la classe [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Cette méthode analyse le fichier PDF et renvoie une valeur booléenne indiquant si des mises à jour incrémentielles ont été détectées. Notez que lorsqu'un document est enregistré en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/save/#save) sans paramètre, il est enregistré de manière incrémentielle.

Le code C# suivant démontre comment utiliser la méthode `HasIncrementalUpdate` :

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Check for incremental updates
        bool updatedIncrementally = document.HasIncrementalUpdate();

        // Output the result
        if (updatedIncrementally)
        {
            Console.WriteLine("This document has been incrementally updated.");
        }
        else
        {
            Console.WriteLine("This document has no incremental updates.");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Check for incremental updates
    bool updatedIncrementally = document.HasIncrementalUpdate();

    // Output the result
    if (updatedIncrementally)
    {
        Console.WriteLine("This document has been incrementally updated.");
    }
    else
    {
        Console.WriteLine("This document has no incremental updates.");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

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