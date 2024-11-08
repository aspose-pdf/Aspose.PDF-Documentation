---
title: Convertir PDF en Excel 
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
keywords: convertir PDF en Excel en utilisant Java, convertir PDF en XLS en utilisant Java, convertir PDF en XLSX en utilisant Java, exporter un tableau de PDF en Excel en Java
description: Aspose.PDF pour Java vous permet de convertir des PDF en format Excel en utilisant Java. Pendant ce processus, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF pour l'API Java vous permet de rendre vos fichiers PDF aux formats de fichiers Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) et [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Nous avons déjà une autre API, connue sous le nom de [Aspose.Cells pour Java](https://products.aspose.com/cells/java), qui offre la capacité de créer et manipuler des classeurs Excel existants. Elle offre également la capacité de transformer des classeurs Excel en format PDF.

{{% alert color="primary" %}}

**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF pour Java vous présente l'application en ligne gratuite ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to Excel avec application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF en Excel XLS

Pour convertir des fichiers PDF au format XLS, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est passé comme deuxième argument à la méthode Document.Save(..).

La conversion d'un fichier PDF en format XLSX fait partie de la bibliothèque Aspose.PDF pour Java version 18.6. Afin de convertir des fichiers PDF en format XLSX, vous devez définir le format en tant que XLSX en utilisant la méthode setFormat() de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Le code suivant montre comment convertir un fichier PDF en format xls et .xlsx :

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // Le chemin vers le répertoire des documents.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Charger le document PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Enregistrer la sortie au format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## Convertir PDF en XLS avec colonne de contrôle

Lorsque vous convertissez un PDF au format XLS, une colonne vide est ajoutée au fichier de sortie comme première colonne. Dans la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions), l'option InsertBlankColumnAtFirst est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Charger le document PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Enregistrer la sortie au format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Convertir un PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec beaucoup de pages vers XLS, chaque page est exportée vers une feuille différente dans le fichier Excel.
 Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour assurer que toutes les pages soient exportées sur une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Charger le document PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Enregistrer la sortie au format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Convertir au format XLSX

Par défaut, Aspose.PDF utilise XML Spreadsheet 2003 pour stocker les données. Afin de convertir des fichiers PDF au format XLSX, Aspose.PDF dispose d'une classe appelée ExcelSaveOptions avec Format. Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est passé comme second argument à la méthode Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Charger le document PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Enregistrer la sortie au format XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```