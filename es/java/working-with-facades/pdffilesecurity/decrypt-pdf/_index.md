---
title: Desencriptar Archivo PDF
type: docs
weight: 20
url: es/java/decrypt-pdf-file/
description: Este tema explica cómo desencriptar un archivo PDF usando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Desencriptar Archivo PDF usando Contraseña de Propietario

{{% alert color="primary" %}}
Prueba en línea <br>
Puede intentar desbloquear el documento usando Aspose.PDF y obtener los resultados en línea en este enlace:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Para desencriptar un archivo PDF, necesita crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) y luego llamar al método [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). También necesita pasar la contraseña de propietario al método [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). El siguiente fragmento de código muestra cómo desencriptar un archivo PDF.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Crear objeto PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Desencriptar documento PDF
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```