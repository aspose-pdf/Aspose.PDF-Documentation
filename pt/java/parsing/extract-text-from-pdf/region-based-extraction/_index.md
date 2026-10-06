---
title: Extração baseada em região usando Java
linktitle: Extração baseada em região
type: docs
weight: 20
url: /pt/java/region-based-extraction/
description: Saiba como extrair texto de uma região específica da página ou inspecionar a geometria de parágrafos em documentos PDF com Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extrair texto de uma região retangular da página

Usar `TextSearchOptions` com um `Rectangle` para restringir a extração a uma área definida em uma página.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para coletar texto da área de página selecionada.
1. Criar [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) para o alvo [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) e habilitar `setLimitToPageBounds(true)` para que a extração permaneça dentro da caixa de página visível.
1. Aplique as opções de pesquisa configuradas ao absorvedor e visite o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Escreva o buffer de texto extraído no arquivo de saída.

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

## Extrair parágrafos com informações de geometria

Usar `ParagraphAbsorber` para inspecionar retângulos de seção e polígonos de parágrafo juntamente com o texto extraído.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) e visite o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para gerar informações de marcação de página.
1. Leia o primeiro resultado de marcação de página e itere através de suas seções e parágrafos.
1. Colete cada retângulo de seção, polígono de parágrafo e o texto do parágrafo reconstruído a partir de seu [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) linhas.
1. Crie o relatório de saída com geometria e detalhes de texto extraído.
1. Escreva os detalhes extraídos no arquivo de saída.

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
