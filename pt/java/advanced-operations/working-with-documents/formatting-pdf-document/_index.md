---
title: Formatar documentos PDF em Java
linktitle: Formatando documento PDF
type: docs
weight: 11
url: /pt/java/formatting-pdf-document/
description: Aprenda a formatar documentos PDF, incorporar fontes, controlar as configurações do visualizador e ajustar as opções de exibição em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formate a janela do documento, as fontes e o comportamento de zoom em arquivos PDF com Java
Abstract: Este artigo explica como formatar documentos PDF usando Aspose.PDF for Java. Ele cobre a leitura e atualização das configurações da janela do documento, a incorporação de fontes, a definição de uma fonte padrão, a listagem de fontes, a subconfiguração de fontes incorporadas e o controle do fator de zoom inicial.
---
Formatação no Aspose.PDF for Java inclui comportamento do visualizador, incorporação de fontes e configurações de exibição.

## Obter configurações da janela do documento

Use este exemplo para inspecionar as preferências de visualização atuais armazenadas em um documento PDF existente.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia as propriedades de janela e exibição necessárias do documento.
1. Exiba as configurações atuais para inspeção ou depuração.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## Definir preferências da janela do documento

Este exemplo atualiza como o PDF deve ser exibido quando aberto em um visualizador compatível.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina as preferências de janela, layout e modo de página necessárias.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## Incorporar fontes em um PDF existente

Use esta abordagem quando um documento deve conter as fontes necessárias para uma renderização mais confiável em outros sistemas.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Habilite incorporação de fontes padrão e itere pelas fontes usadas por cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Marcar qualquer não incorporado objetos [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) para incorporação.
1. Salve o documento atualizado.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Incorporar fontes ao criar um novo PDF

Este exemplo cria um novo PDF e atribui uma fonte incorporada ao conteúdo de texto desde o início.

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie o necessário [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), e [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Resolva o alvo [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) do repositório e marcá-lo como incorporado.
1. Adicione o conteúdo de texto à página e salve o documento de saída.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## Definir uma Font padrão para a saída PDF

Use este padrão quando o documento salvo deve recorrer a uma fonte específica durante a geração da saída.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) e defina o nome da Font padrão.
1. Salve o documento com as opções de salvamento configuradas.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Obter todas as fontes usadas em um PDF

Este exemplo lista todas as Font detectadas no documento para que você possa auditar o uso de Font antes de exportar ou atualizar o arquivo.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumere as fontes retornadas pelos utilitários de fontes do documento.
1. Exiba o nome de cada detectado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Melhorar a incorporação de Font por subdefinição de fonts

Use esta abordagem quando quiser reduzir a carga de fontes enquanto mantém os dados de fontes incorporadas alinhados ao uso do documento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Execute a subdefinição de fontes através das utilidades de fontes do documento com o necessário [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) valores.
1. Salve o documento otimizado.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Definir o fator de zoom ao abrir o documento

Este exemplo configura o nível de zoom inicial que deve ser aplicado quando o PDF é aberto.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com um [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Atribua a ação como a ação de abertura do documento e salve o resultado.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Obter o fator de zoom de abertura do documento

Use este exemplo para verificar se um PDF já define um nível de zoom explícito para sua ação de abertura.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique se a ação de abertura é um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com um [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Exiba o valor de zoom configurado ou informe que nenhum zoom está definido.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
