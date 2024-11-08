---
title: PDF Липкие Аннотации с использованием C++
linktitle: Липкая Аннотация
type: docs
weight: 50
url: /ru/cpp/sticky-annotations/
description: Эта тема о липких аннотациях, в качестве примера мы показываем аннотацию водяного знака в тексте. Она используется для представления графики на странице. Проверьте фрагмент кода для решения этой задачи.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавить Аннотацию Водяного Знака

Аннотация водяного знака должна использоваться для представления графики, которая должна быть напечатана в фиксированном размере и положении на странице, независимо от размеров печатной страницы.

Вы можете добавить текст водяного знака, используя [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) в определенной позиции страницы PDF. Непрозрачность водяного знака также может быть контролирована с использованием свойства opacity.

Пожалуйста, проверьте следующий фрагмент кода, чтобы добавить WatermarkAnnotation.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    //Create Annotation
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    //Add annotaiton into Annotation collection of Page
    page->get_Annotations()->Add(wa);

    //Create TextState for Font settings
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    //Set opacity level of Annotaiton Text
    wa->set_Opacity(0.5);

    //Add Text to Annotation
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    //Save the Document
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## Получить аннотацию водяного знака

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотацию водяного знака из PDF-документа.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // вывести результаты
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## Удалить аннотацию водяного знака

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы удалить аннотацию водяного знака из PDF-документа.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // удалить аннотации
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```