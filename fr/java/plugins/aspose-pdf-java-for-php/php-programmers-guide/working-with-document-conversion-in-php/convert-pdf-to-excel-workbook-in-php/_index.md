---
title: Convertir un PDF en Classeur Excel en PHP
type: docs
weight: 20
url: fr/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir un PDF en Classeur Excel

Pour convertir un document PDF en classeur Excel en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **PdfToExcel**.

Code PHP

```php
# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# Instancier l'objet ExcelSave Option
$excelsave = new ExcelSaveOptions();

# Enregistrer la sortie au format XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Le document a été converti avec succès" . PHP_EOL;

```

**Télécharger le Code Exécutable**

Téléchargez **Convertir PDF en Classeur Excel (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)