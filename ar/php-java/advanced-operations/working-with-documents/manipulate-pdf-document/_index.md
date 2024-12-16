---
title: معالجة مستند PDF
linktitle: معالجة مستند PDF
type: docs
weight: 30
url: /ar/php-java/manipulate-pdf-document/
description: تحتوي هذه المقالة على معلومات حول كيفية التحقق من صحة مستند PDF للمعيار PDF A، وكيفية العمل مع فهرس المحتويات، وكيفية تعيين تاريخ انتهاء صلاحية PDF، وكيفية تحديد تقدم توليد ملف PDF.
lastmod: "2024-06-05"
---

## التحقق من صحة مستند PDF للمعيار PDF A (A 1A و A 1B)

للتحقق من صحة مستند PDF للتوافق مع PDF/A-1a أو PDF/A-1b، استخدم طريقة [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) الخاصة بفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). تتيح لك هذه الطريقة تحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) التعداد: PDF_A_1A أو PDF_A_1B.

تنسيق XML الناتج هو تنسيق Aspose مخصص.
 يحتوي XML على مجموعة من العلامات باسم Problem؛ تحتوي كل علامة على تفاصيل مشكلة معينة. يمثل السمة ObjectID في علامة Problem معرف الكائن المحدد الذي تتعلق به هذه المشكلة. تمثل السمة Clause قاعدة مقابلة في مواصفات PDF.

