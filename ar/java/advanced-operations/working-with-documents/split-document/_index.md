---
title: تقسيم ملفات PDF برمجياً
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: ar/java/split-document/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات Java الخاصة بك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

يمكنك تقسيم ملفات PDF باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا الرابط: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

يوضح هذا الموضوع كيفية تقسيم صفحات PDF باستخدام Aspose.PDF for Java إلى ملفات PDF فردية في تطبيقات Java الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF بصفحة واحدة باستخدام Java، يمكن اتباع الخطوات التالية:

1. قم بالتكرار خلال صفحات مستند PDF من خلال مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. لكل تكرار، قم بإنشاء كائن Document جديد وأضف كائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الفردي إلى المستند الفارغ.
1. احفظ ملف PDF الجديد باستخدام طريقة Save.

يُظهر لك مقطع الشيفرة البرمجية التالي بلغة Java كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // قم بالمرور عبر جميع الصفحات
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```