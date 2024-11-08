---
title: Criptografar Arquivo PDF
type: docs
weight: 10
url: /pt/java/encrypt-pdf-file/
description: Este tópico explica como Criptografar Arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Criptografar Arquivo PDF usando Diferentes Tipos de Criptografia e Algoritmos

Para criptografar um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) e então chamar o método [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Você pode passar a senha do usuário, a senha do proprietário e os privilégios para o método [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Você também precisa passar os valores de Tamanho da Chave e Algoritmo para este método.

O trecho de código a seguir mostra como criptografar um arquivo PDF.

```java
    public static void EncryptPDFFile() {
        // Criar objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Criptografar arquivo usando criptografia de 256 bits
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```