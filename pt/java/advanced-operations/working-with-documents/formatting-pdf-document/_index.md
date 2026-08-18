---
title: Formatar documentos PDF em Java
linktitle: Formatando documento PDF
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Aprenda como formatar documentos PDF, incorporar fontes, controlar configurações do visualizador e ajustar opções de exibição em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formate a janela do documento, as fontes e o comportamento do zoom em arquivos PDF com Java
Abstract: Este artigo explica como formatar documentos PDF usando Aspose.PDF para Java. Ele cobre a leitura e atualização das configurações da janela do documento, incorporação de fontes, definição de uma fonte padrão, listagem de fontes, subconjunto de fontes incorporadas e controle do fator de zoom inicial.
---
A formatação em Aspose.PDF para Java inclui comportamento do visualizador, incorporação de fontes e configurações de exibição.

## Obtenha as configurações da janela do documento

Use este exemplo para inspecionar as preferências atuais do visualizador armazenadas em um documento PDF existente.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia a janela necessária e exiba as propriedades do documento.
1. Produza as configurações atuais para inspeção ou depuração.

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

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina as preferências de janela, layout e modo de página necessárias.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

Use esta abordagem quando um documento precisar ter as fontes necessárias para uma renderização mais confiável em outros sistemas.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ative a incorporação de fontes padrão e itere pelas fontes usadas por cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Marque quaisquer objetos [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) não incorporados para incorporação.
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

Este exemplo cria um novo PDF e atribui uma fonte incorporada ao conteúdo do texto desde o início.

1. Crie um novo [Documento] PDF(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie o [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) e [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) necessários.
1. Resolva o destino [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) do repositório e marque-o como incorporado.
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

## Defina uma fonte padrão para saída de PDF

Use esse padrão quando o documento salvo precisar usar uma fonte específica durante a geração de saída.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) e defina o nome da fonte padrão.
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

## Obtenha todas as fontes usadas em um PDF

Este exemplo lista todas as fontes detectadas no documento para que você possa auditar o uso das fontes antes de exportar ou atualizar o arquivo.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumere as fontes retornadas pelos utilitários de fontes do documento.
1. Produza o nome de cada [Fonte] detectada (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Melhore a incorporação de fontes subdividindo fontes

Use essa abordagem quando quiser reduzir a carga útil da fonte e, ao mesmo tempo, manter os dados da fonte incorporados alinhados com o uso do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Execute o subconjunto de fontes por meio dos utilitários de fontes do documento com os valores [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) necessários.
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

## Defina o fator de zoom de abertura do documento

Este exemplo configura o nível de zoom inicial que deve ser aplicado quando o PDF for aberto.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com um [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Atribua a ação como ação de abertura do documento e salve o resultado.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Obtenha o fator de zoom de abertura do documento

Use este exemplo para inspecionar se um PDF já define um nível de zoom explícito para sua ação de abertura.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique se a ação aberta é [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Produza o valor de zoom configurado ou informe que nenhum zoom está definido.

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
