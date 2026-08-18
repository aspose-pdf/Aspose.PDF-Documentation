---
title: Alterar senha do arquivo PDF
linktitle: Alterar senha do arquivo PDF
type: docs
weight: 10
url: /java/change-password/
description: Aprenda como alterar senhas de PDF em Java com a fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atualizar senhas de usuário e proprietário de PDF em Java
Abstract: Aprenda como alterar senhas de PDF com Aspose.PDF para Java. O conjunto de exemplos Java abrange a alteração direta de senhas de usuário e proprietário, a alteração de senhas ao redefinir as configurações de segurança e um fluxo de trabalho de alteração de senha no estilo try que retorna um sinalizador de sucesso.
---
## Alterar senha do arquivo PDF

Use `PdfFileSecurity` quando precisar alternar credenciais em um PDF já protegido.

### Passos

1. Crie uma instância `PdfFileSecurity`.
2. Vincule o PDF seguro com `bindPdf`.
3. Chame a sobrecarga `changePassword` apropriada, dependendo se você também deseja redefinir os privilégios e o tamanho da chave.
4. Salve o arquivo atualizado e feche o objeto de segurança.

### Exemplos Java

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
