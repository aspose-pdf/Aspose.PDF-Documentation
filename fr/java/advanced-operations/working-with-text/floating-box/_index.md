---
title: Utiliser FloatingBox pour la mise en page PDF en Java
linktitle: Utiliser FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: Découvrez comment utiliser FloatingBox pour la mise en page du texte, le contenu multicolonne et le positionnement précis dans les documents PDF avec Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Créer et positionner des conteneurs FloatingBox stylisés en PDF avec Java
Abstract: Cet article explique comment utiliser FloatingBox dans Aspose.PDF pour Java. Il couvre le placement de texte dans des conteneurs flottants bordés, la création de dispositions répétitives sur plusieurs colonnes, l'utilisation de couleurs d'arrière-plan, de décalages absolus et d'options d'alignement horizontal ou vertical.
---
Aspose.PDF pour Java utilise `FloatingBox` pour créer des conteneurs de texte réutilisables et des mises en page basées sur des colonnes.


## 
Créer et ajouter une boîte flottante



Utilisez cet exemple lorsque le texte doit être placé à l’intérieur d’un conteneur flottant bordé.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `FloatingBox`, définissez sa taille et sa bordure, puis ajoutez du contenu textuel.
1. Ajoutez la boîte à la page et enregistrez le document.


```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## 
Créer une mise en page multicolonne répétitive



Utilisez cet exemple lorsqu'un texte long doit s'étendre sur plusieurs colonnes à l'intérieur d'une seule boîte flottante.


1. 
Créez une page et configurez les marges.

1. 
Calculez les largeurs de colonne et configurez les paramètres de colonne `FloatingBox`.
1. Ajoutez des fragments de texte répétés dans la zone et enregistrez le document.


```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
Commencez chaque fragment comme premier élément d'une colonne



Utilisez cet exemple lorsque chaque fragment inséré doit commencer un nouveau segment de flux de colonne.


1. 
Créez une page et configurez le multi-colonne `FloatingBox`.

1. 
Créez des fragments de texte et marquez-les avec `setFirstParagraphInColumn(true)`.
1. Ajoutez la boîte à la page et enregistrez le PDF.


```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une boîte flottante avec une couleur d'arrière-plan



Utilisez cet exemple lorsque le conteneur flottant doit avoir un remplissage d'arrière-plan visible.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `FloatingBox`, définissez sa couleur d'arrière-plan et ajoutez du texte.
1. Placez la case sur la page et enregistrez le document.


```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
Positionner une boîte flottante avec des décalages absolus



Utilisez cet exemple lorsque la boîte flottante doit apparaître à un décalage exact sur la page.


1. 
Créez une page et préparez le contenu du texte environnant.

1. 
Créez un `FloatingBox`, définissez le positionnement absolu et attribuez des décalages haut et gauche.
1. Ajoutez le contenu à la page et enregistrez le document.


```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## 
Aligner le texte à l'intérieur des boîtes flottantes



Utilisez cet exemple lorsque des boîtes flottantes doivent démontrer différents alignements verticaux avec le même alignement horizontal.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez plusieurs objets `FloatingBox` avec différents paramètres d'alignement.
1. Ajoutez-les à la page et enregistrez le résultat.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
