---
title: Extraire du Texte de Toutes les Pages d'un Document PDF en PHP
type: docs
weight: 30
url: fr/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extraire du Texte de Toutes les Pages

Pour extraire le texte de toutes les pages d'un document PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **ExtractTextFromAllPages**.
Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# créer un objet TextAbsorber pour extraire le texte
$text_absorber = new TextAbsorber();

# accepter l'absorbeur pour toutes les pages
$pdf->getPages()->accept($text_absorber);

# Afin d'extraire le texte d'une page spécifique du document, nous devons spécifier la page particulière en utilisant son index contre la méthode accept(..).
# accepter l'absorbeur pour une page PDF particulière
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obtenir le texte extrait
$extracted_text = $text_absorber->getText();

# créer un writer et ouvrir le fichier
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# écrire une ligne de texte dans le fichier
# tw.WriteLine(extractedText);
# fermer le flux
$writer->close();

print "Texte extrait avec succès. Vérifiez le fichier de sortie." . PHP_EOL;

```


**Télécharger le Code Exécutable**

Téléchargez **Extraire le Texte de Toutes les Pages (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)