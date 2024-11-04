---
title: تقسيم ملف PDF برمجيًا
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /php-java/split-document/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات PHP الخاصة بك. 
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

يمكنك تقسيم ملفات PDF باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا الرابط: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

يوضح هذا الموضوع كيفية تقسيم صفحات PDF باستخدام Aspose.PDF لـ PHP عبر Java إلى ملفات PDF فردية في تطبيقات PHP الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام PHP، يمكن اتباع الخطوات التالية:

1. قم بالتكرار خلال صفحات مستند PDF من خلال مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. لكل تكرار، قم بإنشاء كائن Document جديد وأضف كائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الفردي إلى المستند الفارغ.
1. احفظ ملف PDF الجديد باستخدام طريقة Save.

يظهر لك مقتطف الكود PHP التالي كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```php

    // افتح المستند
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // قم بالتكرار عبر جميع الصفحات
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```