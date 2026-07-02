---
title: 将 PDF 文件转换为 PDF/A
linktitle: 将 PDF 文件转换为 PDF/A
type: docs
weight: 180
url: /zh/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: 本主题向您展示 Aspose.PDF for Java 如何将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF 允许您将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。在此之前，必须对文件进行验证。本文将解释如何操作。

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 合规性。市场上的所有工具都有其各自的“表示”方式来表示 PDF/A 合规性。请查看此文章 on [PDF/A 验证工具](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) 供参考。我们选择 Adobe 产品来验证 Aspose.PDF 生成 PDF 文件的方式，因为 Adobe 是所有与 PDF 相关事物的中心。

在将 PDF 转换为符合 PDF/A 标准的文件之前，请使用 validate 方法验证 PDF。验证结果存储在 XML 文件中，然后该结果也传递给 convert 方法。您还可以使用该方法指定无法转换的元素的操作。 [转换错误操作](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 枚举。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF 转 PDF/A_1b 转换

以下代码片段展示了如何将PDF文件转换为符合PDF/A-1b标准的PDF。

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

如需仅执行验证，请使用以下代码行：

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## PDF 转 PDF/A_3b 转换

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
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

## PDF 转 PDF/A_3a 转换

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
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
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
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

## PDF 转 PDF/A_3U 转换

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
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

## 创建 PDF/A-3 并附加 XML 文件

Aspose.PDF for Android via Java 提供将 PDF 文件转换为 PDF/A 格式的功能，并且还支持将文件作为附件添加到 PDF 文档的能力。若您需要将文件附加到符合 PDF/A 标准的格式，建议使用 com.aspose.pdf.PdfFormat 枚举中的 PDF_A_3A 值，PDF/A_3a 是能够将任何文件格式作为附件附加到符合 PDF/A 的文件的格式。不过，一旦文件被附加后，您应再次将其转换为 Pdf-3a 格式，以修复元数据。请查看以下代码片段。

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
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

