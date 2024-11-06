---
title: Convertir PDF en Microsoft Excel 
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: fr/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
keywords: convertir PDF en Excel en utilisant PHP, convertir PDF en XLS en utilisant PHP, convertir PDF en XLSX en utilisant PHP, exporter tableau de PDF vers Excel en PHP.
description: Aspose.PDF pour PHP vous permet de convertir PDF en format Excel en utilisant PHP. Pendant cela, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF pour PHP API vous permet de rendre vos fichiers PDF aux formats de fichiers Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) et [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Nous avons déjà une autre API, connue sous le nom de [Aspose.Cells pour PHP via Java](https://products.aspose.com/cells/php-java), qui offre la capacité de créer et manipuler des classeurs Excel existants. Elle offre également la capacité de transformer les classeurs Excel en format PDF.

{{% alert color="primary" %}}

**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Excel avec App Gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF en Excel XLS

Pour convertir des fichiers PDF au format XLS, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) est passé en tant que deuxième argument à la méthode Document.Save(..).

La conversion d'un fichier PDF en format XLSX fait partie de la bibliothèque d'Aspose.PDF pour la version PHP 18.6. Afin de convertir des fichiers PDF en format XLSX, vous devez définir le format comme XLSX en utilisant la méthode setFormat() de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Les extraits de code suivants montrent comment convertir un fichier PDF en formats XLS et XLSX :

```php
// Charger le document PDF d'entrée en utilisant la classe Document.
$document = new Document($inputFile);

// Créer une instance de la classe ExcelSaveOptions pour spécifier les options de sauvegarde.
$saveOption = new ExcelSaveOptions();

// Définir le format de sortie sur XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// Définir le format de sortie sur XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// Enregistrer le document PDF en tant que fichier Excel en utilisant les options de sauvegarde spécifiées.
$document->save($outputFile, $saveOption);
```