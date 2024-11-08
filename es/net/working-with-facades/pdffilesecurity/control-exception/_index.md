---
title: Controlar Excepción de Archivo PDF
type: docs
weight: 30
url: /es/net/control-exception/
description: Este tema explica cómo controlar excepciones en un archivo PDF usando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

La clase [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) te permite controlar excepciones. Para hacer esto, necesitas establecer la propiedad [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) a false o true. Si configuras la operación a false, el resultado de [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) devolverá true o false dependiendo de la corrección de la contraseña.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Decrypt PDF document
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Algo salió mal...");
                Console.WriteLine($"Última excepción: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

Si establece la propiedad [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) en verdadero, entonces puede obtener el resultado de la operación utilizando el operador try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // Desencriptar documento PDF
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Algo salió mal...");
                Console.WriteLine($"Excepción: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```