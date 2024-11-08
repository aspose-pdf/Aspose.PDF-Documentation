---
title: 将 PDF/A 转换为 PDF
linktitle: 将 PDF/A 转换为 PDF
type: docs
weight: 350
url: /zh/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: 要将 PDF/A 转换为 PDF，您需要从原始文档中移除限制。Aspose.PDF for Android via Java 可以轻松简单地解决这个问题。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

将 PDF/A 文档转换为 PDF 意味着从原始文档中移除 <abbr title="Portable Document Format Archive
">PDF/A</abbr> 限制。类 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 具有方法 RemovePdfaCompliance(..)，用于移除输入/源文件中的 PDF 合规性信息。

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // 创建 Document 对象
            document = new Document(pdfaDocumentFileName);

            // 移除 PDF/A 合规性信息
            document.removePdfaCompliance();

            // 以 XML 格式保存输出
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


该信息还会在您对文档进行任何更改时（例如，添加页面）被移除。在以下示例中，添加页面后输出文档失去了PDF/A合规性。

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // 创建 Document 对象
        document = new Document(pdfaDocumentFileName);

        // 添加新（空）页面会移除PDF/A合规性信息。
        document.getPages().add();

        // 保存更新后的文档
        document.save(pdfDocumentFileName);
    }
```