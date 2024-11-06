---
title: Decryptar Arquivo PDF
type: docs
weight: 20
url: pt/java/decrypt-pdf-file/
description: Este tópico explica como Decryptar Arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Decryptar Arquivo PDF usando Senha do Proprietário

{{% alert color="primary" %}}
Experimente online <br>
Você pode tentar desbloquear o documento usando Aspose.PDF e obter os resultados online neste link:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Para decryptar um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) e então chamar o método [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Você também precisa passar a senha do proprietário para o método [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). O seguinte trecho de código mostra como decryptar um arquivo PDF.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Criar objeto PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Decryptar documento PDF
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```