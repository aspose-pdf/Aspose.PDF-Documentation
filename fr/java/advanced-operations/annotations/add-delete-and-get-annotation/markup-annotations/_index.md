---
title: Annotations de balisage utilisant Java
linktitle: Annotations de balisage
type: docs
weight: 30
url: /java/markup-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations surlignées, soulignées, ondulées et barrées dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec des annotations de balisage dans des fichiers PDF à l'aide de Java.
Abstract: Cet article explique comment créer, inspecter et supprimer des annotations de balisage de texte dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre les annotations surlignées, soulignées, ondulées et barrées basées sur les exemples Java du référentiel.
---
Les workflows d'annotation de balisage de cette section se concentrent sur les commentaires de style note, les marqueurs caret et les scénarios de remplacement-révision groupés.


## 
Ajouter une annotation de texte



Utilisez cet exemple lorsque vous devez placer une annotation de texte de style pense-bête avec des métadonnées contextuelles sur une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [TextAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) et configurez son titre, son contenu, son icône et sa fenêtre contextuelle.
1. Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenir des annotations de texte



Cet exemple numérise la page et imprime le rectangle de chaque annotation de texte.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations sur la page.
1. Filtrez les annotations par [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` et imprimez leurs rectangles.


```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
Supprimer les annotations de texte



Utilisez cette approche lorsque les annotations de texte existantes doivent être supprimées du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations de type [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Supprimez les annotations collectées et enregistrez le fichier de sortie.


```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une annotation caret



Utilisez cet exemple lorsque vous devez marquer le texte inséré avec une annotation de révision de type curseur.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [CaretAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) et configurez sa fenêtre contextuelle et son apparence.
1. Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 
Obtenir des annotations de signe d'insertion



Cet exemple lit les annotations caret existantes et imprime leurs emplacements.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations de la page.
1. Filtrez les annotations par [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` et imprimez leurs rectangles.


```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## 
Supprimer les annotations de signe d'insertion



Utilisez cette approche lorsque les annotations caret doivent être supprimées de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations dont le type est [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. Supprimez les annotations collectées et enregistrez le document de sortie.


```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des annotations de remplacement groupées



Cet exemple combine une annotation caret avec une annotation barrée pour représenter un commentaire de révision de style remplacement.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez l'annotation caret et la [StrikeOutAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) associée.
1. Liez les annotations via `setInReplyTo` et `setReplyType`, puis enregistrez le document.


```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 
Obtenez des annotations de remplacement groupées



Cet exemple détecte les annotations barrées qui participent à un workflow de remplacement groupé.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations de page et sélectionnez les annotations barrées.
1. Vérifiez la relation de réponse et imprimez le rectangle des annotations correspondantes.


```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## 
Supprimer les annotations de remplacement groupées



Utilisez cette approche lorsque les annotations barrées de remplacement et de révision doivent être supprimées de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations barrées qui représentent le balisage de remplacement.
1. Supprimez les annotations collectées et enregistrez le document mis à jour.


```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Sujets d'annotations associés


- 
[Annotations de texte] (/pdf/java/text-based-annotations/)

- 
[Annotations interactives] (/pdf/java/interactive-annotations/)

- 
[Annotations de forme] (/pdf/java/shape-annotations/)
- [Annotations des médias] (/pdf/java/media-annotations/)

- 
[Annotations de sécurité] (/pdf/java/security-annotations/)

- 
[Annotations en filigrane] (/pdf/java/watermark-annotations/)
