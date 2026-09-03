---
title: Cambiar el tamaño de página PDF en Java
linktitle: Cambiar tamaño de página
type: docs
weight: 40
url: /es/java/change-page-size/
description: Aprende cómo leer y cambiar las dimensiones de la página PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lee y actualiza las dimensiones y cajas de la página con Java
Abstract: Este artículo muestra cómo leer y modificar las dimensiones de la página PDF usando Aspose.PDF for Java. Cubre la obtención del tamaño de la página, la medición del tamaño de la página con rotación aplicada y la actualización de la primera página a un nuevo tamaño mientras se imprimen las dimensiones de la caja antes y después del cambio.
---
Aspose.PDF for Java puede tanto informar las dimensiones de la página como actualizarlas.

## Cambiar el tamaño de la página

Utilice este ejemplo cuando necesite cambiar el tamaño de una página existente e inspeccionar los recuadros de la página antes y después del cambio.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtener el destino [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y imprimir sus valores actuales de la caja.
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

## Obtener el tamaño de la página

Utilice este ejemplo cuando necesite leer las dimensiones visibles de una página.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenga el rectángulo de la página con el manejo de rotación habilitado.
1. Muestre el ancho y la altura de la página.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Obtener el tamaño de la página con la rotación aplicada

Utilice este ejemplo cuando necesite comparar las dimensiones de la página antes y después de tener en cuenta la rotación.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Rotar el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Lee el rectángulo de la página con y sin manejo de rotación y muestra ambos valores.

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