```php

    // افتح المستند
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // تحقق من صحة PDF لـ PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## العمل مع TOC

### إضافة TOC إلى ملف PDF موجود

لإضافة TOC إلى ملف PDF موجود، استخدم فئة [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) في حزمة com.aspose.pdf. يمكن لحزمة com.aspose.pdf إنشاء ملفات PDF جديدة والتعامل مع الملفات الموجودة أيضًا. لاستخدام com.aspose.pdf في إضافة TOC إلى ملف PDF موجود.

يستخدم هذا الجزء من كود PHP Aspose.PDF لإضافة جدول محتويات (TOC) إلى مستند PDF موجود:

```php
    // افتح المستند
    $document = new Document($inputFile);

    // الوصول إلى الصفحة الأولى من ملف PDF
    $tocPage = $document->getPages()->insert(1);

    // إنشاء كائن لتمثيل معلومات TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("جدول المحتويات");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // تعيين العنوان لـ TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // إنشاء كائنات سلسلة ستستخدم كعناصر TOC
    $titles = ["الصفحة الأولى", "الصفحة الثانية", "الصفحة الثالثة", "الصفحة الرابعة"];

    for ($i = 0; $i < 4; $i++) {
        // إنشاء كائن Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // تحديد الصفحة الوجهة لكائن العنوان
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // الصفحة الوجهة
        $heading2->setTop($page->getRect()->getHeight());

        // الإحداثيات الوجهة
        $segment2->setText($titles[$i]);

        // إضافة العنوان إلى الصفحة التي تحتوي على TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

### تعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة

يسمح Aspose.PDF أيضًا بتعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة. تحتاج إلى تعيين خاصية LineDash لـ FormatArray بالقيمة المناسبة لـ TabLeaderType enum كما يلي.

```php
    // افتح المستند
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // تعيين نوع القائد
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("جدول المحتويات");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // أضف قسم القائمة إلى مجموعة الأقسام في مستند PDF
    $tocPage->setTocInfo($tocInfo);

    // تعريف تنسيق القائمة بأربعة مستويات عن طريق تعيين الهوامش اليسرى
    // وإعدادات تنسيق النص لكل مستوى
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // إنشاء قسم في مستند PDF
    $page = $document->getPages()->add();

    // إضافة أربعة عناوين في القسم
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("عنوان عينة" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // أضف العنوان إلى جدول المحتويات.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```


### إخفاء أرقام الصفحات في جدول المحتويات

في حالة إذا كنت لا ترغب في عرض أرقام الصفحات مع العناوين في جدول المحتويات، يمكنك استخدام خاصية [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) من فئة [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) كقيمة false. يرجى التحقق من مقطع الشيفرة التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```php
    // فتح المستند
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    $tocInfo = new TocInfo();

    $title = new TextFragment("جدول المحتويات");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // تعيين العنوان لجدول المحتويات
    $tocInfo->setTitle($title);

    // إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    $tocPage->setTocInfo($tocInfo);

    // تحديد تنسيق القائمة من أربع مستويات من خلال تعيين الهوامش اليسرى
    // وإعدادات تنسيق النص لكل مستوى

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // إضافة أربعة عناوين في القسم
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("هذا هو عنوان المستوى " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```


### تخصيص أرقام الصفحات أثناء إضافة جدول المحتويات

من الشائع تخصيص ترقيم الصفحات في جدول المحتويات عند إضافة جدول المحتويات في مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بادئة قبل رقم الصفحة مثل P1، P2، P3 وهكذا. في مثل هذه الحالة، يوفر Aspose.PDF لـ PHP عبر Java خاصية PageNumbersPrefix لفئة TocInfo التي يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في نموذج الكود التالي.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // الوصول إلى الصفحة الأولى من ملف PDF
    $tocPage = $document->getPages()->insert(1);

    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    $tocInfo = new TocInfo();

    $title = new TextFragment("جدول المحتويات");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // تعيين العنوان لجدول المحتويات
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // إنشاء كائنات سلسلة التي سيتم استخدامها كعناصر جدول المحتويات
    $titles = ["الصفحة الأولى", "الصفحة الثانية", "الصفحة الثالثة", "الصفحة الرابعة"];

    for ($i = 0; $i < 4; $i++) {
        // إنشاء كائن عنوان
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // تحديد الصفحة المستهدفة لكائن العنوان
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // الصفحة المستهدفة
        $heading2->setTop($page->getRect()->getHeight());

        // الإحداثيات المستهدفة
        $segment2->setText($titles[$i]);

        // إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
        $tocPage->getParagraphs()->add($heading2);
    }
    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```


## إضافة طبقات إلى ملف PDF

يمكن استخدام الطبقات في مستندات PDF بطرق عديدة. قد يكون لديك ملف متعدد اللغات ترغب في توزيعه وتريد أن يظهر النص في كل لغة على طبقات مختلفة، مع ظهور التصميم الخلفي على طبقة منفصلة. قد تقوم أيضًا بإنشاء مستندات تحتوي على رسوم متحركة تظهر على طبقة منفصلة. يمكن أن يكون أحد الأمثلة هو إضافة اتفاقية ترخيص إلى ملفك، ولا تريد أن يرى المستخدم المحتوى حتى يوافق على شروط الاتفاقية.

يدعم Aspose.PDF لـ PHP عبر Java إضافة الطبقات إلى ملفات PDF.

للعمل مع الطبقات في ملفات PDF، استخدم أعضاء الـAPI التالية.

فئة [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) تمثل طبقة وتحتوي على الخصائص التالية:

- **Name** – اسم الطبقة.
- **Id** – معرف الطبقة.
- **Contents** – قائمة بمشغلات الطبقة.

بمجرد تحديد كائنات [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer)، قم بإضافتها إلى مجموعة الطبقات الخاصة بكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 يوضح الكود أدناه كيفية إضافة طبقات إلى مستند PDF.

```php
    // فتح المستند
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "خط أحمر");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "خط أخضر");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "خط أزرق");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## تعيين انتهاء صلاحية PDF

تحدد ميزة انتهاء صلاحية PDF مدة صلاحية ملف PDF. في تاريخ معين، إذا حاول شخص ما الوصول إليه، يتم عرض نافذة منبثقة توضح أن الملف قد انتهت صلاحيته وأنه يحتاج إلى ملف جديد.

يسمح Aspose.PDF بتعيين انتهاء الصلاحية عند إنشاء وتحرير ملفات PDF.

يوضح مقتطف الكود أدناه كيفية تعيين تاريخ انتهاء الصلاحية لملف PDF. تحتاج إلى استخدام JavaScript حيث أن الملفات المحفوظة بواسطة مكونات الطرف الثالث (على سبيل المثال OwnerGuard) لا يمكن عرضها على محطات عمل أخرى بدون تلك الأداة.

يمكن إنشاء ملف PDF باستخدام PDF OwnerGuard باستخدام ملف موجود يحتوي على تاريخ انتهاء الصلاحية. ولكن يمكن فتح الملف الجديد فقط على محطة عمل تم تثبيت PDF OwnerGuard عليها. ستعطي محطات العمل بدون PDF OwnerGuard خطأ ExpirationFeatureError. على سبيل المثال، يفتح PDF Reader الملف إذا تم تثبيت OwnerGuard، لكن Adobe Acrobat يعيد خطأ.

```php

    // افتح المستند
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```