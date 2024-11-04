---

title: 从 XML 导入书签到现有 PDF 文件 (facades)  
type: docs  
weight: 30  
url: /java/import-bookmark/  
description: 本节解释如何使用 PdfBookmarEditor 类通过 Aspose.PDF Facades 导入书签。  
lastmod: "2021-06-05"  
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

importBookmarksWithXml 方法允许您从 XML 文件中导入书签到 PDF 文件。

要导入书签：

1. 创建一个 PdfBookmarkEditor 对象，并使用 bindPdf 方法绑定 PDF 文件。
1. 调用 importBookmarksWithXml 方法。
1. 使用 save 方法保存更新后的 PDF 文件。

以下代码段显示了如何从 XML 文件中导入书签。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

从 Aspose.PDF for Java 9.0.0 开始，PdfBookmarkEditor 类实现了带有流参数的 exportBookmarksToXML 和 importBookmarksWithXML 方法。因此，可以从流对象导入提取的书签。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}