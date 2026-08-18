---
title: Melhorando a extração de texto de PDFs com múltiplas colunas
linktitle: Extração de texto de PDFs com múltiplas colunas
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para melhorar a extração de texto de layouts de PDF com várias colunas com Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Layouts de múltiplas colunas geralmente exigem processamento extra para melhorar a ordem de leitura e a qualidade da extração.

## Extraia o texto após reduzir o tamanho da fonte

Esta técnica atualiza os tamanhos das fontes dos fragmentos de texto, salva o documento ajustado na memória e, em seguida, extrai o texto do resultado transformado.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) e visite todas as páginas do documento para coletar objetos [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Itere pelos fragmentos e reduza cada tamanho de fonte na proporção solicitada para que o layout denso da coluna possa ser normalizado antes da extração.
1. Salve o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ajustado em um fluxo de bytes na memória.
1. Reabra um segundo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) desse buffer de memória.
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), visite todas as páginas do documento transformado e escreva o texto extraído no arquivo de saída.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## Extraia texto com um fator de escala

Use `TextExtractionOptions` no modo de formatação pura e ajuste o fator de escala para layouts com muitas colunas.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extração completa do documento.
1. Crie [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) no modo de formatação pura para que o comportamento de extração sensível ao layout seja usado.
1. Defina o fator de escala e aplique as opções de extração ao absorvedor antes de visitar as páginas.
1. Visite todas as páginas do documento e escreva o texto extraído no arquivo de saída.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
