---
title: Criptografar arquivo PDF
linktitle: Criptografar arquivo PDF
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Aprenda como criptografar um PDF e configurar permissões em Java com a fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criptografe arquivos PDF e defina permissões de usuário em Java
Abstract: Aprenda como criptografar um PDF com Aspose.PDF para Java. O conjunto de exemplos Java abrange criptografia baseada em senha com privilégios restritos, criptografia focada em permissão e criptografia baseada em AES com tamanho de chave de 256 bits.
---
## Criptografar arquivo PDF

Use `PdfFileSecurity` quando precisar proteger um PDF com senhas e regras de privilégios.

### Passos

1. Crie uma instância `PdfFileSecurity`.
2. Vincule o PDF de origem com `bindPdf`.
3. Construa um objeto `DocumentPrivilege` que corresponda às ações permitidas.
4. Chame a sobrecarga `encryptFile` apropriada para o tamanho da chave e algoritmo que você precisa.
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
