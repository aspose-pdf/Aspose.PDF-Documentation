---
title: تحسين، ضغط أو تقليل حجم ملف PDF باستخدام PHP
linktitle: تحسين مستند PDF
type: docs
weight: 40
url: /php-java/optimize-pdf/
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة تضمين الخطوط، إزالة الكائنات غير المستخدمة باستخدام PHP.
lastmod: "2024-06-05"
---

يمكن أن يحتوي مستند PDF في بعض الأحيان على بيانات إضافية. تقليل حجم ملف PDF سيساعدك على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، المشاركة على الشبكات الاجتماعية، الإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام العديد من التقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إزالة تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة حقول النموذج المسطحة
- إزالة أو تسوية التعليقات التوضيحية

## تحسين مستند PDF للويب

تشير عملية التحسين أو الخطية إلى جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح الويب.
 Aspose.PDF يدعم هذه العملية.

لتحسين عرض PDF على الويب:

1. افتح المستند المدخل في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. استخدم الأسلوب [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. احفظ المستند المحسن باستخدام أسلوب save(..).

يوضح مقطع الشيفرة التالي كيفية تحسين مستند PDF للويب.

```php

    // افتح المستند
    $document = new Document($inputFile);

    // تحسين للويب
    $document->optimize();

    // احفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## تقليل حجم ملف PDF

هذا الموضوع يشرح الخطوات لتحسين/تقليل حجم ملف PDF. Aspose.PDF API توفر فئة [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) التي تعطي المرونة لتحسين ملف PDF الناتج عن طريق إزالة الكائنات غير الضرورية وضغط ملفات PDF التي تحتوي على صور. يتم توضيح كل من هذه الخيارات في الأقسام التالية.

### إزالة الكائنات غير الضرورية

يمكننا تحسين حجم مستندات PDF عن طريق إزالة الكائنات المكررة وغير المستخدمة. يوضح مقتطف الشيفرة التالي كيفية القيام بذلك.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تحسين موارد مستند PDF. لكن، لاحظ أن هذه الطريقة لا يمكنها ضمان
    // تقليص المستند
    $document->optimizeResources();

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();

```

## تقليص أو ضغط جميع الصور

إذا كان ملف PDF المصدر يحتوي على صور، اعتبر ضغط الصور وضبط جودتها. من أجل تمكين ضغط الصور، قم بتمرير القيمة true كمعامل إلى طريقة setCompressImages(..). سيتم إعادة ضغط جميع الصور في المستند. يتم تعريف الضغط بواسطة طريقة setImageQuality(..)، والتي هي قيمة الجودة بالنسبة المئوية. 100% تعني جودة وحجم الصورة غير متغيرين. لتقليل حجم الصورة، قم بتمرير معامل أقل من 100 إلى طريقة setImageQuality(..).

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    // تعيين خيار ضغط الصور
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // تعيين خيار جودة الصورة
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

طريقة أخرى هي تغيير حجم الصور بدقة أقل. في هذه الحالة، يجب علينا تعيين ResizeImages إلى true و MaxResolution إلى القيمة المناسبة.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    // تعيين خيار ضغط الصور
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // تعيين خيار جودة الصورة
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // تعيين خيار تغيير حجم الصورة
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // تعيين خيار الدقة القصوى
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

مسألة مهمة أخرى هي وقت التنفيذ. لكن مرة أخرى، يمكننا إدارة هذا الإعداد أيضًا. حاليًا، يمكننا استخدام خوارزميتين - قياسية وسريعة. للتحكم في وقت التنفيذ يجب علينا تعيين خاصية Version. يوضح المقطع التالي خوارزمية السريعة:

```php
    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new optimization_OptimizationOptions();

    // تعيين خيار ضغط الصور
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // تعيين خيار جودة الصورة
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // تعيين إصدار ضغط الصورة إلى سريع
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## إزالة الكائنات غير المستخدمة

يحتوي مستند PDF أحيانًا على كائنات PDF غير مرجعية من أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عندما تتم إزالة صفحة من شجرة صفحات المستند ولكن لا تتم إزالة كائن الصفحة نفسه. لا يجعل إزالة هذه الكائنات المستند غير صالح بل يقلل من حجمه.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## إزالة التدفقات غير المستخدمة

أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة.
 هذه التدفقات ليست "كائنات غير مستخدمة" لأنها مشارة إليها من قاموس موارد الصفحة. قد يحدث هذا في حالات تم فيها إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، يحدث هذا الموقف غالبًا عندما يتم استخراج الصفحات من الوثيقة وتكون لدى صفحات الوثيقة موارد "مشتركة"، أي نفس كائن Resources. يتم تحليل محتويات الصفحة لتحديد ما إذا كانت تدفقات الموارد مستخدمة أم لا. يتم إزالة التدفقات غير المستخدمة. أحيانًا يؤدي ذلك إلى تقليل حجم الوثيقة.

```php

    // فتح الوثيقة
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // تحسين وثيقة PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ الوثيقة المحدثة
    $document->save($outputFile);
    $document->close();
```

## ربط التدفقات المكررة

أحيانًا تحتوي الوثيقة على عدة تدفقات موارد متطابقة (على سبيل المثال الصور). قد يحدث هذا على سبيل المثال عندما يتم دمج مستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق الموارد. نقوم بتحليل جميع تدفقات الموارد ونقارنها. إذا كانت التدفقات مكررة، يتم دمجها، أي يتم الاحتفاظ بنسخة واحدة فقط، وتغيير المراجع بشكل مناسب وإزالة نسخ الكائن. أحيانًا يؤدي هذا إلى تقليل حجم المستند.

```php
    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

بالإضافة إلى ذلك، يمكننا استخدام إعدادات AllowReusePageContent. إذا تم تعيين هذه الخاصية إلى true، سيتم إعادة استخدام محتوى الصفحة عند تحسين المستند للصفحات المتطابقة.

```php
    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## إزالة تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مدمجة، فهذا يعني أن جميع بيانات الخط موجودة في المستند. الميزة هي أن المستند يمكن عرضه بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. ولكن تضمين الخطوط يجعل المستند أكبر. طريقة إزالة تضمين الخطوط تزيل جميع الخطوط المدمجة. هذا يقلل من حجم المستند ولكن قد يصبح المستند غير قابل للقراءة إذا لم يتم تثبيت الخط الصحيح.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $document->optimizeResources($optimizationOptions);

    // حفظ المستند المحدّث
    $document->save($outputFile);
    $document->close();
```

## إزالة أو تسطيح التعليقات التوضيحية

يمكن حذف التعليقات التوضيحية عندما تكون غير ضرورية.
 عندما تكون هناك حاجة إليها ولكن لا تتطلب تحريرًا إضافيًا، يمكن تسويتها. كلتا هاتين التقنيتين ستقللان من حجم الملف.

```php

    // فتح المستند
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## إزالة حقول النموذج

إذا كان مستند PDF يحتوي على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسوية حقول النموذج.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // تسوية النماذج
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## تحويل ملف PDF من فضاء ألوان RGB إلى تدرج الرمادي

يتكون ملف PDF من نصوص، صور، مرفقات، تعليقات توضيحية، رسوم بيانية وغيرها من الكائنات. قد تصادف متطلبًا لتحويل ملف PDF من فضاء ألوان RGB إلى تدرج الرمادي بحيث يكون أسرع أثناء طباعة تلك الملفات. أيضًا عند تحويل الملف إلى تدرج الرمادي، يتم تقليل حجم المستند ولكن مع هذا التغيير، قد تنخفض جودة المستند. حاليًا، يتم دعم هذه الميزة بواسطة ميزة Pre-Flight في Adobe Acrobat، ولكن عند الحديث عن أتمتة المكتب، فإن Aspose.PDF هو الحل النهائي لتوفير مثل هذه الامتيازات لمعالجة المستندات.

من أجل تحقيق هذا المتطلب، يمكن استخدام جزء الكود التالي.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```


## ضغط FlateDecode

يوفر Aspose.PDF لـ PHP عبر Java دعمًا لضغط FlateDecode لوظيفة تحسين PDF. يوضح مقتطف الشيفرة التالي كيفية استخدام الخيار في Optimization لتخزين الصور باستخدام ضغط FlateDecode:

```php

    // فتح المستند
    $document = new Document($inputFile);

    // تهيئة خيارات التحسين
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```

## تخزين الصورة في XImageCollection

يوفر Aspose.PDF لـ PHP عبر Java القدرة على تخزين الصور الجديدة في [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) باستخدام ضغط FlateDecode.
 لتمكين هذا الخيار يمكنك استخدام علم ImageFilterType.Flate. يوضح مقتطف الشفرة التالي كيفية استخدام هذه الوظيفة:

```php
    // افتح المستند
    $document = new Document($inputFile);

    // تهيئة المستند
    $page = $document->getPages()->get_Item(1);

    // تحميل الصورة في الدفق
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // تعيين الإحداثيات
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // استخدام معامل ConcatenateMatrix (دمج المصفوفة): يحدد كيفية وضع الصورة
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // حفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```