---
title: Extraire le contenu balisé des PDF en Java
linktitle: Extraire le contenu balisé
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Découvrez comment inspecter le contenu PDF balisé en Java avec Aspose.PDF, y compris l'accès au contenu balisé, l'accès à la structure racine et les éléments de structure enfants.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Utilisez ces API lorsque vous devez inspecter l'arborescence de structure logique d'un PDF balisé et examiner ou mettre à jour les métadonnées des éléments de structure.


## 
Obtenez des métadonnées de contenu balisé

Utilisez cet exemple lorsque vous avez besoin d'accéder au conteneur de contenu balisé et que vous souhaitez définir des métadonnées de base du document telles que le titre et la langue.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Récupérez l'objet [ITaggedContent] (https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) du document.

1. 
Définissez les métadonnées du contenu balisé et enregistrez le fichier de sortie.


```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## 
Obtenez la structure racine d'un PDF balisé

Cet exemple montre comment inspecter les objets racine qui représentent l'arborescence de la structure d'un PDF balisé.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et obtenez son contenu balisé.

1. 
Définissez les métadonnées du document requises.

1. 
Lisez et imprimez la racine de l'arborescence structurelle et l'élément racine logique, puis enregistrez le fichier.


```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## 
Accéder et mettre à jour les éléments de structure enfants

Utilisez cet exemple lorsque vous devez parcourir les éléments enfants dans l'arborescence de la structure, inspecter leurs propriétés et mettre à jour les métadonnées sélectionnées.


1. 
Ouvrez le PDF source balisé [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Lisez les éléments enfants à partir de la racine de l'arborescence de la structure et imprimez les propriétés disponibles.

1. 
Accédez aux éléments enfants du premier enfant racine, mettez à jour leurs métadonnées et enregistrez le document.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
