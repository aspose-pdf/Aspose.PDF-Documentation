---
title: Formatear documentos PDF en Java
linktitle: Formatear documento PDF
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Aprenda a formatear documentos PDF, incrustar fuentes, controlar la configuración del visor y ajustar las opciones de visualización en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formatee la ventana del documento, las fuentes y el comportamiento de zoom en archivos PDF con Java
Abstract: Este artículo explica cómo formatear documentos PDF usando Aspose.PDF para Java. Cubre la lectura y actualización de la configuración de la ventana del documento, la incrustación de fuentes, la configuración de una fuente predeterminada, la lista de fuentes, la creación de subconjuntos de fuentes incrustadas y el control del factor de zoom inicial.
---
El formateo en Aspose.PDF para Java incluye el comportamiento del visor, la incrustación de fuentes y la configuración de visualización.


## 
Obtener la configuración de la ventana del documento



Utilice este ejemplo para inspeccionar las preferencias del visor actual almacenadas en un documento PDF existente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Lea la ventana requerida y muestre las propiedades del documento.
1. Genere la configuración actual para inspección o depuración.


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

## 
Establecer preferencias de ventana de documento



Este ejemplo actualiza cómo se debe mostrar el PDF cuando se abre en un visor compatible.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Establezca las preferencias requeridas de ventana, diseño y modo de página.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


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

## 
Incrustar fuentes en un PDF existente



Utilice este enfoque cuando un documento deba contener las fuentes requeridas para una representación más confiable en otros sistemas.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Habilite la incrustación de fuentes estándar e itere a través de las fuentes utilizadas por cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Marque cualquier objeto [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) no incrustado para incrustarlo.

1. 
Guarde el documento actualizado.


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

## 
Incrustar fuentes al crear un nuevo PDF



Este ejemplo crea un nuevo PDF y asigna una fuente incrustada al contenido del texto desde el principio.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Cree el [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), el [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) y el [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) necesarios.

1. 
Resuelva la [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) de destino del repositorio y márquela como incrustada.

1. 
Agregue el contenido del texto a la página y guarde el documento de salida.


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

## 
Establecer una fuente predeterminada para la salida PDF



Utilice este patrón cuando el documento guardado deba recurrir a una fuente específica durante la generación de salida.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) y establezca el nombre de fuente predeterminado.

1. 
Guarde el documento con las opciones de guardado configuradas.


```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## 
Obtenga todas las fuentes utilizadas en un PDF



Este ejemplo enumera todas las fuentes detectadas en el documento para que pueda auditar el uso de las fuentes antes de exportar o actualizar el archivo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Enumere las fuentes devueltas por las utilidades de fuentes del documento.

1. 
Genere el nombre de cada [Fuente] detectada(https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).


```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## 
Mejorar la incrustación de fuentes subdividiendo fuentes



Utilice este enfoque cuando desee reducir la carga útil de fuentes y al mismo tiempo mantener los datos de fuentes incrustados alineados con el uso del documento.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ejecute el subconjunto de fuentes a través de las utilidades de fuentes del documento con los valores [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) requeridos.

1. 
Guarde el documento optimizado.


```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## 
Establecer el factor de zoom de apertura del documento



Este ejemplo configura el nivel de zoom inicial que se debe aplicar cuando se abre el PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).

1. 
Asigne la acción como acción de apertura del documento y guarde el resultado.


```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## 
Obtener el factor de zoom abierto del documento



Utilice este ejemplo para inspeccionar si un PDF ya define un nivel de zoom explícito para su acción de apertura.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Compruebe si la acción abierta es una [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).

1. 
Imprima el valor de zoom configurado o informe que no hay ningún zoom configurado.

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
