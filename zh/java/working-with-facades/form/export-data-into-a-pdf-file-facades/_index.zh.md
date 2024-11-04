---
title: 从PDF文件导出数据到XML（外观）
type: docs
weight: 20
url: /java/export-data-into-a-pdf-file-facades/
description: 本节解释如何使用Aspose.PDF Facades的Form类从PDF文件导出数据到XML。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类允许您使用 exportXml 方法从 PDF 文件中导出数据到 XML 文件。为了将数据导出到 XML，您需要创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类的对象，使用 bindPDF 方法打开源 PDF 表单，然后使用 OutputStream 对象调用 exportXml 方法。最后，您可以关闭 OutputStream 对象并处理 Form 对象。以下代码片段展示了如何将数据导出到 XML 文件。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}