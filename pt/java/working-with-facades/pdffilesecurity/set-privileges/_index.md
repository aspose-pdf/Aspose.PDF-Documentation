---
title: Definir privilégios em um arquivo PDF existente
linktitle: Definir privilégios em um arquivo PDF existente
type: docs
weight: 40
url: /java/set-privileges/
description: Aprenda como definir privilégios de PDF em Java com a fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerencie permissões de PDF e controles de acesso em Java
Abstract: Aprenda como controlar as permissões de PDF com Aspose.PDF para Java. O conjunto de exemplos Java abrange a aplicação de privilégios sem senhas, a aplicação de privilégios com senhas de usuário e proprietário e um fluxo de trabalho de atualização de privilégios no estilo try que retorna um sinalizador de sucesso.
---
## Defina privilégios em um arquivo PDF existente

Use este fluxo de trabalho quando precisar alterar o que os usuários podem fazer com um PDF existente.

### Passos

1. Crie uma instância `PdfFileSecurity`.
2. Vincule o PDF de origem com `bindPdf`.
3. Crie um objeto `DocumentPrivilege` e configure as ações permitidas.
4. Chame a sobrecarga `setPrivilege` ou `trySetPrivilege` apropriada.
5. Salve o resultado se a atualização for bem-sucedida e feche o objeto.

### Exemplos Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
