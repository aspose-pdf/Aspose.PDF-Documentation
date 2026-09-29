---
title: Trabajar con capas PDF usando Java
linktitle: Trabajar con capas PDF
type: docs
weight: 50
url: /es/java/working-with-pdf-layers/
description: Aprenda cómo agregar, bloquear, extraer, aplanar y combinar capas PDF en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar capas PDF con Java
Abstract: Este artículo explica cómo trabajar con capas PDF, también conocidas como Grupos de contenido opcional, usando Aspose.PDF for Java. Aprenda cómo agregar capas a una página, bloquear una capa existente, extraer el contenido de la capa a archivos o flujos, aplanar el contenido en capas y combinar capas en una sola.
---
Aspose.PDF for Java expone capas PDF a través del `Layer` API en cada página. Puede crear grupos de contenido opcional, modificar su comportamiento y exportar o aplanar su contenido cuando sea necesario.

## Agregar capas a una página PDF

1. Cree un nuevo PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree y configure lo necesario [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) objetos en la página.
1. Guarde el PDF de salida [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Bloquear una capa

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda al objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y obtenga su colección [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Bloquee el objetivo [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
