---
title: Control Exception PDF File
type: docs
weight: 30
url: /net/control-exception/
description: This topic explains how control exception on PDF File using PdfFileSecurity Class Class.
lastmod: "2021-06-05"
draft: false
---

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Decrypt PDF document
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Something wrong...");
                Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```