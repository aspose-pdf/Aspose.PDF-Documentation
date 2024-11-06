---
title: PDF Sticky Annotations 
linktitle: Sticky Annotation
type: docs
weight: 50
url: fr/php-java/sticky-annotations/
description: Ce sujet concerne les annotations adhésives, comme exemple nous montrons l'Annotation Filigrane dans le texte. Il est utilisé pour représenter des graphiques sur la page. Consultez l'extrait de code pour résoudre cette tâche.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter une Annotation Filigrane

Une annotation filigrane doit être utilisée pour représenter des graphiques qui doivent être imprimés à une taille et une position fixes sur une page, indépendamment des dimensions de la page imprimée.

Vous pouvez ajouter un texte de filigrane en utilisant [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) à une position spécifique de la page PDF. L'opacité du filigrane peut également être contrôlée en utilisant la propriété d'opacité.

Veuillez consulter l'extrait de code suivant pour ajouter WatermarkAnnotation.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // obtenir une page particulière
    $page = $document->getPages()->get_Item(1);
    
    //Créer une Annotation
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Ajouter l'annotation dans la collection d'annotations de la page
    $page->getAnnotations()->add($wa);

    //Créer TextState pour les paramètres de police
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Définir le niveau d'opacité du texte de l'annotation
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    //Ajouter du texte à l'annotation
    $wa->setTextAndState($watermarkStrings, $ts);

    // Enregistrer le document PDF résultant.    
    $document->save($outputFile);
    $document->close();
```