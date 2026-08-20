---
title: Extraer fuentes de PDF a través de Java
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Utilice Aspose.PDF para Java para inspeccionar y extraer las fuentes utilizadas en un documento PDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer fuentes de PDF usando Java
Abstract: Este artículo explica cómo inspeccionar las fuentes utilizadas en un documento PDF con Aspose.PDF para Java. Muestra cómo abrir un PDF, llamar a `getFontUtilities().getAllFonts()` e iterar a través de los objetos de fuente resultantes para leer sus nombres.
---
Utilice la extracción de fuentes cuando necesite auditar la tipografía de documentos, inspeccionar recursos integrados o verificar el uso de fuentes antes de la conversión o los flujos de trabajo de archivo.


1. 
Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Llame a `document.getFontUtilities().getAllFonts()` para recopilar cada recurso [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) al que hace referencia el documento.

1. 
Itere a través de los objetos [Fuente](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) extraídos y lea cada nombre de fuente de los metadatos de la fuente.

1. 
Imprima los nombres de las fuentes para que la tipografía del documento pueda auditarse o exportarse.

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
