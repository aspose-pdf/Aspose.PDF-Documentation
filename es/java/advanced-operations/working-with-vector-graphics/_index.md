---
title: Trabajar con gráficos vectoriales en Java
linktitle: Trabajar con gráficos vectoriales
type: docs
weight: 100
url: /es/java/working-with-vector-graphics/
description: Aprenda cómo extraer, mover, eliminar, copiar y exportar gráficos vectoriales en documentos PDF usando Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilice GraphicsAbsorber para inspeccionar y manipular gráficos vectoriales PDF en Java.
Abstract: Este artículo explica cómo trabajar con gráficos vectoriales en Aspose.PDF for Java utilizando la clase GraphicsAbsorber. Aprende cómo inspeccionar elementos vectoriales en una página, moverlos o eliminarlos, copiar gráficos entre páginas y exportar contenido vectorial a SVG.
---
Aspose.PDF for Java expone contenido vectorial a través de `GraphicsAbsorber` y `GraphicElement` objetos. Esto le permite inspeccionar los elementos vectoriales de bajo nivel en una página y luego actualizarlos, eliminarlos, copiarlos o exportarlos.

## Inspeccionar gráficos vectoriales en una página

Utilice este ejemplo cuando necesite enumerar elementos vectoriales y inspeccionar su página, posición y recuento de operadores.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) y visite la página de destino.
1. Itere a través de lo absorbido [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) objetos y muestre sus propiedades.

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## Mover gráficos vectoriales en la página

Use este ejemplo cuando todos los elementos vectoriales detectados deban desplazarse a una nueva posición.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite la página de destino con [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) y suprima temporalmente las actualizaciones.
1. Cambie la posición de cada elemento absorbido, reanude las actualizaciones y guarde el documento.

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## Eliminar gráficos vectoriales por posición con eliminación de elementos

Utiliza este ejemplo cuando los elementos vectoriales dentro de un rectángulo específico deban eliminarse uno a uno.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite la página con [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) y defina el objetivo [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Elimine los elementos coincidentes, reanuda las actualizaciones y guarde el documento.

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## Eliminar gráficos vectoriales eliminando una colección

Utilice este ejemplo cuando los elementos vectoriales coincidentes deban recopilarse primero y luego eliminarse en una sola operación de página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite la página con [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) y recopile los elementos coincidentes.
1. Elimine los gráficos recopilados del contenido de la página y guarde el documento actualizado.

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## Copiar gráficos vectoriales a otro elemento de página, elemento por elemento

Utilice este ejemplo cuando cada elemento vectorial absorbido deba agregarse individualmente a una nueva página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada una página de destino.
1. Visite la página de origen con [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Agregue cada [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) a la página de destino y guarde el documento.

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## Copiar gráficos vectoriales a otra página como una colección

Utilice este ejemplo cuando toda la colección de gráficos vectoriales absorbidos deba copiarse a una nueva página en una sola llamada.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada una página de destino.
1. Visite la página de origen con [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Agregue la colección de gráficos absorbidos a la página de destino y guarde el documento.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
