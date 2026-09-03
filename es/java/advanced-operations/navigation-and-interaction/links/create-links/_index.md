---
title: Crear enlaces PDF en Java
linktitle: Crear enlaces
type: docs
weight: 10
url: /es/java/create-links/
description: Aprenda cómo crear enlaces PDF internos, externos y remotos en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear anotaciones de enlaces en archivos PDF con Java
Abstract: Este artículo muestra cómo crear anotaciones de enlace usando Aspose.PDF for Java. Cubre acciones de lanzamiento, navegación de documento remoto, navegación de página dentro del documento y enlaces web basados en URI al adjuntar acciones a objetos LinkAnnotation.
---
Aspose.PDF for Java usa `LinkAnnotation` junto con un objeto de acción para definir el comportamiento del enlace.

## Crear un enlace de acción de lanzamiento

Utilice este ejemplo cuando una anotación de enlace debe lanzar un archivo externo o un objetivo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y seleccione la página de destino.
1. Crear un [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) y configure su borde y color.
1. Asignar un [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) y guardar el documento.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Crear un enlace remoto de navegación

Utilice este ejemplo cuando el enlace debe abrir una página en otro documento PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) en la página de destino.
1. Asignar un [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) y guarde el archivo de salida.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Crear un enlace interno de salto

Utilice este ejemplo cuando el enlace deba navegar a otra página dentro del mismo documento PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) y configure su apariencia.
1. Asignar un [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) a la página de destino y guardar el documento.

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Crear un enlace URI

Utilice este ejemplo cuando el enlace debe abrir un recurso web a través de una acción URI.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) en la página.
1. Asignar un [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) y guarde el archivo de salida.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
