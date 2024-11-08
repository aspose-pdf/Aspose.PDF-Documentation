title: Travailler avec les En-têtes dans PDF
type: docs
weight: 70
url: /fr/php-java/working-with-headings/
lastmod: "2024-06-05"
description: Créez une numérotation dans l'en-tête de votre document PDF en utilisant PHP. Aspose.PDF pour PHP via Java offre différents types de styles de numérotation.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Appliquer un Style de Numérotation dans l'En-tête

Les en-têtes sont des parties importantes de tout document. Les rédacteurs essaient toujours de rendre les en-têtes plus visibles et significatifs pour leurs lecteurs. S'il y a plus d'un en-tête dans un document, un rédacteur a plusieurs options pour organiser ces en-têtes. L'une des approches les plus courantes pour organiser les en-têtes est d'écrire les en-têtes en Style de Numérotation.

Aspose.PDF pour PHP via Java offre de nombreux styles de numérotation prédéfinis. Ces styles de numérotation prédéfinis sont stockés dans une énumération, NumberingStyle. Les valeurs prédéfinies de l'énumération NumberingStyle et leurs descriptions sont données ci-dessous:

|**Types d'En-têtes**|**Description**|
| :- | :- |

|NumeralsArabic|Type arabe, par exemple, 1,1.1,...|
|NumeralsRomanUppercase|Type romain majuscule, par exemple, I,I.II, ...|
|NumeralsRomanLowercase|Type romain minuscule, par exemple, i,i.ii, ...|
|LettersUppercase|Type anglais majuscule, par exemple, A,A.B, ...|
|LettersLowercase|Type anglais minuscule, par exemple, a,a.b, ...|
La propriété [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) de la classe [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) est utilisée pour définir les styles de numérotation des en-têtes.

Le code source, pour obtenir la sortie montrée dans la figure ci-dessus, est donné ci-dessous dans l'exemple.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("Liste 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("Liste 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("la valeur, à la date d'effet du plan, des biens à distribuer en vertu du plan au titre de chaque autorisé");
    $heading3->setStyle(NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```