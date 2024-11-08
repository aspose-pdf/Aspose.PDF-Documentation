---
title: Kontrol File PDF Pengecualian
type: docs
weight: 30
url: /id/net/control-exception/
description: Topik ini menjelaskan bagaimana mengontrol pengecualian pada File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Kelas [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) memungkinkan Anda untuk mengontrol pengecualian. Untuk melakukan ini, Anda perlu mengatur properti [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) ke false atau true. Jika Anda mengatur operasi ke false, hasil dari [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) akan mengembalikan true atau false tergantung pada kebenaran kata sandi.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // Dekripsi dokumen PDF
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("Ada yang salah...");
                Console.WriteLine($"Pengecualian terakhir: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

Jika Anda mengatur properti [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) ke true, maka Anda dapat mendapatkan hasil operasi menggunakan operator try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // Decrypt PDF document
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Something wrong...");
                Console.WriteLine($"Exception: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```