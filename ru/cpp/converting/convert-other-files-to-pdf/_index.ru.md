---
linktitle: Конвертировать другие форматы файлов в PDF
type: docs
weight: 80
url: /cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать другие форматы файлов в PDF документ.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Конвертация EPUB в PDF

**Aspose.PDF for C++** позволяет просто конвертировать файлы EPUB в формат PDF.

<abbr title="электронное издание">EPUB</abbr> (сокращение от электронное издание) — это бесплатный и открытый стандарт электронных книг от Международного форума цифрового издательства (IDPF). Файлы имеют расширение .epub. EPUB предназначен для контента с возможностью переформатирования, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения.

EPUB также поддерживает контент с фиксированной версткой. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook. Версия EPUB 3 также одобрена Book Industry Study Group (BISG), ведущей торговой ассоциацией книжной отрасли для стандартизованных передовых практик, исследований, информации и мероприятий, для упаковки контента.

Этапы конвертации:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте экземпляр класса [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с упоминанием имени исходного файла и опциями.
1. Загрузите и [Сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл.

Следующий фрагмент кода показывает, как конвертировать файлы EPUB в формат PDF с помощью C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF для C++ предлагает вам бесплатное онлайн-приложение ["EPUB в PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация EPUB в PDF с бесплатным приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Конвертация текста в PDF

**Aspose.PDF для C++** поддерживает функцию конвертации простого текста и предварительно форматированного текстового файла в формат PDF.

Конвертация текста в PDF означает добавление текстовых фрагментов на страницу PDF. Что касается текстовых файлов, мы имеем дело с 2 типами текста: предварительное форматирование (например, 25 строк с 80 символами в строке) и неформатированный текст (простой текст). В зависимости от наших потребностей, мы можем контролировать это добавление самостоятельно или доверить его алгоритмам библиотеки.

### Конвертация простого текстового файла в PDF

В случае простого текстового файла мы можем использовать следующую технику:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.

1. Прочитайте исходный текстовый файл с использованием [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
2. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
3. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) в коллекцию страниц документа.
4. Создайте новый объект TextFragment и передайте объект TextReader его конструктору.
5. Добавьте новый текстовый абзац в коллекцию абзацев и передайте объект TextFragment.
6. Загрузите и [сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Read the source text file
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instantiate a Document object by calling its empty constructor
    auto document = MakeObject<Document>();

    // Add a new page in Pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create an instance of TextFragmet and pass the text from reader object to its constructor as argument
    auto text = MakeObject<TextFragment>(content);

    // Add a new text paragraph in paragraphs collection and pass the TextFragment object
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save resultant PDF file
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```
### Преобразование заранее отформатированного текстового файла в PDF

Преобразование заранее отформатированного текста похоже на обычный текст, но вам необходимо выполнить некоторые дополнительные действия, такие как установка полей, типа и размера шрифта. Очевидно, что шрифт должен быть моноширинным (например, Courier New).

Следуйте этим шагам для преобразования заранее отформатированного текста в PDF с помощью C++:

1. Создайте объект Document, вызвав его пустой конструктор.
1. Установите левые и правые поля для лучшего представления.
1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) и добавьте новую страницу в коллекцию Pages.
1. Загрузите и [сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл изображения.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Преобразование заранее отформатированного текста в PDF: Начало" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Чтение текстового файла как массива строк
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Создание объекта Document, вызвав его пустой конструктор
    auto document = MakeObject<Document>();

    // Добавление новой страницы в коллекцию Pages объекта Document
    auto page = document->get_Pages()->Add();

    // Установка левых и правых полей для лучшего представления
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // проверка, содержит ли строка символ "перевод страницы"
        // см. https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Установка левых и правых полей для лучшего представления
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Создание экземпляра TextFragment и
        // передача строки в его конструктор в качестве аргумента
        auto text = MakeObject<TextFragment>(line);

        // Добавление нового текстового параграфа в коллекцию параграфов и передача объекта TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // Сохранение результирующего PDF-файла
    document->Save(_dataDir + outfilename);
    std::clog << "Преобразование заранее отформатированного текста в PDF: Завершено" << std::endl;
}
```

{{% alert color="success" %}}
**Попробуйте преобразовать ТЕКСТ в PDF онлайн**

Aspose.PDF для C++ предлагает вам бесплатное онлайн-приложение ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование ТЕКСТА в PDF с бесплатным приложением](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Преобразование XPS в PDF

**Aspose.PDF для C++** поддерживает функцию преобразования файлов <abbr title="XML Paper Specification">XPS</abbr> в формат PDF. Ознакомьтесь с этой статьей, чтобы решить ваши задачи.

Тип файла XPS в первую очередь связан с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее кодовое имя Metro и охватывающее концепцию маркетинга Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в свою операционную систему Windows.

{{% alert color="primary" %}}

Формат файла в основном представляет собой заархивированный XML-файл, который в первую очередь используется для распространения и хранения. Это очень сложно редактировать и в основном реализовано Microsoft.

{{% /alert %}}

Для конвертации XPS в PDF с помощью Aspose.PDF для C++, мы представили класс под названием [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). Позже этот объект передается в качестве аргумента во время инициализации объекта Document и помогает PDF-движку рендеринга определить формат входного документа.

Следующий фрагмент кода показывает процесс конвертации файла XPS в формат PDF с использованием C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте преобразовать формат XPS в PDF онлайн**

Aspose.PDF для C++ предлагает вам бесплатное онлайн-приложение ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование XPS в PDF с помощью бесплатного приложения](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Преобразование XML в PDF

Формат XML используется для хранения структурированных данных. Существует несколько способов преобразования <abbr title="Extensible Markup Language">XML</abbr> в PDF в Aspose.PDF.

## Преобразование XSL-FO в PDF

1. Создайте [Класс String](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте экземпляр объекта [XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Установите стратегию обработки ошибок.
1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. [Сохранить](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл изображения.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO в PDF конвертация: Начало" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

    String outfilename("XMLFOtoPDF.pdf");
    // Создать объект XslFoLoadOption
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Установить стратегию обработки ошибок
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Создать объект Document
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать XML в PDF онлайн**

Aspose.PDF для C++ предлагает вам бесплатное приложение онлайн ["XML в PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.
[![Aspose.PDF Конвертация XML в PDF с бесплатным приложением](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}