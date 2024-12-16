---
title: اقتصاص صفحات PDF باستخدام PHP
linktitle: اقتصاص الصفحات
type: docs
weight: 80
url: /ar/php-java/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، والنزيف، والاقتصاص، وصندوق التشذيب باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، النزيف، الاقتصاص، وصندوق التشذيب. يتيح لك Aspose.PDF لـ PHP عبر Java الوصول إلى هذه الخصائص.

- **الصندوق الإعلامي**: الصندوق الإعلامي هو أكبر صندوق للصفحة. يتوافق مع حجم الصفحة (مثل A4، A5، الرسالة الأمريكية، إلخ) المختار عند طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد الصندوق الإعلامي الحجم الفعلي للوسائط التي يتم عرض أو طباعة مستند PDF عليها.
- **صندوق النزيف**: إذا كان لدى المستند نزيف، فسيحتوي PDF أيضًا على صندوق نزيف.
 Bleed هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يتم استخدامه لضمان أنه عند طباعة المستند وقصه إلى الحجم المطلوب ("التشذيب")، سيكون الحبر ممتدًا حتى حافة الصفحة. حتى إذا تم قص الصفحة بشكل خاطئ - قطعت قليلاً عن علامات التشذيب - فلن تظهر حواف بيضاء على الصفحة.

- **Trim box**: يشير صندوق التشذيب إلى الحجم النهائي للمستند بعد الطباعة والتشذيب.

- **Art box**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.

- **Crop box**: صندوق القص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat. للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، خاصة 10.10.1 حدود الصفحة.

- **Page.Rect**: هو تقاطع (المستطيل المرئي عادةً) بين MediaBox وDropBox. الصورة أدناه توضح هذه الخصائص. 
لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

المقتطف أدناه يوضح كيفية قص الصفحة:

```php

    // فتح المستند
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // إنشاء مستطيل صندوق جديد
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // حفظ مستند الإخراج
    $document->save($outputFile);
    $document->close();
```

في هذا المثال استخدمنا ملف عينات [هنا](crop_page.pdf). Initially our page looks like shown on the الشكل 1.
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like الشكل 2.
![Figure 2. Cropped Page](crop_page2.png)