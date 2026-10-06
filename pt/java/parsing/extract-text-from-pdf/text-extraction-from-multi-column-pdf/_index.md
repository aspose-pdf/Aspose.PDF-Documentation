---
title: Melhorando a Extração de Texto de PDFs Multi-Coluna
linktitle: Extração de Texto de PDFs Multi-Coluna
type: docs
weight: 30
url: /pt/java/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para melhorar a extração de texto de layouts de PDF multi-coluna com Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Layouts multi-coluna frequentemente exigem processamento extra para melhorar a ordem de leitura e a qualidade da extração.

## Extrair texto após reduzir o tamanho da fonte

Esta técnica atualiza os tamanhos de fonte dos fragmentos de texto, salva o documento ajustado na memória e então extrai o texto do resultado transformado.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Crie um [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) e visite todas as páginas do documento para coletar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itere pelos fragmentos e reduza cada tamanho da Font pela proporção solicitada para que o layout denso de colunas possa ser normalizado antes da extração.
1. Salve o ajustado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para um fluxo de bytes em memória.
1. Reabra um segundo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a partir desse buffer de memória.
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

## Extrair texto com um fator de escala

Usar `TextExtractionOptions` em modo de formatação pura e ajuste o fator de escala para layouts com muitas colunas.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extração do documento inteiro.
1. Criar [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) no modo de formatação pura para que o comportamento de extração sensível ao layout seja usado.
1. Defina o fator de escala e aplique as opções de extração ao absorvedor antes de visitar as páginas.
1. Visite todas as páginas do documento e grave o texto extraído no arquivo de saída.

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
