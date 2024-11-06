---
title: 从现有PDF文件导出书签到XML（外观）
type: docs
weight: 20
url: zh/java/export-bookmark/
description: 本节解释如何使用PdfBookmarEditor类通过Aspose.PDF Facades导出书签。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

exportBookmarksToXml方法允许您将PDF文件中的书签导出到XML文件。

{{% /alert %}}

要导出书签：

1. 创建一个PdfBookmarkEditor对象，并使用bindPdf方法绑定PDF文件。
2. 调用exportBookmarksToXml方法。

以下代码片段展示了如何将书签导出到XML文件。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

从 Aspose.PDF for Java 9.0.0 开始，PdfBookmarkEditor 类实现了带有 Stream 参数的 exportBookmarksToXML 和 importBookmarksWithXML 方法。因此，提取的书签可以保存到流对象中。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}