---
title: Конвертация PDF в документы Microsoft Word в .NET
linktitle: Конвертация PDF в Word
type: docs
weight: 10
url: /net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Узнайте, как написать код на C# для конвертации PDF в форматы Microsoft Word с использованием Aspose.PDF для .NET и настроить конвертацию PDF в DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

В этой статье объясняется, как **конвертировать PDF в документы Microsoft Word с использованием C#**. Она охватывает следующие темы.

_Формат_: **DOC**

- [C# PDF в DOC](#csharp-pdf-to-doc)
- [C# Конвертация PDF в DOC](#csharp-pdf-to-doc)
- [C# Как конвертировать файл PDF в DOC](#csharp-pdf-to-doc)

_Формат_: **DOCX**

- [C# PDF в DOCX](#csharp-pdf-to-docx)
- [C# Конвертация PDF в DOCX](#csharp-pdf-to-docx)
- [C# Как конвертировать файл PDF в DOCX](#csharp-pdf-to-docx)

_Формат_: **Word**

- [C# PDF в Word](#csharp-pdf-to-docx)
- [C# Конвертация PDF в Word](#csharp-pdf-to-doc)
- [C# Как конвертировать файл PDF в Word](#csharp-pdf-to-docx)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Конвертация PDF в DOC и DOCX

Одной из самых популярных функций является конвертация PDF в Microsoft Word DOC, что облегчает управление содержимым. **Aspose.PDF для .NET** позволяет быстро и эффективно конвертировать файлы PDF в форматы DOC и DOCX.

## Конвертация PDF в DOC (файл Microsoft Word 97-2003)

Конвертируйте файлы PDF в формат DOC легко и с полным контролем. Aspose.PDF для .NET является гибким и поддерживает широкий спектр конверсий. Например, очень популярной функцией является конвертация страниц из документов PDF в изображения.

Многие наши клиенты запросили конвертацию из PDF в DOC: конвертацию файла PDF в документ Microsoft Word. Клиенты желают это, потому что файлы PDF не так легко редактировать, в то время как документы Word можно. Некоторые компании хотят, чтобы их пользователи могли манипулировать текстом, таблицами и изображениями в файлах, которые начинались как PDF.

Сохраняя традиции делать вещи простыми и понятными, Aspose.PDF для .NET позволяет преобразовать исходный файл PDF в файл DOC всего двумя строками кода.
Сохраняя традицию делать вещи простыми и понятными, Aspose.PDF для .NET позволяет преобразовать исходный PDF файл в DOC файл всего двумя строками кода.

Следующий фрагмент кода на C# демонстрирует конвертацию PDF файла в формат DOC.

<a name="csharp-pdf-to-doc"><strong>Шаги: Конвертация PDF в DOC на C#</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в формат **SaveFormat.Doc**, вызвав метод **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // Открыть исходный PDF документ
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Сохранить файл в формате MS document
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### Использование класса DocSaveOptions

Класс [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) предоставляет множество свойств, которые улучшают конвертацию PDF файлов в формат DOC.
Класс [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) предоставляет множество свойств, которые улучшают конвертацию PDF файлов в формат DOC.

- Режим [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) быстрый и хорошо сохраняет оригинальный вид PDF файла, но редактируемость результирующего документа может быть ограничена. Каждый визуально сгруппированный текстовый блок в оригинальном PDF преобразуется в текстовое поле в выходном документе. Это достигает максимального сходства с оригиналом, поэтому выходной документ выглядит хорошо, но полностью состоит из текстовых полей, редактирование которых в Microsoft Word может быть довольно сложным.
- Режим [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) это полный режим распознавания, где движок выполняет группировку и многоуровневый анализ для восстановления оригинального документа согласно замыслу автора, при этом производя легко редактируемый документ.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) - это полный режим распознавания, где движок выполняет группировку и многоуровневый анализ для восстановления оригинального документа в соответствии с намерениями автора, создавая при этом легко редактируемый документ.

Свойство [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) можно использовать для контроля относительной близости между текстовыми элементами. Это означает, что расстояние нормируется размером шрифта. У более крупных шрифтов могут быть большие промежутки между слогами, но они всё ещё считаются единым целым. Указывается в процентах от размера шрифта; например, 1 = 100%. Это означает, что два символа размером 12pt, размещенные на расстоянии 12 pt друг от друга, являются близкими.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) используется для включения распознавания маркеров во время конвертации.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Установить режим распознавания как Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Установить горизонтальную близость как 2.5
        RelativeHorizontalProximity = 2.5f,
        // Включить значение для распознавания маркеров в процессе конвертации
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете изучить функциональность и качество его работы.

[![Конвертировать PDF в DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертирование PDF в DOCX (файл Microsoft Word 2007-2021)

API Aspose.PDF для .NET позволяет читать и конвертировать документы PDF в формат DOCX с использованием C# и любого .NET языка. DOCX — это хорошо известный формат для документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы docx могут быть открыты в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на C# показывает конвертацию файла PDF в формат DOCX.

<a name="csharp-pdf-to-docx"><strong>Шаги: Конвертация PDF в DOCX на C#</strong></a>

1.
1.
2. Сохраните в формате **SaveFormat.DocX**, вызвав метод **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Откройте исходный PDF документ
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Сохраните результат в DOC файл
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Конвертирование PDF в DOCX в улучшенном режиме

Для получения лучших результатов конвертации PDF в DOCX, вы можете использовать режим `EnhancedFlow`.
Основное отличие между режимами Flow и Enhanced Flow заключается в том, что таблицы (как с границами, так и без) распознаются как настоящие таблицы, а не как текст с картинкой на фоне.
Также происходит распознавание нумерованных списков и множество других мелких деталей.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Откройте исходный PDF документ
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Создайте объект DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Укажите выходной формат как DOCX
        Format = DocSaveOptions.DocFormat.DocX,
        // Установите другие параметры DocSaveOptions
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Сохраните документ в формате docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Word Бесплатное приложение](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Смотрите также

Эта статья также охватывает следующие темы. Коды такие же, как указано выше.

_Формат_: **Word**

- [C# Код PDF в Word](#csharp-pdf-to-docx)
- [C# API PDF в Word](#csharp-pdf-to-docx)
- [C# Программное PDF в Word](#csharp-pdf-to-docx)
- [C# Библиотека PDF в Word](#csharp-pdf-to-docx)
- [C# Сохранить PDF как Word](#csharp-pdf-to-docx)
- [C# Создать Word из PDF](#csharp-pdf-to-docx)
- [C# Создать Word из PDF](#csharp-pdf-to-docx)
- [C# Конвертер PDF в Word](#csharp-pdf-to-docx)

_Формат_: **DOC**

- [C# Код PDF в DOC](#csharp-pdf-to-doc)
- [C# API PDF в DOC](#csharp-pdf-to-doc)
- [C# API для конвертации PDF в DOC](#csharp-pdf-to-doc)
- [C# Программное преобразование PDF в DOC](#csharp-pdf-to-doc)
- [C# Библиотека для конвертации PDF в DOC](#csharp-pdf-to-doc)
- [C# Сохранение PDF как DOC](#csharp-pdf-to-doc)
- [C# Генерация DOC из PDF](#csharp-pdf-to-doc)
- [C# Создание DOC из PDF](#csharp-pdf-to-doc)
- [C# Конвертер PDF в DOC](#csharp-pdf-to-doc)

_Формат_: **DOCX**

- [C# Код для конвертации PDF в DOCX](#csharp-pdf-to-docx)
- [C# API для конвертации PDF в DOCX](#csharp-pdf-to-docx)
- [C# Программное преобразование PDF в DOCX](#csharp-pdf-to-docx)
- [C# Библиотека для конвертации PDF в DOCX](#csharp-pdf-to-docx)
- [C# Сохранение PDF как DOCX](#csharp-pdf-to-docx)
- [C# Генерация DOCX из PDF](#csharp-pdf-to-docx)
- [C# Создание DOCX из PDF](#csharp-pdf-to-docx)
- [C# Конвертер PDF в DOCX](#csharp-pdf-to-docx)

