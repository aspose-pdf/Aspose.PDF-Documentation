---
title: Decrypt PDF File
type: docs
weight: 20
url: es/net/decrypt-pdf-file/
description: Este tema explica cómo Desencriptar un Archivo PDF usando la Clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Un documento PDF cifrado con una contraseña o certificado debe ser desbloqueado antes de que se pueda realizar otra operación en él. Si intenta operar en un documento PDF cifrado, lanzará una excepción. Después de desbloquear un PDF cifrado, puede realizar una o más operaciones en él.

## Desencriptar un Archivo PDF usando la Contraseña del Propietario

{{% alert color="primary" %}}
Pruebe en línea <br>
Puede intentar desbloquear el documento usando Aspose.PDF y obtener los resultados en línea en este enlace:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Para desencriptar un archivo PDF, necesita crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Necesitas pasar la contraseña del propietario al método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). El siguiente fragmento de código te muestra cómo descifrar un archivo PDF.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Crear objeto PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Descifrar documento PDF
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```