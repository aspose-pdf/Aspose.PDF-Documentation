---
title: Obtenha privilégios de documento
linktitle: Obtenha privilégios de documento
type: docs
weight: 10
url: /java/get-document-privileges/
description: Aprenda como inspecionar privilégios de documentos PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilégios de documentos PDF usando Aspose.PDF para Java
Abstract: Aprenda como recuperar privilégios de documento com Aspose.PDF para Java. O exemplo Java cria um objeto PdfFileInfo, lê suas configurações de DocumentPrivilege e imprime os sinalizadores de permissão para impressão, cópia, modificação, anotações, preenchimento de formulários, leitores de tela e montagem.
---
## Obtenha privilégios de documento

Use `PdfFileInfo.getDocumentPrivilege()` para inspecionar quais operações o PDF atual permite.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de entrada.
2. Chame `getDocumentPrivilege()` para recuperar o conjunto de privilégios.
3. Leia os sinalizadores booleanos relevantes do objeto `DocumentPrivilege` retornado.
4. Feche a instância `PdfFileInfo` quando terminar.

### Exemplo Java

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
