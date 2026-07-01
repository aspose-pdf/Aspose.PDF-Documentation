---
title: 将 PDF/A 转换为 PDF
linktitle: 将 PDF/A 转换为 PDF
type: docs
weight: 350
url: /zh/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: 要将 PDF/A 转换为 PDF，您需要删除原始文档中的限制。Aspose.PDF for Android via Java 可让您轻松简单地解决此问题。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

将 PDF/A 文档转换为 PDF 意味着删除 <abbr title=\"Portable Document Format Archive\"
\" >PDF/A</abbr> 原始文档的限制。类 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 具有方法 RemovePdfaCompliance(..) 用于移除
输入/源文件中的 PDF 合规性信息。

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

如果对文档进行任何更改（例如添加页面），此信息也会被删除。在下面的示例中，添加页面后输出文档失去 PDF/A 合规性。

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




