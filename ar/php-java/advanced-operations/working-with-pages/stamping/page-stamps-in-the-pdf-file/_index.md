---
title: إضافة ختم صفحة إلى ملف PDF
linktitle: الأختام في ملف PDF
type: docs
weight: 30
url: ar/php-java/page-stamps-in-the-pdf-file/
description: إضافة ختم صفحة إلى ملف PDF باستخدام فئة PdfPageStamp مع PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة ختم صفحة

يمكن استخدام [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) عندما تحتاج إلى تطبيق ختم مركب يحتوي على رسومات ونصوص وجداول. المثال التالي يوضح كيفية استخدام ختم لإنشاء قرطاسية مثل استخدام Adobe InDesign, Illustrator, Microsoft Word. نفترض أن لدينا بعض المستندات ونريد تطبيق نوعين من الحدود بألوان زرقاء وبرقوقية.

```php

    // فتح المستند
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();  
```