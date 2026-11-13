---
title: Contar artefactos PDF en Java
linktitle: Contar artefactos
type: docs
weight: 40
url: /es/java/counting-artifacts/
description: Aprenda cómo inspeccionar y contar artefactos de paginación en documentos PDF usando Java con Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contar artefactos en PDF usando Java
Abstract: Este artículo explica cómo inspeccionar y contar artefactos de paginación en documentos PDF usando Aspose.PDF for Java. Muestra cómo iterar a través de los artefactos de página y contar los subtipos de watermark, background, header y footer.
---
## Contar artefactos de paginación en una página

Utilice este ejemplo cuando necesite un recuento rápido de los subtipos principales de artefactos de paginación en una página.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea la colección de artefactos [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) de la página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Recorra la colección de artefactos [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) de la página y cuente los artefactos de cada subtipo de paginación que necesite informar.

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

## Temas relacionados

- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
- [Extraer detalles de marca de agua](/pdf/es/java/extract-watermarks/)
- [Eliminar fondos](/pdf/es/java/remove-backgrounds/)
- [Eliminar marcas de agua](/pdf/es/java/remove-watermarks/)
- [Eliminar numeración Bates](/pdf/es/java/remove-bates-numbering/)
- [Eliminar encabezados y pies de página](/pdf/es/java/remove-headers-footers/)
