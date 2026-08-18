---
title: Converta PDF em HTML em Java
linktitle: Converter PDF para formato HTML
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: Aprenda como converter PDF em HTML em Java com Aspose.PDF, incluindo saída de várias páginas, pastas de imagens externas, manipulação de SVG e renderização de HTML em camadas.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para HTML em Java
Abstract: Este artigo explica como converter arquivos PDF em HTML usando Aspose.PDF para Java. Abrange exportação HTML básica junto com opções para pastas de imagens, divisão de páginas, saída SVG, gráficos SVG compactados, planos de fundo de páginas PNG, marcação somente no corpo, renderização de texto transparente e conversão de camada de documento.
---
Aspose.PDF para Java oferece suporte à exportação de HTML com opções de imagens, SVG, divisão de página, transparência e renderização de camada. Use [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para controlar como as páginas PDF, os recursos e a marcação são gravados na saída HTML.

## Converter PDF em HTML

Use este exemplo quando um PDF precisar ser exportado para um documento HTML padrão.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o padrão [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para serialização HTML padrão.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo da página PDF seja exportado como marcação HTML.
1. Salve a saída HTML gerada.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML e armazene imagens separadamente

Use este exemplo quando as imagens extraídas devem ser gravadas como arquivos separados durante a exportação HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e defina `setSpecialFolderForAllImages(...)` para um diretório de saída de imagem dedicado.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que as imagens raster sejam emitidas como arquivos de recursos separados em vez de saída somente embutida.
1. Salve a saída HTML junto com os ativos de imagem gerados.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML de várias páginas

Use este exemplo quando cada página PDF precisar ser representada separadamente na saída HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e ative `setSplitIntoPages(true)`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que cada página PDF seja escrita como uma saída HTML separada.
1. Salve os arquivos HTML gerados.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML e armazene SVG separadamente

Use este exemplo quando o conteúdo vetorial precisar ser emitido como recursos SVG separados.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e defina `setSpecialFolderForSvgImages(...)` como um diretório de recursos SVG externo.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que os gráficos vetoriais sejam armazenados fora do arquivo HTML principal.
1. Salve a saída HTML e os ativos SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML com SVG compactado

Use este exemplo quando a saída SVG precisar ser otimizada durante a exportação HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e configure uma pasta dedicada para recursos SVG.
1. Habilite `setCompressSvgGraphicsIfAny(true)` para que os ativos SVG sejam compactados durante a exportação.
1. Ligue para `document.save(outputFile.toString(), saveOptions)` e salve os arquivos HTML convertidos.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML com planos de fundo de páginas PNG

Use este exemplo quando os planos de fundo da página devem ser renderizados como imagens PNG na saída HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e defina o modo de salvamento de imagem raster para planos de fundo de página PNG.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do plano de fundo da página seja emitido como camadas HTML suportadas por PNG.
1. Salve a saída HTML convertida.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta apenas o conteúdo do corpo de PDF em HTML

Use este exemplo quando apenas a marcação do corpo for necessária em vez de um shell de documento HTML completo.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e defina o modo de geração de marcação como `WriteOnlyBodyContent`.
1. Mantenha `setSplitIntoPages(true)` habilitado quando a saída somente do corpo ainda deve ser separada por páginas.
1. Chame `document.save(outputFile.toString(), saveOptions)` e salve a saída HTML.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML com renderização de texto transparente

Use este exemplo quando o texto transparente precisar ser preservado na exportação HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e habilite a preservação de texto transparente e sombreado.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que a aparência do texto relacionada à transparência seja mantida no resultado HTML.
1. Salve a saída HTML convertida.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta PDF em HTML com renderização de camada de documento

Use este exemplo quando a visibilidade da camada PDF deve ser refletida no resultado HTML.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e ative `setConvertMarkedContentToLayers(true)`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo PDF marcado seja mapeado em camadas HTML.
1. Salve os arquivos HTML exportados.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
