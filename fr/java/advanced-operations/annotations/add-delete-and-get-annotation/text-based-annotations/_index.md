---
title: Annotations basées sur du texte utilisant Java
linktitle: Annotations de texte
type: docs
weight: 10
url: /java/text-based-annotations/
description: Découvrez comment créer, inspecter et supprimer des annotations PDF basées sur du texte à l'aide d'Aspose.PDF pour Java, y compris le texte libre, le balisage surligné, barré, ondulé et souligné.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec des annotations PDF texte en Java.
Abstract: Cet article montre comment utiliser cinq types d'annotations basées sur du texte dans Aspose.PDF pour Java, notamment les annotations de texte libre, de surbrillance, de barré, de ondulé et de soulignement. Apprenez à ajouter, récupérer et supprimer des annotations, ainsi que des techniques avancées telles que le marquage du texte et l'aplatissement du balisage interactif.
---
Les annotations textuelles permettent aux réviseurs et aux développeurs d'ajouter des notes interactives, des surlignages et des balises aux documents PDF sans altérer le contenu principal. Cette section couvre cinq types d'annotations pratiques utilisés dans les flux de travail de révision de documents, les scénarios de conformité et les cycles de commentaires collaboratifs.


## 
Référence rapide : types d'annotations



Cet article couvre les types d'annotations textuelles suivants :


- 
**Texte libre** : zones de texte modifiables pour ajouter des notes et des commentaires

- 
**Point culminant** : accent visuel sur les passages de texte importants
- **Biffé** : marquer le texte pour suppression ou révision lors de la révision

- 
**Squiggly** : soulignement ondulé pour indiquer des erreurs ou des problèmes

- 
**Souligné** : soulignement traditionnel avec précision en quatre points en option


## 
Ajouter, obtenir et supprimer des annotations de texte gratuites



Les annotations de texte libre agissent comme des zones de texte flottantes qui peuvent être modifiées sans affecter la structure du document. Utilisez ces exemples pour ajouter des zones de commentaires, inspecter leurs propriétés ou les supprimer.

### Ajouter des annotations de texte libres


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [FreeTextAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) avec un rectangle et des paramètres d'apparence.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 
Obtenez des annotations de texte gratuites

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations sur la page et filtrez par [AnnotationType.FreeText] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. 
Récupérez les propriétés ou les limites de l'annotation.


```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 
Supprimer les annotations de texte libre


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recherchez des annotations de texte libres en parcourant les annotations de page et en filtrant par type.

1. 
Ajoutez les annotations correspondantes à une liste de suppression et supprimez-les de la page.

1. 
Enregistrez le document mis à jour.


```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
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
Ajouter, obtenir et supprimer des annotations de surbrillance



Les annotations de surbrillance marquent les passages importants avec une superposition semi-transparente. Utilisez ces exemples pour créer des surlignages pour la révision de documents, localiser les surlignages existants et nettoyer le balisage.

### Ajouter des annotations de surbrillance


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [HighlightAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) avec un rectangle définissant la zone de surbrillance.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 
Obtenez des annotations de surbrillance

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations et filtrez par [AnnotationType.Highlight] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. 
Lisez les propriétés de l'annotation telles que les limites ou la couleur.


```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 
Supprimer les annotations de surbrillance


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collectez les annotations de surbrillance en filtrant les annotations par type.

1. 
Supprimez chaque annotation de la page.

1. 
Enregistrez le document mis à jour.


```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
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
Ajouter, obtenir et supprimer des annotations barrées



Les annotations barrées barrent le texte pour indiquer une suppression, un rejet ou une révision. Utilisez ces exemples pour appliquer un balisage barré lors de la révision de documents, rechercher du texte marqué et supprimer des annotations barrées.

### Ajouter des annotations barrées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [StrikeOutAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) avec un rectangle, un titre et une couleur.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 
Obtenir des annotations barrées

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations et filtrez par [AnnotationType.StrikeOut] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. 
Lisez les métadonnées ou les limites des annotations.


```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 
Supprimer les annotations barrées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collectez les annotations barrées en les filtrant par type.

1. 
Supprimez chaque annotation de la page.

1. 
Enregistrez le document mis à jour.


```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
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
Ajouter, obtenir et supprimer des annotations ondulées



Les annotations ondulées (soulignés ondulés) mettent en évidence les erreurs potentielles, les problèmes ou les éléments nécessitant une attention particulière. Utilisez ces exemples pour marquer le texte problématique, inspecter les annotations ondulées et les supprimer des documents.

### Ajouter des annotations ondulées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [SquigglyAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) avec un rectangle et un titre.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 
Obtenez des annotations ondulées

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations et filtrez par [AnnotationType.Squiggly] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. 
Lisez les limites des annotations ou les métadonnées.


```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 
Supprimer les annotations ondulées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collectez des annotations ondulées en les filtrant par type.

1. 
Supprimez chaque annotation de la page.

1. 
Enregistrez le document mis à jour.


```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
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
Ajouter, obtenir et supprimer des annotations soulignées



Les annotations soulignées mettent l'accent sur les passages importants avec un soulignement traditionnel. Utilisez ces exemples pour créer des soulignements, lire le contenu du texte marqué et supprimer les annotations soulignées des pages.

### Ajouter des annotations soulignées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [UnderlineAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) avec un rectangle et une couleur.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 
Obtenir des annotations soulignées

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations et filtrez par [AnnotationType.Underline] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. 
Lire les propriétés ou les limites des annotations.


```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 
Supprimer les annotations soulignées


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collectez les annotations soulignées en les filtrant par type.

1. 
Supprimez chaque annotation de la page.

1. 
Enregistrez le document mis à jour.


```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
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
Ajouter une annotation soulignée avec des points quadruples



Cet exemple définit explicitement la zone de soulignement via des points quadruples dérivés d'un rectangle.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [UnderlineAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) et calculez ses points quadruples.

1. 
Ajoutez l'annotation à la page et enregistrez le document.


```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenez le texte marqué à partir des annotations soulignées



Récupérez le contenu du texte réel couvert par les annotations soulignées. Ces exemples montrent deux approches : lire le texte marqué complet comme une seule chaîne ou traiter des fragments de texte individuellement pour une analyse détaillée.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations soulignées sur la page.

1. 
Lisez soit `getMarkedText()` ou `getMarkedTextFragments()` et imprimez les résultats.


```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## 
Supprimer les annotations soulignées par titre



Supprimez les annotations de manière sélective en filtrant sur les propriétés des métadonnées telles que le titre. Cette approche permet un nettoyage ciblé des annotations par auteur ou objectif.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Filtrez les annotations soulignées par titre.

1. 
Supprimez les annotations correspondantes et enregistrez le document mis à jour.


```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter et aplatir une annotation soulignée



Convertissez une annotation soulignée interactive en contenu de page permanent en l'aplatissant. Cela empêche toute modification ultérieure tout en préservant l’apparence soulignée dans n’importe quelle visionneuse PDF.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [UnderlineAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) à la page.

1. 
Appelez `flatten()` sur l'annotation et enregistrez le fichier de sortie.


```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## 
Sujets d'annotations associés


- 
[Annotations interactives] (/pdf/java/interactive-annotations/)
- [Annotations de balisage] (/pdf/java/markup-annotations/)

- 
[Annotations de sécurité] (/pdf/java/security-annotations/)

- 
[Annotations de forme] (/pdf/java/shape-annotations/)

- 
[Annotations en filigrane] (/pdf/java/watermark-annotations/)

- 
[Importer et exporter des annotations] (/pdf/java/import-export-annotations/)
