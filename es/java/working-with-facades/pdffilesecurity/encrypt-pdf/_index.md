---
title: Encriptar Archivo PDF
type: docs
weight: 10
url: /es/java/encrypt-pdf-file/
description: Este tema explica cómo Encriptar un Archivo PDF usando la Clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Encriptar Archivo PDF usando Diferentes Tipos de Encriptación y Algoritmos

Para encriptar un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) y luego llamar al método [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Puedes pasar la contraseña de usuario, la contraseña del propietario y los privilegios al método [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). También necesitas pasar los valores de KeySize y Algorithm a este método.

El siguiente fragmento de código te muestra cómo encriptar un archivo PDF.

```java
    public static void EncryptPDFFile() {
        // Crear objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Encriptar archivo usando encriptación de 256 bits
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```