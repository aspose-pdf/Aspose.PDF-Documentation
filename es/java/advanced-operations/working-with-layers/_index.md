---
title: Trabajar con capas de PDF usando Java
linktitle: Trabajar con capas de PDF
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Aprenda a agregar, bloquear, extraer, aplanar y fusionar capas de PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar capas de PDF con Java
Abstract: Este artículo explica cómo trabajar con capas de PDF, también conocidas como grupos de contenido opcionales, utilizando Aspose.PDF para Java. Aprenda a agregar capas a una página, bloquear una capa existente, extraer contenido de capas a archivos o secuencias, aplanar contenido en capas y fusionar capas en una sola.
---
Aspose.PDF para Java expone capas de PDF a través de la API `Layer` en cada página. Puede crear grupos de contenido opcionales, modificar su comportamiento y exportar o aplanar su contenido cuando sea necesario.


## 
Agregar capas a una página PDF


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree y configure los objetos [Capa](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) requeridos en la página.
1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```


El ejemplo completo crea tres capas separadas con contenido de líneas rojas, verdes y azules.


## 
Bloquear una capa


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Acceda a la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino y obtenga su colección [Capa](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Bloquee el objetivo [Capa](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).

1. 
Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
