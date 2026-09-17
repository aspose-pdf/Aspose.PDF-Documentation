---
title: Extraction basée sur la région à l'aide de Java
linktitle: Extraction basée sur la région
type: docs
weight: 20
url: /java/region-based-extraction/
description: Découvrez comment extraire du texte d'une zone de page spécifique ou inspecter la géométrie des paragraphes dans des documents PDF avec Aspose.PDF pour Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
Extraire le texte d'une zone de page rectangulaire



Utilisez `TextSearchOptions` avec un `Rectangle` pour limiter l'extraction à une zone définie sur une page.

1. Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) pour collecter le texte de la zone de page sélectionnée.

1. 
Créez [TextSearchOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) pour la cible [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) et activez `setLimitToPageBounds(true)` pour que l'extraction reste dans la zone de page visible.

1. 
Appliquez les options de recherche configurées à l'absorbeur et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Écrivez le tampon de texte extrait dans le fichier de sortie.

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## Extraire des paragraphes avec des informations géométriques



Utilisez `ParagraphAbsorber` pour inspecter les rectangles de section et les polygones de paragraphe avec le texte extrait.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ParagraphAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) et visitez la cible [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) pour créer des informations de balisage de page.

1. 
Lisez le premier résultat du balisage de page et parcourez ses sections et paragraphes.
1. Collectez chaque rectangle de section, polygone de paragraphe et le texte de paragraphe reconstruit à partir de ses lignes [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Créez le rapport de sortie avec la géométrie et les détails du texte extraits.

1. 
Écrivez les détails extraits dans le fichier de sortie.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
