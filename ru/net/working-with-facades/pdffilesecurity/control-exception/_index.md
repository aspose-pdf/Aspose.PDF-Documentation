---
title: Управление Исключениями в PDF Файле
type: docs
weight: 30
url: /ru/net/control-exception/
description: Эта тема объясняет, как управлять исключениями в PDF файле с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Класс [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) позволяет управлять исключениями. Для этого необходимо установить свойство [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) в значение false или true. Если вы установите операцию в false, результат [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) вернет true или false в зависимости от правильности пароля.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Расшифровать PDF документ
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Что-то пошло не так...");
                Console.WriteLine($"Последнее исключение: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

Если вы установите свойство [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) в значение true, то сможете получить результат операции, используя оператор try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // Расшифровать PDF документ
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Что-то пошло не так...");
                Console.WriteLine($"Исключение: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```