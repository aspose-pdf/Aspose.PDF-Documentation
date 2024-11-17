---
title: Convertir PDF en Excel en .NET
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: La bibliothèque Aspose.PDF pour .NET vous permet de convertir des PDF en format Excel en utilisant C#. Ces formats incluent XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Vue d'ensemble

Cet article explique comment **convertir des PDF en formats Excel en utilisant C#**. Il couvre les sujets suivants.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

_Format_ : **XLS**

- [C# PDF en XLS](#csharp-pdf-to-xls)
- [C# Convertir PDF en XLS](#csharp-pdf-to-xls)
- [C# Comment convertir un fichier PDF en XLS](#csharp-pdf-to-xls)

_Format_ : **XLSX**

- [C# PDF en XLSX](#csharp-pdf-to-xlsx)
- [C# Convertir PDF en XLSX](#csharp-pdf-to-xlsx)
- [C# Comment convertir un fichier PDF en XLSX](#csharp-pdf-to-xlsx)
- [C# Comment convertir un fichier PDF en XLSX](#csharp-pdf-to-xlsx)

_Format_ : **Excel**

- [C# PDF en Excel](#csharp-pdf-to-xlsx)
- [C# PDF en Excel XLS](#csharp-pdf-to-xls)
- [C# PDF en Excel XLSX](#csharp-pdf-to-xlsx)

_Format_ : **Feuille Excel unique**

- [C# Convertir PDF en XLS avec une seule feuille de calcul](#csharp-pdf-to-excel-single)
- [C# Convertir PDF en XLSX avec une seule feuille de calcul](#csharp-pdf-to-excel-single)

_Format_ : **Format de feuille de calcul XML 2003**

- [C# PDF en Excel XML](#csharp-pdf-to-excel-xml-2003)
- [C# Convertir PDF en feuille de calcul Excel XML](#csharp-pdf-to-excel-xml-2003)

_Format_ : **CSV**

- [C# PDF en CSV](#csharp-pdf-to-csv)
- [C# Convertir PDF en CSV](#csharp-pdf-to-csv)
- [C# Comment convertir un fichier PDF en CSV](#csharp-pdf-to-csv)

_Format_ : **ODS**

- [C# PDF en ODS](#csharp-pdf-to-ods)
- [C# Convertir PDF en ODS](#csharp-pdf-to-ods)
- [C# Comment convertir un fichier PDF en ODS](#csharp-pdf-to-ods)

## C# Conversions de PDF en Excel

**Aspose.PDF for .NET** prend en charge la fonctionnalité de conversion des fichiers PDF en formats Excel 2007, CSV et SpeadsheetML.
**Aspose.PDF pour .NET** prend en charge la fonctionnalité de conversion des fichiers PDF aux formats Excel 2007, CSV et SpeadsheetML.

Aspose.PDF pour .NET est un composant de manipulation de PDF, nous avons introduit une fonctionnalité qui permet de rendre un fichier PDF en classeur Excel (fichiers XLSX). Lors de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

{{% alert color="success" %}}
**Essayez de convertir un PDF en Excel en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Excel avec application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Pour convertir des fichiers PDF au format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
Pour convertir des fichiers PDF au format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF possède une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF pour .NET.

<a name="csharp-pdf-to-xls"><strong>Étapes : Convertir PDF en XLS en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions**.
3. Sauvegardez-le au format **XLS** en spécifiant l'**extension .xls** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Étapes : Convertir PDF en XLSX en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions**.
3. Sauvegardez-le au format **XLSX** en spécifiant l'**extension .xlsx** en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**

```csharp
// Code for converting PDF to XLS or XLSX
```
## Convertir PDF en XLS avec contrôle de colonne

Lors de la conversion d'un PDF en format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne. L'option InsertBlankColumnAtFirst de la classe ExcelSaveOptions est utilisée pour contrôler cette colonne. La valeur par défaut est `false`, ce qui signifie que les colonnes vides ne seront pas insérées.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Charger le document PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Instancier l'objet ExcelSave Option
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Sauvegarder le résultat au format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Convertir PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec de nombreuses pages vers XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour s'assurer que toutes les pages soient exportées vers une seule et même feuille dans le fichier Excel final, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

<a name="csharp-pdf-to-excel-single"><strong>Étapes : Convertir PDF en feuille XLS ou XLSX unique en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **MinimizeTheNumberOfWorksheets = true**.
3. Enregistrez-le au format **XLS** ou **XLSX** avec une seule feuille en appelant la méthode **Document.Save()** et en lui passant **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Charger le document PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instancier l'objet ExcelSave Option
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Sauvegarder le résultat au format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Convertir vers d'autres formats de feuille de calcul

### Convertir au format XML Spreadsheet 2003

Depuis la version 20.8, Aspose.PDF utilise par défaut le format de fichier Microsoft Excel Open XML Spreadsheet 2007 pour stocker les données. Pour convertir des fichiers PDF au format XML Spreadsheet 2003, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) avec [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) est passé comme second argument à la méthode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Étapes : Convertir un PDF en format Excel 2003 XML en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2.
2.
3. Sauvegardez-le au format **XLS - Format XML Excel 2003** en appelant la méthode **Document.Save()** et en passant **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Charger le document PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instancier l'objet ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Sauvegarder la sortie au format XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Convertir en CSV

La conversion au format CSV se fait de la même manière que ci-dessus. Tout ce dont vous avez besoin est de définir le format approprié.

<a name="csharp-pdf-to-csv"><strong>Étapes : Convertir PDF en CSV en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2.
2.
3. Enregistrez-le au format **CSV** en appelant la méthode **Document.Save()** et en passant **ExcelSaveOptions**.


```csharp
 // Instancier l'objet ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Convertir en ODS

<a name="csharp-pdf-to-ods"><strong>Étapes : Convertir PDF en ODS en C#</strong></a>

1. Créez une instance de l'objet **Document** avec le document PDF source.
2. Créez une instance de **ExcelSaveOptions** avec **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Enregistrez-le au format **ODS** en appelant la méthode **Document.Save()** et en passant **ExcelSaveOptions**.


La conversion au format ODS s'effectue de la même manière que pour tous les autres formats.

```csharp
 // Instancier l'objet ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## Voir aussi 

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_ : **Excel**
- [Code C# PDF vers Excel](#csharp-pdf-to-xlsx)
- [API C# PDF vers Excel](#csharp-pdf-to-xlsx)
- [API C# PDF vers Excel](#csharp-pdf-to-xlsx)
- [C# PDF vers Excel Programmé](#csharp-pdf-to-xlsx)
- [Bibliothèque C# PDF vers Excel](#csharp-pdf-to-xlsx)
- [C# Enregistrer PDF en tant qu'Excel](#csharp-pdf-to-xlsx)
- [C# Générer Excel à partir de PDF](#csharp-pdf-to-xlsx)
- [C# Créer Excel à partir de PDF](#csharp-pdf-to-xlsx)
- [Convertisseur C# PDF vers Excel](#csharp-pdf-to-xlsx)

_Format_ : **XLS**
- [Code C# PDF vers XLS](#csharp-pdf-to-xls)
- [API C# PDF vers XLS](#csharp-pdf-to-xls)
- [C# PDF vers XLS Programmé](#csharp-pdf-to-xls)
- [Bibliothèque C# PDF vers XLS](#csharp-pdf-to-xls)
- [C# Enregistrer PDF en tant que XLS](#csharp-pdf-to-xls)
- [C# Générer XLS à partir de PDF](#csharp-pdf-to-xls)
- [C# Créer XLS à partir de PDF](#csharp-pdf-to-xls)
- [Convertisseur C# PDF vers XLS](#csharp-pdf-to-xls)

_Format_ : **XLSX**
- [Code C# PDF vers XLSX](#csharp-pdf-to-xlsx)
- [API C# PDF vers XLSX](#csharp-pdf-to-xlsx)
- [C# PDF vers XLSX Programmé](#csharp-pdf-to-xlsx)
- [Bibliothèque C# PDF vers XLSX](#csharp-pdf-to-xlsx)
- [C# Enregistrer PDF en tant que XLSX](#csharp-pdf-to-xlsx)
- [C# Générer XLSX à partir de PDF](#csharp-pdf-to-xlsx)
- [C# Générer XLSX à partir de PDF](#csharp-pdf-to-xlsx)
- [C# Créer XLSX à partir de PDF](#csharp-pdf-to-xlsx)
- [C# Convertisseur PDF en XLSX](#csharp-pdf-to-xlsx)

_Format_ : **CSV**
- [C# Code PDF en CSV](#csharp-pdf-to-csv)
- [C# API PDF en CSV](#csharp-pdf-to-csv)
- [C# PDF en CSV Programmation](#csharp-pdf-to-csv)
- [C# Bibliothèque PDF en CSV](#csharp-pdf-to-csv)
- [C# Enregistrer PDF comme CSV](#csharp-pdf-to-csv)
- [C# Générer CSV à partir de PDF](#csharp-pdf-to-csv)
- [C# Créer CSV à partir de PDF](#csharp-pdf-to-csv)
- [C# Convertisseur PDF en CSV](#csharp-pdf-to-csv)

_Format_ : **ODS**
- [C# Code PDF en ODS](#csharp-pdf-to-ods)
- [C# API PDF en ODS](#csharp-pdf-to-ods)
- [C# PDF en ODS Programmation](#csharp-pdf-to-ods)
- [C# Bibliothèque PDF en ODS](#csharp-pdf-to-ods)
- [C# Enregistrer PDF comme ODS](#csharp-pdf-to-ods)
- [C# Générer ODS à partir de PDF](#csharp-pdf-to-ods)
- [C# Créer ODS à partir de PDF](#csharp-pdf-to-ods)
- [C# Convertisseur PDF en ODS](#csharp-pdf-to-ods)
