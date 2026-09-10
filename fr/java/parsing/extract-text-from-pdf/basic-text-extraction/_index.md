---
title: Extraction de texte de base à l'aide de Java
linktitle: Extraction de texte de base
type: docs
weight: 10
url: /java/basic-text-extraction/
description: Apprenez à extraire du texte de documents PDF en Java avec Aspose.PDF à partir de toutes les pages, d'une page spécifique ou par structure de paragraphe.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

L'extraction de texte de base est le point de départ de la lecture de contenu PDF en Java. Aspose.PDF propose deux approches courantes :


- 
Utilisez `TextAbsorber` lorsque vous avez besoin d'un résultat en texte brut à partir d'un document ou d'une page.
- Utilisez `ParagraphAbsorber` lorsque vous devez conserver le regroupement de pages, de sections, de paragraphes, de lignes et de fragments.



Les pages PDF ne stockent pas de texte comme un document de traitement de texte, l'ordre d'extraction dépend donc du flux de contenu et de la mise en page de la page. Pour l'extraction spécifique à une région, les détails géométriques, les mises en page multi-colonnes, les annotations, le texte en surbrillance ou la détection d'exposant et d'indice, utilisez les articles d'extraction associés dans cette section.


## 
Extraire le texte de toutes les pages



Utilisez `TextAbsorber` pour collecter un flux de texte plat à partir de l'ensemble du document et l'écrire dans un fichier. Il s’agit de l’option la plus simple lorsque vous n’avez besoin que du contenu textuel lisible et que vous n’avez pas besoin de limites ou de coordonnées de paragraphe.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) pour accumuler du texte dans tout le document.

1. 
Appelez `document.getPages().accept(textAbsorber)` pour que chaque [page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) soit visitée par l'absorbeur.

1. 
Écrivez le tampon de texte extrait dans le fichier de sortie.


```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
Extraire le texte d'une page spécifique



Appliquez l'absorbeur uniquement sur la page dont vous avez besoin. Les numéros de page dans la collection de pages `Document` sont basés sur 1, donc `get_Item(1)` lit la première page.

1. Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) pour l'extraction d'une seule page.

1. 
Appelez `accept(textAbsorber)` sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) sélectionnée par numéro de page.

1. 
Écrivez le tampon de texte extrait dans le fichier de sortie.


```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
Extraire le texte par structure de paragraphe

Utilisez `ParagraphAbsorber` lorsque vous avez besoin d'un regroupement structurel au lieu d'un seul flux de texte brut. Il renvoie les balises de page avec des sections, des paragraphes, des lignes et des objets `TextFragment`, ce qui est utile lorsque la sortie doit conserver des blocs logiques de texte.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ParagraphAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) et visitez l'intégralité du document pour générer des résultats de balisage de page.

1. 
Parcourez les balises de page, les sections, les paragraphes, les lignes et les objets [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) exposés par l'absorbeur.

1. 
Créez le texte de sortie avec une numérotation explicite des pages, des sections et des paragraphes afin que le regroupement structurel soit préservé.
1. Écrivez le texte du paragraphe extrait dans le fichier de sortie.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
