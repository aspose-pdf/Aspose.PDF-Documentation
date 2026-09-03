---
title: Formatear documentos PDF en Java
linktitle: Formato de documento PDF
type: docs
weight: 11
url: /es/java/formatting-pdf-document/
description: Aprende cómo formatear documentos PDF, incrustar fuentes, controlar la configuración del visor y ajustar las opciones de visualización en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formatea la ventana del documento, las fuentes y el comportamiento de zoom en archivos PDF con Java.
Abstract: Este artículo explica cómo formatear documentos PDF usando Aspose.PDF for Java. Cubre la lectura y actualización de la configuración de la ventana del documento, la incrustación de fuentes, la configuración de una fuente predeterminada, la lista de fuentes, la subconfiguración de fuentes incrustadas y el control del factor de zoom inicial.
---
El formato en Aspose.PDF for Java incluye el comportamiento del visor, la incrustación de Font y la configuración de visualización.

## Obtener la configuración de la ventana del documento

Utilice este ejemplo para inspeccionar las preferencias de visualización actuales almacenadas en un documento PDF existente.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea las propiedades de ventana y visualización requeridas del documento.
1. Muestra la configuración actual para inspección o depuración.

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

## Establecer preferencias de ventana del documento

Este ejemplo actualiza cómo se debe mostrar el PDF cuando se abre en un visor compatible.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Establezca las preferencias de ventana, diseño y modo de página requeridas.
1. Guardar el PDF actualizado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Incrustar fuentes en un PDF existente

Utilice este enfoque cuando un documento deba llevar sus fuentes requeridas para una renderización más fiable en otros sistemas.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Habilitar la incrustación estándar de fuentes e iterar a través de las fuentes usadas por cada una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Marcar cualquier no incrustado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objetos para incrustar.
1. Guarde el documento actualizado.

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

## Incrustar fuentes al crear un nuevo PDF

Este ejemplo crea un nuevo PDF y asigna una fuente incrustada al contenido de texto desde el principio.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crear lo requerido [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [Segmento de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), y [Estado de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Resolver el objetivo [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) del repositorio y marcarlo como incrustado.
1. Agregar el contenido de texto a la página y guardar el documento de salida.

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

## Establecer una Font predeterminada para la salida PDF

Utilice este patrón cuando el documento guardado deba recurrir a una fuente específica durante la generación de salida.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) y establecer el nombre de fuente predeterminado.
1. Guarde el documento con las opciones de guardado configuradas.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Obtener todas las fuentes usadas en un PDF

Este ejemplo enumera todas las fuentes detectadas en el documento para que pueda auditar el uso de fuentes antes de exportar o actualizar el archivo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerar los Fonts devueltos por las utilidades de Fonts del documento.
1. Muestra el nombre de cada detectado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Mejorar la incrustación de fuentes mediante la creación de subconjuntos de fuentes

Utilice este enfoque cuando desee reducir la carga útil de fuentes mientras mantiene los datos de fuentes incrustadas alineados con el uso del documento.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ejecute el subconjunto de fuentes mediante las utilidades de fuentes del documento con lo necesario [Estrategia de Subconjunto de Fuentes](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) valores.
1. Guardar el documento optimizado.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Establecer el factor de zoom al abrir el documento

Este ejemplo configura el nivel de zoom inicial que debe aplicarse cuando se abre el PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZDestinoExplícito](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Asignar la acción como la acción de apertura del documento y guardar el resultado.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Obtener el factor de zoom al abrir el documento

Utilice este ejemplo para inspeccionar si un PDF ya define un nivel de zoom explícito para su acción de apertura.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique si la acción de apertura es una [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZDestinoExplícito](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Mostrar el valor de zoom configurado o informar que no se ha establecido ningún zoom.

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
