---
title: Descriptografar arquivo PDF
linktitle: Descriptografar arquivo PDF
type: docs
weight: 20
url: /pt/java/decrypt-pdf-file/
description: Aprenda como descriptografar um PDF em Java com a fachada PdfFileSecurity.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover restrições de segurança de PDF com Java
Abstract: Aprenda como descriptografar um PDF com Aspose.PDF for Java. O conjunto de exemplos Java inclui descriptografia direta por senha do proprietário e um fluxo de trabalho de descriptografia em estilo try que permite tratar falhas sem gerar exceção.
---
## Descriptografar arquivo PDF

Use este fluxo de trabalho quando você possui a senha do proprietário e precisa remover a segurança de um PDF.

### Etapas

1. Crie uma instância de `PdfFileSecurity`.
2. Vincule o PDF criptografado com `bindPdf`.
3. Chame `decryptFile` ou `tryDecryptFile` com a senha do proprietário.
4. Salve a saída se a descriptografia for bem-sucedida.
5. Feche o objeto de segurança.

### Exemplos de Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
