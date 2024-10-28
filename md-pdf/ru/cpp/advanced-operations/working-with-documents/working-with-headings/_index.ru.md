---
title: Работа с заголовками в PDF
type: docs
weight: 90
url: /cpp/working-with-headings/
lastmod: "2021-11-11"
description: Создайте нумерацию в заголовке вашего PDF документа с помощью C++. Aspose.PDF for C++ демонстрирует различные стили нумерации.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Применение стиля нумерации в заголовке

Любой текст в документе начинается с заголовка. Заголовки являются неотъемлемой частью содержания, независимо от стиля и темы.
Заголовки помогают привлечь внимание к тексту и помогают пользователям находить необходимую информацию в документе, улучшая читаемость и визуальное восприятие. Используя стили заголовков, вы также можете быстро создать оглавление, изменить структуру документа.
Итак, давайте рассмотрим, как работать с заголовками, используя библиотеку Aspose.PDF for C++.

[Aspose.PDF for C++](/pdf/cpp/) предлагает множество предопределенных стилей нумерации. Эти предопределенные стили нумерации хранятся в перечислении NumberingStyle. Предопределенные значения перечисления NumberingStyle и их описания приведены ниже:

|**Типы заголовков**|**Описание**|
| :- | :- |
|NumeralsArabic|Арабский тип, например, 1,1.1,...|
|NumeralsRomanUppercase|Римский верхний тип, например, I,I.II, ...|
|NumeralsRomanLowercase|Римский нижний тип, например, i,i.ii, ...|
|LettersUppercase|Английский верхний тип, например, A,A.B, ...|
|LettersLowercase|Английский нижний тип, например, a,a.b, ...|

Свойство **Style** класса **Aspose.PDF.Heading** используется для установки стилей нумерации заголовков.

|**Рисунок: Предопределенные стили нумерации**|
| :- |
Исходный код, для получения вывода, показанного на приведенной выше иллюстрации, приведен ниже в примере.

```cpp
void WorkingWithHeadingsInPDF() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"Список 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"Список 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"значение, на дату вступления в силу плана, имущества, подлежащего распределению в рамках плана в счет каждой разрешенной");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Сохранить объединенный выходной файл
    document->Save(_dataDir + outputFileName);
}
```