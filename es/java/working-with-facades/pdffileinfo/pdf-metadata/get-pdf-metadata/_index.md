---
title: Obtener metadatos PDF
linktitle: Obtener metadatos PDF
type: docs
weight: 20
url: /es/java/get-pdf-metadata/
description: Aprenda a leer los metadatos PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar metadatos PDF usando Aspose.PDF for Java.
Abstract: Aprenda a recuperar metadatos PDF con Aspose.PDF for Java. El ejemplo Java lee campos estándar como asunto, título, palabras clave, creador, fecha de creación y fecha de modificación, junto con indicadores de estado del archivo y una entrada de metadatos personalizada `Reviewer`.
---
## Obtener metadatos PDF

Este ejemplo lee información estándar del documento, indicadores de estado del archivo y una clave de metadatos personalizada.

### Pasos

1. Crear un `PdfFileInfo` objeto para el PDF de origen.
2. Lee los campos de metadatos estándar, como asunto, título, palabras clave y creador.
3. Inspecciona los indicadores del estado del archivo, como si el archivo es válido, está encriptado, protegido con contraseña o es una cartera.
4. Leer un valor de metadatos personalizado con `getMetaInfo`.
5. Cerrar el `PdfFileInfo` instancia.

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
