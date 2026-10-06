---
title: Criptografar e descriptografar arquivos PDF em Java
linktitle: Criptografar e descriptografar arquivo PDF
type: docs
weight: 70
url: /pt/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda como definir privilégios de PDF, criptografar arquivos, descriptografar PDFs protegidos e alterar senhas em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir permissões de PDF e gerenciar a criptografia em Java
Abstract: Este artigo explica como proteger arquivos PDF usando Aspose.PDF for Java. Ele aborda a criptografia de documentos com senhas de usuário e proprietário, a aplicação de restrições de permissão, a descriptografia de arquivos, a alteração de senhas e a definição de privilégios com ou sem métodos seguros contra exceções.
---
Aspose.PDF for Java expõe operações de segurança PDF através da fachada `PdfFileSecurity`.

## Criptografar um PDF com senhas de usuário e proprietário

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) para o documento PDF de origem.
1. Configure o [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) e [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) propriedades exigidas pelo exemplo.
1. Salve o documento PDF atualizado através [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Criptografar um PDF com um algoritmo específico

`encryptPdfWithEncryptionAlgorithm` usa `KeySize.x256` juntamente com `Algorithm.AES` para aplicar configurações de criptografia mais fortes.

## Descriptografar um PDF protegido

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) para o documento PDF de origem.
1. Descriptografe o documento protegido com a senha de proprietário.
1. Salve o documento PDF atualizado através [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Alterar senhas e redefinir segurança

A classe `PdfFileSecurityExamples` demonstra:

- `changeUserAndOwnerPassword` para substituir ambas as senhas.
- `changePasswordAndResetSecurity` para alterar senhas e reaplicar privilégios em um único passo.
- `tryChangePasswordWithoutException` para um fluxo de mudança de senha que não lança exceções.

## Definir privilégios do documento

Para restringir ações como impressão e cópia:

1. Crie e vincule a fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) para o documento PDF de origem.
1. Defina o necessário [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) opções de permissões ou criptografia.
1. Defina as propriedades necessárias para o exemplo.
1. Salve o documento PDF atualizado através [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
