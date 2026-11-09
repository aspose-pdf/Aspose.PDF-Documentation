---
title: Eliminar fondos de PDF en Java
linktitle: Eliminar fondos
type: docs
weight: 80
url: /es/java/remove-backgrounds/
description: Eliminar artefactos de fondo de la primera página de un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar fondos en Java
Abstract: Eliminar artefactos de fondo de la primera página de un PDF en Java.
---
Eliminar artefactos de fondo de la primera página de un PDF en Java.

## Eliminar artefactos de fondo

Utilice este método cuando los artefactos de fondo existentes deban eliminarse de la página.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recorra la colección de artefactos de la página en orden inverso.
1. Elimine los artefactos cuyo tipo es paginación y subtipo es fondo, luego guarde el documento.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Temas relacionados

- [Agregar fondos](/pdf/es/java/add-backgrounds/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
