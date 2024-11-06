---
title: Конвертация PDF в PowerPoint в .NET
linktitle: Конвертация PDF в PowerPoint
type: docs
weight: 30
url: ru/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF позволяет конвертировать PDF в формат PPT (PowerPoint) используя .NET. Один из способов - это конвертация PDF в PPTX с сохранением слайдов в виде изображений.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Обзор

В этой статье объясняется, как **конвертировать PDF в PowerPoint с использованием C#**. Она охватывает следующие темы.

_Формат_: **PPTX**
- [C# PDF в PPTX](#csharp-pdf-to-pptx)
- [C# Конвертация PDF в PPTX](#csharp-pdf-to-pptx)
- [C# Как конвертировать PDF файл в PPTX](#csharp-pdf-to-pptx)

_Формат_: **PowerPoint**
- [C# PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Конвертация PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Как конвертировать PDF файл в PowerPoint](#csharp-pdf-to-powerpoint)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## C# Конвертация PDF в PowerPoint и PPTX
## Преобразование PDF в PowerPoint и PPTX

**Aspose.PDF для .NET** позволяет отслеживать прогресс преобразования PDF в PPTX.

У нас есть API под названием Aspose.Slides, который предлагает функционал для создания и управления презентациями PPT/PPTX. Этот API также предоставляет возможность преобразования файлов PPT/PPTX в формат PDF. Недавно многие наши клиенты выразили потребность в поддержке возможности преобразования PDF в формат PPTX. Начиная с версии Aspose.PDF для .NET 10.3.0, мы ввели функцию преобразования документов PDF в формат PPTX. Во время этого преобразования отдельные страницы файла PDF конвертируются в отдельные слайды в файле PPTX.

Во время преобразования PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, текст отображается как текст, который вы можете выбрать или обновить.
При конвертации PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, текст отображается как текст, который вы можете выбрать/обновить.

## Простая конвертация PDF в PowerPoint с использованием C# и Aspose.PDF .NET

Для конвертации PDF в PPTX, Aspose.PDF для .NET рекомендует использовать следующие шаги кода.

<a name="csharp-pdf-to-powerpoint"><strong>Шаги: Конвертация PDF в PowerPoint на C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Шаги: Конвертация PDF в PPTX на C#</strong></a>

1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. Создайте экземпляр класса [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)
3. Используйте метод **Save** объекта **Document** для сохранения PDF в виде PPTX

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Загрузка документа PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Создание экземпляра PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Сохранение результата в формате PPTX
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## Конвертация PDF в PPTX с использованием слайдов как изображений

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете ознакомиться с функциональностью и качеством его работы.

[![Конвертация Aspose.PDF из PDF в PPTX с помощью бесплатного приложения](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Если вам нужно конвертировать поисковый PDF в PPTX в виде изображений, а не выбираемого текста, Aspose.PDF предоставляет такую функцию через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Для этого установите свойство [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) класса [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) в 'true', как показано в следующем примере кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Загрузка документа PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Создание экземпляра PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Сохранение результата в формате PPTX
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## Детали прогресса конвертации PPTX

Aspose.PDF для .NET позволяет отслеживать прогресс конвертации PDF в PPTX. Класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) предоставляет свойство [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler), которое может быть указано для пользовательского метода отслеживания прогресса конвертации, как показано в следующем примере кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по адресу https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Загрузка документа PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Создание экземпляра PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//Указание пользовательского обработчика прогресса
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Сохранение результата в формате PPTX
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
Ниже приведен пользовательский метод для отображения прогресса конвертации.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Прогресс конвертации : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Создана разметка {1} из {2} страницы результата.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Страница результата {1} из {2} экспортирована.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Анализирована исходная страница {1} из {2}.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    default:
        break;
}
```
## Смотрите также

Эта статья также охватывает следующие темы. Коды такие же, как указано выше.

_Формат_: **PowerPoint**
- [C# код для конвертации PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# API для конвертации PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# программная конвертация PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# библиотека для конвертации PDF в PowerPoint](#csharp-pdf-to-powerpoint)
- [C# сохранение PDF как PowerPoint](#csharp-pdf-to-powerpoint)
- [C# генерация PowerPoint из PDF](#csharp-pdf-to-powerpoint)
- [C# создание PowerPoint из PDF](#csharp-pdf-to-powerpoint)
- [C# конвертер PDF в PowerPoint](#csharp-pdf-to-powerpoint)

_Формат_: **PPTX**
- [C# код для конвертации PDF в PPTX](#csharp-pdf-to-pptx)
- [C# API для конвертации PDF в PPTX](#csharp-pdf-to-pptx)
- [C# программная конвертация PDF в PPTX](#csharp-pdf-to-pptx)
- [C# библиотека для конвертации PDF в PPTX](#csharp-pdf-to-pptx)
- [C# сохранение PDF как PPTX](#csharp-pdf-to-pptx)
- [C# генерация PPTX из PDF](#csharp-pdf-to-pptx)
- [C# создание PPTX из PDF](#csharp-pdf-to-pptx)
- [C# конвертер PDF в PPTX](#csharp-pdf-to-pptx)
