---
title: Agregar encabezados y pies de página de PDF en Java
linktitle: Agregar encabezado y pie de página a PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: Aprenda a agregar encabezados y pies de página a archivos PDF en Java usando texto, imágenes y contenido estructurado.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue encabezados y pies de página a archivos PDF con Java
Abstract: Este artículo muestra cómo agregar encabezados y pies de página a documentos PDF usando Aspose.PDF para Java. Cubre texto, numeración de páginas, HTML, imágenes, tablas y contenido de encabezado y pie de página basado en LaTeX.
---
Aspose.PDF para Java le permite asignar objetos `HeaderFooter` a cada página y completarlas con diferentes tipos de contenido.


## 
Agregar encabezados y pies de página de texto



Utilice este ejemplo cuando necesite contenido de texto simple en la parte superior e inferior de cada página.


1. 
Cree objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) y agregue fragmentos de texto.

1. 
Configure los márgenes para el encabezado y pie de página.
1. Aplíquelos a cada página del PDF de origen y guarde el resultado.


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

## 
Agregue encabezados y pies de página con numeración de páginas



Utilice este ejemplo cuando el encabezado o pie de página deba mostrar el número de página actual y el recuento total de páginas.


1. 
Cree objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) con marcadores de posición de numeración de páginas.

1. 
Configure los márgenes para ambos objetos.
1. Aplíquelos a cada página y guarde el PDF actualizado.


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

## 
Agregar encabezados y pies de página HTML



Utilice este ejemplo cuando el contenido del encabezado y pie de página deba incluir formato HTML en línea.


1. 
Cree objetos [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) y agregue contenido [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/).

1. 
Configure los márgenes para la colocación.
1. Asigne el encabezado y pie de página a cada página y guarde el documento.


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

## 
Agregar encabezados y pies de página de imágenes



Utilice este ejemplo cuando el encabezado y el pie de página deban mostrar una imagen en cada página.


1. 
Cree objetos [Imagen](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) y agréguelos a los contenedores de encabezado y pie de página.

1. 
Configura márgenes y asigna los contenedores a cada página.
1. Guarde el PDF actualizado.


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

## 
Agregar encabezados y pies de página basados en tablas



Utilice este ejemplo cuando el contenido del encabezado y pie de página deba utilizar diseño de tabla y estilo de texto.


1. 
Cree los estilos de texto y objetos de tabla necesarios.

1. 
Agregue las tablas a los contenedores [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/).
1. Aplique el encabezado y pie de página a cada página y guarde el documento.


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

## 
Agregue encabezados y pies de página de LaTeX



Utilice este ejemplo cuando el encabezado y el pie de página deban representar contenido TeX o LaTeX.


1. 
Abra el PDF de origen y determine el recuento total de páginas.

1. 
Cree contenido [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) para el encabezado y pie de página de cada página.
1. Asigna el contenido y guarda el documento.

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
