---
title: 导入和导出书签
type: docs
weight: 20
url: zh/net/import-and-export-bookmarks/
description: 本节解释如何使用 Aspose.PDF Facades 导入和导出书签。
lastmod: "2021-06-05"
draft: false
---

## 从 XML 导入书签到现有 PDF 文件

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) 方法允许您从 XML 文件导入书签到 PDF 文件中。 为了导入书签，您需要创建[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)方法绑定PDF文件。之后，您需要调用[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1)方法。最后，使用[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)方法保存更新后的PDF文件。以下代码片段展示了如何从XML文件导入书签。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## 从现有PDF文件导出书签到XML

ExportBookmarksToXml方法允许您将PDF文件中的书签导出到XML文件。

要导出书签： Create a PdfBookmarkEditor 对象并使用 BindPdf 方法绑定 PDF 文件。
1. 调用 ExportBookmarksToXml 方法。
1. 使用 Save 方法保存更新的 PDF 文件。

以下代码片段向您展示如何将书签导出到 XML 文件中。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}