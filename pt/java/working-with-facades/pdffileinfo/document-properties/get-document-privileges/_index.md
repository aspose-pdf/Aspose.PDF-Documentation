---
title: Obter privilégios do documento
linktitle: Obter privilégios do documento
type: docs
weight: 10
url: /pt/java/get-document-privileges/
description: Saiba como inspecionar os privilégios de documentos PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilégios de documentos PDF usando Aspose.PDF for Java
Abstract: Saiba como recuperar os privilégios de documento com Aspose.PDF for Java. O exemplo Java cria um objeto PdfFileInfo, lê suas configurações DocumentPrivilege e imprime os indicadores de permissão para impressão, cópia, modificação, anotações, preenchimento de formulário, leitores de tela e montagem.
---
## Obter privilégios do documento

Use `PdfFileInfo.getDocumentPrivilege()` para inspecionar quais operações o PDF atual permite.

### Etapas

1. Crie um objeto `PdfFileInfo` para o PDF de entrada.
2. Ligar `getDocumentPrivilege()` para recuperar o conjunto de privilégios.
3. Leia as flags booleanas relevantes do retornado objeto `DocumentPrivilege`.
4. Feche o `PdfFileInfo` instância quando concluído.

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
