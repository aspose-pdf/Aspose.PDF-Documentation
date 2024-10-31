---
title: Convertir PDF en Excel 
linktitle: Convertir PDF en Excel 
type: docs
weight: 90
url: /androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF pour Android via Java vous permet de convertir des PDF au format Excel. Pendant ce processus, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pour Android via Java API vous permet de rendre vos fichiers PDF aux formats de fichier Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) et [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Nous avons déjà une autre API, connue sous le nom de [Aspose.Cells pour Java](https://products.aspose.com/cells/java), qui offre la possibilité de créer et de manipuler des classeurs Excel existants. Elle offre également la capacité de transformer des classeurs Excel au format PDF.

{{% alert color="primary" %}}

Essayez en ligne.
 Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## Convertir PDF en Excel XLS

Pour convertir des fichiers PDF au format XLS, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est passé comme deuxième argument au constructeur Document.Save(..).

La conversion d'un fichier PDF en format XLSX fait partie de la bibliothèque d'Aspose.PDF pour la version Java 18.6. Afin de convertir des fichiers PDF au format XLSX, vous devez définir le format comme XLSX en utilisant la méthode setFormat() de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Le fragment de code suivant montre comment convertir un fichier PDF en format xls et .xlsx :

```java
public void convertPDFtoExcelSimple() {
        // Ouvrir le document PDF source
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Enregistrer le fichier au format MS document
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir PDF en XLS avec contrôle de colonne

Lors de la conversion d'un PDF en format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne. L'option InsertBlankColumnAtFirst de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Ouvrir le document PDF source
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier un objet ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Enregistrer le fichier au format document MS
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Convertir un PDF en une Feuille de Calcul Excel Unique

Lors de l'exportation d'un fichier PDF avec de nombreuses pages vers XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour s'assurer que toutes les pages sont exportées vers une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Ouvrir le document PDF source
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier l'objet ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Enregistrer la sortie en XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Enregistrer le fichier au format MS Excel
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

Par défaut, Aspose.PDF utilise XML Spreadsheet 2003 pour stocker les données. Afin de convertir les fichiers PDF au format XLSX, Aspose.PDF dispose d'une classe appelée ExcelSaveOptions avec Format. Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est passé en tant que deuxième argument à la méthode Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Charger le document PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier l'objet d'option d'enregistrement Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Enregistrer la sortie en CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Enregistrer le fichier au format CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```