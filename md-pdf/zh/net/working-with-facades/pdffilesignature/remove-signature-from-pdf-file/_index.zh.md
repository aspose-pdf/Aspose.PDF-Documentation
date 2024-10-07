---
title: 从 PDF 文件中移除签名
type: docs
weight: 20
url: /net/remove-signature-from-pdf/
description: 本节介绍如何使用 PdfFileSignature 类从 PDF 文件中移除签名。
lastmod: "2021-06-05"
draft: false
---

## 从 PDF 文件中移除数字签名

当一个签名被添加到 PDF 文件中时，可以将其移除。您可以移除特定的签名或文件中的所有签名。移除签名的最快方法同时也会移除签名字段，但也可以仅移除签名，保留签名字段，以便文件可以再次签名。

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 RemoveSignature 方法允许您从 PDF 文件中移除签名。 该方法将签名名称作为输入。可以直接指定签名名称，若要删除所有签名，请使用[GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername)方法获取签名名称。

以下代码片段展示了如何从PDF文件中移除数字签名。

```csharp
 public static void RemoveSignature()
        {
            // 创建 PdfFileSignature 对象
            PdfFileSignature pdfSign = new PdfFileSignature();
            // 打开PDF文档
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // 获取签名名称列表
            var sigNames = pdfSign.GetSignNames();
            // 从PDF文件中删除所有签名
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // 保存更新的PDF文件
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### 移除签名但保留签名字段

如上所示，[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) 方法允许您从 PDF 文件中移除签名字段。在使用 9.3.0 版本之前的版本时，签名和签名字段都会被移除。一些开发者希望仅移除签名并保留签名字段，以便可以重新签署文档。要保留签名字段并仅移除签名，请使用以下代码片段。

```csharp
public static void RemoveSignatureButKeepField()
        {
            // 创建 PdfFileSignature 对象
            PdfFileSignature pdfSign = new PdfFileSignature();

            // 打开 PDF 文档
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // 保存更新后的 PDF 文件
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

以下示例显示了如何从字段中删除所有签名。

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // 创建 PdfFileSignature 对象
            PdfFileSignature pdfSign = new PdfFileSignature();

            // 打开 PDF 文档
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // 保存更新后的 PDF 文件
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```