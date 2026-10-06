---
title: Definir privilégios em um arquivo PDF existente
linktitle: Definir privilégios em um arquivo PDF existente
type: docs
weight: 40
url: /pt/java/set-privileges/
description: Saiba como definir privilégios de PDF em Java com a fachada PdfFileSecurity.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciar permissões de PDF e controles de acesso em Java
Abstract: Saiba como controlar permissões de PDF com Aspose.PDF for Java. O conjunto de exemplos em Java abrange a aplicação de privilégios sem senhas, a aplicação de privilégios com senhas de usuário e proprietário, e um fluxo de trabalho de atualização de privilégios no estilo try que retorna um indicador de sucesso.
---
## Definir privilégios em um arquivo PDF existente

Use este fluxo de trabalho quando precisar alterar o que os usuários podem fazer com um PDF existente.

### Etapas

1. Criar um `PdfFileSecurity` instância.
2. Vincular o PDF de origem com `bindPdf`.
3. Criar um `DocumentPrivilege` objeto e configure as ações permitidas.
4. Chame o apropriado `setPrivilege` ou `trySetPrivilege` sobrecarga.
5. Salve o resultado se a atualização for bem-sucedida, e então feche o objeto.

### Exemplos de Java

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
