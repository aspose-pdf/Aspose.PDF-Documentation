---
title: Obtener metadatos PDF
linktitle: Obtener metadatos PDF
type: docs
weight: 20
url: /es/java/get-pdf-metadata/
description: Aprenda cómo leer los metadatos PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar metadatos PDF usando Aspose.PDF for Java.
Abstract: Aprenda cómo recuperar los metadatos PDF con Aspose.PDF for Java. El ejemplo Java lee campos estándar como asunto, título, palabras clave, creador, fecha de creación y fecha de modificación, junto con banderas de estado del archivo y una entrada de metadatos personalizada `Reviewer`.
---
## Obtener metadatos PDF

Este ejemplo lee la información estándar del documento, las banderas de estado del archivo y una clave de metadatos personalizada.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de origen.
2. Lea los campos de metadatos estándar, como asunto, título, palabras clave y creador.
3. Inspeccione los indicadores de estado del archivo, como si el archivo es válido, está cifrado, protegido con contraseña o es un portafolio.
4. Lea un valor de metadatos personalizados con `getMetaInfo`.
5. Cierre la instancia de `PdfFileInfo`.

### Ejemplo de Java

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
