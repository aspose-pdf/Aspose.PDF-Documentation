---
title: Adicionar cabeçalhos e rodapés de PDF em Java
linktitle: Adicionando cabeçalho e rodapé ao PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: Aprenda como adicionar cabeçalhos e rodapés a arquivos PDF em Java usando texto, imagens e conteúdo estruturado.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione cabeçalhos e rodapés a arquivos PDF com Java
Abstract: Este artigo mostra como adicionar cabeçalhos e rodapés a documentos PDF usando Aspose.PDF para Java. Abrange texto, numeração de páginas, HTML, imagem, tabela e conteúdo de cabeçalho e rodapé baseado em LaTeX.
---
Aspose.PDF para Java permite atribuir objetos `HeaderFooter` a cada página e preenchê-los com diferentes tipos de conteúdo.

## Adicione cabeçalhos e rodapés de texto

Use este exemplo quando precisar de conteúdo de texto simples na parte superior e inferior de cada página.

1. Crie objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) e adicione fragmentos de texto.
1. Configure margens para o cabeçalho e rodapé.
1. Aplique-os a cada página do PDF de origem e salve o resultado.

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione cabeçalhos e rodapés com numeração de páginas

Use este exemplo quando o cabeçalho ou rodapé mostrar o número da página atual e a contagem total de páginas.

1. Crie objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) com espaços reservados para numeração de páginas.
1. Configure margens para ambos os objetos.
1. Aplique-os a cada página e salve o PDF atualizado.

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione cabeçalhos e rodapés HTML

Use este exemplo quando o conteúdo do cabeçalho e rodapé incluir formatação HTML embutida.

1. Crie objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) e adicione conteúdo [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/).
1. Configure margens para posicionamento.
1. Atribua o cabeçalho e rodapé a cada página e salve o documento.

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione cabeçalhos e rodapés de imagens

Use este exemplo quando o cabeçalho e o rodapé exibirem uma imagem em cada página.

1. Crie objetos [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) e adicione-os aos contêineres de cabeçalho e rodapé.
1. Configure as margens e atribua os containers a cada página.
1. Salve o PDF atualizado.

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione cabeçalhos e rodapés baseados em tabelas

Use este exemplo quando o conteúdo do cabeçalho e rodapé precisar usar layout de tabela e estilo de texto.

1. Crie os estilos de texto e objetos de tabela necessários.
1. Adicione as tabelas aos contêineres [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/).
1. Aplique o cabeçalho e rodapé a cada página e salve o documento.

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione cabeçalhos e rodapés LaTeX

Use este exemplo quando o cabeçalho e o rodapé devem renderizar conteúdo TeX ou LaTeX.

1. Abra o PDF de origem e determine a contagem total de páginas.
1. Crie conteúdo [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) para o cabeçalho e rodapé de cada página.
1. Atribua o conteúdo e salve o documento.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```
