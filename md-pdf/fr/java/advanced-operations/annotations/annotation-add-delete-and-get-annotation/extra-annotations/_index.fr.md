---

title: Utilisation de types supplémentaires d'annotations PDF  
linktitle: Annotations supplémentaires  
type: docs  
weight: 60  
url: /java/extra-annotations/  
description: Cette section décrit comment ajouter, obtenir et supprimer des types supplémentaires d'annotations de votre document PDF.  
lastmod: "2021-11-24"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  

---

## Comment ajouter une annotation de type Caret dans un fichier PDF existant

L'annotation Caret est un symbole qui indique l'édition de texte. L'annotation Caret est également une annotation de balisage, donc la classe Caret dérive de la classe Markup et fournit également des fonctions pour obtenir ou définir les propriétés de l'annotation Caret et réinitialiser le flux de l'apparence de l'annotation Caret.

Étapes avec lesquelles nous créons une annotation Caret :

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Créez une nouvelle [Annotation de Caret](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) et définissez les paramètres de Caret (nouveau Rectangle, titre, Sujet, Drapeaux, couleur, largeur, StartingStyle et EndingStyle). Cette annotation est utilisée pour indiquer l'insertion de texte.
1. Créez une nouvelle [Annotation de Barré](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) et définissez les paramètres (nouveau Rectangle, titre, couleur, nouveaux QuadPoints et nouveaux points, Sujet, InReplyTo, ReplyType).
1. Ensuite, nous pouvons ajouter des annotations à la page.

Le code suivant montre comment ajouter une annotation de Caret à un fichier PDF :

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        // Cette annotation est utilisée pour indiquer l'insertion de texte
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Utilisateur Aspose");
        caretAnnotation1.setSubject("Texte inséré 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // Cette annotation est utilisée pour indiquer le remplacement de texte
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Utilisateur Aspose");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Texte inséré 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Barrer");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Obtenir l'Annotation Caret

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation Caret dans un document PDF

```java
    public static void GetCaretAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // imprimer les résultats
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Supprimer l'Annotation Caret

L'extrait de code suivant montre comment supprimer l'annotation Caret d'un fichier PDF.

```java
public static void DeleteCaretAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // supprimer l'annotation
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


Un [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) est un lien hypertexte qui mène à une destination ailleurs dans le document ou à une action à exécuter.

## Ajouter une Annotation de Lien

Un lien est une zone rectangulaire qui peut être placée n'importe où sur la page. Chaque lien a une action PDF correspondante qui lui est associée. Cette action est exécutée lorsque l'utilisateur clique dans la zone de ce lien.

Le code suivant montre comment ajouter une annotation de lien à un fichier PDF en utilisant un exemple de numéro de téléphone :

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // Le chemin vers le répertoire des documents.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Charger le fichier PDF
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Créer un objet TextFragmentAbsorber pour trouver un numéro de téléphone
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Accepter l'absorbeur uniquement pour la 1ère page
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Créer une annotation de lien et définir l'action pour appeler un numéro de téléphone
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Ajouter l'annotation à la page
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Obtenir l'Annotation de Lien

Veuillez essayer d'utiliser le snippet de code suivant pour obtenir l'annotation de lien à partir d'un document PDF.

```java
    public static void GetLinkAnnotations() {

        // Charger le fichier PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrer les annotations en utilisant AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // imprimer les résultats
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Imprimer l'URL de chaque annotation de lien
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Imprimer le texte associé à l'hyperlien
            System.out.println(extractedText);
        }
    }
```


## Supprimer l'annotation de lien

Le code suivant montre comment supprimer l'annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la première page. Ensuite, nous enregistrerons le document avec l'annotation supprimée.

```java
    public static void DeleteLinkAnnotations() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrer les annotations à l'aide de AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Enregistrer le document avec l'annotation supprimée
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Rédiger une certaine région de page avec une annotation de rédaction en utilisant Aspose.PDF pour Java

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajout ainsi que de manipulation des annotations dans un fichier PDF existant. Récemment, certains de nos clients ont demandé une fonctionnalité pour expurger (supprimer du texte, des images, etc. d'une région spécifique) d'une page d'un document PDF. Afin de répondre à cette demande, une classe nommée RedactionAnnotation est fournie, qui peut être utilisée pour expurger certaines régions de page ou elle peut être utilisée pour manipuler des RedactionAnnotations existantes et les expurger (c'est-à-dire aplatir l'annotation et supprimer le texte en dessous).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Ouvrir le document
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Créer une instance de RedactionAnnotation pour une région de page spécifique
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Texte à imprimer sur l'annotation d'expurgation
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Répéter le texte de superposition sur l'annotation d'expurgation
        annot.setRepeat(true);

        // Ajouter l'annotation à la collection d'annotations de la première page
        page.getAnnotations().add(annot);

        // Aplatit l'annotation et expurge le contenu de la page (c'est-à-dire supprime le texte et l'image
        // Sous l'annotation expurgée)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Approche des façades

Le namespace Aspose.PDF.Facades contient également une classe nommée [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) qui offre la fonctionnalité de manipuler les annotations existantes dans un fichier PDF. Cette classe contient une méthode nommée [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) qui offre la capacité de supprimer certaines régions de page.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Rédiger une certaine région de page
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```