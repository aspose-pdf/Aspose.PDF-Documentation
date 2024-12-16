---
title: دمج PDF برمجياً
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/php-java/merge-pdf-documents/
description: تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام PHP.
lastmod: "2024-06-05"
---

الآن، دمج ملفات pdf هو أحد المهام المطلوبة بشكل كبير.
توضح هذه المقالة كيفية دمج ملفات PDF متعددة في مستند PDF واحد باستخدام Aspose.PDF for PHP عبر Java. المثال مكتوب بلغة Java، لكن يمكن استخدام API في لغات برمجة أخرى. يتم دمج ملفات PDF بحيث يتم إلحاق الأول في نهاية المستند الآخر.

## دمج ملفات PDF باستخدام PHP

{{% alert color="primary" %}}

يمكنك دمج ملفات PDF باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا الرابط: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

لدمج ملفين PDF:

1. أنشئ كائنين [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)، يحتوي كل منهما على أحد ملفات PDF المدخلة.

1. ثم استدعاء طريقة Add لمجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) لكائن Document الذي تريد إضافة ملف PDF الآخر إليه.
1. مرر مجموعة PageCollection لكائن Document الثاني إلى طريقة Add لمجموعة PageCollection الأولى.
1. وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة Save.

يُظهر مقتطف الشيفرة التالي كيفية دمج ملفات PDF باستخدام PHP.

```php
    // فتح المستند الأول
    $document1 = new Document($inputFile1);
    
    // فتح المستند الثاني
    $document2 = new Document($inputFile2);

    // إضافة صفحات المستند الثاني إلى الأول
    $document1->getPages()->add($document2->getPages());

    // حفظ ملف الإخراج المدموج
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```