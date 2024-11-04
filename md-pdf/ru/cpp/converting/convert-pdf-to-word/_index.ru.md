---
title: Convert PDF to Microsoft Word Documents in C++
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ библиотека позволяет легко и полностью контролировать процесс конвертации PDF в формат Word с использованием C++. Эти форматы включают DOC и DOCX. Узнайте больше о том, как настроить конвертацию PDF в документы Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Обзор

Эта статья объясняет, как конвертировать PDF в документы Microsoft Word с использованием C++. Она охватывает следующие темы.

_Формат_: **DOC**
- [C++ PDF в DOC](#cpp-pdf-to-doc)
- [C++ Конвертация PDF в DOC](#cpp-pdf-to-doc)
- [C++ Как конвертировать файл PDF в DOC](#cpp-pdf-to-doc)

_Формат_: **DOCX**
- [C++ PDF в DOCX](#cpp-pdf-to-docx)
- [C++ Конвертация PDF в DOCX](#cpp-pdf-to-docx)
- [C++ Как конвертировать файл PDF в DOCX](#cpp-pdf-to-docx)

_Формат_: **Microsoft Word DOC формат**
- [C++ PDF в Word](#cpp-pdf-to-word-doc)
- [C++ Конвертация PDF в Word](#cpp-pdf-to-word-doc)

- [C++ Как конвертировать файл PDF в Word](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX формат**  
- [C++ PDF в Word](#cpp-pdf-to-word-docx)  
- [C++ Конвертация PDF в Word](#cpp-pdf-to-word-docx)  
- [C++ Как конвертировать PDF файл в Word](#cpp-pdf-to-word-docx)  

Другие темы, охватываемые этой статьей  
- [См. также](#see-also)  

## Конвертация PDF в Word на C++  

Одна из самых популярных функций — это конвертация PDF в Microsoft Word DOC, что делает содержание легким для редактирования. Aspose.PDF для C++ позволяет конвертировать PDF файлы в DOC.  

## Конвертировать PDF в DOC (Word 97-2003) файл  

Конвертируйте PDF файл в формат DOC с легкостью и полным контролем. Aspose.PDF для C++ гибкий и поддерживает широкий спектр конверсий. Конвертация страниц из PDF документов в изображения, например, очень популярная функция.  

Конвертация, которую многие из наших клиентов запрашивали, это PDF в DOC: конвертация PDF файла в документ Microsoft Word. Пользователи хотят этого, потому что PDF файлы не могут быть легко отредактированы, тогда как документы Word могут. Некоторые компании хотят, чтобы их пользователи могли изменять текст, таблицы и изображения в файлах, которые начинались как PDF.

Сохраняя традицию делать вещи простыми и понятными, Aspose.PDF for C++ позволяет преобразовать исходный PDF файл в DOC файл с помощью двух строк кода. Для реализации этой функции мы ввели перечисление под названием SaveFormat, и его значение .Doc позволяет сохранить исходный файл в формате Microsoft Word.

Следующий фрагмент кода на C++ демонстрирует процесс преобразования PDF файла в формат DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Шаги: Преобразование PDF в DOC на C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Шаги: Преобразование PDF в формат Microsoft Word DOC на C++</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным документом PDF.
2. Сохраните его в формате **SaveFormat::Doc**, вызвав метод **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Сохранить файл в формате MS документа
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

Следующий фрагмент кода показывает процесс преобразования PDF файла в DOC в расширенной версии:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Установить режим распознавания как Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Установить горизонтальную близость как 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Включить распознавание маркеров в процессе конвертации
    saveOptions->set_RecognizeBullets(true);

    try {
        // Сохранить файл в формате MS документа
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте преобразовать PDF в DOC онлайн**

Aspose.PDF для C++ предлагает вам бесплатное онлайн-приложение ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.

[![Преобразовать PDF в DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Преобразование PDF в DOCX

Aspose.PDF для C++ API позволяет читать и преобразовывать PDF документы в DOCX с использованием языка C++. DOCX — это известный формат документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы Docx могут быть открыты в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на C++ показывает процесс преобразования файла PDF в формат DOCX.

<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Шаги: Преобразование PDF в DOCX на C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Шаги: Преобразование PDF в формат Microsoft Word DOCX на C++</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF-документом.
2. Сохраните его в формате **SaveFormat::DocX**, вызвав метод **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Сохранить файл в формате MS документа
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

Класс [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) имеет свойство с именем Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX. Чтобы преобразовать PDF файл в формат DOCX, пожалуйста, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

Пожалуйста, обратите внимание на следующий фрагмент кода, который предоставляет возможность преобразования PDF файла в формат DOCX с использованием C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Установить другие параметры DocSaveOptions
    // ...

    // Сохранить файл в формате MS документа

    try {
        // Сохранить файл в формате MS документа
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF для C++ предоставляет вам бесплатное онлайн-приложение ["PDF в DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Приложение для конвертации PDF в Word бесплатно](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Код такой же, как и выше.

_Формат_: **Формат Microsoft Word DOC**
- [Код C++ для конвертации PDF в Word](#cpp-pdf-to-word-doc)
- [API C++ для конвертации PDF в Word](#cpp-pdf-to-word-doc)
- [Программная конвертация PDF в Word на C++](#cpp-pdf-to-word-doc)
- [Библиотека C++ для конвертации PDF в Word](#cpp-pdf-to-word-doc)
- [Сохранение PDF как Word на C++](#cpp-pdf-to-word-doc)
- [Создание Word из PDF на C++](#cpp-pdf-to-word-doc)
- [Генерация Word из PDF на C++](#cpp-pdf-to-word-doc)
- [Конвертер PDF в Word на C++](#cpp-pdf-to-word-doc)

_Формат_: **Формат Microsoft Word DOCX**

- [Код C++ для конвертации PDF в Word](#cpp-pdf-to-word-docx)
- [C++ PDF в Word API](#cpp-pdf-to-word-docx)
- [C++ PDF в Word Программно](#cpp-pdf-to-word-docx)
- [C++ PDF в Word Библиотека](#cpp-pdf-to-word-docx)
- [C++ Сохранить PDF как Word](#cpp-pdf-to-word-docx)
- [C++ Создать Word из PDF](#cpp-pdf-to-word-docx)
- [C++ Генерация Word из PDF](#cpp-pdf-to-word-docx)
- [C++ Конвертер PDF в Word](#cpp-pdf-to-word-docx)

_Формат_: **DOC**
- [C++ PDF в DOC Код](#cpp-pdf-to-doc)
- [C++ PDF в DOC API](#cpp-pdf-to-doc)
- [C++ PDF в DOC Программно](#cpp-pdf-to-doc)
- [C++ PDF в DOC Библиотека](#cpp-pdf-to-doc)
- [C++ Сохранить PDF как DOC](#cpp-pdf-to-doc)
- [C++ Создать DOC из PDF](#cpp-pdf-to-doc)
- [C++ Генерация DOC из PDF](#cpp-pdf-to-doc)
- [C++ Конвертер PDF в DOC](#cpp-pdf-to-doc)

_Формат_: **DOC**
- [C++ PDF в DOCX Код](#cpp-pdf-to-docx)
- [C++ PDF в DOCX API](#cpp-pdf-to-docx)
- [C++ PDF в DOCX Программно](#cpp-pdf-to-docx)
- [C++ PDF в DOCX Библиотека](#cpp-pdf-to-docx)
- [C++ Сохранить PDF как DOCX](#cpp-pdf-to-docx)

- [C++ Создать DOCX из PDF](#cpp-pdf-to-docx)

- [C++ Создание DOCX из PDF](#cpp-pdf-to-docx)
- [C++ Конвертер PDF в DOCX](#cpp-pdf-to-docx)
```