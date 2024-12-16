---
title: 将 PDF 文件转换为 PDF/A 
linktitle: 将 PDF 文件转换为 PDF/A 
type: docs
weight: 180
url: /zh/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: 本主题向您展示如何使用 Aspose.PDF for Java 将 PDF 文件转换为符合 PDF/A 的 PDF 文件。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF 允许您将 PDF 文件转换为符合 PDF/A 的 PDF 文件。在此之前，必须对文件进行验证。本文将解释如何进行。

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 合规性。市场上的所有工具都有自己对 PDF/A 合规性的“表示”。请参考这篇关于[PDF/A 验证工具](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)的文章。我们选择 Adobe 产品来验证 Aspose.PDF 如何生成 PDF 文件，因为 Adobe 是所有与 PDF 相关事物的核心。

在将 PDF 转换为符合 PDF/A 的文件之前，请使用 validate 方法验证 PDF。
 验证结果存储在一个XML文件中，然后这个结果也会传递给convert方法。您还可以使用[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)枚举来指定不能转换的元素的操作。

{{% alert color="primary" %}}

在线试用。您可以在此链接查看Aspose.PDF转换的质量并在线查看结果[products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF到PDF/A_1b转换

以下代码片段展示了如何将PDF文件转换为符合PDF/A-1b标准的PDF。

```java
public void convertPDFtoPDFa1b() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为符合PDF/A标准的文档
        // 在转换过程中，还会进行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // 保存输出文档
        document.save(pdfaFileName.toString());
    }
```

要仅执行验证，请使用以下代码行：

```java
public void ValidatePDF_A_1B() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 验证为符合PDF/A的文档

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("文档有效");
        }
        else {
            resultMessage.setText("文档无效");
        }
    }
```

## PDF到PDF/A_3b转换

```java
    public void convertPDFtoPDFa3b() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为符合PDF/A的文档
        // 在转换过程中，也会执行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // 保存输出文档
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF 到 PDF/A_3a 转换

```java
public void convertPDFtoPDFa3a() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为符合 PDF/A 的文档
        // 在转换过程中，也会进行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // 保存输出文档
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF 到 PDF/A_2a 转换

```java
public void convertPDFtoPDFa2a() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为符合 PDF/A 的文档
        // 在转换过程中，也会进行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 保存输出文档
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## PDF到PDF/A_3U转换

```java
 public void convertPDFtoPDFa3u() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为PDF/A兼容文档
        // 在转换过程中，也会进行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 保存输出文档
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 创建PDF/A-3并附加XML文件

Aspose.PDF for Android via Java 提供了将PDF文件转换为PDF/A格式的功能，并且还支持将文件作为附件添加到PDF文档的功能。
 在需要将文件附加到 PDF/A 合规格式的情况下，我们建议使用 com.aspose.pdf.PdfFormat 枚举中的 PDF_A_3A 值，PDF/A_3a 是一种支持将任何文件格式作为附件附加到 PDF/A 合规文件的格式。然而，一旦文件被附加，您应该再次将其转换为 Pdf-3a 格式，以修复元数据。请查看以下代码片段。

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 转换为 PDF/A 合规文档
        // 在转换过程中，也会进行验证
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // 保存输出文档
        try {
            // 加载 XML 文件
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "示例 xml 文件");
            // 将附件添加到文档的附件集合中
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```