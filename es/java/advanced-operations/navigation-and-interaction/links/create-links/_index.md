---
title: Crear enlaces PDF en Java
linktitle: Crear enlaces
type: docs
weight: 10
url: /java/create-links/
description: Aprenda a crear enlaces PDF internos, externos y remotos en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree anotaciones de enlaces en archivos PDF con Java
Abstract: Este artículo muestra cómo crear anotaciones de enlaces usando Aspose.PDF para Java. Cubre acciones de inicio, navegación remota de documentos, navegación de páginas dentro de documentos y enlaces web basados ​​en URI adjuntando acciones a objetos LinkAnnotation.
---
Aspose.PDF para Java usa `LinkAnnotation` junto con un objeto de acción para definir el comportamiento del enlace.


## 
Crear un enlace de acción de lanzamiento



Utilice este ejemplo cuando una anotación de enlace deba iniciar un archivo o destino externo.


1. Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y seleccione la página de destino.

1. Cree una [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) y configure su borde y color.
1. Asigne una [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) y guarde el documento.


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

## 
Crear un enlace de acceso remoto



Utilice este ejemplo cuando el enlace deba abrir una página en otro documento PDF.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) en la página de destino.
1. Asigne una [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) y guarde el archivo de salida.


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

## 
Crear un enlace de acceso interno



Utilice este ejemplo cuando el enlace deba navegar a otra página dentro del mismo documento PDF.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) y configure su apariencia.
1. Asigne una [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) a la página de destino y guarde el documento.


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

## 
Crear un enlace URI



Utilice este ejemplo cuando el enlace deba abrir un recurso web a través de una acción de URI.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) en la página.
1. Asigne una [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) y guarde el archivo de salida.

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
