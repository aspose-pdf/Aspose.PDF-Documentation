---
title: Extraire le texte des tampons
type: docs
weight: 60
url: fr/php-java/extract-text-from-stamps/
---

## Extraire le texte des annotations de tampon

Aspose.PDF pour PHP via Java vous permet d'extraire le texte des annotations de tampon. Afin d'extraire le texte des annotations de tampon dans un PDF, les étapes suivantes peuvent être utilisées.

1. Charger le document PDF
1. Obtenir la page souhaitée du document
1. Créer une nouvelle instance de la classe StampAnnotation
1. Créer une nouvelle instance de la classe AnnotationSelector et lui passer l'annotation de tampon
1. Accepter le sélecteur d'annotations sur la page
1. Obtenir les annotations de tampon sélectionnées
1. Créer une nouvelle instance de la classe TextAbsorber
1. Obtenir la première annotation de tampon
1. Obtenir l'apparence normale de l'annotation de tampon
1. Visiter l'apparence en utilisant le text absorber
1. Obtenir le texte extrait du text absorber
1. Fermer le document

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```