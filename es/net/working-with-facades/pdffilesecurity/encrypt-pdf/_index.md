---
title: Encryptar Archivo PDF
type: docs
weight: 10
url: /es/net/encrypt-pdf-file/
description: Este tema explica cómo Encriptar un Archivo PDF usando la Clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Encriptar un documento PDF protege su contenido de acceso no autorizado desde el exterior, especialmente durante el intercambio o archivo de archivos.

Los documentos PDF confidenciales pueden ser encriptados y protegidos con contraseña. Solo los usuarios que conozcan la contraseña podrán desencriptar, abrir y ver estos documentos.

Veamos cómo funciona la encriptación de PDF con la biblioteca Aspose.PDF.

## Encriptar Archivo PDF usando Diferentes Tipos de Encriptación y Algoritmos

Para encriptar un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Puedes pasar la contraseña del usuario, la contraseña del propietario y los privilegios al método [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). También necesitas pasar los valores de KeySize y Algorithm a este método.

Revisa una posible lista de tal [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm): 

|**Nombre del miembro**|**Valor**|**Descripción**|
| :- | :- | :- |
|RC4x40|0|RC4 con longitud de clave 40.|
|RC4x128|1|RC4 con longitud de clave 128.|
|AESx128|2|AES con longitud de clave 128.|
|AESx256|3|AES con longitud de clave 256.|

El siguiente fragmento de código te muestra cómo encriptar un archivo PDF.

```csharp
public static void EncryptPDFFile()
        {
            // Crear objeto PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // Encriptar archivo usando encriptación de 256 bits
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```