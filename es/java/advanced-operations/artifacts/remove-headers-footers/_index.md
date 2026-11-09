---
title: Eliminar encabezados y pies de página PDF en Java
linktitle: Eliminar encabezados y pies de página
type: docs
weight: 110
url: /es/java/remove-headers-footers/
description: Eliminar los artefactos de encabezado y pie de página de la primera página de un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar encabezados y pies de página en Java
Abstract: Eliminar los artefactos de encabezado y pie de página de la primera página de un PDF en Java.
---
Eliminar los artefactos de encabezado y pie de página de la primera página de un PDF en Java.

## Eliminar artefactos de encabezado y pie de página

Utilice este enfoque cuando los artefactos de encabezado y pie de página existentes deban eliminarse de la página.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recorra la colección de artefactos de la página en orden inverso.
1. Elimine los artefactos de paginación cuyo subtipo es encabezado o pie de página, luego guarde el documento.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Temas relacionados

- [Agregar encabezados y pies de página](/pdf/es/java/artifacts-header-footer/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
