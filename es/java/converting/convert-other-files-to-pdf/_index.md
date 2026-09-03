---
title: Convertir otros formatos de archivo a PDF en Java
linktitle: Convertir otros formatos de archivo a PDF
type: docs
weight: 80
url: /es/java/convert-other-files-to-pdf/
lastmod: "2026-09-03"
description: Aprenda cómo convertir archivos EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD y TeX a PDF en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir otros formatos de archivo a PDF en Java
Abstract: Este artículo explica cómo convertir múltiples formatos de archivo de origen a PDF usando Aspose.PDF for Java. Cubre flujos de trabajo de conversión de EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, texto, XML, XPS y XSL-FO utilizando opciones de carga específicas del formato y pasos de preprocesamiento cuando sea necesario.
---
Aspose.PDF for Java admite la conversión de formatos de documento, marcado y de descripción de página a PDF.

## Convertir OFD a PDF

Utilice este ejemplo cuando un documento OFD deba convertirse en PDF.

1. Abra la fuente OFD pasando la ruta del archivo y [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF analice el paquete OFD en el modelo de documento PDF.
1. Guarde el PDF resultante en la ruta de salida objetivo.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Convertir TeX a PDF

Utilice este ejemplo cuando el contenido TeX debe renderizarse directamente como PDF.

1. Abra la fuente TeX pasando la ruta del archivo y [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF interprete el marcado TeX y construya el diseño del PDF durante la carga.
1. Guarda el PDF generado.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PostScript a PDF

Utilice este ejemplo cuando se deba convertir un archivo PostScript en un documento PDF.

1. Abrir el origen PostScript con [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF traduzca el flujo de descripción de página PostScript a un modelo de documento PDF.
1. Guarde el archivo PDF convertido.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir EPS a PDF

Utilice este ejemplo cuando un archivo Encapsulated PostScript deba convertirse a PDF.

1. Abrir la fuente EPS con [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) porque EPS sigue la misma ruta de carga basada en PostScript.
1. Cargar el archivo en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) por lo que el contenido de la descripción de la página se convierte durante la importación.
1. Guardar el PDF de salida.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir EPUB a PDF

Utilice este ejemplo cuando un eBook EPUB deba convertirse a PDF.

1. Abra la fuente EPUB pasando la ruta del archivo y [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF cargue la estructura del libro electrónico y la convierta en páginas PDF.
1. Guarde el PDF convertido.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir Markdown a PDF

Utilice este ejemplo cuando el contenido Markdown debe renderizarse y guardarse como PDF.

1. Abra la fuente Markdown pasando la ruta del archivo y [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF interprete el contenido Markdown y lo renderice en contenido de página PDF.
1. Guarde el archivo PDF de salida.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir texto a PDF con un flujo de trabajo sencillo

Utilice este ejemplo cuando se deba convertir rápidamente un archivo de texto plano a PDF.

1. Lea la fuente de texto sin formato con decodificación UTF-8 para que el contenido del texto esté disponible como una cadena Java.
1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Envuelve el texto en un [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y añádelo a la colección de párrafos de la página.
1. Guarda el PDF generado.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir texto a PDF con opciones avanzadas

Utilice este ejemplo cuando el texto sin formato debe convertirse con opciones adicionales de diseño o codificación.

1. Lea todas las líneas de texto del archivo de entrada para que se puedan inspeccionar los marcadores de salto de página durante la conversión.
1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y configure cada uno [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) con márgenes y estado de texto predeterminado.
1. Resolver la fuente monoespaciada mediante [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) y agrega cada línea como un [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Guarda el archivo de salida después de que se complete el bucle de construcción de páginas.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PCL a PDF

Utilice este ejemplo cuando un flujo de impresión PCL deba convertirse en PDF.

1. Crear [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) y habilitar los errores de análisis suprimidos cuando se requiera un comportamiento de importación indulgente.
1. Abra la fuente PCL pasando la ruta del archivo y las opciones de carga en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Guarda el resultado como PDF.

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir XML a PDF mediante XSLT y HTML

Utilice este ejemplo cuando los datos XML deban transformarse antes de la generación final del PDF.

1. Transforma la fuente XML con el archivo XSLT en un archivo HTML temporal llamando al método de transformación dedicado.
1. Pase el archivo HTML generado a la función de conversión HTML a PDF existente para que el PDF final utilice el estándar [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) Workflow.
1. Eliminar el archivo HTML temporal en el `finally` bloquear después de que se complete la conversión.
1. Guarde el archivo PDF generado.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Convertir XPS a PDF

Utilice este ejemplo cuando un documento XPS deba convertirse en PDF.

1. Abra la fuente XPS pasando la ruta del archivo y [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF interprete la descripción de página XPS durante la carga del documento.
1. Guarde el PDF convertido.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir XSL-FO a PDF

Utilice este ejemplo cuando el contenido XSL-FO deba renderizarse como PDF.

1. Crear [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) con la ruta XSLT para que la fuente XML pueda transformarse durante la carga.
1. Configure el modo de manejo de errores de análisis para lanzar inmediatamente cuando se encuentre un XSL-FO no válido.
1. Abra la fuente XML en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con esas opciones de carga.
1. Guarde el documento PDF resultante.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Transformar XML a HTML intermedio

Utilice este método cuando los datos XML deben transformarse a HTML antes del paso final de conversión a PDF.

1. Abra los archivos de entrada XML y XSLT como fuentes de transformación.
1. Crear un `Transformer` desde la hoja de estilos XSLT y ejecútala contra la fuente XML.
1. Escriba el archivo HTML transformado en el disco para que la función de conversión PDF posterior pueda cargarlo.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
