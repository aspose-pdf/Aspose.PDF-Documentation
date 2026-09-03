---
title: Clase PdfViewer
linktitle: Clase PdfViewer
type: docs
weight: 135
url: /es/java/pdfviewer-class/
description: Aprenda cómo usar la fachada PdfViewer en Java para decodificar páginas PDF e inspeccionar la configuración relacionada con el visor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decodifique páginas PDF e inspeccione datos del visor en Java con PdfViewer
Abstract: Esta sección explica cómo usar la fachada PdfViewer en Aspose.PDF for Java para tareas de decodificación de páginas e inspección relacionada con el visor. Los ejemplos actuales de Java cubren la generación de todas las páginas como imágenes, la decodificación de una página específica y la inspección del recuento de páginas, tipo de coordenadas, resolución y configuración del visor vinculado.
---
El Java `PdfViewerExamples` La clase demuestra los principales flujos de trabajo del visor disponibles a través de la API Facades.

## Decodificar todas las páginas PDF

Utilice este flujo de trabajo cuando cada página del PDF de origen deba renderizarse como una imagen.

### Pasos

1. Crear y configurar un `PdfViewer` instancia.
2. Vincular el PDF de origen con `bindPdf`.
3. Llamar `decodeAllPages()` para renderizar el documento en un `BufferedImage` matriz.
4. Guarde cada página decodificada en un archivo de imagen de salida.
5. Cierre el archivo PDF enlazado.

### Ejemplo de Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Decodifica una página PDF específica

Utiliza este flujo de trabajo cuando solo se necesita renderizar una página a una imagen.

### Pasos

1. Crear y configurar un `PdfViewer` instancia.
2. Vincula el PDF de origen.
3. Llamar `decodePage()` para la página que deseas renderizar.
4. Guarde la página decodificada en un archivo de imagen de salida.
5. Cierre el visor.

### Ejemplo de Java

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## Inspeccionar metadatos PDF

Utilice este flujo de trabajo cuando necesite información del documento relacionada con el visor antes de renderizar o imprimir.

### Pasos

1. Crear y configurar un `PdfViewer` instancia.
2. Vincula el PDF de origen.
3. Lea la cantidad de páginas, el tipo de coordenadas y la resolución de renderizado.
4. Utilice o imprima los valores recuperados.
5. Cierre el archivo PDF enlazado.

### Ejemplo de Java

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## Inspeccionar la configuración del visor enlazado

Utilice este flujo de trabajo cuando necesite confirmar o ajustar el comportamiento del visor después de vincular el PDF.

### Pasos

1. Crear y configurar un `PdfViewer` instancia.
2. Vincula el PDF de origen.
3. Establezca opciones del visor como ajuste automático de tamaño, rotación automática y visibilidad del cuadro de diálogo de impresión.
4. Lea la configuración del visor activo y el recuento de páginas.
5. Cierre el visor.

### Ejemplo de Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
