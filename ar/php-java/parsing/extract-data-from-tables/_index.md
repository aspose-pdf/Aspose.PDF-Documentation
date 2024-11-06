---
title: استخراج بيانات الجدول من PDF
linktitle: استخراج بيانات الجدول
type: docs
weight: 40
url: ar/php-java/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج الجداول من PDF باستخدام Aspose.PDF لـ PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج الجداول من PDF برمجياً

استخراج الجداول من ملفات PDF ليس مهمة سهلة لأن الجدول يمكن إنشاؤه بطرق مختلفة.

Aspose.PDF لـ PHP عبر Java لديه أداة لتسهيل استرجاع الجداول. لاستخراج بيانات الجدول، يجب عليك تنفيذ الخطوات التالية:

1. افتح مستند PDF - أنشئ كائن [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
2. أنشئ كائن TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) لاستخراج الجداول من المستند.
3. قم بالتكرار على كل صفحة من المستند.

1. قرر أي الصفحات التي سيتم تحليلها وطبق [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) على الصفحات المطلوبة. سيتم مسح البيانات الجدولية، وسيتم حفظ النتيجة في قائمة من [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). يمكننا الحصول على هذه القائمة من خلال طريقة [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

2. للحصول على البيانات، قم بتكرار `TableList` وتعامل مع قائمة [absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) وقائمة absorbed cells. يمكننا الوصول إلى القائمة الأولى عن طريق استدعاء طريقة [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) وإلى الثانية عن طريق استدعاء طريقة [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. تحتوي كل [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) على [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). يمكنك معالجة هذا لأغراضك الخاصة.

المثال التالي يوضح استخراج الجدول من جميع الصفحات:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // قم بالتكرار عبر كل خلية في الصف.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // قم بالتكرار عبر كل جزء نص في الخلية.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // قم بالتكرار عبر كل جزء في الجزء النصي.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// احفظ بيانات الجدول في ملف الإخراج.
file_put_contents($outputFile, $responseData);

// أغلق مستند الـ PDF.
$document->close();
```


## استخراج بيانات الجدول من PDF وتخزينها في ملف CSV

يوضح المثال التالي كيفية استخراج الجدول وتخزينه كملف CSV.  
لرؤية كيفية تحويل PDF إلى جدول بيانات Excel، يرجى الرجوع إلى مقالة [تحويل PDF إلى Excel](/pdf/php-java/convert-pdf-to-excel/).

```php

    // تحميل مستند PDF المدخل باستخدام فئة المستند.
    $document = new Document($inputFile);

    // إنشاء مثيل لفئة ExcelSaveOptions لتحديد خيارات الحفظ.
    $saveOption = new ExcelSaveOptions();

    // تعيين تنسيق الإخراج إلى CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // حفظ مستند PDF كملف Excel باستخدام خيارات الحفظ المحددة.
    $document->save($outputFile, $saveOption);
```