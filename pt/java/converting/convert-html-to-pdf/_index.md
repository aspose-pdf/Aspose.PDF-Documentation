---
title: Converta HTML para PDF em Java
linktitle: Converter arquivo HTML em PDF
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: Aprenda como converter HTML, MHTML e páginas da web em PDF em Java com Aspose.PDF, incluindo configurações de mídia, regras de página CSS, incorporação de fontes, conteúdo SVG e saída de página única.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter HTML para PDF em Java com Aspose.PDF
Abstract: Este artigo explica como converter arquivos HTML e MHTML em PDF usando Aspose.PDF para Java. Ele cobre o fluxo de trabalho básico de HTML para PDF e mostra como controlar a renderização com tipos de mídia, prioridade de regras de página CSS, fontes incorporadas, conteúdo SVG, saída de página única e conversão direta de uma página da web ativa.
---
Aspose.PDF para Java pode converter arquivos HTML locais, conteúdo MHTML arquivado e páginas da web ativas em documentos PDF. Você pode controlar o pipeline de conversão com `HtmlLoadOptions` e `MhtLoadOptions` para influenciar o dimensionamento do layout, manipulação de mídia CSS, prioridade de regra de página, incorporação de fonte, resolução de recursos e comportamento de renderização de página única.

## Converter HTML em PDF

Use este exemplo quando um arquivo HTML local precisar ser convertido diretamente em um documento PDF.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância para configurar como a fonte HTML é interpretada durante a importação.
1. Definir [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) para `ScaleToPageWidth` portanto, o conteúdo HTML amplo é dimensionado para a largura da página PDF de destino em vez de ser cortado.
1. Abra o arquivo HTML de origem passando seu caminho e as opções de carregamento configuradas para o arquivo [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Salve o gerado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como um arquivo PDF no caminho de saída de destino.

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta HTML em PDF com opções de tipo de mídia

Use este exemplo quando o tratamento do tipo de mídia CSS precisar ser controlado durante a conversão de HTML.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância para as configurações de conversão.
1. Definir [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) para `Screen` quando o HTML deve ser renderizado com regras CSS destinadas à exibição na tela em vez de mídia impressa.
1. Abra o arquivo HTML com as opções de carregamento configuradas para que os estilos dependentes da consulta de mídia sejam aplicados durante a conversão.
1. Salve o resultado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como um arquivo PDF.

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta HTML em PDF com prioridade de regra de página CSS

Use este exemplo quando CSS `@page` as regras devem influenciar o layout final da página do PDF.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância antes de abrir o arquivo HTML.
1. Configurar `setPriorityCssPageRule(false)` quando outras configurações de layout devem ter precedência sobre CSS `@page` declarações na marcação de origem.
1. Carregue o conteúdo HTML em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com as opções configuradas para que o layout da página seja resolvido durante a importação.
1. Salve o arquivo PDF gerado.

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta HTML para PDF com fontes incorporadas

Use este exemplo quando o PDF de saída precisar preservar as fontes HTML incorporando-as.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância para a configuração de importação HTML.
1. Habilitar `setEmbedFonts(true)` portanto, as fontes resolvidas durante a renderização HTML são armazenadas no PDF de saída.
1. Abra o código-fonte HTML com estas opções de carregamento para manter a tipografia original disponível no documento final.
1. Salve o [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como um PDF com os recursos de fonte incorporados incluídos.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Renderizar conteúdo HTML em uma única página PDF

Use este exemplo quando um conteúdo HTML longo precisar ser mantido em uma página PDF em vez de fluir por várias páginas.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância para as configurações de conversão.
1. Habilitar `setRenderToSinglePage(true)` portanto, o HTML importado é apresentado em uma página PDF em vez de dividido em várias páginas.
1. Abra o HTML de origem com as opções de carregamento configuradas e deixe o Aspose.PDF construir o layout da página em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Salve o arquivo PDF de saída.

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter HTML contendo SVG embutido

Use este exemplo quando a fonte HTML incluir dados SVG embutidos que devem ser renderizados no PDF.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância com o diretório pai do arquivo HTML como caminho base para que os recursos relacionados possam ser resolvidos de forma consistente durante a conversão.
1. Abra o arquivo HTML que contém a marcação SVG embutida, passando o caminho de origem e as opções de carregamento para o arquivo [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Deixe o Aspose.PDF renderizar o HTML DOM junto com os elementos SVG incorporados no conteúdo da página PDF.
1. Salve o documento PDF gerado.

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta uma página da web em PDF

Use este exemplo quando um URL da web ativo precisar ser renderizado e salvo como um documento PDF.

1. Crie um [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instância com o URL de destino para que recursos relativos, como folhas de estilo e imagens, possam ser resolvidos nesse endereço.
1. Converta a string do URL em um `URL` objeto e abra seu fluxo de entrada para buscar o conteúdo HTML ao vivo.
1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) do fluxo de resposta e das opções de carregamento configuradas para que a página baixada seja processada com o URL base correto.
1. Salve a página da web renderizada como um arquivo PDF e feche os recursos de fluxo automaticamente com try-with-resources.

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## Converter MHTML em PDF

Use este exemplo quando um arquivo MHTML arquivado precisar ser convertido em um documento PDF.

1. Crie um [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) instância para dizer ao Aspose.PDF para carregar a fonte como conteúdo HTML MIME.
1. Abra o `.mht` ou `.mhtml` arquivo passando seu caminho e as opções de carregamento MHTML para o [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Deixe o Aspose.PDF analisar o conteúdo HTML arquivado e seus recursos incorporados no modelo de documento PDF.
1. Salve o arquivo PDF gerado.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
