---
title: Obtener y establecer propiedades de página PDF en Java
linktitle: Obtener y establecer propiedades de página
type: docs
weight: 90
url: /es/java/get-and-set-page-properties/
description: Aprende cómo inspeccionar las propiedades de página PDF, como el recuento, los recuadros, la rotación y la información de color, en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecciona el recuento de páginas, los recuadros y el tipo de color en archivos PDF con Java
Abstract: Este artículo explica cómo inspeccionar las propiedades de la página usando Aspose.PDF for Java. Cubre la lectura del recuento de páginas, la generación de párrafos y la verificación del recuento resultante antes de guardar, imprimiendo todos los valores principales de los page box, y la identificación del tipo de color de cada página.
---
Aspose.PDF for Java puede inspeccionar el recuento de páginas, los page box, la rotación y el tipo de color de la página.

## Obtener el recuento de páginas

Utilice este ejemplo cuando necesite leer el número total de páginas en un PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea el tamaño de la colección de páginas.
1. Muestre el recuento total de páginas.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Obtén el recuento de páginas antes de guardar

Usa este ejemplo cuando necesites saber cuántas páginas producirá el contenido generado antes de escribir el archivo.

1. Crea un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega contenido a una página.
1. Procese los párrafos para forzar el cálculo del diseño.
1. Lea el recuento de páginas resultante y muéstrelo.

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

## Obtener propiedades de la caja de página

Utilice este ejemplo cuando necesite inspeccionar todas las dimensiones principales de la caja y los valores de rotación de la página.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y acceda a la página objetivo.
1. Recopile los valores del cuadro de página en un mapa.
1. Muestre las dimensiones y la información de rotación de la página.

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

## Obtenga el tipo de color de cada página

Utilice este ejemplo cuando necesite identificar si las páginas son en blanco y negro, en escala de grises o RGB.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de todas las páginas y lea cada página [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Convierta el valor del enum a texto legible y muestre el resultado.

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
