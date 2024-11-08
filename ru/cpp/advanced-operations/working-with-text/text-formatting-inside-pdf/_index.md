---
title: Форматирование текста в PDF с использованием C++
linktitle: Форматирование текста в PDF
type: docs
weight: 30
url: /ru/cpp/text-formatting-inside-pdf/
description: Эта страница объясняет, как форматировать текст внутри PDF-файла. Сюда входят добавление отступа строки, добавление границы текста, добавление подчеркивания текста, добавление границы вокруг добавленного текста, выравнивание текста для содержимого плавающего блока и т. д.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как добавить отступ строки в PDF

Чтобы добавить отступ строки в PDF, Aspose.PDF для C++ использует свойство [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) в классе [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) и также использует коллекции [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) и [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).

Пожалуйста, используйте следующий фрагмент кода, чтобы использовать свойство:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("SubsequentIndent_out.pdf");


    // Создать новый объект документа
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // Инициализировать TextFormattingOptions для фрагмента текста и указать значение SubsequentLinesIndent

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## Как добавить границу текста

Следующий фрагмент кода показывает, как добавить границу к тексту, используя TextBuilder и установив свойство DrawTextRectangleBorder в [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Создать новый объект документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();

    // Создать текстовый фрагмент
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Установить свойства текста
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Установить свойство StrokingColor для рисования границы (обводки) вокруг текстового
    // прямоугольника
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Установить значение свойства DrawTextRectangleBorder в true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Сохранить документ
    document->Save(_dataDir + outputFileName);
}
```

## Как добавить подчеркнутый текст

Следующий фрагмент кода показывает, как добавить подчеркнутый текст при создании нового PDF файла.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("AddUnderlineText_out.pdf");

    // Создать новый объект документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();

    // TextFragment с примером текста
    auto fragment = MakeObject<TextFragment>("Текст с подчеркиванием");
    // Установить шрифт для TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Установить форматирование текста как подчеркнутое
    fragment->get_TextState()->set_Underline(true);

    // Указать позицию, где должен быть размещен TextFragment
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Добавить TextFragment в PDF файл
    tb->AppendText(fragment);

    // Сохранить полученный PDF документ.
    document->Save(_dataDir + outputFileName);
}
```

## Как добавить рамку вокруг добавленного текста

Вы можете контролировать внешний вид добавляемого текста. Пример ниже показывает, как добавить рамку вокруг текста, который вы добавили, нарисовав вокруг него прямоугольник. Узнайте больше о классе [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("sample.pdf");

    // Строка для имени выходного файла
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Сохранить результирующий PDF-документ.
    editor->Save(_dataDir + outputFileName);
}
```

## Как добавить символ новой строки

Для добавления текста с символом новой строки, пожалуйста, используйте [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) с [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

Следующий фрагмент кода показывает, как добавить символ новой строки в ваш PDF файл:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("AddNewLineFeed_out.pdf");

    // Создать новый объект документа
    auto document = MakeObject<Document>();
    // Получить конкретную страницу
    auto page = document->get_Pages()->Add();

    // Инициализировать новый TextFragment с текстом, содержащим необходимые маркеры новой строки
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Установить свойства текстового фрагмента, если необходимо
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Создать объект TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Добавить новый TextFragment в абзац
    par->AppendLine(textFragment);

    // Установить позицию абзаца
    par->set_Position(MakeObject<Position>(100, 600));

    // Создать объект TextBuilder
    auto textBuilder = new TextBuilder(page);
    // Добавить TextParagraph с помощью TextBuilder
    textBuilder->AppendParagraph(par);

    // Сохранить результирующий PDF документ.
    document->Save(_dataDir + outputFileName);
}
```

## Как добавить зачеркнутый текст

Вы можете использовать класс [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) для установки форматирования текста, такого как жирный, курсив, подчеркивание, а также API предоставляет возможность отмечать форматирование текста как зачеркнутое.

Попробуйте использовать следующий фрагмент кода для добавления TextFragment с форматированием зачеркнутого текста.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddStrikeOutText_out.pdf");

    // Open document
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();

    // Create text fragment
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Set text properties
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Set StrikeOut property
    textFragment->get_TextState()->set_StrikeOut(true);
    // Mark text as Bold
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Применение градиентной заливки к тексту

Класс [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) был дополнительно усовершенствован за счет введения нового свойства [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), которое можно использовать для указания цветов заливки для текста. Это новое свойство добавляет различные градиентные заливки к тексту, например, осевую заливку, радиальную (Тип 3) заливку, как показано в следующем кодовом фрагменте:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("sample.pdf");

    // Строка для имени выходного файла
    String outputFileName("ApplyGradientShading_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Создать новый цвет с паттерном цветов
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Чтобы применить радиальный градиент, вы можете установить свойство ‘PatternColorSpace’ равным ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ в приведенном выше примере кода.

## Как выровнять текст относительно плавающего содержимого

Aspose.PDF поддерживает установку выравнивания текста для содержимого внутри элемента Floating Box. Свойства выравнивания экземпляра [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) могут быть использованы для этого, как показано в следующем примере кода.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("sample.pdf");

    // Строка для имени выходного файла
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Создать новый цвет с цветовым пространством шаблона
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```