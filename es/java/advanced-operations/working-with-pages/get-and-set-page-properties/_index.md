---
title: Obtener y configurar propiedades de página PDF en Java
linktitle: Obtener y configurar propiedades de página
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Aprenda a inspeccionar las propiedades de una página PDF, como el recuento, los cuadros, la rotación y la información de color en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspeccione el número de páginas, los cuadros y el tipo de color en archivos PDF con Java
Abstract: Este artículo explica cómo inspeccionar las propiedades de la página usando Aspose.PDF para Java. Cubre la lectura del recuento de páginas, la generación de párrafos y la verificación del recuento resultante antes de guardar, la impresión de todos los valores de los cuadros de páginas principales y la identificación del tipo de color de cada página.
---
Aspose.PDF para Java puede inspeccionar el recuento de páginas, los cuadros de páginas, la rotación y el tipo de color de la página.


## 
Obtener el recuento de páginas



Utilice este ejemplo cuando necesite leer el número total de páginas de un PDF.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Lea el tamaño de la colección de páginas.
1. Imprime el recuento total de páginas.


```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## 
Obtenga el recuento de páginas antes de guardar



Utilice este ejemplo cuando necesite saber cuántas páginas generará el contenido generado antes de escribir el archivo.


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue contenido a una página.

1. Procese los párrafos para forzar el cálculo del diseño.
1. Lea el recuento de páginas resultante y envíelo.


```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## 
Obtener propiedades del cuadro de página



Utilice este ejemplo cuando necesite inspeccionar todas las dimensiones principales del cuadro y los valores de rotación de página.


1. Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y acceda a la página de destino.

1. Recopile los valores del cuadro de página en un mapa.
1. Genere las dimensiones y la información de rotación de página.


```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## 
Obtenga el tipo de color de cada página.



Utilice este ejemplo cuando necesite identificar si las páginas son en blanco y negro, en escala de grises o RGB.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Recorra todas las páginas y lea cada página [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Convierta el valor de enumeración en texto legible y genere el resultado.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
