---
title: 예외 제어 PDF 파일
type: docs
weight: 30
url: /ko/net/control-exception/
description: 이 주제는 PdfFileSecurity 클래스 클래스를 사용하여 PDF 파일에서 예외를 제어하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 클래스는 예외를 제어할 수 있게 합니다. 이를 위해 [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 속성을 false 또는 true로 설정해야 합니다. 작업을 false로 설정하면 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)의 결과는 비밀번호의 정확성에 따라 true 또는 false를 반환합니다.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // PDF 문서 복호화
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("문제가 발생했습니다...");
                Console.WriteLine($"마지막 예외: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

If you set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 속성을 true로 설정하면 try-catch 연산자를 사용하여 작업의 결과를 얻을 수 있습니다.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // PDF 문서 암호 해독
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("문제가 발생했습니다...");
                Console.WriteLine($"Exception: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```