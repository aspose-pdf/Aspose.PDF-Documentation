---
title: Extraire le Contenu Étiqueté d'un PDF
linktitle: Extraire le Contenu Étiqueté
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Cet article explique comment extraire le contenu étiqueté d'un document PDF en utilisant Aspose.PDF pour Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir le Contenu Étiqueté d'un PDF

Pour obtenir le contenu d'un document PDF avec du texte étiqueté, Aspose.PDF propose la méthode [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Le code suivant montre comment obtenir le contenu d'un document PDF avec du texte étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";

// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Travailler avec le contenu Pdf étiqueté
//

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document Pdf Étiqueté Simple");
taggedContent.setLanguage("en-US");

// Enregistrer le document Pdf étiqueté
document.save(path + "TaggedPDFContent.pdf");
```


## Obtenir la Structure Racine

Afin d'obtenir la structure racine d'un document PDF étiqueté, Aspose.PDF propose les méthodes [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) et **getStructureElement()** de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le snippet de code suivant montre comment obtenir la structure racine d'un document PDF étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document PDF étiqueté");
taggedContent.setLanguage("en-US");

// Les propriétés StructTreeRootElement et RootElement sont utilisées pour accéder à
// l'objet StructTreeRoot du document pdf et à l'élément de structure racine (élément de structure du document).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## Accéder aux éléments enfants

Afin d'accéder aux éléments enfants d'un document PDF balisé, Aspose.PDF propose la classe **ElementList**. Le code suivant montre comment accéder aux éléments enfants d'un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Ouvrir le document PDF
Document document = new Document( path +"StructureElements.pdf");

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Accès à l'élément racine
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Obtenir les propriétés
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Accès aux éléments enfants du premier élément dans l'élément racine
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Définir les propriétés
        structureElement.setTitle("titre");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("texte actuel");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Enregistrer le document PDF balisé
document.save( path +"AccessChildrenElements.pdf");
```