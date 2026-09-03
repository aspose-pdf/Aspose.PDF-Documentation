---
title: Contar artefactos PDF en Java
linktitle: Contando artefactos
type: docs
weight: 40
url: /es/java/counting-artifacts/
description: Aprenda cómo inspeccionar y contar los artefactos de paginación en documentos PDF usando Java con Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando artefactos en PDF usando Java
Abstract: Este artículo explica cómo inspeccionar y contar los artefactos de paginación en documentos PDF usando Aspose.PDF for Java. Muestra cómo iterar a través de los artefactos de página y contar los subtipos de marca de agua, fondo, encabezado y pie de página.
---
## Contar artefactos de paginación en una página

Utilice este ejemplo cuando necesite un recuento rápido de los principales subtipos de artefactos de paginación en una página.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea el [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) colección del destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Iterar a través de la página [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) colección y contar cada subtipo de paginación que necesites informar.

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
