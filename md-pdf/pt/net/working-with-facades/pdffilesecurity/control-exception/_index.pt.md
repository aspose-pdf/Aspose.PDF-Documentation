---
title: Controlar Exceção de Arquivo PDF
type: docs
weight: 30
url: /net/control-exception/
description: Este tópico explica como controlar exceção em Arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

A classe [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) permite que você controle exceções. Para fazer isso, você precisa definir a propriedade [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) como false ou true. Se você definir a operação como false, o resultado de [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) retornará true ou false dependendo da correção da senha.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Descriptografar documento PDF
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Algo deu errado...");
                Console.WriteLine($"Última exceção: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

Se você definir a propriedade [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) como true, então você pode obter o resultado da operação usando o operador try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // Descriptografar documento PDF
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Algo deu errado...");
                Console.WriteLine($"Exceção: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```