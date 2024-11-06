---
title: 如何数字签名PDF
linktitle: 数字签名PDF
type: docs
weight: 10
url: zh/java/digitally-sign-pdf-file/
description: 使用Java对PDF文档进行数字签名。使用基于Java的应用程序和PDF库验证或验证数字签名的PDF。您可以使用PKCS1证书来认证PDF文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

使用签名对PDF文档进行签名时，您基本上确认其内容应保持“原样”。因此，之后进行的任何更改都会使签名失效，从而可以知道文档是否已被更改。首先认证文档，允许您指定用户可以对文档进行更改而不使认证失效。

换句话说，文档仍然被认为保持其完整性，接收者仍然可以信任该文档。有关更多详细信息，请访问认证和签署PDF。

为了实现上述要求，已经进行了以下公共API更改。

isCertified(…) 方法已添加到 PdfFileSignature 类。

## 使用数字签名签署 PDF

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // 使用 PKCS7/PKCS7Detached
                                                                                              // 对象
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // 保存输出 PDF 文件
        signature.save(outFile);
    }
```

## 为数字签名添加时间戳

Aspose.PDF for Java 支持使用时间戳服务器或 Web 服务对 PDF 进行数字签名。

为了实现这一要求，已将 [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) 类添加到 Aspose.PDF 命名空间。请查看以下代码片段，该片段获取时间戳并将其添加到 PDF 文档中：

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // 用户/密码可以省略
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // 创建三种签名类型中的任何一种
        signature.sign(1, "签名原因", "联系方式", "位置", true, rect, pkcs);
        // 保存输出 PDF 文件
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```