---
title: Contar artefactos PDF en Java
linktitle: Contar artefactos
type: docs
weight: 40
url: /java/counting-artifacts/
description: Aprenda a inspeccionar y contar artefactos de paginación en documentos PDF usando Java con Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contar artefactos en PDF usando Java
Abstract: Este artículo explica cómo inspeccionar y contar artefactos de paginación en documentos PDF usando Aspose.PDF para Java. Muestra cómo recorrer los artefactos de la página y contar los subtipos de marcas de agua, fondos, encabezados y pies de página.
---
## Contar artefactos de paginación en una página



Utilice este ejemplo cuando necesite un recuento rápido de los principales subtipos de artefactos de paginación en una página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Lea la colección [Artefacto](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) de la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Itere a través de la colección de páginas [Artefacto](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) y cuente cada subtipo de paginación que necesita informar.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
