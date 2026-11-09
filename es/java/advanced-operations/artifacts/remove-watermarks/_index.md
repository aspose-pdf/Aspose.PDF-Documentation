---
title: Eliminar marcas de agua PDF en Java
linktitle: Eliminar marcas de agua
type: docs
weight: 90
url: /es/java/remove-watermarks/
description: Eliminar artefactos de marca de agua de la primera página de un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar marcas de agua en Java
Abstract: Eliminar artefactos de marca de agua de la primera página de un PDF en Java.
---
Eliminar artefactos de marca de agua de la primera página de un PDF en Java.

## Eliminar artefactos de marca de agua

El ejemplo solo elimina de la primera página los artefactos de tipo `Pagination` y subtipo `Watermark`. Las marcas de agua visibles almacenadas como texto normal de la página, imágenes o anotaciones permanecen en el PDF.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recorra la colección de artefactos de la página en orden inverso.
1. Elimine los artefactos de paginación cuyo subtipo es marca de agua, y luego guarde el documento.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Temas relacionados

- [Agregar marcas de agua](/pdf/es/java/add-watermarks/)
- [Extraer detalles de la marca de agua](/pdf/es/java/extract-watermarks/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
