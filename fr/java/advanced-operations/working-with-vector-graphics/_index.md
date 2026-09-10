---
title: Travailler avec des graphiques vectoriels en Java
linktitle: Travailler avec des graphiques vectoriels
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: Découvrez comment extraire, déplacer, supprimer, copier et exporter des graphiques vectoriels dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilisez GraphicsAbsorber pour inspecter et manipuler des graphiques vectoriels PDF en Java
Abstract: Cet article explique comment utiliser des graphiques vectoriels dans Aspose.PDF pour Java à l'aide de la classe GraphicsAbsorber. Découvrez comment inspecter les éléments vectoriels sur une page, les déplacer ou les supprimer, copier des graphiques entre les pages et exporter du contenu vectoriel au format SVG.
---
Aspose.PDF pour Java expose le contenu vectoriel via les objets `GraphicsAbsorber` et `GraphicElement`. Cela vous permet d'inspecter les éléments vectoriels de bas niveau sur une page, puis de les mettre à jour, de les supprimer, de les copier ou de les exporter.


## 
Inspecter les graphiques vectoriels sur une page



Utilisez cet exemple lorsque vous devez énumérer des éléments vectoriels et inspecter leur nombre de pages, leur position et leur nombre d'opérateurs.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) et visitez la page cible.
1. Parcourez les objets [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) absorbés et affichez leurs propriétés.


```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## 
Déplacer les graphiques vectoriels sur la page



Utilisez cet exemple lorsque tous les éléments vectoriels détectés doivent être déplacés vers une nouvelle position.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez la page cible avec [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) et supprimez temporairement les mises à jour.
1. Modifiez la position de chaque élément absorbé, reprenez les mises à jour et enregistrez le document.


```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## 
Supprimer les graphiques vectoriels par position avec suppression d'élément



Utilisez cet exemple lorsque les éléments vectoriels à l’intérieur d’un rectangle spécifique doivent être supprimés un par un.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez la page avec [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) et définissez la cible [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Supprimez les éléments correspondants, reprenez les mises à jour et enregistrez le document.


```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## 
Supprimer les graphiques vectoriels en supprimant une collection



Utilisez cet exemple lorsque les éléments vectoriels correspondants doivent d’abord être collectés, puis supprimés en une seule opération.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez la page avec [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) et collectez les éléments correspondants.
1. Supprimez les graphiques collectés du contenu de la page et enregistrez le document mis à jour.


```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## 
Copier les graphiques vectoriels sur une autre page élément par élément



Utilisez cet exemple lorsque chaque élément vectoriel absorbé doit être ajouté individuellement à une nouvelle page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page de destination.

1. 
Visitez la page source avec [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Ajoutez chaque [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) à la page de destination et enregistrez le document.


```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## 
Copiez les graphiques vectoriels sur une autre page en tant que collection



Utilisez cet exemple lorsque la totalité de la collection de graphiques vectoriels absorbés doit être copiée sur une nouvelle page en un seul appel.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page de destination.

1. 
Visitez la page source avec [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Ajoutez la collection de graphiques absorbés à la page de destination et enregistrez le document.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
