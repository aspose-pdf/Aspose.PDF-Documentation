---
title: Извлечение текста из PDF-файла
type: docs
weight: 30
url: /net/extract-text/
description: Этот раздел объясняет, как извлечь текст из pdf с использованием класса PdfExtractor.
lastmod: "2021-06-05"
---

В этой статье мы рассмотрим детали извлечения текста из PDF-файла. Все эти функции извлечения предоставлены в одном месте, в классе [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Мы увидим, как использовать эти функции в нашем коде.

Класс [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) предоставляет три типа возможностей извлечения. Эти три категории - Текст, Изображения и Вложения. Для выполнения извлечения в каждой из этих трех категорий PdfExtractor предлагает различные методы, которые работают вместе, чтобы дать вам окончательный результат.

Например, для извлечения текста вы можете использовать три метода, т.е. 
[ExtractText, GetText, HasNextPageText и GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index).
``` Теперь, чтобы начать извлечение текста, прежде всего, вам нужно вызвать метод [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); это извлечет текст из файла PDF и сохранит его в памяти. После этого метод [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) возьмет этот извлеченный текст и сохранит его на диск в указанном месте в файле. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) помогает вам пройтись по каждой странице и проверить, есть ли на следующей странице какой-либо текст. Если он содержит текст, то [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) поможет вам сохранить текст отдельной страницы в файл.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Создать объект класса PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Привязать входной PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // Извлечь текст
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Извлечь текст в отдельные файлы
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
Для извлечения режима извлечения текста используйте следующий код:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Создайте объект класса PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Привяжите входной PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // Извлечение текста
    // pdfExtractor.ExtractTextMode = 0; //чистый режим
    pdfExtractor.ExtractTextMode = 1; //сырой режим
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Извлекайте текст в отдельные файлы
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```