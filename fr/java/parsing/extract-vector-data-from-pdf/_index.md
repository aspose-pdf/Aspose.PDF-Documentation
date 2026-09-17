---
title: Extraire des données vectorielles à partir d'un fichier PDF à l'aide de Java
linktitle: Extraire les données vectorielles d'un PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF facilite l'extraction de données vectorielles à partir d'un fichier PDF. Vous pouvez obtenir les données vectorielles, telles que la position, les limites du rectangle et la sortie SVG.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## 
Accéder aux données vectorielles à partir d'un document PDF



Utilisez `GraphicsAbsorber` pour inspecter les éléments graphiques vectoriels sur une page et écrire leur géométrie de base dans un fichier texte.

1. Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) pour collecter les opérations graphiques vectorielles.

1. 
Parcourez les objets [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraits et lisez leurs collections de rectangles, de positions et d'opérateurs.

1. 
Créez le texte de sortie avec les détails de la géométrie et du nombre d'opérateurs pour chaque élément.

1. 
Écrivez les données vectorielles extraites dans le fichier de sortie.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Enregistrer les graphiques vectoriels de la page au format SVG


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Obtenez la cible [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du document.

1. 
Appelez `page.trySaveVectorGraphics(outputFile.toString())` pour exporter le contenu graphique vectoriel de cette page directement vers SVG.


```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 
Enregistrez chaque élément extrait dans un SVG distinct

1. Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez le répertoire de sortie pour les sous-chemins extraits avant d'écrire des fichiers.

1. 
Parcourez les objets [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraits et appelez `saveToSvg(...)` pour chaque élément.

1. 
Enregistrez chaque élément extrait dans un fichier SVG distinct.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Combinez les éléments extraits en un seul SVG


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez le balisage du wrapper SVG qui contiendra les fragments vectoriels combinés.

1. 
Parcourez les objets [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraits et ajoutez chaque fragment SVG généré.
1. Écrivez la sortie SVG combinée dans le fichier cible.


```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## 
Extraire un seul élément vectoriel


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [GraphicsAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Obtenez le [GraphicElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) requis à partir de la collection d'éléments extraits.
1. Vérifiez si l'élément sélectionné est un [XFormPlacement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) et descendez dans ses éléments imbriqués si nécessaire.

1. 
Enregistrez l'élément vectoriel sélectionné dans le fichier SVG de sortie.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
