---
title: تنسيق مستند PDF
linktitle: تنسيق مستند PDF
type: docs
weight: 20
url: /php-java/formatting-pdf-document/
description: تنسيق مستند PDF باستخدام Aspose.PDF لـ PHP عبر Java. استخدم الكود المقتطف التالي لحل مهامك.
lastmod: "2024-06-05"
---

## الحصول على خصائص نافذة المستند وعرض الصفحة

يساعدك هذا الموضوع في فهم كيفية الحصول على خصائص نافذة المستند، وتطبيق المشاهد، وكيفية عرض الصفحات.

لتعيين هذه الخصائص المختلفة، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يمكنك الآن الحصول على طرق كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)، مثل

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – تمركز نافذة المستند على الشاشة. الافتراضي: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – ترتيب القراءة.
 This determines how pages are laid out when displayed side by side. Default: من اليسار إلى اليمين.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: false (يتم عرض العنوان).
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – يحصل على العلم الذي يحدد ما إذا كان يجب إخفاء شريط القوائم عندما يكون المستند نشطًا.
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – يحصل على العلم الذي يحدد ما إذا كان يجب إخفاء شريط الأدوات عندما يكون المستند نشطًا.
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – يحصل على العلم الذي يحدد ما إذا كان يجب إخفاء عناصر واجهة المستخدم عندما يكون المستند نشطًا.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – يحصل على وضع الصفحة، يحدد كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – تخطيط الصفحة.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – يحصل على وضع الصفحة، يحدد كيفية عرض المستند عند فتحه.

يوضح لك مقتطف الكود التالي كيفية الحصول على الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // فتح المستند
    $document = new Document($inputFile);

    // الحصول على خصائص المستند المختلفة
    // موقع نافذة المستند - الافتراضي: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // ترتيب القراءة السائد؛ تحديد موقع الصفحة
    // عند عرضها جنبًا إلى جنب - الافتراضي: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند.
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
    // الصفحة الأولى المعروضة - الافتراضي: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وترك محتويات الصفحة فقط معروضة - الافتراضي: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // وضع صفحة المستند. كيفية عرض المستند عند الخروج
    // من وضع الشاشة الكاملة.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // تخطيط الصفحة أي صفحة واحدة، عمود واحد
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // كيفية عرض المستند عند فتحه.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## تعيين خصائص نافذة المستند وعرض الصفحة

يشرح هذا الموضوع كيفية تعيين خصائص نافذة المستند، تطبيق العارض وعرض الصفحة.

لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. قم بتعيين خصائص كائن المستند.
1. احفظ ملف PDF المحدث باستخدام طريقة Save.

الطرق المتاحة هي:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

يوضح لك مقطع الشيفرة التالي كيفية تعيين الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    // افتح المستند
    $document = new Document($inputFile);
    // تعيين خصائص المستند المختلفة
    // تحديد موضع نافذة المستند - الافتراضي: false
    $document->setCenterWindow(true);
    // الترتيب السائد للقراءة؛ تحديد موضع الصفحة
    // عند العرض جنباً إلى جنب - الافتراضي: L2R
    $document->setDirection(Direction::$R2L);
    // تحديد ما إذا كان يجب أن تعرض شريط عنوان النافذة عنوان المستند
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    $document->setDisplayDocTitle(true);
    // تحديد ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
    // الصفحة الأولى المعروضة - الافتراضي: false
    $document->setFitWindow(true);
    // تحديد ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي:
    // false
    $document->setHideMenubar(true);
    // تحديد ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي:
    // false
    $document->setHideToolBar(true);
    // تحديد ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وترك محتويات الصفحة معروضة فقط - الافتراضي: false
    $document->setHideWindowUI(true);
    // وضع صفحة المستند. تحديد كيفية عرض المستند عند الخروج من
    // وضع الشاشة الكاملة.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // تحديد تخطيط الصفحة أي صفحة واحدة، عمود واحد
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // تحديد كيفية عرض المستند عند الفتح
    // أي عرض الصور المصغرة، وضع الشاشة الكاملة، عرض لوحة المرفقات
    $document->setPageMode(PageMode::$UseThumbs);
    // حفظ ملف PDF المحدث
    $document->save($outputFile);
    $document->close();

