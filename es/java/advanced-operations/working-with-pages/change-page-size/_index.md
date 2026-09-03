---
title: Cambiar el tamaño de la página PDF en Java
linktitle: Cambiar el tamaño de la página
type: docs
weight: 40
url: /java/change-page-size/
description: Aprenda a leer y cambiar las dimensiones de una página PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leer y actualizar dimensiones y cuadros de página con Java
Abstract: Este artículo demuestra cómo leer y modificar las dimensiones de una página PDF usando Aspose.PDF para Java. Cubre cómo obtener el tamaño de la página, medir el tamaño de la página con la rotación aplicada y actualizar la primera página a un nuevo tamaño mientras se imprimen las dimensiones del cuadro antes y después del cambio.
---
Aspose.PDF para Java puede informar las dimensiones de la página y actualizarlas.


## 
Cambiar el tamaño de la página



Utilice este ejemplo cuando necesite cambiar el tamaño de una página existente e inspeccionar los cuadros de la página antes y después del cambio.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Obtenga la [Página] de destino (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e imprima los valores de cuadro actuales.
1. Establezca el nuevo tamaño de página y guarde el documento.


```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## 
Obtener el tamaño de la página



Utilice este ejemplo cuando necesite leer las dimensiones visibles de una página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Obtenga el rectángulo de la página con el manejo de rotación habilitado.
1. Imprima el ancho y alto de la página.


```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 
Obtenga el tamaño de página con la rotación aplicada



Utilice este ejemplo cuando necesite comparar las dimensiones de la página antes y después de tener en cuenta la rotación.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Gire el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Lea el rectángulo de la página con y sin manejo de rotación y genere ambos valores.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
