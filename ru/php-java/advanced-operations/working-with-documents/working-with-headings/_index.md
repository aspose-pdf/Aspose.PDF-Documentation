title: Работа с Заголовками в PDF
type: docs
weight: 70
url: /ru/php-java/working-with-headings/
lastmod: "2024-06-05"
description: Создайте нумерацию в заголовке вашего PDF документа с использованием PHP. Aspose.PDF for PHP via Java предлагает различные стили нумерации.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Применение Стиля Нумерации в Заголовке

Заголовки — важные части любого документа. Авторы всегда стараются сделать заголовки более заметными и значимыми для своих читателей. Если в документе более одного заголовка, у автора есть несколько вариантов для организации этих заголовков. Один из самых распространенных подходов к организации заголовков — это написание заголовков в стиле нумерации.

Aspose.PDF для PHP через Java предлагает множество предопределенных стилей нумерации. Эти предопределенные стили нумерации хранятся в перечислении NumberingStyle. Предопределенные значения перечисления NumberingStyle и их описания приведены ниже:

|**Типы Заголовков**|**Описание**|
| :- | :- |

|NumeralsArabic|Арабский тип, например, 1,1.1,...|
|NumeralsRomanUppercase|Римский верхний регистр, например, I,I.II, ...|
|NumeralsRomanLowercase|Римский нижний регистр, например, i,i.ii, ...|
|LettersUppercase|Английский верхний регистр, например, A,A.B, ...|
|LettersLowercase|Английский нижний регистр, например, a,a.b, ...|
Свойство [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) класса [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) используется для установки стилей нумерации заголовков.

Исходный код для получения вывода, показанного на рисунке выше, приведен ниже в примере.

```php

    // Открыть документ
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
    $heading->setText("Список 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("Список 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("значение, на дату вступления плана в силу, имущества, подлежащего распределению по плану, в счет каждой разрешенной");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```