```


## تضمين الخطوط في ملف PDF موجود

تدعم قارئات PDF [مجموعة أساسية من 14 خطًا](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) بحيث يمكن عرض المستندات بنفس الطريقة بغض النظر عن المنصة التي يتم عرض المستند عليها. عندما يحتوي ملف PDF على خط خارج الخطوط الأساسية، قم بتضمين الخط لتجنب استبدال الخط.

يدعم Aspose.PDF لـ PHP عبر Java تضمين الخطوط في مستندات PDF الموجودة. يمكنك تضمين خط كامل أو جزء منه. لتضمين الخط:

1. افتح ملف PDF موجود باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. استخدم فئة [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) لتضمين الخط.
   1. تقوم طريقة setEmbedded(true) بتضمين الخط بالكامل.
   1. تقوم [طريقة isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) بتضمين جزء من الخط.

يتضمن جزء الخط فقط الأحرف المستخدمة وهو مفيد حيث تستخدم الخطوط لجمل قصيرة أو شعارات، على سبيل المثال حيث يستخدم خط الشركة للشعار، ولكن ليس لنص الجسم.
 استخدام مجموعة فرعية يقلل من حجم ملف PDF الناتج.

ومع ذلك، إذا تم استخدام خط مخصص للنص الرئيسي، فيجب تضمينه بالكامل.

يظهر مقتطف الشيفرة التالي كيفية تضمين خط في ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // تحقق مما إذا كان الخط مضمنًا بالفعل
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // التحقق من كائنات النموذج
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // تحقق مما إذا كان الخط مضمنًا بالفعل
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // حفظ ملف PDF المحدّث
    $document->save($outputFile);
    $document->close();
```

## تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة إلى استخدام أي خط بخلاف الخطوط الأساسية الأربعة عشر التي يدعمها Adobe Reader، فيجب تضمين وصف الخط أثناء توليد ملف PDF. إذا لم يتم تضمين معلومات الخط، سيقوم Adobe Reader بأخذها من نظام التشغيل إذا كانت مثبتة عليه، أو سيقوم بإنشاء خط بديل وفقًا لوصف الخط في ملف PDF. يرجى ملاحظة أن الخط المضمن يجب أن يكون مثبتًا على الجهاز المضيف، أي في حالة الكود التالي، الخط 'Univers Condensed' مثبت على النظام.

نستخدم خاصية setEmbedded من فئة [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) لتضمين معلومات الخط في ملف PDF. ضبط قيمة هذه الخاصية إلى 'true' سيقوم بتضمين ملف الخط الكامل في ملف PDF، مع العلم بأن ذلك سيزيد من حجم ملف PDF. فيما يلي جزء الكود الذي يمكن استخدامه لتضمين معلومات الخط في ملف PDF.

```php

    // إنشاء كائن PDF باستدعاء منشئه الفارغ
    $document = new Document();

    // إنشاء قسم في كائن Pdf
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("هذا نص مثال يستخدم خط مخصص.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // حفظ ملف PDF المحدث
    $document->save($outputFile);
    $document->close();
```


## تعيين اسم الخط الافتراضي عند حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، يقوم API باستبدال هذه الخطوط بالخط الافتراضي. عندما يكون الخط متاحًا (مثبتًا على الجهاز أو مضمنًا في المستند)، يجب أن يحتوي ملف PDF الناتج على نفس الخط (لا يجب استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (وليس مسار ملفات الخط). لقد قمنا بتنفيذ ميزة لتعيين اسم الخط الافتراضي عند حفظ مستند كملف PDF. يمكن استخدام الشفرة التالية لتعيين الخط الافتراضي:

```php

    // تحميل مستند PDF موجود
    $document = new Document($inputFile);
    $newName = "Arial";

    // تهيئة خيارات الحفظ لصيغة PDF
    $ops = new PdfSaveOptions();

    // تعيين اسم الخط الافتراضي
    $ops->setDefaultFontName($newName);

    // حفظ ملف PDF
    $document->save($outputFile, $ops);
    // حفظ ملف PDF المحدث
    $document->close();
```

## الحصول على جميع الخطوط من مستند PDF

في حالة رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة **Document.getFontUtilities().getAllFonts()** المقدمة في فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 يرجى التحقق من مقطع الشيفرة التالي من أجل الحصول على جميع الخطوط من مستند PDF موجود:

```php

    // تحميل مستند PDF موجود
    $document = new Document($inputFile);

    // الحصول على جميع الخطوط من المستند
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // حفظ ملف PDF المحدث
    $document->close();
```

## تعيين أو الحصول على عامل التكبير لملف PDF

في بعض الأحيان، ترغب في تعيين أو الحصول على عامل التكبير لمستند PDF. يمكنك بسهولة تحقيق هذا المتطلب باستخدام Aspose.PDF.

يسمح لك كائن [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) بالحصول على قيمة التكبير المرتبطة بملف PDF. وبالمثل، يمكن استخدامه لتعيين عامل التكبير للملف.

```php

    // تحميل مستند PDF موجود
    $document = new Document($inputFile);

    // إنشاء كائن GoToAction
    $action = $document->getOpenAction();

    // الحصول على عامل التكبير لملف PDF
    $responseData = $action->getDestination()->getZoom();

    // حفظ ملف PDF المحدث
    $document->close();  
```

يظهر مقتطف الشيفرة التالي كيفية الحصول على عامل التكبير لملف PDF.

```php

    // تحميل مستند PDF موجود
    $document = new Document($inputFile);
    $zoom = 0.5;
    // ضبط عامل التكبير للمستند
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // ضبط الإجراء ليتناسب مع عرض الصفحة
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // ضبط الإجراء ليتناسب مع ارتفاع الصفحة
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // حفظ ملف PDF المحدث
    $document->save($outputFile);
    $document->close();  
```