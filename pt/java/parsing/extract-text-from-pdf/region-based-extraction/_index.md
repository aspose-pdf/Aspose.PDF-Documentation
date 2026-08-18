---
title: Extração baseada em região usando Java
linktitle: Extração Baseada em Região
type: docs
weight: 20
url: /java/region-based-extraction/
description: Aprenda como extrair texto de uma região específica da página ou inspecionar a geometria do parágrafo em documentos PDF com Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extraia texto de uma região retangular da página

Use `TextSearchOptions` com `Rectangle` para restringir a extração a uma área definida em uma página.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para coletar texto da área da página selecionada.
1. Crie [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) para o alvo [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) e ative `setLimitToPageBounds(true)` para que a extração permaneça dentro da caixa de página visível.
1. Aplique as opções de pesquisa configuradas ao absorvedor e visite a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino.
1. Grave o buffer de texto extraído no arquivo de saída.

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

## Extraia parágrafos com informações geométricas

Use `ParagraphAbsorber` para inspecionar retângulos de seção e polígonos de parágrafo junto com o texto extraído.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) e visite a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino para criar informações de marcação de página.
1. Leia o resultado da marcação da primeira página e percorra suas seções e parágrafos.
1. Colete cada retângulo de seção, polígono de parágrafo e o texto do parágrafo reconstruído a partir de suas linhas [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Crie o relatório de saída com geometria e detalhes de texto extraídos.
1. Grave os detalhes extraídos no arquivo de saída.

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
