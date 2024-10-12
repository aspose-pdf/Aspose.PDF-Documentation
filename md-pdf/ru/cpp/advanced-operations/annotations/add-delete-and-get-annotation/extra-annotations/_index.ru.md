---
title: Дополнительные аннотации с использованием C++
linktitle: Дополнительные аннотации
type: docs
weight: 60
url: /cpp/extra-annotations/
description: Этот раздел описывает, как добавлять, получать и удалять различные виды аннотаций из вашего PDF-документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как добавить аннотацию Caret в существующий PDF-файл

Аннотация Caret — это символ, указывающий на редактирование текста. Аннотация Caret также является аннотацией разметки, поэтому класс Caret наследуется от класса Markup и также предоставляет функции для получения или установки свойств аннотации Caret и сброса потока внешнего вида аннотации Caret.

Шаги, с помощью которых мы создаем аннотацию Caret:

1. Загрузите PDF-файл - новый [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создайте новую [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) и установите параметры Caret (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания вставки текста.
1. Создайте новую [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) и установите параметры Caret (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания замены текста.
1. Создайте новую [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) и установите параметры (новый Rectangle, title, color, new QuadPoints и new points, Subject, InReplyTo, ReplyType).
1. После этого мы можем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить аннотацию Caret в PDF файл:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Загружаем PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // Эта аннотация используется для указания вставки текста
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Inserted text 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // Эта аннотация используется для указания замены текста
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Aspose User");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Inserted text 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Cross-out");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### Получить Аннотацию Caret

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотацию Caret в PDF-документе

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Фильтр аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // вывести результаты
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Удалить Аннотацию Caret

Следующий фрагмент кода показывает, как удалить аннотацию Caret из PDF файла.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Фильтр аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // удалить аннотацию
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## Как добавить аннотацию ссылки

[Аннотация ссылки](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) — это гипертекстовая ссылка, которая ведет к месту назначения в другом месте документа или к действию, которое нужно выполнить.

Ссылка — это прямоугольная область, которую можно разместить в любом месте на странице. Каждая ссылка имеет соответствующее действие в PDF, связанное с ней. Это действие выполняется, когда пользователь нажимает в области этой ссылки.

Следующий фрагмент кода показывает, как добавить аннотацию ссылки в PDF файл, используя пример с номером телефона:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // Создать объект TextFragmentAbsorber для поиска номера телефона
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Применить абсорбер только для 1-й страницы
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Создать аннотацию ссылки и задать действие для вызова номера телефона
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Добавить аннотацию на страницу
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### Получить Аннотацию Ссылки

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить LinkAnnotation из PDF документа.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // вывод результатов
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Вывести URL каждой аннотации ссылки
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Вывести текст, связанный с гиперссылкой
        Console::WriteLine(extractedText);
    }
}
```

### Удаление Аннотации Ссылки

Следующий фрагмент кода показывает, как удалить аннотацию ссылки из PDF-файла. Для этого нам нужно найти и удалить все аннотации ссылок на первой странице. После этого мы сохраним документ с удаленной аннотацией.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Фильтрация аннотаций с использованием AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // вывод результатов
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Сохранить документ с удаленной аннотацией
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Редактирование определенной области страницы с помощью аннотации редактирования в Aspose.PDF для C++

Aspose.PDF для C++ поддерживает возможность добавления и управления аннотациями в существующем PDF-файле. Недавно некоторые из наших клиентов запросили возможность редактирования (удаления текста, изображений и т.д.) определенной области страницы PDF-документа. Для выполнения этого требования предоставлен класс с именем RedactionAnnotation, который может быть использован для редактирования определенных областей страницы или для управления существующими RedactionAnnotations и их редактирования (т.е. упрощения аннотации и удаления текста под ней).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Создать экземпляр RedactionAnnotation для определенной области страницы
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Текст, который будет напечатан на аннотации редактирования
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Повторить текст наложения на аннотации редактирования
    annot->set_Repeat(true);

    // Добавить аннотацию в коллекцию аннотаций первой страницы
    page->get_Annotations()->Add(annot);

    // Упрощает аннотацию и редактирует содержимое страницы (т.е. удаляет текст и изображения
    // Под редактированной аннотацией)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Подход с фасадами

Aspose.PDF.Facades поддерживает класс [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/), который предоставляет возможность управлять существующими аннотациями внутри PDF-файла.

Этот класс содержит метод под названием [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63), который предоставляет возможность удалять определенные области страницы.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Редактирование определенной области страницы
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```