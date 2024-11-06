---
title: Извлечение страниц PDF
type: docs
weight: 40
url: ru/net/extract-pdf-pages/
description: В этом разделе объясняется, как извлекать страницы PDF с использованием Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Извлечение страниц PDF между двумя номерами, используя пути к файлам

Метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет извлекать указанный диапазон страниц из PDF файла. Этот перегруженный метод позволяет извлекать страницы при манипуляции PDF файлами с диска. Этот перегруженный метод требует следующие параметры: путь к входному файлу, начальная страница, конечная страница и путь к выходному файлу. Страницы от начальной до конечной будут извлечены, и результат будет сохранен на диске. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами, используя пути к файлам.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Создать объект PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Извлечение страниц
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Извлечение массива страниц PDF с использованием путей к файлам

Если вы не хотите извлекать диапазон страниц, а определенный набор страниц, метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) позволяет сделать это также. Сначала вам нужно создать целочисленный массив со всеми номерами страниц, которые необходимо извлечь. Этот перегруженный метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) принимает следующие параметры: входной PDF файл, целочисленный массив страниц, которые нужно извлечь, и выходной PDF файл. Следующий фрагмент кода показывает, как извлечь страницы PDF, используя пути к файлам.

```csharp
public static void Extract_PDFPages_Streams()
{
    // Создать объект PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Создать потоки
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // Извлечь страницы
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## Извлечение страниц PDF между двумя номерами с использованием потоков

Метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет извлечь диапазон страниц с использованием потоков. Вам необходимо передать следующие параметры в эту перегрузку: входной поток, начальная страница, конечная страница и выходной поток. Страницы, указанные в диапазоне между начальной и конечной страницами, будут извлечены из входного потока и сохранены в выходной поток. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами с использованием потоков.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Создаем объект PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Извлечение страниц
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Извлечение массива страниц PDF с использованием потоков

Массив страниц можно извлечь из PDF потока и сохранить в выходной поток, используя соответствующую перегрузку метода [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Если вы не хотите извлекать диапазон страниц, а набор конкретных страниц, метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) позволяет сделать это. Сначала вам нужно создать массив целых чисел со всеми номерами страниц, которые необходимо извлечь. Эта перегрузка метода [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) принимает следующие параметры: входной поток, массив целых чисел страниц для извлечения и выходной поток. 
Следующий фрагмент кода показывает, как извлекать страницы PDF, используя потоки.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Создать объект PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Создать потоки
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Извлечь страницы
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```