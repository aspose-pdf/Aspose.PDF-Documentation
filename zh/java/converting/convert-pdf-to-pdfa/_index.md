---
title: 将 PDF 转换为 PDF/A 格式
linktitle: 将 PDF 转换为 PDF/A 格式
type: docs
weight: 100
url: zh/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF 文件转换为符合 PDF/A 的 PDF 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java** 允许您将 PDF 文件转换为符合 PDF/A 的 PDF 文件。在此之前，必须对文件进行验证。本文将解释如何进行。

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 的符合性。市场上的所有工具都有自己的 PDF/A 符合性“表示”。请查看这篇关于 [PDF/A 验证工具](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) 的文章以供参考。我们选择 Adobe 产品来验证 Aspose.PDF 如何生成 PDF 文件，因为 Adobe 是与 PDF 相关的一切的核心。

在将 PDF 转换为符合 PDF/A 的文件之前，请使用验证方法验证 PDF。
 验证结果存储在一个XML文件中，然后该结果也会传递给convert方法。您还可以使用[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)枚举来指定无法转换的元素的操作。

## PDF到PDF/A_1b的转换

以下代码片段显示了如何将PDF文件转换为符合PDF/A-1b的PDF。

```java
// 打开文档
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// 转换为符合PDF/A标准的文档
// 在转换过程中，也会进行验证
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// 保存输出文档
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

若只进行验证，请使用以下代码行：

```java
// 打开文档
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// 验证PDF是否符合PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("有效");
} else {
    System.out.println("无效");
}
document.close();
```

## PDF 到 PDF/A_3b 转换

从 [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java) 开始，API 还支持将 PDF 文件转换为 PDF/A_3b 格式。

```java
// 打开文档
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// 转换为符合 PDF/A 的文档
// 在转换过程中，还会进行验证
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// 保存输出文档
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF 到 PDF/A_3a 转换

从 [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java) 开始，API 还支持将 PDF 文件转换为 PDF/A_3a 格式。

```java
// 打开文档
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// 转换为符合 PDF/A 的文档
// 在转换过程中，还会进行验证
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// 保存输出文档
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## PDF 到 PDF/A_2a 转换

从 [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java) 版本开始，该 API 提供将 PDF 文件转换为 PDF/A3 格式的功能。

```java
    public static void ConvertPDFtoPDFa2a() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // 转换为符合 PDF/A 标准的文档
        // 在转换过程中，也会进行验证
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 保存输出文档
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF 到 PDF/A_3U 转换

从 Aspose.PDF for Java 17.2.0 版本开始，该 API 提供将 PDF 文件转换为 PDF/A_3U 格式的功能。

```java
    public static void ConvertPDFtoPDFa3u() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // 转换为符合 PDF/A 标准的文档
        // 在转换过程中，也会进行验证
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 保存输出文档
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## 创建 PDF/A-3 并附加 XML 文件

Aspose.PDF for Java 提供了将 PDF 文件转换为 PDF/A 格式的功能，并且还支持将文件作为附件添加到 PDF 文档中的功能。如果您需要将文件附加到符合 PDF/A 的格式，我们建议使用 com.aspose.pdf.PdfFormat 枚举中的 PDF_A_3A 值，PDF/A_3a 是提供将任何文件格式作为附件附加到符合 PDF/A 的文件的功能的格式。但是，一旦文件被附加，您应该再次将其转换为 Pdf-3a 格式，以便修复元数据。请查看下面的代码片段。

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // 将页面添加到 PDF 文件
        doc.getPages().add();
        // 加载 XML 文件
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "示例 xml 文件");
        // 将附件添加到文档的附件集合中
        doc.getEmbeddedFiles().add(fileSpecification);
        // 执行 PDF/A_3a 转换
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* 或 PDF_A_3B */, ConvertErrorAction.Delete);
        // 保存最终的 PDF 文件
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF 到 PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}