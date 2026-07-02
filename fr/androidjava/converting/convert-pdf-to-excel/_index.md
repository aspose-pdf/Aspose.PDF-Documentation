---
title: Convertir PDF en Excel
linktitle: Convertir PDF en Excel
type: docs
weight: 90
url: /fr/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java vous permet de convertir le PDF au format Excel. À cet égard, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'API Aspose.PDF for Android via Java vous permet de convertir vos fichiers PDF en Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) et [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) formats de fichiers. Nous disposons déjà d’une autre API, connue sous le nom de [Aspose.Cells for Java](https://products.aspose.com/cells/java), qui offre la capacité de créer et de manipuler des classeurs Excel existants. Il offre également la capacité de transformer des classeurs Excel au format PDF.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et visualiser les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Convertir le PDF en Excel XLS

Pour convertir des fichiers PDF au format XLS, Aspose.PDF possède une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objet de la [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) la classe est passée comme deuxième argument au constructeur Document.Save(..) . 

La conversion d'un fichier PDF en format XLSX fait partie de la bibliothèque d'Aspose.PDF pour Java version 18.6. Afin de convertir des fichiers PDF en format XLSX, vous devez définir le format comme XLSX en utilisant la méthode setFormat() de [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Classe.

L'extrait de code suivant montre comment convertir un fichier PDF en format xls et .xlsx :

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir PDF en XLS avec colonne de contrôle

Lors de la conversion d'un PDF au format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne. Le in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) L'option class InsertBlankColumnAtFirst est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir le PDF en une seule feuille de calcul Excel 

Lors de l'exportation d'un fichier PDF contenant de nombreuses pages vers XLS, chaque page est exportée vers une feuille différente du fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour garantir que toutes les pages soient exportées vers une seule feuille du fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Convertir au format XLSX 

Par défaut, Aspose.PDF utilise XML Spreadsheet 2003 pour stocker les données. Afin de convertir les fichiers PDF au format XLSX, Aspose.PDF possède une classe appelée ExcelSaveOptions avec Format. Un objet de la [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) classe est passée comme deuxième argument à la méthode Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
