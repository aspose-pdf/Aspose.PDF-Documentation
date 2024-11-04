---
title: PDF Annotations Collantes 
linktitle: Annotation Collante
type: docs
weight: 50
url: /java/sticky-annotations/
description: Ce sujet concerne les annotations collantes, à titre d'exemple nous montrons l'Annotation Filigrane dans le texte. Il est utilisé pour représenter des graphiques sur la page. Consultez l'extrait de code pour résoudre cette tâche.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter une Annotation de Filigrane

Une annotation de filigrane doit être utilisée pour représenter des graphiques qui doivent être imprimés à une taille et une position fixes sur une page, quelles que soient les dimensions de la page imprimée.

Vous pouvez ajouter un texte de filigrane en utilisant [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) à une position spécifique de la page PDF. L'opacité du filigrane peut également être contrôlée en utilisant la propriété d'opacité.

Veuillez consulter l'extrait de code suivant pour ajouter une WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        //Créer une Annotation
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        //Ajouter l'annotation dans la collection d'Annotations de la Page
        page.getAnnotations().add(wa);

        //Créer TextState pour les paramètres de police
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        //Définir le niveau d'opacité du texte de l'Annotation
        wa.setOpacity(0.5);

        //Ajouter du texte à l'Annotation
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        //Enregistrer le document
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## Obtenir l'Annotation de Filigrane

```java
    public static void GetWatermarkAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // imprimer les résultats
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Supprimer l'Annotation de Filigrane

```java
    public static void DeleteWatermarkAnnotation() {
         // Charger le fichier PDF
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Filtrer les annotations en utilisant AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // supprimer les annotations
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```