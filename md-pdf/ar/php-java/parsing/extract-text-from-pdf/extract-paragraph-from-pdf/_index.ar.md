---
title: استخراج فقرة من PDF 
linktitle: استخراج فقرة
type: docs
weight: 20
url: /php-java/extract-paragraph-from-pdf/
description: يصف هذا المقال كيفية استخدام ParagraphAbsorber - أداة خاصة في Aspose.PDF لاستخراج النص من مستندات PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج النص من مستند PDF في شكل فقرات

يمكننا الحصول على نص من مستند PDF عن طريق البحث عن نص معين (باستخدام "نص عادي" أو "تعبيرات منتظمة") من صفحة واحدة أو المستند بأكمله، أو يمكننا الحصول على النص الكامل لصفحة واحدة أو نطاق من الصفحات أو المستند بأكمله. ومع ذلك، في بعض الحالات، تحتاج إلى استخراج الفقرات من مستند PDF أو النص في شكل فقرات. لقد قمنا بتنفيذ وظيفة للبحث عن الأقسام والفقرات في نص صفحات مستند PDF. لقد قدمنا فئة ParagraphAbsorber (مثل TextFragmentAbsorber وTextAbsorber)، والتي يمكن استخدامها لاستخراج الفقرات من مستندات PDF.

### التكرار عبر مجموعة الفقرات والحصول على نصها

```php

// فتح ملف PDF موجود
$document = new Document($inputFile);
// إنشاء مثيل لـ ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "الفقرة " . $j++ . " من القسم " . $i++ . " على الصفحة" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// حفظ النص المستخرج في ملف الإخراج.
file_put_contents($outputFile, $responseData);
```