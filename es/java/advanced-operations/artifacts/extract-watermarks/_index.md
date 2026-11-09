---
title: Extraer los detalles de la marca de agua PDF en Java
linktitle: Extraer detalles de la marca de agua
type: docs
weight: 50
url: /es/java/extract-watermarks/
description: Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer detalles de la marca de agua en Java
Abstract: Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Java.
---
Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Java.

## Extraer los artefactos de marca de agua de un PDF

Utilice este ejemplo cuando necesite inspeccionar los artefactos de marca de agua existentes y leer su texto o posición.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recorra la colección de artefactos de la página de destino.
1. Filtre los artefactos de paginación de marcas de agua y muestre su texto y rectángulos.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Temas relacionados

- [Agregar marcas de agua](/pdf/es/java/add-watermarks/)
- [Eliminar marcas de agua](/pdf/es/java/remove-watermarks/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
