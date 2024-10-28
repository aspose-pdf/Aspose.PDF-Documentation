---
title: 在 PDF 文件中添加签名
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: 本节介绍如何使用 PdfFileSignature 类向 PDF 文件添加签名。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件中添加数字签名

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类允许您在 PDF 文件中添加签名。 你需要使用输入和输出 PDF 文件创建一个 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的对象。你还需要创建一个 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 对象，在你想要添加签名的位置，并且为了设置外观，你可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 对象的 [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) 属性指定一个图像。Aspose.Pdf.Facades 还提供不同种类的签名，如 PKCS#1、PKCS#7 和 PKCS#7Detached。为了创建特定类型的签名，你需要使用证书文件和密码创建特定类的对象，比如 **PKCS1**、**PKCS7** 或 **PKCS7Detached**。

一旦创建了特定签名类型的对象，你可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) 方法来签署 PDF，并将特定的签名对象传递给这个类。 你还可以为此方法指定其他属性。最后，您需要使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存已签名的 PDF。以下代码片段展示了如何在 PDF 文件中添加签名。

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 为签名位置创建一个矩形
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // 设置签名外观
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // 创建三种签名类型之一
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "我是文档作者", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // 保存输出的 PDF 文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
以下代码示例展示了我们在文档上签署两个签名的能力。在我们的示例中，我们在第一页上放置第一个签名，在第二页上放置第二个签名。您可以指定您需要的页面。

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // 使用第一个签名

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 为第一个签名位置创建一个矩形
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 创建第一个签名对象
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "我是文档作者", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // 使用第二个签名

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 为第二个签名位置创建一个矩形
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 创建第二个签名对象
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "我是文档审阅者", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

            // 保存输出 PDF 文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

对于需要签名的包含表单或acroforms的文档，请参见以下示例。
您需要使用输入和输出PDF文件创建一个[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)类的对象。使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1)进行绑定。创建一个可以添加所需属性的签名。在我们的示例中，它们是“Reason”和“CustomAppearance”。

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // 创建任意三种签名类型之一
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "签名为作者",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // 保存输出PDF文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

如果我们的文档有两个字段，签署它的算法类似于第一个例子。

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // 创建三种签名类型中的任意一种
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "作为作者签名",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // 保存输出的 PDF 文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 创建三种签名类型中的任意一种
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "作为审阅者签名",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // 保存输出的 PDF 文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```