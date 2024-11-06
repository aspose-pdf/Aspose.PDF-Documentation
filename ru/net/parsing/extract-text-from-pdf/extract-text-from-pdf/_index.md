---
title: Извлечение текста из PDF C#
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: ru/net/extract-text-from-all-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF-документов с использованием Aspose.PDF на C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF-документа

Извлечение текста из PDF-документа является распространенной задачей. В этом примере вы увидите, как Aspose.PDF для .NET позволяет извлекать текст со всех страниц PDF-документа. Вам нужно создать объект класса **TextAbsorber**. После этого откройте PDF с помощью класса **Document** и вызовите метод **Accept** коллекции **Pages**. Класс **TextAbsorber** поглощает текст из документа и возвращает его в свойстве **Text**. Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Создать объект TextAbsorber для извлечения текста
TextAbsorber textAbsorber = new TextAbsorber();
// Принять абсорбер для всех страниц
pdfDocument.Pages.Accept(textAbsorber);
// Получить извлеченный текст
string extractedText = textAbsorber.Text;
// Создать писателя и открыть файл
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Написать строку текста в файл
tw.WriteLine(extractedText);
// Закрыть поток
tw.Close();
```
Вызовите метод **Accept** на определенной странице объекта Document. Index - это номер страницы, с которой необходимо извлечь текст.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Создать объект TextAbsorber для извлечения текста
TextAbsorber textAbsorber = new TextAbsorber();

// Принять абсорбер для конкретной страницы
pdfDocument.Pages[1].Accept(textAbsorber);

// Получить извлеченный текст
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Создать писателя и открыть файл
TextWriter tw = new StreamWriter(dataDir);

// Записать строку текста в файл
tw.WriteLine(extractedText);

// Закрыть поток
tw.Close();
```
## Извлечение текста со страниц с использованием класса TextDevice

Вы можете использовать класс **TextDevice** для извлечения текста из файла PDF. TextDevice использует TextAbsorber в своей реализации, таким образом, на самом деле они делают одно и то же, но TextDevice просто реализован для унификации подхода "Device" для извлечения чего-либо со страницы: ImageDevice, PageDevice и т.д. TextAbsorber может извлекать текст со страницы, всего PDF или XForm, этот TextAbsorber более универсален.

### Извлечение текста со всех страниц

Следующие шаги и фрагмент кода показывают, как извлечь текст из PDF с помощью текстового устройства.

1. Создайте объект класса Document с указанием входного файла PDF
1. Создайте объект класса TextDevice
1. Используйте объект класса TextExtractOptions для указания параметров извлечения
1. Используйте метод Process класса TextDevice для конвертации содержимого в текст
1. Сохраните текст в выходной файл

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// Строка для хранения извлеченного текста
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Создать текстовое устройство
        TextDevice textDevice = new TextDevice();

        // Установить параметры извлечения текста - установить режим извлечения текста (Raw или Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Конвертировать конкретную страницу и сохранить текст в поток
        textDevice.Process(pdfPage, textStream);
        // Конвертировать конкретную страницу и сохранить текст в поток
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Закрыть поток памяти
        textStream.Close();

        // Получить текст из потока памяти
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Сохранить извлеченный текст в текстовом файле
File.WriteAllText(dataDir, builder.ToString());
```
## Извлечение текста из определенной области страницы

Класс **TextAbsorber** предоставляет возможность извлекать текст с определенной или со всех страниц PDF-документа. Этот класс возвращает извлеченный текст в свойстве **Text**. Однако, если возникает необходимость извлечь текст из определенной области страницы, можно использовать свойство **Rectangle** класса **TextSearchOptions**. Свойство Rectangle принимает объект Rectangle в качестве значения, и с помощью этого свойства можно указать область страницы, из которой нужно извлечь текст.

Метод **Accept** страницы вызывается для извлечения текста. Создайте объекты классов **Document** и **TextAbsorber**. Вызовите метод **Accept** на отдельной странице, как **Page** Index, объекта **Document**. **Index** - это номер конкретной страницы, откуда нужно извлечь текст. Вы можете получить текст из свойства **Text** класса **TextAbsorber**. Следующий фрагмент кода показывает, как извлечь текст с отдельной страницы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Создать объект TextAbsorber для извлечения текста
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Применить absorber к первой странице
pdfDocument.Pages[1].Accept(absorber);

// Получить извлеченный текст
string extractedText = absorber.Text;
// Создать писателя и открыть файл
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Записать строку текста в файл
tw.WriteLine(extractedText);
// Закрыть поток
tw.Close();
```

