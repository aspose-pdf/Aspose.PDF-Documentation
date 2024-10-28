---
title: 在 PDF 文件中添加签名
type: docs
weight: 10
url: /java/add-signature-in-pdf/
description: 本节解释如何使用 PdfFileSignature 类在 PDF 文件中处理签名。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件中添加数字签名（facades）

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类允许您在 PDF 文件中添加签名。您需要使用输入和输出 PDF 文件创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的对象。您还需要创建一个矩形对象以添加签名，并且为了设置外观，您可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 对象的 setSignatureAppearance 属性指定图像。

Aspose.Pdf.Facades 还提供不同类型的签名，如 PKCS#1、PKCS#7 和 PKCS#7Detached。
 为了创建特定类型的签名，您需要使用证书文件和密码创建特定类的对象，例如 PKCS1、PKCS7 或 PKCS7Detached。

一旦创建了特定签名类型的对象，您可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的 sign 方法来签署 PDF，并将特定的签名对象传递给此类。您还可以为此方法指定其他属性。最后，您需要使用 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的 save 方法保存已签名的 PDF。以下代码片段向您展示如何在 PDF 文件中添加签名。

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 为签名位置创建一个矩形
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // 设置签名外观
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // 创建三种签名类型中的任意一种
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "我是文档作者", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // 保存输出 PDF 文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

以下代码示例展示了我们用两个签名签署文档的能力。在我们的示例中，我们将第一个签名放在第一页，第二个签名放在第二页。您可以指定您需要的页面。

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // 使用第一个签名签署

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 创建第一个签名位置的矩形
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // 创建第一个签名对象
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "我是文档作者", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // 使用第二个签名签署

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // 创建第二个签名位置的矩形
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // 创建第二个签名对象
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "我是文档审阅者", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true,
                rect2, signature2);

        // 保存输出PDF文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


对于需要签名的带有表单或acroforms的文档，请参见以下示例。您需要使用输入和输出PDF文件创建[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature)类的对象。使用bindPdf进行绑定。创建一个能够添加所需属性的签名。在我们的示例中，它们是“Reason”和“CustomAppearance”。

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // 创建任意三种签名类型之一
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("签署作为作者");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // 保存输出PDF文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


如果我们的文档有两个字段，那么签署它的算法与第一个例子类似。

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // 创建三种签名类型中的任何一种
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("作为作者签名"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // 保存输出的 PDF 文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // 创建三种签名类型中的任何一种
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("作为审阅者签名"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // 保存输出的 PDF 文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```