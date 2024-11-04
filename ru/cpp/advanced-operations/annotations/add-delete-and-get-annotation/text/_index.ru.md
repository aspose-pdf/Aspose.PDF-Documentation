---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /cpp/text-annotation/
description: Aspose.PDF для C++ позволяет добавлять, получать и удалять текстовые аннотации из вашего PDF-документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Как добавить текстовую аннотацию в существующий PDF файл

Текстовая аннотация — это аннотация, привязанная к определенному месту в PDF-документе. В закрытом виде аннотация отображается как значок; при открытии она должна отображать всплывающее окно, содержащее текст заметки в шрифте и размере, выбранных читателем.

Аннотации содержатся в коллекции [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) конкретной страницы. Эта коллекция содержит аннотации только для данной страницы; каждая страница имеет свою собственную коллекцию аннотаций.

Чтобы добавить аннотацию на определенную страницу, добавьте ее в коллекцию аннотаций этой страницы с помощью метода [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).

1. Во-первых, создайте аннотацию, которую вы хотите добавить в PDF.
1. Затем откройте входной PDF.
1. Добавьте аннотацию в коллекцию Annotations объекта [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

Следующий фрагмент кода показывает, как добавить аннотацию на страницу PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Загрузите PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Пользователь Aspose");
    textAnnotation->set_Subject(u"Пример темы");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Пример содержимого для аннотации");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## Получить текстовую аннотацию

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить текстовую аннотацию в PDF-документе:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF-файл
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // вывод результатов
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## Удалить текстовую аннотацию из PDF-файла

Следующий фрагмент кода показывает, как удалить текстовую аннотацию из PDF-файла.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Загрузить PDF-файл
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // удаление аннотаций
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## Как добавить (или Создать) новую аннотацию свободного текста

Аннотация свободного текста отображает текст непосредственно на странице. В следующем фрагменте мы добавляем аннотацию свободного текста над первым вхождением строки.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Демонстрация свободного текста");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Получение Аннотации Свободного Текста

Попробуйте использовать следующий фрагмент кода для получения аннотации текста в PDF документе:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузите PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Фильтр аннотаций с помощью AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // вывод результатов
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Сделать Аннотацию Свободного Текста Невидимой

Иногда необходимо создать водяной знак, который не виден в документе при его просмотре, но должен быть виден при печати документа. Используйте флаги аннотации для этой цели. Следующий фрагмент кода показывает, как это сделать.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // Сохранить выходной файл
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Удаление аннотации FreeText

Следующий фрагмент кода показывает, как удалить аннотацию FreeText из PDF-файла.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF-файл
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // удалить аннотации
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```