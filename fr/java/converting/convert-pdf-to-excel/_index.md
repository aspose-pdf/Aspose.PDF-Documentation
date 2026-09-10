---
title: Convertir un PDF en Excel en Java
linktitle: Convertir un PDF en Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: Découvrez comment convertir des fichiers PDF en Excel en Java avec Aspose.PDF, y compris la sortie XML Spreadsheet 2003, XLSX, XLSM, CSV et ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en Excel en Java
Abstract: Cet article explique comment convertir des fichiers PDF en formats compatibles Excel avec Aspose.PDF pour Java. Il couvre la sortie XML Spreadsheet 2003, XLSX, XLSM, CSV et ODS, ainsi que les options d'insertion de colonnes vides et de réduction du nombre de feuilles de calcul.
---
Aspose.PDF pour Java peut exporter du contenu PDF vers plusieurs formats de feuilles de calcul avec différentes options de mise en page. Utilisez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) pour choisir le format de classeur cible et contrôler la façon dont le contenu de la page est mappé dans les feuilles de calcul et les colonnes.


## 
Convertir un PDF en XML Excel 2003



Utilisez cet exemple lorsque le contenu PDF doit être exporté au format de feuille de calcul XML Excel 2003.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) et définissez son format sur `XMLSpreadSheet2003`.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le PDF chargé soit sérialisé dans le schéma XML Excel 2003.

1. 
Enregistrez le fichier de sortie converti.


```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en XLSX



Utilisez cet exemple lorsque le contenu PDF doit être converti au format Excel 2007+ XLSX.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) et définissez son format sur `XLSX`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que la mise en page PDF soit exportée en tant que classeur Office Open XML.

1. 
Enregistrez le fichier de feuille de calcul de sortie.


```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en XLSX avec le contrôle des colonnes



Utilisez cet exemple lorsque la gestion des colonnes doit être ajustée lors de la conversion PDF vers Excel.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) pour la sortie `XLSX`.

1. 
Activez `setInsertBlankColumnAtFirst(true)` lorsqu'une colonne de début supplémentaire est nécessaire pour améliorer la mise en page de la feuille de calcul produite à partir du PDF.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et écrivez le fichier XLSX converti.


```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en une seule feuille de calcul Excel

Utilisez cet exemple lorsque toutes les pages PDF doivent être exportées dans une seule feuille de calcul.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) pour l'exportation `XLSX`.

1. 
Activez `setMinimizeTheNumberOfWorksheets(true)` pour que plusieurs pages PDF soient regroupées en moins de feuilles de calcul.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez le fichier de sortie XLSX.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF en XLSM



Utilisez cet exemple lorsque la sortie PDF doit être enregistrée en tant que classeur Excel prenant en charge les macros.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) et définissez le format sur `XLSM`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF soit exporté vers un conteneur de classeur prenant en charge les macros.
1. Enregistrez le fichier XLSM.


```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en CSV



Utilisez cet exemple lorsque le contenu tabulaire PDF doit être exporté au format CSV.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) et définissez le format sur `CSV`.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu du PDF soit aplati en sortie de texte séparé par des virgules.

1. 
Enregistrez le fichier CSV généré.


```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en ODS



Utilisez cet exemple lorsque le contenu PDF doit être exporté au format de feuille de calcul OpenDocument.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`ExcelSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) et définissez le format sur `ODS`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le PDF soit exporté au format de feuille de calcul OpenDocument.

1. 
Enregistrez le fichier ODS converti.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
