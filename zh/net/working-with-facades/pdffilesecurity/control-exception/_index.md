---
title: 控制异常 PDF 文件
type: docs
weight: 30
url: zh/net/control-exception/
description: 本主题解释如何使用 PdfFileSecurity 类控制 PDF 文件上的异常。
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 类允许您控制异常。为此，您需要将 [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 属性设置为 false 或 true。如果您将操作设置为 false，[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 的结果将根据密码的正确性返回 true 或 false。

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // 解密 PDF 文档
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("出现问题...");
                Console.WriteLine($"最后的异常: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

如果将 [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 属性设置为 true，则可以使用 try-catch 操作符获取操作结果。

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // 解密 PDF 文档
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("出错了...");
                Console.WriteLine($"异常: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```