---
title: Конвертировать PDF файл в HTML формат
linktitle: Конвертировать PDF файл в HTML формат
type: docs
weight: 50
url: ru/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в HTML формат с помощью библиотеки C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** предоставляет множество функций для преобразования различных форматов файлов в PDF документы и преобразования PDF файлов в различные выходные форматы. Эта статья обсуждает, как конвертировать PDF файл в <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for C++ предоставляет возможность конвертировать HTML файлы в формат PDF, используя подход InLineHtml. Мы получили много запросов на функциональность, которая конвертирует PDF файл в HTML формат, и предоставили эту функцию. Обратите внимание, что эта функция также поддерживает XHTML 1.0.

**Aspose.PDF for C++** поддерживает функции для конвертации PDF файла в HTML. Основные задачи, которые вы можете выполнить с библиотекой Aspose.PDF, перечислены:

- конвертация PDF в HTML;
- разделение вывода на многостраничный HTML;
- указание папки для хранения SVG-файлов;
- сжатие SVG-изображений во время конвертации;
- указание папки для изображений;
- создание последующих файлов только с содержимым тела;
- прозрачная отрисовка текста;
- отрисовка слоев PDF-документа.

Aspose.PDF для C++ предоставляет двухстрочный код для преобразования исходного PDF-файла в HTML. `Перечисление SaveFormat` содержит значение Html, которое позволяет сохранить исходный файл в HTML. Следующий фрагмент кода показывает процесс конвертации PDF-файла в HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Сохранить вывод в формате HTML
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF для C++ предлагает вашему вниманию бесплатное онлайн-приложение ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Разделение вывода на многостраничный HTML

При конвертации большого PDF файла с несколькими страницами в формат HTML, вывод отображается как одна HTML страница. Она может оказаться очень длинной. Чтобы контролировать размер страницы, можно разделить вывод на несколько страниц во время конвертации PDF в HTML. Пожалуйста, попробуйте использовать следующий фрагмент кода.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Указать разделение вывода на несколько страниц
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Сохранить вывод в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Указание папки для хранения SVG файлов

Во время конвертации PDF в HTML можно указать папку, в которую должны сохраняться изображения SVG. Используйте [`класс HtmlSaveOption`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`свойство SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f), чтобы указать специальный каталог для изображений SVG. Это свойство получает или задает путь к каталогу, в который должны сохраняться изображения SVG, когда они встречаются в процессе конвертации. Если параметр пуст или равен null, то любые файлы SVG сохраняются вместе с другими файлами изображений.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Указать папку, в которую сохраняются изображения SVG во время конвертации PDF в HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Сохранить выходные данные в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Сжатие SVG изображений во время конвертации

Для сжатия SVG изображений во время конвертации PDF в HTML попробуйте использовать следующий код:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для названия пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для названия файла
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения в HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Указать папку, в которую будут сохранены SVG изображения во время конвертации PDF в HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Сохранить выходной файл в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Указание папки для изображений

Мы также можем указать папку, в которую будут сохраняться изображения во время конвертации PDF в HTML:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where All images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Создавайте последующие файлы только с содержимым тела

Недавно нас попросили ввести функцию, где PDF-файлы преобразуются в HTML, и пользователь может получить только содержимое тега `<body>` для каждой страницы. Этот код создаст один файл с CSS, деталями `<html>`, `<head>`, и все страницы в других файлах только с содержимым `<body>`.

Чтобы удовлетворить это требование, было введено новое свойство, HtmlMarkupGenerationMode, в класс [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

С помощью следующего простого фрагмента кода вы можете разделить выходной HTML на страницы. В выходных страницах все HTML-объекты должны размещаться точно так же, как они размещаются сейчас (обработка и вывод шрифтов, создание и вывод CSS, создание и вывод изображений), за исключением того, что выходной HTML будет содержать содержимое, которое в настоящее время размещено внутри тегов (теперь теги “body” будут опущены). Однако, при использовании этого подхода, ссылка на CSS является ответственностью вашего кода, потому что такие вещи будут удалены. Для этой цели вы можете прочитать CSS с помощью File.ReadAllText() и отправить его через AJAX на веб-страницу, где он будет применен с помощью jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Открытие документа
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создание объекта опций сохранения HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Сохранение вывода в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Прозрачное отображение текста

В случае, если исходный/входной PDF-файл содержит прозрачные тексты, затененные передними изображениями, могут возникнуть проблемы с отображением текста. Поэтому, чтобы учитывать такие сценарии, можно использовать свойства [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) и SaveTransparentTexts.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект HTML Save Option
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Сохранить результат в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Рендеринг слоев PDF документа

Мы можем отобразить слои PDF документа в отдельном элементе типа слоя во время конвертации PDF в HTML:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Указать рендеринг слоев PDF документа отдельно в выходном HTML
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Сохранить вывод в формате HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```