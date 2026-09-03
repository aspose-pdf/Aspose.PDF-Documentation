---
title: Obtener privilegios de documentos
linktitle: Obtener privilegios de documentos
type: docs
weight: 10
url: /java/get-document-privileges/
description: Aprenda a inspeccionar los privilegios de documentos PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilegios de documentos PDF utilizando Aspose.PDF para Java
Abstract: Aprenda cómo recuperar privilegios de documentos con Aspose.PDF para Java. El ejemplo de Java crea un objeto PdfFileInfo, lee su configuración DocumentPrivilege e imprime los indicadores de permiso para imprimir, copiar, modificar, anotaciones, completar formularios, lectores de pantalla y ensamblar.
---
## Obtener privilegios de documentos



Utilice `PdfFileInfo.getDocumentPrivilege()` para inspeccionar qué operaciones permite el PDF actual.


### 
Pasos


1. Cree un objeto `PdfFileInfo` para el PDF de entrada.

2. Llame a `getDocumentPrivilege()` para recuperar el conjunto de privilegios.
3. Lea los indicadores booleanos relevantes del objeto `DocumentPrivilege` devuelto.

4. Cierre la instancia `PdfFileInfo` cuando haya terminado.


### 
Ejemplo de Java

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
