---
title: Converter PDF para HTML em Java
linktitle: Converter PDF para formato HTML
type: docs
weight: 50
url: /pt/java/convert-pdf-to-html/
lastmod: "2026-10-06"
description: Aprenda como converter PDF para HTML em Java com Aspose.PDF, incluindo saída de múltiplas páginas, pastas de imagens externas, manipulação de SVG e renderização de HTML em camadas.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para HTML em Java
Abstract: Este artigo explica como converter arquivos PDF para HTML usando Aspose.PDF for Java. Ele cobre a exportação básica de HTML juntamente com opções para pastas de imagens, divisão de páginas, saída SVG, gráficos SVG compactados, fundos de página PNG, marcação apenas do corpo, renderização de texto transparente e conversão de camada de documento.
---
O Aspose.PDF for Java oferece suporte à exportação HTML com opções para imagens, SVG, divisão de página, transparência e renderização de camadas. Use [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para controlar como as páginas PDF, recursos e marcação são gravados na saída HTML.

## Converter PDF para HTML

Use este exemplo quando um PDF deve ser exportado para um documento HTML padrão.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar padrão [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para serialização HTML padrão.
1. Chamada `document.save(outputFile.toString(), saveOptions)` então o conteúdo da página PDF é exportado como marcação HTML.
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

## Converter PDF para HTML e armazenar imagens separadamente

Use este exemplo quando as imagens extraídas devem ser gravadas como arquivos separados durante a exportação HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e definir `setSpecialFolderForAllImages(...)` para um diretório de saída de imagens dedicado.
1. Chamada `document.save(outputFile.toString(), saveOptions)` portanto, as imagens raster são emitidas como arquivos de recurso separados em vez de saída apenas em linha.
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

## Converter PDF para HTML de várias páginas

Use este exemplo quando cada página PDF deve ser representada separadamente na saída HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e habilitar `setSplitIntoPages(true)`.
1. Chamada `document.save(outputFile.toString(), saveOptions)` assim, cada página PDF é gravada como saída HTML separada.
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

## Converter PDF para HTML e armazenar SVG separadamente

Use este exemplo quando o conteúdo vetorial deve ser emitido como recursos SVG separados.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e definir `setSpecialFolderForSvgImages(...)` para um diretório externo de recursos SVG.
1. Chamada `document.save(outputFile.toString(), saveOptions)` portanto, gráficos vetoriais são armazenados fora do arquivo HTML principal.
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

## Converter PDF para HTML com SVG compactado

Use este exemplo quando a saída SVG deve ser otimizada durante a exportação HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e configure uma pasta dedicada para recursos SVG.
1. Habilitar `setCompressSvgGraphicsIfAny(true)` Portanto, os ativos SVG são comprimidos durante a exportação.
1. Chamada `document.save(outputFile.toString(), saveOptions)` e salve os arquivos HTML convertidos.

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

## Converter PDF para HTML com fundos de página PNG

Use este exemplo quando os fundos de página devem ser renderizados como imagens PNG na saída HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e definir o modo de salvamento da imagem raster para fundos de página PNG.
1. Chamada `document.save(outputFile.toString(), saveOptions)` Então o conteúdo de fundo da página é emitido como camadas HTML baseadas em PNG.
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

## Converter PDF apenas para o conteúdo do corpo em HTML

Use este exemplo quando apenas a marcação do corpo for necessária em vez de um shell completo de documento HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e definir o modo de geração de marcação para `WriteOnlyBodyContent`.
1. Manter `setSplitIntoPages(true)` ativado quando a saída apenas do corpo ainda deve ser separada por páginas.
1. Chamada `document.save(outputFile.toString(), saveOptions)` e salvar a saída HTML.

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

## Converter PDF para HTML com renderização de texto transparente

Use este exemplo quando o texto transparente deve ser preservado na exportação HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e habilite a preservação de texto transparente e sombreado.
1. Chamada `document.save(outputFile.toString(), saveOptions)` assim, a aparência do texto relacionada à transparência é mantida no resultado HTML.
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

## Converter PDF para HTML com renderização de camada de documento

Use este exemplo quando a visibilidade das camadas do PDF deve ser refletida no resultado HTML.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) e habilitar `setConvertMarkedContentToLayers(true)`.
1. Chamada `document.save(outputFile.toString(), saveOptions)` Assim, o conteúdo de PDF marcado é mapeado em camadas HTML.
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
