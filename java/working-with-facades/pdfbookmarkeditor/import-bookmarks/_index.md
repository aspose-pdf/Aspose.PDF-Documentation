---
title: Import Bookmarks from XML to an Existing PDF File (facades)
type: docs
weight: 30
url: /java/import-bookmark/
description: This section explains how to import bookmarks with Aspose.PDF Facades using PdfBookmarEditor Class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The importBookmarksWithXml method allows you to import bookmarks into a PDF file from an XML file.

To import bookmarks:

1. Create a PdfBookmarkEditor object and bind the PDF file using the bindPdf method.
1. Call the importBookmarksWithXml method.
1. Save the updated PDF file using the save method.

The following code snippet shows how to import bookmarks from an XML file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, the PdfBookmarkEditor class implements the exportBookmarksToXML and importBookmarksWithXML methods with Stream arguments. As a result, extracted bookmarks can be imported from a stream object.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}
