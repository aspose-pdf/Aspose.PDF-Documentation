---
title: Export Bookmarks to XML from an Existing PDF File (facades)
type: docs
weight: 20
url: /java/export-bookmark/
description: This section explains how to export bookmarks with Aspose.PDF Facades using PdfBookmarEditor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The exportBookmarksToXml method allows you to export bookmarks from a PDF file to an XML file.

{{% /alert %}}

To export bookmarks:

1. Create a PdfBookmarkEditor object and bind the PDF file using the bindPdf method.
1. Call the exportBookmarksToXml method.

The following code snippet shows you how to export bookmarks to an XML file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, the PdfBookmarkEditor class implements the exportBookmarksToXML and importBookmarksWithXML methods with Stream arguments. As a result, extracted bookmarks can be saved to a stream object.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}

