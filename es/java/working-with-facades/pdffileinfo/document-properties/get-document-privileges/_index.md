---
title: Obtener privilegios del documento
linktitle: Obtener privilegios del documento
type: docs
weight: 10
url: /es/java/get-document-privileges/
description: Aprenda cómo inspeccionar los privilegios de documentos PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilegios de documentos PDF usando Aspose.PDF for Java
Abstract: Aprenda cómo recuperar los privilegios del documento con Aspose.PDF for Java. El ejemplo en Java crea un objeto PdfFileInfo, lee sus configuraciones DocumentPrivilege y muestra las banderas de permiso para imprimir, copiar, modificar, anotaciones, rellenar formularios, lectores de pantalla y ensamblado.
---
## Obtener privilegios del documento

Utilice `PdfFileInfo.getDocumentPrivilege()` para inspeccionar qué operaciones permite el PDF actual.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de entrada.
2. Llame `getDocumentPrivilege()` para recuperar el conjunto de privilegios.
3. Lea los indicadores booleanos relevantes del objeto `DocumentPrivilege` devuelto.
4. Cierre la instancia de `PdfFileInfo` cuando termine.

### Ejemplo en Java

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
