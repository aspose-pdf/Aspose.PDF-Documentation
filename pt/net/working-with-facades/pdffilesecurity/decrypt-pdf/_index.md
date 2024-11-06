---
title: Decrypt PDF File
type: docs
weight: 20
url: pt/net/decrypt-pdf-file/
description: Este tópico explica como Descriptografar Arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Um documento PDF criptografado com uma senha ou certificado deve ser desbloqueado antes que outra operação possa ser realizada nele. Se você tentar operar em um documento PDF criptografado, você lançará uma exceção. Após desbloquear um PDF criptografado, você pode realizar uma ou mais operações nele.

## Descriptografar Arquivo PDF usando Senha de Proprietário

{{% alert color="primary" %}}
Experimente online <br>
Você pode tentar desbloquear documento usando Aspose.PDF e obter os resultados online neste link:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Para descriptografar um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) e então chamar o método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Você também precisa passar a senha do proprietário para o método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). O trecho de código a seguir mostra como descriptografar um arquivo PDF.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Criar objeto PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Descriptografar documento PDF
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```