---
title: 从PDF文件中移除签名
type: docs
weight: 20
url: zh/java/remove-signature-from-pdf/
description: 本节介绍如何使用PdfFileSignature类处理PDF文件中的签名。
lastmod: "2021-06-05"
draft: false
---

## 从PDF文件中移除数字签名

当一个签名被添加到PDF文件中时，可以将其移除。您可以移除特定的签名，也可以移除文件中的所有签名。移除签名的最快方法同时也会移除签名域，但也可以只移除签名，保留签名域，以便文件可以再次签名。

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature)类的RemoveSignature方法允许您从PDF文件中移除签名。
 此方法将签名名称作为输入。可以直接指定签名名称，若要删除所有签名，请使用[getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--)方法获取签名名称。

以下代码片段展示了如何从PDF文件中移除数字签名。

```java
 public static void RemoveSignature() {
        // 创建 PdfFileSignature 对象
        PdfFileSignature pdfSign = new PdfFileSignature();
        // 打开 PDF 文档
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // 获取签名名称列表
        List<String> sigNames = pdfSign.getSignNames();
        // 从 PDF 文件中移除所有签名
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removed " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // 保存更新后的 PDF 文件
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### 移除签名但保留签名字段

如上所示，[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的 [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) 方法可以让您从 PDF 文件中移除签名字段。在使用 9.3.0 之前的版本时，签名和签名字段都会被移除。一些开发人员希望仅移除签名并保留签名字段，以便可以重新签署文档。要保留签名字段并仅移除签名，请使用以下代码片段。

```java
 public static void RemoveSignatureButKeepField() {
        // 创建 PdfFileSignature 对象
        PdfFileSignature pdfSign = new PdfFileSignature();

        // 打开 PDF 文档
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // 保存更新后的 PDF 文件
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


以下示例展示了如何从字段中移除所有签名。

```java
public static void RemoveSignatureButKeepField2() {
        // 创建 PdfFileSignature 对象
        PdfFileSignature pdfSign = new PdfFileSignature();

        // 打开 PDF 文档
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // 保存更新的 PDF 文件
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```