---
title: العمل مع العناوين في PDF
type: docs
weight: 70
url: /ar/php-java/working-with-headings/
lastmod: "2024-06-05"
description: إنشاء ترقيم في العنوان لمستند PDF الخاص بك باستخدام PHP. يوفر Aspose.PDF for PHP via Java أنماط ترقيم مختلفة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تطبيق نمط الترقيم في العنوان

العناوين هي الأجزاء الهامة في أي مستند. يحاول الكتاب دائمًا جعل العناوين أكثر بروزًا ومعنى للقراء. إذا كان هناك أكثر من عنوان في المستند، فإن الكاتب لديه عدة خيارات لتنظيم هذه العناوين. واحدة من أكثر الطرق شيوعًا لتنظيم العناوين هي كتابة العناوين بنمط الترقيم.

يوفر Aspose.PDF for PHP via Java العديد من أنماط الترقيم المحددة مسبقًا. هذه الأنماط المحددة مسبقًا مخزنة في تعداد، NumberingStyle. القيم المحددة مسبقًا لتعداد NumberingStyle ووصفها موضح أدناه:

|**أنواع العناوين**|**الوصف**|
| :- | :- |

|NumeralsArabic|نوع عربي، على سبيل المثال، 1,1.1,...|
|NumeralsRomanUppercase|نوع روماني علوي، على سبيل المثال، I,I.II, ...|
|NumeralsRomanLowercase|نوع روماني سفلي، على سبيل المثال، i,i.ii, ...|
|LettersUppercase|نوع إنجليزي علوي، على سبيل المثال، A,A.B, ...|
|LettersLowercase|نوع إنجليزي سفلي، على سبيل المثال، a,a.b, ...|
تُستخدم خاصية [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) في فئة [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) لتعيين أنماط الترقيم للعناوين.

كود المصدر، للحصول على الإخراج الموضح في الشكل أعلاه، موضح أدناه في المثال.

```php

    // فتح المستند
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("القائمة 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("القائمة 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("القيمة، اعتبارًا من التاريخ الفعلي للخطة، للممتلكات التي سيتم توزيعها بموجب الخطة بناءً على كل ما تم السماح به");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```