---
title: Extraer fuentes de PDF 
linktitle: Extraer fuentes
type: docs
weight: 30
url: /es/java/extract-fonts-from-pdf/
description: Cómo extraer fuentes de PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método `Document.IDocumentFontUtilities.getAllFonts()` proporcionado en la clase Document. Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // La ruta al directorio de documentos.
    String filePath = "<... ingrese el nombre del archivo ...>";
    
    // Cargar documento PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```