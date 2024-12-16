---
title: Объединение PDF документов в C#
linktitle: Объединение PDF документов
type: docs
weight: 20
url: /ru/net/concatenate-pdf-documents/
description: Этот раздел объясняет, как объединить PDF документы с использованием Aspose.PDF Facades и класса PdfFileEditor.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **Обзор**

Эта статья объясняет, как объединить, комбинировать или склеить разные PDF файлы в один PDF с использованием C#. Она охватывает такие темы, как

- [C# Объединение PDF файлов](#concatenate-pdf-files-using-file-paths)
- [C# Комбинирование PDF файлов](#concatenate-pdf-files-using-file-paths)

- [C# Объединение нескольких PDF файлов в один PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Объединить несколько PDF файлов в один PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Объединить все PDF файлы в папке](#concatenating-all-pdf-files-in-particular-folder)
- [C# Объединить все PDF файлы в папке](#concatenating-all-pdf-files-in-particular-folder)
- [C# Объединить PDF файлы, используя пути к файлам](#concatenate-pdf-files-using-file-paths)
- [C# Объединить PDF файлы, используя потоки](#concatenate-array-of-pdf-files-using-streams)
- [C# Объединить все PDF файлы в папке](#concatenate-pdf-files-in-folder)

## Объединение PDF файлов, используя пути к файлам

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) это класс в [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades), который позволяет объединять несколько PDF файлов. Вы можете не только объединять файлы с помощью FileStreams, но и использовать MemoryStreams. В этой статье будет объяснен процесс объединения файлов с использованием MemoryStreams, а затем показан с помощью примера кода.

Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) может быть использован для объединения двух PDF-файлов. Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) позволяет передать три параметра: первый входной PDF, второй входной PDF и выходной PDF. Итоговый выходной PDF содержит оба входных PDF-файла.

Следующий пример кода на C# показывает, как объединить PDF-файлы, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

В некоторых случаях, когда имеется много оглавлений, пользователи могут отключить их, установив CopyOutlines в false, и улучшить производительность объединения.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Объединение нескольких PDF-файлов с использованием MemoryStreams

Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) принимает исходные PDF-файлы и PDF-файл назначения в качестве параметров. Эти параметры могут быть либо путями к PDF-файлам на диске, либо они могут быть MemoryStreams. Теперь, для этого примера, мы сначала создадим два потока файлов для чтения PDF-файлов с диска. Затем мы конвертируем эти файлы в массивы байтов. Эти массивы байтов PDF-файлов будут преобразованы в MemoryStreams. Как только мы получим MemoryStreams из PDF-файлов, мы сможем передать их в метод объединения и объединить в один выходной файл.

Следующий фрагмент кода C# показывает, как объединить несколько PDF-файлов с использованием MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Объединение массива PDF-файлов с использованием путей к файлам

Если вы хотите объединить несколько PDF-файлов, вы можете использовать перегрузку метода [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), которая позволяет передавать массив PDF-файлов. Итоговый результат сохраняется как объединенный файл, созданный из всех файлов в массиве. Следующий фрагмент кода на C# показывает, как объединить массив PDF-файлов, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Объединение массива PDF-файлов с использованием потоков

Объединение массива PDF-файлов не ограничивается только файлами, находящимися на диске. Вы также можете объединить массив PDF файлов из потоков. Если вы хотите объединить несколько PDF файлов, вы можете использовать соответствующую перегрузку метода [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Сначала вам нужно создать массив входных потоков и один поток для выходного PDF, а затем вызвать метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Выходной результат будет сохранен в выходном потоке. Следующий фрагмент кода на C# показывает, как объединить массив PDF файлов, используя потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Объединение всех PDF файлов в определенной папке

Вы даже можете прочитать все PDF файлы в определенной папке во время выполнения и объединить их, даже не зная имен файлов. Предоставьте путь к каталогу, который содержит PDF-документы, которые вы хотите объединить.

Попробуйте использовать следующий фрагмент кода C#, чтобы достичь этой функциональности.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Объединение PDF-форм и сохранение уникальности имен полей

Класс [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) в [пространстве имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предлагает возможность объединения PDF-файлов. Теперь, если PDF файлы, которые нужно объединить, содержат поля формы с одинаковыми именами полей, Aspose.PDF предоставляет возможность сделать поля в результирующем PDF файле уникальными, а также вы можете указать суффикс, чтобы сделать имена полей уникальными. Свойство [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) как true сделает имена полей уникальными при объединении PDF форм. Также свойство [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) класса PdfFileEditor может быть использовано для указания пользовательского формата суффикса, который добавляется к имени поля, чтобы сделать его уникальным при объединении форм. Эта строка должна содержать подстроку `%NUM%`, которая будет заменена на числа в результирующем файле.

Пожалуйста, смотрите следующий простой пример кода для достижения этой функциональности.
## Объединение PDF файлов и создание оглавления

## Объединение PDF файлов

Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы узнать, как объединять PDF файлы.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Вставка пустой страницы

После объединения PDF файлов мы можем вставить пустую страницу в начало документа, на которой можно создать оглавление. Чтобы выполнить это требование, мы можем загрузить объединенный файл в объект **Document** и вызвать метод Page.Insert(...), чтобы вставить пустую страницу.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Добавление текстовых штампов

Для создания оглавления нам необходимо добавить текстовые штампы на первой странице, используя объекты [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). 
Класс Stamp предоставляет метод `BindLogo(...)` для добавления [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext), и мы также можем указать местоположение для добавления этих текстовых штампов с помощью метода `SetOrigin(..)`. В этой статье мы объединяем два PDF-файла, поэтому нам нужно создать два объекта текстовых штампов, указывающих на эти отдельные документы.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Создать локальные ссылки

Теперь нам нужно добавить ссылки на страницы внутри объединенного файла. Чтобы выполнить это требование, мы можем использовать метод `CreateLocalLink(..)` класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). В следующем фрагменте кода мы передали Transparent в качестве 4-го аргумента, чтобы прямоугольник вокруг ссылки не был виден.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
```
### Полный код

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

## Объединение PDF файлов в папке

Класс [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) в пространстве имен Aspose.Pdf.Facades предоставляет возможность объединять PDF файлы. Вы можете даже прочитать все PDF файлы в определенной папке во время выполнения и объединить их, даже не зная имен файлов. Просто укажите путь к каталогу, содержащему PDF документы, которые вы хотите объединить.

Попробуйте использовать следующий фрагмент кода на C# для достижения этой функциональности с помощью Aspose.PDF:

```csharp
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Извлечь имена всех PDF файлов в определенном каталоге
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Получить текущую системную дату и установить ее формат
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Получить текущее системное время и установить его формат
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Установить значение для итогового результирующего PDF документа
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Создать экземпляр объекта PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Вызвать метод Concatenate объекта PdfFileEditor для объединения всех входных файлов
// В один выходной файл
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```