---
title: Извлечение изображений с использованием PdfExtractor
type: docs
weight: 20
url: /ru/net/extract-images/
description: Этот раздел объясняет, как извлекать изображения с помощью Aspose.PDF Facades, используя класс PdfExtractor.
lastmod: "2021-07-15"
---

## Извлечение изображений из всего PDF в файлы (Facades)

Класс [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) позволяет извлекать изображения из PDF файла. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Во-первых, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. Как только изображения извлечены, вы можете получить их с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с использованием цикла while. Чтобы сохранить изображения на диск, вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), который принимает путь к файлу в качестве аргумента. Следующий фрагмент кода показывает, как извлечь изображения из всего PDF в файлы.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Открыть входной PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Извлечь все изображения
            pdfExtractor.ExtractImage();

            // Получить все извлеченные изображения
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Извлечение изображений из всего PDF в потоки (Фасады)

Класс [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) позволяет извлекать изображения из PDF файла в потоки. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Во-первых, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений, вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно перебрать все извлеченные изображения с помощью цикла while. Чтобы сохранить изображения в поток, вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), которая принимает Stream в качестве аргумента. Следующий фрагмент кода показывает, как извлечь изображения из всего PDF в потоки.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Открыть входной PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Извлечь изображения
            pdfExtractor.ExtractImage();
            // Получить все извлеченные изображения
            while (pdfExtractor.HasNextImage())
            {
                // Прочитать изображение в поток памяти
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Записать на диск, если хотите, или использовать иначе.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Извлечение изображений с определенной страницы PDF (Фасады)

Вы можете извлечь изображения с определенной страницы PDF файла. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the particular page you want to extract images from.

Для этого вам нужно установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) на конкретную страницу, с которой вы хотите извлечь изображения. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). ```
Во-вторых, необходимо установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage).
``` После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям, используя цикл while. Вы можете либо сохранить изображения на диск, либо передать их в поток. Вам нужно только вызвать соответствующую перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Следующий фрагмент кода показывает, как извлечь изображения с определенной страницы PDF в потоки.

```csharp
public static void ExtractImagesParticularPage()
{
    // Открыть входной PDF
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Установить свойства StartPage и EndPage на номер страницы, с
    // которой вы хотите извлечь изображения
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Извлечь изображения
    pdfExtractor.ExtractImage();
    // Получить извлеченные изображения
    while (pdfExtractor.HasNextImage())
    {
        // Считать изображение в поток памяти
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Записать на диск, если хотите, или использовать иначе.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Извлечение изображений из диапазона страниц PDF (Фасады)

Вы можете извлечь изображения из диапазона страниц PDF файла. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) свойства на диапазон страниц, с которых вы хотите извлечь изображения. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) свойства. После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) для извлечения всех изображений в память. Как только изображения извлечены, вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно перебрать все извлеченные изображения с помощью цикла while. Вы можете сохранить изображения либо на диск, либо в поток. Вам нужно только вызвать соответствующую перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Следующий фрагмент кода показывает, как извлечь изображения из диапазона страниц PDF в потоки.

```csharp
public static void ExtractImagesRangePages()
{
    // Открыть входной PDF
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Установите свойства StartPage и EndPage на номер страницы,
    // с которой вы хотите извлечь изображения
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Извлечь изображения
    pdfExtractor.ExtractImage();
    // Получить извлеченные изображения
    while (pdfExtractor.HasNextImage())
    {
        // Прочитать изображение в поток памяти
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Записать на диск, если хотите, или использовать иначе.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Извлечение изображений с использованием режима извлечения изображений (Фасады)

Класс [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) позволяет извлекать изображения из PDF файла. Aspose.PDF поддерживает два режима извлечения; первый - это ActuallyUsedImage, который извлекает изображения, действительно используемые в PDF-документе. ```
Второй режим — это [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode), который извлекает изображения, определенные в ресурсах PDF-документа (режим извлечения по умолчанию).
``` 
Сначала вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` После этого укажите режим извлечения изображений, используя свойство [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Затем вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) для извлечения всех изображений в память в зависимости от указанного вами режима. Как только изображения извлечены, вы можете получить их с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям, используя цикл while. Для сохранения изображений на диск вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), которая принимает путь к файлу в качестве аргумента.

Следующий фрагмент кода показывает, как извлечь изображения из PDF-файла, используя опцию ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // Открыть входной PDF
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Указать режим извлечения изображений
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // Извлечь изображения на основе режима извлечения изображений
    extractor.ExtractImage();

    // Получить все извлеченные изображения
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

Для проверки, содержит ли PDF текст или изображения, используйте следующий код:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // Создать объект memoryStream для хранения извлеченного текста из документа
            MemoryStream ms = new MemoryStream();
            // Создать объект PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // Привязать входной PDF-документ к extractor
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // Извлечь текст из входного PDF-документа
            extractor.ExtractText();
            // Сохранить извлеченный текст в текстовый файл
            extractor.GetText(ms);
            // Проверить, больше ли длина MemoryStream или равна 1

            bool containsText = ms.Length >= 1;

            // Извлечь изображения из входного PDF-документа
            extractor.ExtractImage();

            // Вызов метода HasNextImage в цикле while. Когда изображения закончатся, цикл выйдет
            bool containsImage = extractor.HasNextImage();

            // Теперь выяснить, является ли этот PDF только текстовым или только изображением

            if (containsText && !containsImage)
                Console.WriteLine("PDF содержит только текст");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF содержит только изображение");
            else if (containsText && containsImage)
                Console.WriteLine("PDF содержит как текст, так и изображение");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF не содержит ни текста, ни изображений");
        }

    }
```