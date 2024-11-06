---
title: تصدير البيانات إلى XML من ملف PDF (Facades)
type: docs
weight: 20
url: ar/java/export-data-into-a-pdf-file-facades/
description: يشرح هذا القسم كيفية تصدير البيانات إلى XML من ملف PDF باستخدام Aspose.PDF Facades باستخدام فئة Form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تسمح لك فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة exportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)، وفتح نموذج PDF المصدر باستخدام طريقة bindPDF ثم استدعاء طريقة exportXml باستخدام كائن OutputStream. أخيرًا، يمكنك إغلاق كائن OutputStream والتخلص من كائن Form. يوضح لك مقطع الشفرة التالي كيفية تصدير البيانات إلى ملف XML.


{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}