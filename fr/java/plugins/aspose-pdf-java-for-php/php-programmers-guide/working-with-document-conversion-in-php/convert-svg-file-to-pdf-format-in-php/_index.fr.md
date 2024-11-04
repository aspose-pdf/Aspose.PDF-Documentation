---
title: Convertir un fichier SVG en format PDF en PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir SVG en PDF

Pour convertir un fichier SVG en format PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **SvgToPdf**.

Code PHP

```php
# Instancier un objet LoadOption en utilisant l'option de chargement SVG
$options = new SvgLoadOptions();

# Créer un objet document
$pdf = new Document($dataDir . 'Example.svg', $options);

# Sauvegarder le résultat au format XLS
$pdf->save($dataDir . "SVG.pdf");

print "Le document a été converti avec succès";

```

**Télécharger le code en cours d'exécution**

Téléchargez **Convertir SVG en PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)