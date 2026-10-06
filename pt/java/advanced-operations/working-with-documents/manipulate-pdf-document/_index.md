---
title: Manipular documentos PDF em Java
linktitle: Manipular documento PDF
type: docs
weight: 20
url: /pt/java/manipulate-pdf-document/
description: Aprenda como validar, estruturar e modificar documentos PDF em Java, incluindo gerenciamento de TOC e verificações de PDF/A.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar, reestruture e achate documentos PDF com Java
Abstract: Este artigo explica como manipular documentos PDF usando Aspose.PDF for Java. Ele aborda a validação da conformidade PDF/A, a adição e personalização de um sumário, a ocultação ou personalização dos números de página do TOC, a atribuição de um script de expiração e o achatamento de campos de formulário interativos.
---
Aspose.PDF for Java inclui operações de estrutura de documento que vão além da edição simples de página.

## Validar conformidade PDF/A-1a

Use este exemplo quando precisar verificar se um documento atende ao padrão de arquivamento PDF/A-1a.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Execute a validação contra o requerido [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) alvo.
1. Salve o relatório de validação no caminho de saída especificado.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Validar conformidade PDF/A-1b

Esta variação valida o mesmo documento de origem contra o nível de conformidade PDF/A-1b.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame o método de validação com o [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) valor para PDF/A-1b.
1. Escreva o resultado da validação no arquivo de relatório de saída.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Adicionar um índice

Use esta abordagem quando o documento deve incluir uma página de TOC gerada com links para as páginas de conteúdo.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insira um novo TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e configure-o [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crie [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas que apontam para as páginas de destino.
1. Salve o documento atualizado.

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Personalizar níveis e formatação do TOC

Este exemplo demonstra como atribuir diferentes configurações visuais a vários níveis do índice.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e configure o [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) formatar array.
1. Crie amostra [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas com diferentes níveis.
1. Salve o documento com o TOC formatado.

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Ocultar números de página na TOC

Use este exemplo quando o índice deve mostrar os títulos das entradas sem números de página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e desabilitar números de página em [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crie o necessário [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entrada e adicione-a à página de conteúdo.
1. Salve o documento atualizado.

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## Personalizar prefixos de número de página do TOC

Este exemplo adiciona um prefixo personalizado aos números de página exibidos no sumário gerado.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insira um TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e defina o prefixo de número de página desejado em [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crie [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas que apontam para cada página.
1. Salve o documento atualizado.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Adicionar um script de expiração de PDF

Use esta abordagem quando o documento deve executar JavaScript na abertura e exibir um aviso de expiração após uma data específica.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione qualquer conteúdo necessário.
1. Crie um [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) com a lógica de expiração.
1. Atribua o script como a ação de abertura do documento e salve o arquivo de saída.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## Achatar um formulário PDF preenchível

Este exemplo converte campos de formulário interativos em conteúdo de página estático, de modo que o documento resultante não pode mais ser editado como um formulário.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique se o documento contém widgets de formulário.
1. Achatar cada [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) representado por um [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Salve o documento achatado.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