## Извлечение текста по колонкам

Файл PDF может содержать элементы Текста, Изображений, Аннотаций, Вложений, Графиков и др., и Aspose.PDF для .NET предлагает функции добавления и управления всеми этими элементами.
PDF файл может содержать текст, изображения, аннотации, вложения, графики и другие элементы, и Aspose.PDF для .NET предлагает возможность добавлять и манипулировать всеми этими элементами.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по адресу https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Необходимо уменьшить размер шрифта как минимум на 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### Второй подход - Использование ScaleFactor

В этом новом выпуске мы также ввели несколько улучшений в TextAbsorber и в механизме внутреннего форматирования текста. Теперь при извлечении текста в режиме ‘Pure’, вы можете указать опцию ScaleFactor, которая может быть другим подходом для извлечения текста из многостолбцового PDF-документа помимо вышеуказанного подхода. Этот масштабирующий коэффициент может быть установлен для корректировки сетки, используемой в механизме внутреннего форматирования текста во время извлечения текста. Указание значений ScaleFactor между 1 и 0.1 (включая 0.1) имеет тот же эффект, что и уменьшение шрифта.

Указание значений ScaleFactor между 0.1 и -0.1 обрабатывается как нулевое значение, но это заставляет алгоритм вычислять необходимый масштабирующий коэффициент во время автоматического извлечения текста.
Указание значений ScaleFactor между 0.1 и -0.1 обрабатывается как нулевое значение, но это заставляет алгоритм автоматически рассчитывать необходимый масштабирующий коэффициент при извлечении текста.

Мы предлагаем использовать автомасштабирование (ScaleFactor = 0) при обработке большого количества PDF-файлов для извлечения текстового содержимого. Или вручную установить избыточное уменьшение ширины сетки (примерно ScaleFactor = 0.5). Однако вы не должны определять, необходимо ли масштабирование для конкретных документов или нет. Если вы установите избыточное уменьшение ширины сетки для документа (которому это не нужно), извлеченное текстовое содержимое останется полностью адекватным. Пожалуйста, ознакомьтесь с следующим фрагментом кода.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Установка коэффициента масштабирования 0.5 достаточно для разделения колонок в большинстве документов
// Установка нуля позволяет алгоритму автоматически выбирать коэффициент масштабирования
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

Обратите внимание, что нет прямого соответствия между новым ScaleFactor и старым коэффициентом ручного уменьшения шрифта. Однако по умолчанию алгоритм учитывает значение размера шрифта, которое уже было уменьшено по некоторым внутренним причинам. Например, уменьшение размера шрифта с 10 до 7 имеет такой же эффект, как установка масштабирующего коэффициента в 5/8 (= 0.625).

{{% /alert %}}

## Извлечение выделенного текста из PDF-документа

В различных сценариях извлечения текста из PDF-документа может возникнуть потребность извлекать только выделенный текст из документа. Для реализации этой функциональности мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлекать выделенный текст из PDF-документа, фильтруя TextMarkupAnnotation и используя указанные методы. Следующий фрагмент кода показывает, как вы можете извлечь выделенный текст из PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Перебор всех аннотаций
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Фильтрация TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Извлечение выделенных фрагментов текста
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Вывод выделенного текста
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Доступ к элементам Text Fragment и Segment из XML

Иногда нам нужен доступ к элементам TextFragement или TextSegment при обработке PDF-документов, сгенерированных из XML.
Иногда нам требуется доступ к элементам TextFragement или TextSegment при обработке PDF документов, сгенерированных из XML.

Следующий пример кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
