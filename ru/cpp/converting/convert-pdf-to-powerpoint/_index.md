---
title: Convert PDF to Microsoft PowerPoint in C++
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: ru/cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF позволяет конвертировать PDF в формат PowerPoint с использованием C++. Есть возможность конвертировать PDF в PPTX с изображениями слайдов.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

Эта статья объясняет, как **конвертировать PDF в форматы PowerPoint с использованием C++**. Она охватывает следующие темы.

_Формат_: **PPTX**
- [C++ PDF в PPTX](#cpp-pdf-to-pptx)
- [C++ Конвертирование PDF в PPTX](#cpp-pdf-to-pptx)
- [C++ Как конвертировать файл PDF в PPTX](#cpp-pdf-to-pptx)

_Формат_: **Формат Microsoft PowerPoint PPTX**
- [C++ PDF в PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Конвертирование PDF в PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Как конвертировать файл PDF в PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Другие темы, рассмотренные в этой статье.
- [См. также](#see-also)

## Преобразования PDF в PowerPoint на C++

**Aspose.PDF для C++** позволяет отслеживать процесс преобразования PDF в PPTX.

Во время преобразования PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> текст отображается как текст, который вы можете выбрать/обновить. Пожалуйста, обратите внимание, что для преобразования PDF-файлов в формат PPTX Aspose.PDF предоставляет класс с именем [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Объект класса PptxSaveOptions передается в качестве второго аргумента методу [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). Следующий фрагмент кода демонстрирует процесс преобразования PDF-файлов в формат PPTX.

## Простое преобразование PDF в PPTX с использованием Aspose.PDF для C++

Для преобразования PDF в PPTX, Aspose.PDF для C++ советует использовать следующие шаги кода.


<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Шаги: Преобразование PDF в PPTX на C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Шаги: Преобразование PDF в формат PowerPoint PPTX на C++</strong></a>

1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Создайте экземпляр класса [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. Используйте метод **Save** объекта **Document**, чтобы _сохранить PDF как PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Сохранить вывод в формате PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Конвертация PDF в PPTX с слайдами в виде изображений

Если вам нужно преобразовать PDF с возможностью поиска в PPTX как изображения вместо выделяемого текста, Aspose.PDF предоставляет такую возможность через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Чтобы достичь этого, установите свойство [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) класса [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) в 'true', как показано в следующем примере кода.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Сохранить вывод в формате PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Детали прогресса конвертации в PPTX

Aspose.PDF для C++ позволяет отслеживать прогресс конвертации PDF в PPTX. The [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) класс предоставляет свойство [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474), которое можно указать для пользовательского метода отслеживания хода конверсии, как показано в следующем примере кода.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Указать пользовательский обработчик прогресса
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Сохранить вывод в формате PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Следующий метод предназначен для отображения процесса конверсии.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Прогресс конверсии : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Страница результата " << eventInfo->Value << " из " << eventInfo->MaxValue << " создана." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Страница результата " << eventInfo->Value << " из " << eventInfo->MaxValue << " экспортирована." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Исходная страница " << eventInfo->Value << " из " << eventInfo->MaxValue << " проанализирована." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF for C++ предоставляет вам бесплатное онлайн-приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Коды такие же, как и выше.

_Формат_: **PowerPoint**
- [C++ PDF в PowerPoint Код](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint Программно](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint Библиотека](#cpp-pdf-to-powerpoint-pptx)
- [C++ Сохранить PDF как PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Создать PowerPoint из PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Генерация PowerPoint из PDF](#cpp-pdf-to-powerpoint-pptx)

- [C++ Конвертер PDF в PowerPoint](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX формат**
- [C++ PDF в PowerPoint PPTX Код](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint PPTX Программно](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint PPTX Библиотека](#cpp-pdf-to-powerpoint-pptx)
- [C++ Сохранить PDF как PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Генерация PowerPoint PPTX из PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Создать PowerPoint PPTX из PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF в PowerPoint PPTX Конвертер](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF в PPTX Код](#cpp-pdf-to-pptx)
- [C++ PDF в PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF в PPTX Программно](#cpp-pdf-to-pptx)
- [C++ PDF в PPTX Библиотека](#cpp-pdf-to-pptx)
- [C++ Сохранить PDF как PPTX](#cpp-pdf-to-pptx)
- [C++ Генерация PPTX из PDF](#cpp-pdf-to-pptx)
- [C++ Создать PPTX из PDF](#cpp-pdf-to-pptx)
- [C++ PDF в PPTX Конвертер](#cpp-pdf-to-pptx)