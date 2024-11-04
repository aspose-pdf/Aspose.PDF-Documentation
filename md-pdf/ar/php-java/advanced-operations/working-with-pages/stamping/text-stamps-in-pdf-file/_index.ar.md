---
title: إضافة طوابع نصية في PDF برمجيًا
linktitle: الطوابع النصية في ملف PDF
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: إضافة طابع نصي إلى ملف PDF باستخدام فئة TextStamp مع PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة طابع نصي باستخدام Java

يوفر Aspose.PDF لـ PHP عبر Java فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) لإضافة طابع نصي في ملف PDF.
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class provides necessary methods to specify font size, font style, and font color etc for stamp object. In order to add text stamp, first you need to create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and a [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) object using required methods. After that, you may call [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp in the PDF document.

يُظهر لك مقتطف الشيفرة البرمجية التالي كيفية إضافة ختم نصي في ملف PDF.

```php

    // افتح المستند
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // إنشاء ختم نصي
    $textStamp = new TextStamp("Sample Stamp");
    // تعيين ما إذا كان الختم في الخلفية
    $textStamp->setBackground(true);
    // تعيين الأصل
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // تدوير الختم
    $textStamp->setRotate((new Rotation())->On90);    
    // تعيين خصائص النص
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // إضافة الختم إلى صفحة معينة
    $pages->get_Item(1)->addStamp($textStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```

## تحديد المحاذاة لكائن TextStamp

إضافة العلامات المائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر وAspose.PDF لـ PHP عبر Java قادر تمامًا على إضافة الصور وكذلك العلامات المائية النصية. توفر فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) ميزة إضافة الطوابع النصية فوق ملف PDF. مؤخرًا كانت هناك حاجة لدعم ميزة تحديد محاذاة النص عند استخدام كائن [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). لذلك من أجل تلبية هذا الطلب، قمنا بإدخال طريقة setTextAlignment(..) في فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). باستخدام هذه الطريقة، يمكنك تحديد محاذاة النص الأفقية.

توضح مقتطفات الشيفرة التالية مثالاً على كيفية تحميل مستند PDF موجود وإضافة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) عليه.

```php

    // فتح المستند
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // إنشاء كائن FormattedText مع سلسلة نموذجية
    $text = new FormattedText("This");

    // إضافة سطر نص جديد إلى FormattedText
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // إنشاء طابع نصي
    $textStamp = new TextStamp($text);

    // تحديد المحاذاة الأفقية للطابع النصي كمحاذاة مركزية
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // تحديد المحاذاة الرأسية للطابع النصي كمحاذاة مركزية
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // تحديد المحاذاة الأفقية للنص لـ TextStamp كمحاذاة مركزية
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // تعيين هامش علوي لكائن الطابع
    $textStamp->setTopMargin(20);
    
    // إضافة الطابع إلى صفحة معينة
    $pages->get_Item(1)->addStamp($textStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();  
```


## ملء نص الحد كختم في ملف PDF

لقد قمنا بتنفيذ إعداد وضع الرسم لسيناريوهات إضافة وتحرير النصوص. لعرض نص الحد، يرجى إنشاء كائن [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) وضبط RenderingMode إلى TextRenderingMode.StrokeText وأيضًا اختيار اللون لخاصية StrokingColor. لاحقًا، اربط TextState بالختم باستخدام طريقة bindTextState().

يظهر مقطع الشيفرة التالي إضافة نص ملء الحد:

```php

   // إنشاء كائن TextState لنقل الخصائص المتقدمة
    $ts = new TextState();
        
    // ضبط لون الحد
    $ts->setStrokingColor((new Color())->getGray());

    // ضبط وضع رسم النص
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // تحميل مستند PDF مدخل
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // ربط TextState
    $stamp->bindTextState($ts);
    
    // ضبط أصل X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity(5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation(45.0);
    $stamp->setBackground(false);

    // إضافة الختم
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```