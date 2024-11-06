---
title: Convertir PDF en format DOC ou DOCX en PHP
type: docs
weight: 10
url: fr/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF en DOC ou DOCX

Pour convertir un document PDF en format DOC ou DOCX en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **PdfToDoc**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# Enregistrer le fichier de sortie concaténé (le document cible)
$pdf->save($dataDir . "output.doc");

print "Le document a été converti avec succès";

```

**Télécharger le Code Exécutable**

Téléchargez **Convertir PDF en DOC ou DOCX (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)