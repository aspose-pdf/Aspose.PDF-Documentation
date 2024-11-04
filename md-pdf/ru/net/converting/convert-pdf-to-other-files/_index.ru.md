---
title: Конвертация PDF в EPUB, LaTeX, Text, XPS на C#
linktitle: Конвертация PDF в другие форматы
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: конвертировать, PDF, EPUB, LaTeX, Текст, XPS, C#
description: Эта тема показывает, как конвертировать PDF файл в другие форматы файлов, такие как EPUB, LaTeX, Text, XPS и другие, используя C# или .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертация PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в EPUB с помощью бесплатного приложения](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Электронная публикация">EPUB</abbr>** — это свободный и открытый стандарт электронных книг от Международного форума цифровых изданий (IDPF).
**<abbr title="Электронная публикация">EPUB</abbr>** - это свободный и открытый стандарт электронных книг от Международного форума цифровых изданий (IDPF).
EPUB предназначен для контента с изменяемым макетом, что означает, что читатель EPUB может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированным макетом. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Aspose.PDF для .NET также поддерживает функцию конвертации документов PDF в формат EPUB. Aspose.PDF для .NET имеет класс под названием EpubSaveOptions, который можно использовать в качестве второго аргумента в методе [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) для генерации файла EPUB.
Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этой задачи на C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Загрузить документ PDF
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Создать опции сохранения Epub
EpubSaveOptions options = new EpubSaveOptions();
// Указать макет для содержимого
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// Сохранить документ EPUB
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## Конвертация PDF в LaTeX/TeX

**Aspose.PDF для .NET** поддерживает конвертацию PDF в LaTeX/TeX.
Формат файла LaTeX - это текстовый файл с специальной разметкой, который используется в системе подготовки документов на базе TeX для высококачественной вёрстки.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с помощью бесплатного приложения](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для конвертации файлов PDF в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions), который предоставляет свойство OutDirectoryPath для сохранения временных изображений в процессе конвертации.

Следующий фрагмент кода показывает процесс конвертации файлов PDF в формат TEX с помощью C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Создание объекта документа
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// Создание объекта настроек сохранения LaTeX          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// Указание директории вывода
string pathToOutputDirectory = dataDir;

// Установка пути к директории вывода для объекта настроек сохранения
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// Сохранение файла PDF в формат LaTeX           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## Конвертация PDF в текст

**Aspose.PDF для .NET** поддерживает конвертацию всего документа PDF и отдельной страницы в текстовый файл.

### Конвертация всего документа PDF в текстовый файл

Вы можете конвертировать документ PDF в файл TXT с помощью метода [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) класса [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

Следующий фрагмент кода объясняет, как извлечь тексты со всех страниц.

```csharp
public static void ConvertPDFDocToTXT()
{
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Сохранить извлеченный текст в текстовый файл
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

{{% /alert %}}


### Конвертация страницы PDF в текстовый файл

Вы можете конвертировать документ PDF в файл TXT с помощью Aspose.PDF для .NET. Вы должны использовать метод `Visit` класса `TextAbsorber` для решения этой задачи.

Следующий фрагмент кода объясняет, как извлечь тексты с определенных страниц.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // Сохраните извлеченный текст в текстовом файле
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## Конвертировать PDF в XPS

**Aspose.PDF для .NET** предоставляет возможность конвертировать файлы PDF в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать представленный фрагмент кода для конвертации файлов PDF в формат XPS на C#.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с помощью бесплатного приложения](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь связан со спецификацией XML Paper от корпорации Microsoft. Спецификация XML Paper (XPS), ранее имевшая кодовое название Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации файлов PDF в XPS, Aspose.PDF использует класс [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions), который используется в качестве второго аргумента метода [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) для генерации файла XPS.
Для конвертации PDF файлов в XPS, Aspose.PDF использует класс [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions), который используется в качестве второго аргумента метода [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) для генерации файла XPS.

Следующий фрагмент кода показывает процесс конвертации PDF файла в формат XPS.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Загрузить PDF документ
Document pdfDocument = new Document(dataDir + "input.pdf");

// Создать опции сохранения в XPS
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// Сохранить документ XPS
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
