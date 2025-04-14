---
title: Convertir PDF en Excel dans .NET
linktitle: Convertir PDF en Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: La bibliothèque Aspose.PDF for .NET vous permet de convertir des PDF au format Excel en utilisant C#. Ces formats incluent XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Découvrez la puissante capacité de Aspose.PDF for .NET à convertir sans effort des documents PDF en divers formats Excel, y compris XLS, XLSX, CSV et ODS, en utilisant C#. Cette fonctionnalité permet non seulement la transformation de pages PDF individuelles en feuilles de calcul Excel séparées, mais offre également des options pour des feuilles combinées, offrant ainsi une flexibilité aux utilisateurs pour gérer efficacement leurs données PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1597",
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
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Aperçu

Cet article explique comment **convertir des PDF en formats Excel en utilisant C#**. Il couvre les sujets suivants.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

- [Convertir PDF en XLS](#csharp-pdf-to-xls)
- [Convertir PDF en XLSX](#csharp-pdf-to-xlsx)
- [Convertir PDF en Excel](#csharp-pdf-to-xlsx)
- [Convertir PDF en XLS ayant une seule feuille de calcul](#csharp-pdf-to-excel-single)
- [Convertir PDF en XLSX ayant une seule feuille de calcul](#csharp-pdf-to-excel-single)
- [Convertir PDF en XML Excel](#csharp-pdf-to-excel-xml-2003)
- [Convertir PDF en CSV](#csharp-pdf-to-csv)
- [Convertir PDF en ODS](#csharp-pdf-to-ods)
- [Convertir PDF en XLSM](#csharp-pdf-to-xlsm)

## Conversions PDF en Excel C#

**Aspose.PDF for .NET** prend en charge la fonctionnalité de conversion de fichiers PDF en formats Excel 2007, CSV et SpeadsheetML.

Aspose.PDF for .NET est un composant de manipulation PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLSX). Lors de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

{{% alert color="success" %}}
**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF for .NET vous présente une application en ligne gratuite ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Excel avec l'application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Pour convertir des fichiers PDF en format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/fr/net/aspose.pdf/excelsaveoptions). Un objet de la classe ExcelSaveOptions est passé comme deuxième argument au constructeur Document.Save(..).

Le code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>Convertir PDF en XLS</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions**.
3. Enregistrez-le au format **XLS** en spécifiant l'**extension .xls** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>Convertir PDF en XLSX</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions**.
3. Enregistrez-le au format **XLSX** en spécifiant l'**extension .xlsx** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## Convertir PDF en XLS avec contrôle de colonne

Lors de la conversion d'un PDF en format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne. L'option InsertBlankColumnAtFirst de la classe ExcelSaveOptions est utilisée pour contrôler cette colonne. La valeur par défaut est `false`, ce qui signifie que les colonnes vides ne seront pas insérées.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Convertir PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec de nombreuses pages en XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour s'assurer que toutes les pages sont exportées vers une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>Convertir PDF en XLS ou XLSX avec une seule feuille de calcul</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **MinimizeTheNumberOfWorksheets = true**.
3. Enregistrez-le au format **XLS** ou **XLSX** ayant une seule feuille de calcul en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Convertir en d'autres formats de feuille de calcul

### Convertir en format XML Spreadsheet 2003

Depuis la version 20.8, Aspose.PDF utilise le format de fichier Microsoft Excel Open XML Spreadsheet 2007 par défaut pour stocker des données. Pour convertir des fichiers PDF en format XML Spreadsheet 2003, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/fr/net/aspose.pdf/excelsaveoptions) avec [Format](https://reference.aspose.com/pdf/fr/net/aspose.pdf/excelsaveoptions/properties/format). Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/fr/net/aspose.pdf/excelsaveoptions) est passé comme deuxième argument à la méthode [Document.Save(..)](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save/index).

Le code suivant montre le processus de conversion d'un fichier PDF en format XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>Convertir PDF en format Excel 2003 XML</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. Enregistrez-le au format **XLS - Format Excel 2003 XML** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### Convertir en CSV

La conversion en format CSV s'effectue de la même manière que ci-dessus. Tout ce que vous devez faire est de définir le format approprié.

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>Convertir PDF en CSV</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. Enregistrez-le au format **CSV** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**. 


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### Convertir en ODS

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>Convertir PDF en ODS</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. Enregistrez-le au format **ODS** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**. 


La conversion en format ODS s'effectue de la même manière que tous les autres formats.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

### Convertir en XLSM

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>Convertir PDF en XLSM</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **Format = ExcelSaveOptions.ExcelFormat.XLSM**.
3. Enregistrez-le au format **XLSM** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

La conversion en format XLSM s'effectue de la même manière que tous les autres formats.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in XLSM format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```