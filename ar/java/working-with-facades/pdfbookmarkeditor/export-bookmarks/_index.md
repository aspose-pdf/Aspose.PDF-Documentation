---
title: تصدير الإشارات المرجعية إلى XML من ملف PDF موجود (واجهات)
type: docs
weight: 20
url: /ar/java/export-bookmark/
description: يوضح هذا القسم كيفية تصدير الإشارات المرجعية باستخدام Aspose.PDF Facades باستخدام فئة PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

تسمح لك طريقة exportBookmarksToXml بتصدير الإشارات المرجعية من ملف PDF إلى ملف XML.

{{% /alert %}}

لتصدير الإشارات المرجعية:

1. قم بإنشاء كائن PdfBookmarkEditor واربط ملف PDF باستخدام طريقة bindPdf.
2. استدعاء طريقة exportBookmarksToXml.

يُظهر لك مقتطف الشيفرة التالي كيفية تصدير الإشارات المرجعية إلى ملف XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0، تقوم فئة PdfBookmarkEditor بتنفيذ أساليب exportBookmarksToXML وimportBookmarksWithXML مع متغيرات Stream. نتيجة لذلك، يمكن حفظ العلامات المرجعية المستخرجة في كائن تدفق.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}