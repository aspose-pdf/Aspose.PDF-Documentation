---
title: Clase Visor de PDF
linktitle: Clase Visor de PDF
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Aprenda a utilizar la fachada de PdfViewer en Java para decodificar páginas PDF e inspeccionar la configuración relacionada con el visor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decodifica páginas PDF e inspecciona los datos del visor en Java con PdfViewer
Abstract: Esta sección explica cómo utilizar la fachada de PdfViewer en Aspose.PDF para Java para la decodificación de páginas y tareas de inspección relacionadas con el visor. Los ejemplos actuales de Java cubren la representación de todas las páginas en imágenes, la decodificación de una página específica y la inspección del recuento de páginas, el tipo de coordenadas, la resolución y la configuración del visor enlazado.
---
La clase Java `PdfViewerExamples` demuestra los principales flujos de trabajo del visor disponibles a través de la API de Fachadas.


## 
Decodifica todas las páginas PDF



Utilice este flujo de trabajo cuando cada página del PDF de origen deba representarse como una imagen.


### 
Pasos


1. Cree y configure una instancia `PdfViewer`.
2. Vincule el PDF de origen con `bindPdf`.

3. Llame a `decodeAllPages()` para representar el documento en una matriz `BufferedImage`.

4. Guarde cada página decodificada en un archivo de imagen de salida.

5. Cierre el archivo PDF encuadernado.


### 
Ejemplo de Java

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

## Decodificar una página PDF específica



Utilice este flujo de trabajo cuando solo sea necesario representar una página en una imagen.


### 
Pasos


1. Cree y configure una instancia `PdfViewer`.

2. Enlaza el PDF de origen.
3. Llame a `decodePage()` para obtener la página que desea representar.

4. Guarde la página decodificada en un archivo de imagen de salida.

5. Cierra el visor.


### 
Ejemplo de Java


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

## 
Inspeccionar metadatos PDF

Utilice este flujo de trabajo cuando necesite información del documento relacionada con el visor antes de renderizarlo o imprimirlo.


### 
Pasos


1. Cree y configure una instancia `PdfViewer`.

2. Enlaza el PDF de origen.

3. Lea el recuento de páginas, el tipo de coordenadas y la resolución de representación.
4. Utilice o imprima los valores recuperados.

5. Cierre el archivo PDF encuadernado.


### 
Ejemplo de Java


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

## 
Inspeccionar la configuración del visor enlazado



Utilice este flujo de trabajo cuando necesite confirmar o ajustar el comportamiento del visor después de vincular el PDF.

### Pasos


1. Cree y configure una instancia `PdfViewer`.

2. Enlaza el PDF de origen.

3. Configure las opciones del visor, como el cambio de tamaño automático, la rotación automática y la visibilidad del cuadro de diálogo de impresión.

4. Lea la configuración del visor activo y el recuento de páginas.
5. Cierra el visor.


### 
Ejemplo de Java

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
