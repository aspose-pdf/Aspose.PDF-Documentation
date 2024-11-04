---
title: إضافة صفحات في PDF
linktitle: إضافة صفحات
type: docs
weight: 10
url: /php-java/add-pages/
description: تُعلِّم هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المرغوب في ملف PDF. تعلّم كيفية نقل، إزالة (حذف) الصفحات من ملف PDF باستخدام PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة أو إدراج صفحة في ملف PDF

تتيح لك Aspose.PDF for PHP عبر Java إدراج صفحة في مستند PDF في أي موقع في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF. تحتاج إلى تمرير الموقع الذي تريد إدراج الصفحة الفارغة فيه إلى طريقة الإدراج.
يظهر هذا القسم كيفية إضافة صفحات إلى PDF باستخدام Aspose.PDF for PHP عبر Java.

### إدراج صفحة فارغة في ملف PDF في الموقع المرغوب

يظهر مقتطف الكود التالي كيفية إدراج صفحة فارغة في ملف PDF:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المدخل.
2. أضف الصفحة، وقم بإدراجها في ملف PDF.

1. احفظ ملف PDF الناتج باستخدام طريقة Save.

يوضح لك جزء الكود التالي كيفية إدراج صفحة في ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إضافة صفحة
    $document->getPages()->add();

    // إدراج صفحة فارغة في ملف PDF
    $document->getPages()->insert(2);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```

في المثال أعلاه، أضفنا صفحة فارغة مع المعايير الافتراضية. إذا كنت بحاجة إلى جعل حجم الصفحة مماثلًا لصفحة أخرى في المستند، يجب عليك إضافة
بضعة أسطر من الكود:

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إضافة صفحة
    $page1 = $document->getPages()->add();

    // إدراج صفحة فارغة في ملف PDF
    $page2 = $document->getPages()->insert(2);

    // نسخ معايير الصفحة من الصفحة 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```


### إضافة صفحة فارغة في نهاية ملف PDF

في بعض الأحيان، قد ترغب في التأكد من أن المستند ينتهي بصفحة فارغة. يشرح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) باستخدام ملف PDF المدخل.
2. أضف صفحة، وأدرجها في ملف PDF.
3. احفظ ملف PDF الناتج باستخدام طريقة الحفظ.

يعرض لك مقتطف الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إضافة صفحة
    $document->getPages()->add();

    // إدراج صفحة فارغة في ملف PDF
    $document->getPages()->insert(2);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```