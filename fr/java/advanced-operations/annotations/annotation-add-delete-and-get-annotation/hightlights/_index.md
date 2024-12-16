---
title: Annotation des surlignages PDF
linktitle: Annotation des surlignages
type: docs
weight: 20
url: /fr/java/highlights-annotation/
description: Les annotations de balisage sont présentées dans le texte sous forme de surlignages, de soulignements, de barrages ou de soulignements en zigzag dans le texte d'un document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les annotations de balisage de texte doivent apparaître sous forme de surlignages, de soulignements, de barrages ou de soulignements en zigzag dans le texte d'un document. Lorsqu'elles sont ouvertes, elles doivent afficher une fenêtre pop-up contenant le texte de la note associée.

Les propriétés des annotations de balisage de texte dans le document PDF peuvent être modifiées à l'aide de la fenêtre des propriétés fournie dans le contrôle du visualiseur PDF. La couleur, l'opacité, l'auteur et le sujet de l'annotation de balisage de texte peuvent être modifiés.

Il est possible d'obtenir ou de définir les paramètres des annotations de surlignage en utilisant la propriété highlightSettings.
 La propriété highlightSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de surlignage.

Il est également possible d'obtenir ou de définir les paramètres des annotations de barré en utilisant la propriété strikethroughSettings. La propriété strikethroughSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de barré.

La prochaine fonctionnalité est la capacité d'obtenir ou de définir les paramètres des annotations de soulignement en utilisant la propriété underlineSettings. La propriété underlineSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de soulignement.

## Ajouter une Annotation de Marquage de Texte

Afin d'ajouter une Annotation de Marquage de Texte au document PDF, nous devons effectuer les actions suivantes :

1. Charger le fichier PDF - nouvel objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Créer des annotations :

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) et définir les paramètres (titre, couleur).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) et définir les paramètres (titre, couleur).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) et définir les paramètres (titre, couleur).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) et définir les paramètres (titre, couleur).

1. Après, nous devrions ajouter toutes les annotations à la page.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // Charger le fichier PDF
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // Créer des annotations
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Utilisateur Aspose");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Utilisateur Aspose");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Utilisateur Aspose");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Utilisateur Aspose");
            underlineAnnotation.setColor(Color.getViolet());

            // Ajouter l'annotation à la page
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


Si vous souhaitez mettre en évidence un fragment multi-lignes, vous devez utiliser un exemple avancé :

```java
    /// <summary>
    /// Exemple avancé pour vous souhaitez mettre en évidence un fragment multi-lignes
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Utilisateur Aspose");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Utilisateur Aspose");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// Comment obtenir un texte surligné
    /// </summary>
    public static void GetHighlightedText() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## Obtenir une Annotation de Marquage de Texte

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir une annotation de marquage de texte à partir d'un document PDF.

```java
     public static void GetTextMarkupAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimer les résultats
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## Supprimer l'Annotation de Marquage de Texte

Le snippet de code suivant montre comment supprimer l'annotation de marquage de texte d'un fichier PDF.

```java
   public static void DeleteTextMarkupAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimer les résultats
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```