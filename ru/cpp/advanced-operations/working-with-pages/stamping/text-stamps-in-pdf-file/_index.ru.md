---
title: Добавление текстовых штампов в PDF файл
linktitle: Текстовые штампы в PDF файле
type: docs
weight: 20
url: /cpp/text-stamps-in-the-pdf-file/
description: Добавьте текстовый штамп в PDF файл с использованием класса TextStamp на C++.
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление текстового штампа на C++

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) для добавления текстового штампа в PDF файл. Класс TextStamp предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текстовый штамп, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp страницы для добавления штампа в PDF. Следующий фрагмент кода показывает, как добавить текстовый штамп в PDF файл.

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать текстовый штамп
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Установить, является ли штамп фоном
    textStamp->set_Background(true);
    // Установить происхождение
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Повернуть штамп
    textStamp->set_Rotate(Rotation::on90);

    // Установить свойства текста
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Добавить штамп на конкретную страницу
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Сохранить выходной документ
    document->Save(_dataDir + outputFileName);
}
```

## Определение выравнивания для объекта TextStamp

Добавление водяных знаков в PDF-документы — это одна из часто востребованных функций, и Aspose.PDF для C++ полностью поддерживает добавление как изображений, так и текстовых водяных знаков. У нас есть класс с именем [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp), который предоставляет возможность добавлять текстовые штампы в PDF-файл. Недавно возникло требование поддерживать возможность указания выравнивания текста при использовании объекта TextStamp. Поэтому, чтобы удовлетворить это требование, мы ввели свойство TextAlignment в класс TextStamp. С помощью этого свойства мы можем указать горизонтальное выравнивание текста.

Следующие фрагменты кода показывают пример того, как загрузить существующий PDF-документ и добавить в него TextStamp.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // instantiate FormattedText object with sample string
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // add new text line to FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // create TextStamp object using FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // specify the Horizontal Alignment of text stamp as Center aligned
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // specify the Vertical Alignment of text stamp as Center aligned
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // specify the Text Horizontal Alignment of TextStamp as Center aligned
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // set top margin for stamp object
    stamp->set_TopMargin(20);
    // add stamp to all pages of PDF file
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // save output document
    document->Save(_dataDir + outputFileName);
}
```

## Заливка текста штриховкой как штамп в PDF-файле

Мы реализовали настройку режима рендеринга для сценариев добавления и редактирования текста. Чтобы отобразить штрихованный текст, создайте объект TextState и установите RenderingMode на TextRenderingMode.StrokeText, а также выберите цвет для свойства StrokingColor. Затем, привяжите TextState к штампу, используя метод BindTextState().

Следующий фрагмент кода демонстрирует добавление текста с заливкой штриховкой:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Создать объект TextState для передачи расширенных свойств
    auto ts = MakeObject<TextState>();

    // Установить цвет для штриховки
    ts->set_StrokingColor(Color::get_Gray());

    // Установить режим рендеринга текста
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Загрузить входной PDF-документ
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Привязать TextState
    stamp->BindTextState(ts);

    // Установить X,Y начало
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Добавить штамп
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```