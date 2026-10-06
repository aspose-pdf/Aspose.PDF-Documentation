---
title: Criptografar arquivo PDF
linktitle: Criptografar arquivo PDF
type: docs
weight: 30
url: /pt/java/encrypt-pdf-file/
description: Aprenda como criptografar um PDF e configurar permissões em Java com a fachada PdfFileSecurity.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criptografar arquivos PDF e definir permissões de usuário em Java
Abstract: Aprenda como criptografar um PDF com Aspose.PDF for Java. O conjunto de exemplos em Java abrange criptografia baseada em senha com privilégios restritos, criptografia focada em permissões e criptografia baseada em AES com tamanho de chave de 256 bits.
---
## Criptografar arquivo PDF

Use `PdfFileSecurity` quando precisar proteger um PDF com senhas e regras de privilégios.

### Etapas

1. Crie uma instância de `PdfFileSecurity`.
2. Vincule o PDF de origem com `bindPdf`.
3. Construa um objeto `DocumentPrivilege` que corresponde às ações permitidas.
4. Chame o apropriado `encryptFile` sobrecarga para o tamanho da chave e algoritmo que você precisa.
5. Salve o arquivo protegido e feche o objeto.

### Exemplos Java

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

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
