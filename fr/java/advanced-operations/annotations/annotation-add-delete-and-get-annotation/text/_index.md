---
title: Annotation de Texte PDF
Texttitle: Annotation de Texte
type: docs
weight: 10
url: fr/java/text-annotation/
description: Aspose.PDF pour Java vous permet d'ajouter, d'obtenir et de supprimer des annotations de texte dans votre document PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Ajouter, supprimer et obtenir des annotations sont similaires pour différents types d'annotations. Prenons comme exemple une annotation de texte.

## Comment ajouter une annotation de texte dans un fichier PDF existant

Dans ce tutoriel, vous apprendrez comment ajouter du texte à un document PDF existant. L'outil de texte vous permet d'ajouter du texte n'importe où dans le document. Une annotation de texte est une annotation attachée à un emplacement spécifique dans un document PDF. Lorsqu'elle est fermée, l'annotation est affichée sous forme d'icône ; lorsqu'elle est ouverte, elle doit afficher une fenêtre contextuelle contenant le texte de la note dans la police et la taille choisies par le lecteur.

Les annotations sont contenues par la collection [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) d'une page particulière.
 Cette collection contient les annotations uniquement pour cette page individuelle ; chaque page a sa propre collection d'Annotations.

Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page avec la méthode Add.

1. Tout d'abord, créez une annotation que vous souhaitez ajouter au PDF.
1. Ensuite, ouvrez le PDF d'entrée.
1. Ajoutez l'annotation à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

L'extrait de code suivant vous montre comment ajouter une annotation dans une page PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Utilisateur Aspose");
        textAnnotation.setSubject("Sujet d'exemple");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Contenu d'exemple pour l'annotation");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## Ajouter une Annotation de Texte Libre (ou Créer)

Une annotation de texte libre affiche du texte directement sur la page. La méthode PdfContentEditor.CreateFreeText permet de créer ce type d'annotation. Dans l'extrait suivant, nous ajoutons une annotation de texte libre au-dessus de la première occurrence de la chaîne.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Démonstration de Texte Libre");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## Obtenir une Annotation de Texte Libre

Aspose.PDF pour Java vous permet d'obtenir une annotation de texte libre à partir de votre document PDF.

Veuillez consulter l'extrait de code suivant pour résoudre cette tâche :

```java
public static void GetFreeTextAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // imprimer les résultats
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Supprimer une Annotation de Texte Libre

Aspose.PDF pour Java vous permet de supprimer une annotation de texte libre de votre document PDF.

Veuillez consulter l'extrait de code suivant pour résoudre cette tâche :

```java
  public static void DeleteFreeTextAnnotation() {
         // Charger le fichier PDF
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Filtrer les annotations en utilisant AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // supprimer les annotations
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Supprimer toutes les annotations d'une page d'un fichier PDF

La collection [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) d'un objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) contient toutes les annotations pour cette page particulière.
 Pour supprimer toutes les annotations d'une page, appelez la méthode *Delete* de la collection AnnotationCollection.

Le code suivant vous montre comment supprimer toutes les annotations d'une page particulière.

```java
    public static void DeleteTextAnnotation() {
         // Charger le fichier PDF
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Filtrer les annotations en utilisant AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // supprimer les annotations
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Obtenir toutes les annotations d'une page d'un document PDF

Aspose.PDF vous permet d'obtenir des annotations à partir d'un document entier ou d'une page donnée. Pour obtenir toutes les annotations d'une page dans un document PDF, parcourez la collection [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) des ressources de page souhaitées. L'extrait de code suivant vous montre comment obtenir toutes les annotations d'une page.

```java
  public static void GetTextAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // imprimer les résultats
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```