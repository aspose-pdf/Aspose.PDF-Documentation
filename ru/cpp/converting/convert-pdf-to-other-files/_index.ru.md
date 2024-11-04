---
title: Конвертировать PDF файл в другие форматы 
linktitle: Конвертировать PDF в другие форматы 
type: docs
weight: 90
url: /cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в другие форматы.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертировать PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF для C++ представляет вам бесплатное онлайн-приложение ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (сокращение от Electronic Publication) — это бесплатный и открытый стандарт для электронных книг от Международного форума цифровых публикаций (IDPF). Файлы имеют расширение .epub.
EPUB предназначен для текучего контента, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированной версткой. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF for C++ также поддерживает функцию конвертации PDF-документов в формат EPUB. Aspose.PDF for C++ имеет класс под названием EpubSaveOptions, который можно использовать в качестве второго аргумента в методе [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa), чтобы создать файл EPUB. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования с C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени выходного файла
    String outfilename("PDFToEPUB_out.epub");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Сохранить PDF-файл в формате EPUB
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Преобразование PDF в LaTeX/TeX

**Aspose.PDF for C++** поддерживает преобразование PDF в LaTeX/TeX. Формат файла LaTeX — это текстовый формат файла со специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной вёрстки.

Для преобразования PDF в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options), который предоставляет свойство OutDirectoryPath для сохранения временных изображений во время процесса конверсии.

Следующий фрагмент кода показывает процесс преобразования PDF-файлов в формат TEX с использованием C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени выходного файла
    String outfilename("PDFToTeX_out.tex");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения LaTeX
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // Установить путь к выходному каталогу для объекта параметров сохранения
    saveOptions->set_OutDirectoryPath(_dataDir);

    // Сохранить PDF-файл в формате LaTeX
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF для C++ предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Конвертируйте PDF в текст

**Aspose.PDF для C++** поддерживает преобразование всего PDF-документа и отдельной страницы в текстовый файл.

### Конвертация всего PDF-документа в текстовый файл

Вы можете преобразовать PDF-документ в TXT-файл, используя класс [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

Следующий код объясняет, как извлечь текст со всех страниц.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени выходного файла
    String outfilename("input_Text_Extracted_out.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Сохранить извлеченный текст в текстовом файле
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Преобразование страницы PDF в текстовый файл

Вы можете конвертировать PDF-документ в TXT-файл с помощью Aspose.PDF для C++. Для решения этой задачи следует использовать класс [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

Следующий фрагмент кода объясняет, как извлечь текст с определенных страниц.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample-4pages.pdf");
    // Строка для имени выходного файла
    String outfilename("sample-4pages_out.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // Сохранить извлеченный текст в текстовый файл
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF для C++ представляет вашему вниманию бесплатное онлайн приложение ["PDF в текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертация PDF в XPS

**Aspose.PDF для C++** предоставляет возможность конвертировать PDF файлы в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать предоставленный фрагмент кода для конвертации PDF файлов в формат XPS с помощью C++.

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее кодовое имя Metro и включающий маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации PDF файлов в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options), который используется в качестве второго аргумента метода [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) для генерации XPS файла.

Следующий фрагмент кода показывает процесс преобразования PDF файла в формат XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени выходного файла
    String outfilename("PDFToXPS_out.xps");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // Сохранить PDF файл в формате XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF для C++ предлагает бесплатное онлайн-приложение ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать изучить функциональность и качество его работы.


[![Aspose.PDF Конвертация PDF в SVG с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}