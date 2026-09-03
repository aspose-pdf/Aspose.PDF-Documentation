---
title: Crear archivos PDF en Java
linktitle: Crear documento PDF
type: docs
weight: 10
url: /es/java/create-pdf-document/
description: Aprenda cómo crear archivos PDF y generar PDFs buscables en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree archivos PDF y documentos PDF buscables con Java
Abstract: Este artículo muestra cómo crear documentos PDF usando Aspose.PDF for Java. Cubre la creación de un PDF nuevo desde cero y la conversión de un documento basado en imágenes a un PDF searchable proporcionando la salida HOCR de un motor OCR externo.
---
Aspose.PDF for Java admite tanto la creación simple de documentos como los flujos de trabajo de PDF buscables asistidos por OCR.

## Crear un nuevo documento PDF

Usa este enfoque cuando necesites generar un archivo PDF simple desde cero.

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y añádelo a la página.
1. Guardar el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Crear un PDF buscable

El `createSearchablePdf` ejemplos de uso `Document.convert(...)` con un `CallBackGetHocr` implementación. La devolución de llamada escribe la imagen fuente en un archivo temporal, invoca a Tesseract con el `hocr` opción, lee el marcado HOCR generado y lo devuelve a Aspose.PDF.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear el `CallBackGetHocr` callback y convierta el documento fuente a contenido PDF buscable.
1. Guardar el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## Obtener la configuración de la ventana del documento

Utilice este ejemplo para inspeccionar las preferencias de visualización actuales almacenadas en un documento PDF existente.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea las propiedades de ventana y visualización requeridas del documento.
1. Imprima la configuración actual para inspección o depuración.

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

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Establezca las preferencias de ventana, diseño y modo de página requeridas.
1. Guardar el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Habilitar la incrustación estándar de fuentes e iterar a través de las fuentes usadas por cada una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
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

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crea lo requerido [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), y [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Resolver el objetivo [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) del repositorio y marcarlo como incrustado.
1. Agrega el contenido de texto a la página y guarda el documento de salida.

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

## Establecer una fuente predeterminada para la salida PDF

Utilice este patrón cuando el documento guardado deba recurrir a una fuente específica durante la generación de la salida.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) y establezca el nombre de la fuente predeterminada.
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

## Obtén todas las fuentes usadas en un PDF

Este ejemplo enumera cada fuente detectada en el documento para que pueda auditar el uso de fuentes antes de exportar o actualizar el archivo.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerar los fonts devueltos por las utilidades de fuentes del documento.
1. Mostrar el nombre de cada detectado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Mejorar la incrustación de Font mediante la subsegmentación de fuentes

Utilice este enfoque cuando desee reducir la carga útil de font mientras mantiene los datos de font incrustados alineados con el uso del documento.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ejecute la subconfiguración de fuentes a través de las utilidades de fuentes del documento con lo requerido [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) valores.
1. Guarda el documento optimizado.

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

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
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

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique si la acción de apertura es una [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) con un [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
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
