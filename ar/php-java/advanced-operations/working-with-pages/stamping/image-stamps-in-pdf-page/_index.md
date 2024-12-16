---
title: إضافة أختام الصور في ملف PDF برمجياً
linktitle: أختام الصور في ملف PDF
type: docs
weight: 10
url: /ar/php-java/image-stamps-in-pdf-page/
description: أضف ختم الصورة في مستند PDF الخاص بك باستخدام فئة ImageStamp مع مكتبة Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم صورة في ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) لإضافة صورة كختم في مستند PDF. توفر فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) طرقًا لتحديد الارتفاع والعرض والشفافية وما إلى ذلك.

لإضافة ختم صورة:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وكائن ImageStamp باستخدام الخصائص المطلوبة.

1. قم باستدعاء طريقة [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) من فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) لإضافة الطابع إلى ملف PDF.

يُظهر جزء الشيفرة التالي كيفية إضافة طابع صورة في ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // إنشاء طابع صورة
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // إضافة الطابع إلى صفحة معينة
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // حفظ مستند الخرج
    $document->save($outputFile);
    $document->close()
```

## التحكم في جودة الصورة عند إضافة الطابع

تسمح لك فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) بإضافة صورة كطابع في مستند PDF.
 يسمح لك أيضًا بالتحكم في جودة الصورة عند إضافة صورة كعلامة مائية في ملف PDF. للسماح بذلك، تمت إضافة طريقة تسمى setQuality(...) إلى فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). يمكن العثور على طريقة مماثلة أيضًا في فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) من حزمة com.aspose.pdf.facades.

يظهر لك مقطع الشفرة التالي كيفية التحكم في جودة الصورة عند إضافتها كختم في ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // إنشاء ختم صورة
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();        
```

## ختم الصورة كخلفية في صندوق عائم

تتيح لك Aspose.PDF API إضافة ختم الصورة كخلفية في صندوق عائم. خاصية BackgroundImage لفئة FloatingBox يمكن استخدامها لتعيين صورة الخلفية لصندوق عائم كما هو موضح في عينة الكود التالية.

يوضح هذا المقتطف من الكود عملية إنشاء مستند PDF وإضافة صندوق عائم إليه. يحتوي الصندوق العائم على جزء نصي، وحافة، وصورة خلفية، ولون خلفية. يتم بعد ذلك حفظ المستند الناتج في ملف إخراج.

```php

    // فتح المستند
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // إضافة صفحة إلى مستند PDF
    $page = $pages->add();

    // إنشاء كائن FloatingBox
    $aBox = new FloatingBox(200, 100);

    // تعيين الموضع الأيسر لـ FloatingBox
    $aBox->setLeft(40);

    // تعيين الموضع العلوي لـ FloatingBox
    $aBox->setTop(80);

    // تعيين المحاذاة الأفقية لـ FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // إضافة جزء نص إلى مجموعة الفقرات لـ FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("النص الرئيسي"));

    // تعيين الحافة لـ FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // إضافة صورة خلفية
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // تعيين لون الخلفية لـ FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // إضافة FloatingBox إلى مجموعة الفقرات لكائن الصفحة
    $page->getParagraphs()->add($aBox);
    
    // حفظ مستند الإخراج
    $document->save($outputFile);
    $document->close();
```