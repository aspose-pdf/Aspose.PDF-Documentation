---

title: استيراد الإشارات المرجعية من XML إلى ملف PDF موجود (واجهات)
type: docs
weight: 30
url: ar/java/import-bookmark/
description: يوضح هذا القسم كيفية استيراد الإشارات المرجعية باستخدام Aspose.PDF Facades باستخدام فئة PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك طريقة importBookmarksWithXml استيراد الإشارات المرجعية إلى ملف PDF من ملف XML.

لاستيراد الإشارات المرجعية:

1. إنشاء كائن PdfBookmarkEditor وربط ملف PDF باستخدام طريقة bindPdf.
2. استدعاء طريقة importBookmarksWithXml.
3. حفظ ملف PDF المحدث باستخدام طريقة save.

يظهر مقطع الشيفرة التالي كيفية استيراد الإشارات المرجعية من ملف XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

من Aspose.PDF لـ Java 9.0.0، تقوم فئة PdfBookmarkEditor بتنفيذ طرق exportBookmarksToXML وimportBookmarksWithXML مع حجج Stream. ونتيجة لذلك، يمكن استيراد الإشارات المرجعية المستخرجة من كائن stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}