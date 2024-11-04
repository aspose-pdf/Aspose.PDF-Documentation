---
title: Извлечение страниц PDF
type: docs
weight: 20
url: /java/extract-pdf-pages/
description: Этот раздел объясняет, как извлекать страницы PDF с помощью com.aspose.pdf.facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Извлечение страниц PDF между двумя номерами, используя пути к файлам

Метод [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) класса [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) позволяет извлекать указанный диапазон страниц из PDF файла. Этот перегруженный метод позволяет извлекать страницы при манипуляции PDF файлами с диска. Для этого перегруженного метода требуются следующие параметры: путь к входному файлу, начальная страница, конечная страница и путь к выходному файлу. Страницы от начальной до конечной будут извлечены, и результат будет сохранен на диске. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами, используя пути к файлам.

```java
  public static void Extract_PDFPages_FilePaths() {
        // Создание объекта PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // Извлечение страниц
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## Извлечение массива страниц PDF с использованием путей к файлам

Если вы не хотите извлекать диапазон страниц, а определенный набор страниц, метод [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) позволяет сделать это. Сначала вам нужно создать массив целых чисел со всеми номерами страниц, которые необходимо извлечь. Эта перегрузка метода [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) принимает следующие параметры: входной PDF файл, массив целых чисел страниц для извлечения и выходной PDF файл. Следующий фрагмент кода показывает, как извлечь страницы PDF, используя пути к файлам.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // Создать объект PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // Извлечь страницы
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## Извлечение страниц PDF между двумя номерами с использованием потоков

Метод [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) класса [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) позволяет извлечь диапазон страниц с использованием потоков. Необходимо передать следующие параметры для этой перегрузки: входной поток, начальная страница, конечная страница и выходной поток. Страницы, указанные в диапазоне между начальной и конечной страницей, будут извлечены из входного потока и сохранены в выходной поток. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами с использованием потоков.

```java
public static void Extract_PDFPages_Streams()
    {
         // Создать объект PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // Создать потоки
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // Извлечение страниц
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## Извлечение массива страниц PDF с использованием потоков

Массив страниц может быть извлечен из PDF потока и сохранен в выходном потоке с использованием соответствующей перегрузки метода [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). Если вы не хотите извлекать диапазон страниц, а предпочитаете набор определенных страниц, метод [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) позволяет сделать это. Сначала вам нужно создать массив целых чисел с номерами всех страниц, которые необходимо извлечь. Эта перегрузка метода [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) принимает следующие параметры: входной поток, массив целых чисел страниц для извлечения и выходной поток.
Следующий фрагмент кода показывает, как извлечь страницы PDF с использованием потоков.

```java
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