---
title: Criptografar e descriptografar arquivos PDF em Java
linktitle: Criptografar e descriptografar arquivo PDF
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda como definir privilégios de PDF, criptografar arquivos, descriptografar PDFs protegidos e alterar senhas em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Defina permissões de PDF e gerencie criptografia em Java
Abstract: Este artigo explica como proteger arquivos PDF usando Aspose.PDF para Java. Abrange a criptografia de documentos com senhas de usuário e proprietário, aplicação de restrições de permissão, descriptografia de arquivos, alteração de senhas e configuração de privilégios com ou sem métodos seguros para exceções.
---
Aspose.PDF para Java expõe operações de segurança de PDF por meio da fachada `PdfFileSecurity`.

## Criptografe um PDF com senhas de usuário e proprietário

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ao documento PDF de origem.
1. Configure as propriedades [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) e [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) exigidas pelo exemplo.
1. Salve o documento PDF atualizado através de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

## Criptografe um PDF com um algoritmo específico

`encryptPdfWithEncryptionAlgorithm` usa `KeySize.x256` junto com `Algorithm.AES` para aplicar configurações de criptografia mais fortes.

## Descriptografar um PDF protegido

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ao documento PDF de origem.
1. Descriptografe o documento protegido com a senha do proprietário.
1. Salve o documento PDF atualizado através de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

O conjunto de exemplos também inclui `tryDecryptPdfWithoutException`, que retorna `false` em vez de lançar quando a descriptografia falha.

## Alterar senhas e redefinir a segurança

A classe `PdfFileSecurityExamples` demonstra:

- `changeUserAndOwnerPassword` para substituir ambas as senhas.
- `changePasswordAndResetSecurity` para alterar senhas e reaplicar privilégios em uma única etapa.
- `tryChangePasswordWithoutException` para um fluxo de alteração de senha sem lançamento.

## Definir privilégios de documento

Para restringir ações como impressão e cópia:

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ao documento PDF de origem.
1. Defina as permissões [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) ou opções de criptografia necessárias.
1. Defina as propriedades exigidas pelo exemplo.
1. Salve o documento PDF atualizado através de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
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
```
