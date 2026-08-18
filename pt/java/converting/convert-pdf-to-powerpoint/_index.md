---
title: Converta PDF para PowerPoint em Java
linktitle: Converter PDF em PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: Aprenda como converter arquivos PDF para PowerPoint em Java com Aspose.PDF, incluindo slides PPTX editáveis, slides baseados em imagens e resolução de imagem personalizada.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como converter PDF para PowerPoint em Java
Abstract: Este artigo explica como converter arquivos PDF em apresentações do PowerPoint usando Aspose.PDF para Java. Ele cobre conversão PPTX padrão, saída de slide como imagem e controle de resolução de imagem por meio de `PptxSaveOptions`.
---
Aspose.PDF para Java suporta a exportação de páginas PDF para apresentações editáveis ​​do PowerPoint com opções de renderização de slides. Use [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) para controlar como as páginas PDF são mapeadas em slides do PowerPoint.

## Converter PDF em PPTX

Use este exemplo quando um documento PDF precisar ser exportado como uma apresentação padrão do PowerPoint.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o padrão [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) para exportação editável do PowerPoint.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que as páginas PDF sejam serializadas como uma apresentação `.pptx`.
1. Salve o arquivo PPTX convertido.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em PPTX com slides como imagens

Use este exemplo quando cada página PDF se tornar um slide do PowerPoint baseado em imagem.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) e ative `setSlidesAsImages(true)`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que cada página do PDF seja renderizada como um slide com imagem na apresentação.
1. Salve o arquivo PPTX gerado.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em PPTX com resolução de imagem personalizada

Use este exemplo quando a qualidade da imagem do slide precisar ser controlada durante a exportação de PDF para PPTX.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) e defina `setImageResolution(300)` para maior fidelidade da imagem do slide.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do slide rasterizado seja gerado na resolução solicitada.
1. Salve a apresentação de saída.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
