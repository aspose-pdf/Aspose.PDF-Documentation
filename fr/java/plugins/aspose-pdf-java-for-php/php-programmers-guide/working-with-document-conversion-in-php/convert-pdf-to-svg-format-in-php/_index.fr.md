---
title: Convertir PDF en format SVG en PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF en SVG

Pour convertir un PDF en format SVG en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **PdfToSvg**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# instancier un objet de SvgSaveOptions
$save_options = new SvgSaveOptions();

# ne pas compresser l'image SVG dans une archive Zip
$save_options->CompressOutputToZipArchive = false;

# Enregistrer la sortie au format XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "Le document a été converti avec succès" . PHP_EOL;

```

**Télécharger le code en cours d'exécution**

Téléchargez **Convertir PDF en format SVG (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)