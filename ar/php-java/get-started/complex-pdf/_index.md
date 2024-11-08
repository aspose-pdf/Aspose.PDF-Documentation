---
title: إنشاء ملف PDF معقد 
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 60
url: /ar/php-java/complex-pdf-example/
description: Aspose.PDF لـ PHP عبر Java يتيح لك إنشاء مستندات أكثر تعقيدًا تحتوي على صور وشظايا نصية وجداول في مستند واحد.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

عرض مثال [Hello, World](/pdf/ar/php-java/hello-world-example/) خطوات بسيطة لإنشاء مستند PDF باستخدام Aspose.PDF. في هذه المقالة، سنلقي نظرة على إنشاء مستند أكثر تعقيدًا باستخدام Aspose.PDF لـ PHP عبر Java. كمثال، سنأخذ مستندًا من شركة وهمية تعمل في خدمات العبارات لنقل الركاب.

إذا قمنا بإنشاء مستند من الصفر، فنحن بحاجة إلى اتباع خطوات معينة:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). في هذه الخطوة، سنقوم بإنشاء مستند PDF فارغ مع بعض البيانات الوصفية ولكن بدون صفحات.

1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) إلى كائن المستند. الآن سيكون لمستندنا صفحة واحدة.
1. أضف [صورة](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). إنها عملية معقدة تعتمد على إجراءات منخفضة المستوى مع مشغلي PDF.
    - تحميل الصورة من التدفق
    - إضافة الصورة إلى مجموعة الصور في موارد الصفحة
    - استخدام مشغل GSave: هذا المشغل يحفظ حالة الرسوم الحالية.
    - إنشاء كائن [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - استخدام مشغل ConcatenateMatrix: يحدد كيفية وضع الصورة.
    - استخدام مشغل Do: هذا المشغل يرسم الصورة.
    - استخدام مشغل GRestore: هذا المشغل يستعيد حالة الرسوم.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) للرأس. من أجل الرأس سنستخدم خط Arial بحجم 24 نقطة ومحاذاة في المنتصف.

1. إضافة رأس إلى الصفحة [الفقرات](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) للوصف. للوصف سنستخدم خط Arial بحجم خط 24pt ومحاذاة مركزية.
1. إضافة (الوصف) إلى فقرات الصفحة.
1. إنشاء جدول، إضافة خصائص الجدول.
1. إضافة (الجدول) إلى [الفقرات](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. حفظ الوثيقة "Complex.pdf".

```php

    $document = new Document();
    //إضافة صفحة
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // إضافة صورة
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // إضافة رأس
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("طرق جديدة للعبّارات في خريف 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // إضافة وصف
    $descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت وتقتصر التذاكر على 5000 يوميًا. يتم تشغيل خدمة العبارات بنصف السعة وعلى جدول زمني مخفض. توقعوا الانتظار في الطوابير.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // إضافة جدول
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("يغادر المدينة");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("يغادر الجزيرة");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```