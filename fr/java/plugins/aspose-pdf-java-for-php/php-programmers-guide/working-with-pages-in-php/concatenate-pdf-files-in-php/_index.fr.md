---
title: Concaténer des fichiers PDF en PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concaténer des fichiers PDF

Pour concaténer des fichiers PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **ConcatenatePdfFiles**.

Code PHP

```php

# Ouvrir le document cible
$pdf1 = new Document($dataDir . 'input1.pdf');

# Ouvrir le document source
$pdf2 = new Document($dataDir . 'input2.pdf');

# Ajouter les pages du document source au document cible
$pdf1->getPages()->add($pdf2->getPages());

# Sauvegarder le fichier de sortie concaténé (le document cible)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "Le nouveau document a été enregistré, veuillez vérifier le fichier de sortie" . PHP_EOL;

```

**Télécharger le code d'exécution**

Téléchargez **Concaténer des fichiers PDF (Aspose.PDF)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)