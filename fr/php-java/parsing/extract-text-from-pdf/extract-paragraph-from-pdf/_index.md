---
title: Extraire un paragraphe d'un PDF 
linktitle: Extraire un paragraphe
type: docs
weight: 20
url: fr/php-java/extract-paragraph-from-pdf/
description: Cet article décrit comment utiliser ParagraphAbsorber - un outil spécial dans Aspose.PDF pour extraire du texte à partir de documents PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire du texte d'un document PDF sous forme de paragraphes

Nous pouvons obtenir du texte à partir d'un document PDF en recherchant un texte particulier (en utilisant du "texte brut" ou des "expressions régulières") d'une seule page ou de l'ensemble du document, ou nous pouvons obtenir le texte complet d'une seule page, d'une plage de pages ou de l'ensemble du document. Cependant, dans certains cas, vous devez extraire des paragraphes d'un document PDF ou du texte sous forme de paragraphes. Nous avons implémenté une fonctionnalité pour rechercher des sections et des paragraphes dans le texte des pages de documents PDF. Nous avons introduit la classe ParagraphAbsorber (comme TextFragmentAbsorber et TextAbsorber), qui peut être utilisée pour extraire des paragraphes de documents PDF.

### Itérer à travers la collection de paragraphes et obtenir leur texte

```php

// Ouvrir un fichier PDF existant
$document = new Document($inputFile);
// Instancier ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "Paragraphe " . $j++ . " de la section " . $i++ . " sur la page" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// Enregistrer le texte extrait dans le fichier de sortie.
file_put_contents($outputFile, $responseData);
```