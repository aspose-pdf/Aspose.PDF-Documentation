---
title: Manipular documentos PDF en Java
linktitle: Manipular documento PDF
type: docs
weight: 20
url: /es/java/manipulate-pdf-document/
description: Aprenda cómo validar, estructurar y modificar documentos PDF en Java, incluyendo la gestión de TOC y las verificaciones de PDF/A.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valide, reestructure y aplaste documentos PDF con Java
Abstract: Este artículo explica cómo manipular documentos PDF usando Aspose.PDF for Java. Cubre la validación del cumplimiento de PDF/A, la adición y personalización de una tabla de contenidos, la ocultación o personalización de los números de página del TOC, la asignación de un script de expiración y el aplanado de campos de formulario interactivos.
---
Aspose.PDF for Java incluye operaciones de estructura de documento que van más allá de la edición simple de páginas.

## Validar cumplimiento PDF/A-1a

Utilice este ejemplo cuando necesite comprobar si un documento cumple con el estándar de archivo PDF/A-1a.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ejecutar validación contra lo requerido [FormatoPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) objetivo.
1. Guarde el informe de validación en la ruta de salida especificada.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Validar la conformidad con PDF/A-1b

Esta variante valida el mismo documento fuente contra el nivel de conformidad PDF/A-1b.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Llame al método de validación con el [FormatoPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) valor para PDF/A-1b.
1. Escribe el resultado de la validación en el archivo de informe de salida.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Agregar una tabla de contenidos

Utilice este enfoque cuando el documento deba incluir una página TOC generada con enlaces a las páginas de contenido.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insertar un nuevo TOC [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y configúrelo [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crear [Encabezado](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas que apuntan a las páginas de destino.
1. Guarda el documento actualizado.

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

## Personalizar niveles y formato de TOC

Este ejemplo muestra cómo asignar diferentes configuraciones visuales a varios niveles de tabla de contenido.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un TOC [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y configure el [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) formatear matriz.
1. Crear muestra [Encabezado](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas con diferentes niveles.
1. Guarde el documento con el TOC formateado.

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

## Ocultar los números de página en el TOC

Utilice este ejemplo cuando el índice debe mostrar los títulos de las entradas sin números de página.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un TOC [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y desactivar los números de página en [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crea lo necesario [Encabezado](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entrada y añádelo a la página de contenido.
1. Guarda el documento actualizado.

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

## Personalizar prefijos de número de página del TOC

Este ejemplo agrega un prefijo personalizado a los números de página mostrados en la tabla de contenidos generada.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insertar un TOC [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y establezca el prefijo de número de página deseado en [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Crear [Encabezado](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entradas que apuntan a cada página.
1. Guarda el documento actualizado.

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

## Agregar un script de expiración de PDF

Utilice este enfoque cuando el documento deba ejecutar JavaScript al abrirse y mostrar una advertencia de expiración después de una fecha específica.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega cualquier contenido requerido.
1. Crear un [AcciónJavascript](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) con la lógica de expiración.
1. Asigne el script como la acción de apertura del documento y guarde el archivo de salida.

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

## Aplanar un formulario PDF rellenable

Este ejemplo convierte los campos de formulario interactivos en contenido estático de página, de modo que el documento resultante ya no sea editable como formulario.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique si el documento contiene widgets de formulario.
1. Aplanar cada [Campo](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) representado por un [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Guarde el documento aplanado.

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
