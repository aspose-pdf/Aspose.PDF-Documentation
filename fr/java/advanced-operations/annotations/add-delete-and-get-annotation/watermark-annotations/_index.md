---
title: Annotations en filigrane utilisant Java
linktitle: Annotations en filigrane
type: docs
weight: 70
url: /java/watermark-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations en filigrane dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec des annotations en filigrane dans des fichiers PDF à l'aide de Java.
Abstract: Cet article explique comment créer, inspecter et supprimer des annotations en filigrane dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'ajout d'une annotation de filigrane de texte avec un état et une opacité de texte personnalisés, la lecture des zones d'annotation de filigrane existantes et la suppression des annotations de filigrane.
---
Les annotations en filigrane vous permettent de placer du contenu de superposition réutilisable sur une page tout en le gérant via la collection d'annotations.


## 
Ajouter une annotation en filigrane



Utilisez cet exemple lorsque vous avez besoin d’une annotation de filigrane de texte avec des paramètres de police et une opacité personnalisés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [WatermarkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) et ajoutez-la à la page.
1. Configurez le [TextState] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), le texte du filigrane et l'opacité, puis enregistrez le document.


```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## 
Obtenir des annotations en filigrane



Cet exemple analyse la collection d'annotations et imprime le rectangle de chaque annotation en filigrane.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations sur la page cible.
1. Filtrez les annotations par [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` et imprimez leurs rectangles.


```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## 
Supprimer les annotations en filigrane



Utilisez cette approche lorsque les annotations de filigrane existantes doivent être supprimées du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations de type [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Supprimez les annotations collectées et enregistrez le fichier de sortie.


```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Sujets d'annotations associés


- 
[Annotations interactives] (/pdf/java/interactive-annotations/)

- 
[Annotations de balisage] (/pdf/java/markup-annotations/)

- 
[Annotations de sécurité] (/pdf/java/security-annotations/)
- [Annotations de forme] (/pdf/java/shape-annotations/)

- 
[Annotations de texte] (/pdf/java/text-based-annotations/)

- 
[Importer et exporter des annotations] (/pdf/java/import-export-annotations/)
