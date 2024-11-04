---
title: إضافة رقم الصفحة إلى PDF
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: /php-java/add-page-number/
description: يسمح لك Aspose.PDF for PHP عبر Java بإضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumber Stamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يجب أن تحتوي جميع الوثائق على أرقام الصفحات فيها. تجعل أرقام الصفحات من السهل على القارئ تحديد أجزاء مختلفة من الوثيقة.
**Aspose.PDF for PHP عبر Java** يسمح لك بإضافة أرقام الصفحات باستخدام PageNumberStamp.

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

يمكنك استخدام فئة [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) لإضافة ختم رقم الصفحة في مستند PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) توفر الفئة طرقًا لإنشاء ختم يعتمد على رقم الصفحة مثل التنسيق والهوامش والمحاذاة والرقم المبدئي، إلخ. لإضافة ختم برقم الصفحة، تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وكائن [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) مع خصائص النص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) الخاصة بفئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) لإضافة الختم في ملف PDF. يمكنك أيضًا تعيين خصائص الخط لختم رقم الصفحة.

يوضح لك جزء الشيفرة التالي كيفية إضافة أرقام الصفحات في ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إنشاء ختم رقم الصفحة
    $pageNumberStamp = new PageNumberStamp();

    // ما إذا كان الختم في الخلفية
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // تعيين خصائص النص
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // إضافة الختم إلى صفحة معينة
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```