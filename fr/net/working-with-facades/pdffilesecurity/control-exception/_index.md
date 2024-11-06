---
title: Contrôler l'Exception du Fichier PDF
type: docs
weight: 30
url: fr/net/control-exception/
description: Ce sujet explique comment contrôler l'exception sur le fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

La classe [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) vous permet de contrôler les exceptions. Pour ce faire, vous devez définir la propriété [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) à false ou true. Si vous définissez l'opération sur false, le résultat de [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) retournera true ou false selon la justesse du mot de passe.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Déchiffrer le document PDF
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Quelque chose ne va pas...");
                Console.WriteLine($"Dernière exception : {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

Si vous définissez la propriété [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) sur true, vous pouvez alors obtenir le résultat de l'opération en utilisant l'opérateur try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // Décrypter le document PDF
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Quelque chose ne va pas...");
                Console.WriteLine($"Exception: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```