---
title: Alterar Senha de Arquivo PDF
type: docs
weight: 40
url: /java/change-password/
description: Este tópico explica como alterar a senha de um arquivo PDF usando a classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Alterar Senha de um Arquivo PDF

Para alterar a senha de um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) e então chamar o método [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). Você precisa passar a senha de proprietário existente e as novas senhas de usuário e proprietário para o método [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

O trecho de código a seguir mostra como alterar as senhas de um arquivo PDF.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Criar objeto PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```