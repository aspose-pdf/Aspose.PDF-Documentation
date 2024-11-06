---
title: الحصول على و ضبط خصائص الصفحة
type: docs
weight: 30
url: ar/php-java/get-and-set-page-properties/
description: يشرح هذا الموضوع كيفية الحصول على الأرقام في ملف PDF، والحصول على خصائص الصفحة وتحديد لون الصفحة باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
---

يتيح لك Aspose.PDF لـ PHP عبر Java قراءة وضبط خصائص الصفحات في ملف PDF في تطبيقات Java الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وضبط خصائص الصفحة.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتوي عليها. مع Aspose.PDF، يستغرق هذا الأمر أكثر من سطرين من الكود.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. ثم يتم استرجاع صفحات المستند. يتم المحاولة للحصول على عدد الصفحات من الصفحات المسترجعة.

يظهر مقتطف الكود التالي كيفية الحصول على عدد الصفحات في ملف PDF.


```php

    // فتح المستند
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // الحصول على عدد الصفحات
    $responseData = $responseData . "عدد الصفحات : " + $pages->size();
```

### الحصول على عدد الصفحات بدون حفظ المستند

ما لم يتم حفظ ملف PDF ووضع جميع العناصر فعليًا داخل ملف PDF، لا يمكننا الحصول على عدد الصفحات لمستند معين (لأنه لا يمكننا التأكد من عدد الصفحات التي ستستوعب جميع العناصر). ومع ذلك، بدءًا من إصدار Aspose.PDF for PHP عبر Java، قمنا بتقديم طريقة تسمى [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) التي توفر إمكانية الحصول على عدد الصفحات لمستند PDF، دون حفظ الملف. لذلك يمكننا الحصول على معلومات عدد الصفحات مباشرة. يرجى محاولة استخدام مقتطف الشفرة التالي لتحقيق هذا المتطلب.

```php

    // فتح المستند
    $document = new Document($inputFile);      

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    $page = $document->getPages()->add();
    
    // إنشاء حلقة لإضافة 300 مثيل من TextFragment
    for ($i=0; $i < 300; $i++) { 
       // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من ملف PDF
       $page->getParagraphs()->add(new TextFragment("اختبار عدد الصفحات"));
    }
    
    // معالجة الفقرات للحصول على معلومات عن عدد الصفحات
    $document->processParagraphs();

    $pages = $document->getPages();

    // الحصول على عدد الصفحات
    $responseData = $responseData . "عدد الصفحات : " + $pages->size();
```


## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، وصندوق النزيف، القص، والتشذيب. يسمح لك Aspose.PDF بالوصول إلى هذه الخصائص.

### **فهم خصائص الصفحة: الفرق بين Artbox، BleedBox، CropBox، MediaBox، TrimBox وخصائص Rect**

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق للصفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، US Letter، إلخ) الذي تم اختياره عند طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض أو طباعة مستند PDF عليها.
- **صندوق النزيف**: إذا كان المستند يحتوي على نزيف، فسيكون لدى PDF أيضًا صندوق نزيف.
 النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يتم استخدامه للتأكد من أنه عند طباعة المستند وتقطيعه إلى الحجم ("مقلم")، سيصل الحبر إلى حافة الصفحة. حتى إذا تم تقليم الصفحة بشكل خاطئ - تم قطعها قليلاً عن علامات التقليم - لن تظهر حواف بيضاء على الصفحة.

- **صندوق القص**: يشير صندوق القص إلى الحجم النهائي للمستند بعد الطباعة والتقطيع.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يتم استخدام هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق المحاصيل**: صندوق المحاصيل هو حجم "الصفحة" الذي يتم عرض مستند PDF به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق المحاصيل فقط في Adobe Acrobat.

  للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، خصوصاً 10.10.1 حدود الصفحة.

- **Page.Rect**: تقاطع (المستطيل الظاهر عادة) بين MediaBox وDropBox. الصورة أدناه توضح هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### الوصول إلى خصائص الصفحة

يقوم جزء الشيفرة التالي بالحصول على خصائص مثل ArtBox، BleedBox، CropBox، MediaBox، TrimBox، Rect، رقم الصفحة، والتدوير لصفحة معينة في الوثيقة. ثم يقوم بتخزين البيانات المستخرجة في متغيرات منفصلة ودمجها في سلسلة استجابة.

1. إنشاء كائن وثيقة جديد باستخدام المتغير $inputFile.
2. الحصول على مجموعة الصفحات من الوثيقة باستخدام الطريقة getPages().
3. الحصول على صفحة معينة من مجموعة الصفحات باستخدام الطريقة get_Item().
4. استخراج الخصائص المختلفة (ArtBox، BleedBox، CropBox، MediaBox، TrimBox، Rect، رقم الصفحة، التدوير) من كائن الصفحة المحدد وتخزينها في متغيرات منفصلة.
5. يقوم الكود بدمج القيم المستخرجة للخصائص في سلاسل استجابة منفصلة ($responseData1، $responseData2، إلخ).
1. بعد ذلك، يحاول استرداد عدد الصفحات باستخدام الطريقة size() على الكائن $pages، ولكن المتغير $pages غير معرّف.

يعرض مقطع الشيفرة التالي كيفية الحصول على خصائص الصفحة.

```php

   // فتح المستند
    $document = new Document($inputFile);

    // الحصول على مجموعة الصفحات
    $pageCollection = $document->getPages();

    // الحصول على صفحة معينة
    $page = $pageCollection->get_Item(1);

    // الحصول على خصائص الصفحة
    $responseData1 = "ArtBox : الارتفاع = " . $page->getArtBox()->getHeight()
        . ", العرض = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : الارتفاع = " . $page->getBleedBox()->getHeight() . ", العرض = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : الارتفاع = " . $page->getCropBox()->getHeight() . ", العرض = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = "MediaBox : الارتفاع = " . $page->getMediaBox()->getHeight() . ", العرض = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = "TrimBox : الارتفاع = " . $page->getTrimBox()->getHeight() . ", العرض = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = "Rect : الارتفاع = " . $page->getRect()->getHeight() . ", العرض = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = "رقم الصفحة :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = "التدوير :-" . $page->getRotate() . PHP_EOL;

    // الحصول على عدد الصفحات
    $responseData8 = $responseData8 . "عدد الصفحات : " . $pages->size();
```


## تحديد لون الصفحة

توفر [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) الصف خصائص تتعلق بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، أسود وأبيض، تدرج الرمادي أو غير معرف - الذي تستخدمه الصفحة.

تحتوي مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) على جميع صفحات ملفات PDF. تحدد خاصية [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) لون العناصر على الصفحة. للحصول على أو تحديد معلومات اللون لصفحة PDF معينة، استخدم خاصية [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) الخاصة بكائن الصف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

يوضح مقطع الشيفرة التالي كيفية التكرار عبر صفحة فردية من ملف PDF للحصول على معلومات اللون.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // التكرار عبر جميع صفحات ملف PDF
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // الحصول على معلومات نوع اللون لصفحة PDF معينة
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="الصفحة # -" . $pageCount . " بالأبيض والأسود..";
                break;
            case 1:
                $responseData ="الصفحة # -" . $pageCount . " بتدرج الرمادي...";
                break;
            case 0:
                $responseData ="الصفحة # -" . $pageCount . " بنظام RGB..";
                break;
            case 3:
                $responseData ="لون الصفحة # -" . $pageCount . " غير معرف..";
                break;
        }
    }
```