---
title: Поворот текста внутри PDF с использованием C++
linktitle: Поворот текста внутри PDF
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: Узнайте о различных способах поворота текста в PDF. Aspose.PDF позволяет поворачивать текст на любой угол, поворачивать фрагмент текста или целый абзац.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Поворот текста внутри PDF с использованием свойства Rotation

Используя свойство Rotation класса [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/), вы можете поворачивать текст под различными углами. Поворот текста может использоваться в различных сценариях генерации документов. Вы можете указать угол поворота в градусах, чтобы повернуть текст в соответствии с вашими требованиями. Пожалуйста, ознакомьтесь с различными сценариями, в которых можно реализовать поворот текста.

## Реализация поворота с использованием TextFragment и TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Инициализация объекта документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();
    // Создать фрагмент текста
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Установить свойства текста
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Создать повернутый фрагмент текста
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Установить свойства текста
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Создать повернутый фрагмент текста
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Установить свойства текста
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // создать объект TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Добавить фрагмент текста на страницу PDF
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Сохранить документ
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Реализация вращения с использованием TextParagraph и TextBuilder (Повернутые фрагменты)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // Инициализация объекта документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // Создать текстовый фрагмент
    auto textFragment1 = MakeObject<TextFragment>("повернутый текст");
    // Установить свойства текста
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Установить вращение
    textFragment1->get_TextState()->set_Rotation(45);

    // Создать текстовый фрагмент
    auto textFragment2 = MakeObject<TextFragment>("основной текст");
    // Установить свойства текста
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Создать текстовый фрагмент
    auto textFragment3 = MakeObject<TextFragment>("еще один повернутый текст");
    // Установить свойства текста
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Установить вращение
    textFragment3->get_TextState()->set_Rotation(-45);

    // Добавить текстовые фрагменты в абзац
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // Создать объект TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Добавить текстовый абзац на страницу PDF
    textBuilder->AppendParagraph(paragraph);
    // Сохранить документ
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Реализация Поворота с Использованием TextFragment и Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // Инициализация объекта документа
    auto document = MakeObject<Document>();
    // Получение определенной страницы
    auto page = document->get_Pages()->Add();
    // Создание текстового фрагмента
    auto textFragment1 = MakeObject<TextFragment>("главный текст");
    // Установка свойств текста
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Создание текстового фрагмента
    auto textFragment2 = MakeObject<TextFragment>("повернутый текст");

    // Установка свойств текста
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Установка поворота
    textFragment2->get_TextState()->set_Rotation(315);

    // Создание текстового фрагмента
    auto textFragment3 = MakeObject<TextFragment>("повернутый текст");
    // Установка свойств текста
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Установка поворота
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // Сохранение документа
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Реализация вращения с использованием TextParagraph и TextBuilder (вращается весь абзац)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Инициализация объекта документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // Указать вращение
        paragraph->set_Rotation(i * 90 + 45);
        // Создать текстовый фрагмент
        auto textFragment1 = MakeObject<TextFragment>("Paragraph Text");
        // Создать текстовый фрагмент
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Создать текстовый фрагмент
        auto textFragment2 = MakeObject<TextFragment>("Second line of text");
        // Установить свойства текста
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Создать текстовый фрагмент
        auto textFragment3 = MakeObject<TextFragment>("And some more text...");
        // Установить свойства текста
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // Создать объект TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // Добавить текстовый фрагмент на страницу PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // Сохранить документ
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```