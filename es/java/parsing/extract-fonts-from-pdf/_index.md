---
title: Extraer fuentes de PDF mediante Java
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /es/java/extract-fonts-from-pdf/
description: Utilice Aspose.PDF for Java para inspeccionar y extraer las fuentes utilizadas en un documento PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer fuentes de PDF usando Java
Abstract: Este artículo explica cómo inspeccionar las fuentes utilizadas en un documento PDF con Aspose.PDF for Java. Muestra cómo abrir un PDF, llamar a `getFontUtilities().getAllFonts()`, y recorrer los objetos de fuente resultantes para leer sus nombres.
---
Utilice la extracción de fuentes cuando necesite auditar la tipografía del documento, inspeccionar recursos incrustados o verificar el uso de fuentes antes de conversiones o flujos de trabajo de archivado.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Llamar `document.getFontUtilities().getAllFonts()` para recopilar cada [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) recurso referenciado por el documento.
1. Iterar a través de los extraídos [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objetos y leer cada nombre de fuente de los metadatos de la fuente.
1. Imprima los nombres de fuente para que la tipografía del documento pueda ser auditada o exportada.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
