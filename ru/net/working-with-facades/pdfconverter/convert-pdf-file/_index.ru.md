---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: Этот раздел объясняет, как конвертировать PDF файл с использованием Aspose.PDF Facades, используя класс PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convert PDF Pages to Different Image Formats (Facades)

Для того чтобы конвертировать страницы PDF в различные форматы изображений, необходимо создать объект [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) и открыть PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно вызвать метод [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) для инициализации задач. Затем вы можете пройтись по всем страницам с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). Метод [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) позволяет создать изображение конкретной страницы. Вам также нужно передать ImageFormat этому методу, чтобы создать изображение конкретного типа, например, JPEG, GIF или PNG и т.д. Наконец, вызовите метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) класса [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). Следующий фрагмент кода показывает, как конвертировать страницы PDF в изображения.

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // Создать объект PdfConverter
            PdfConverter converter = new PdfConverter();

            // Привязать входной PDF файл
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Инициализировать процесс конвертации
            converter.DoConvert();

            // Проверить, существуют ли страницы, и затем конвертировать их в изображение по одной
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Закрыть объект PdfConverter
            converter.Close();
        }
```
В следующем фрагменте кода мы покажем, как можно изменить некоторые параметры. С помощью [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) мы устанавливаем рамку 'CropBox'. Также мы можем изменить [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution), указывая количество точек на дюйм. Следующий параметр - [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - режим представления формы. Затем мы указываем [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage), с которой начинается номер страницы для конвертации. Мы также можем указать последнюю страницу, задав диапазон.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // Создаем объект PdfConverter
            PdfConverter converter = new PdfConverter();

            // Привязываем входной pdf файл
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Инициализируем процесс конвертации
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // Проверяем, существуют ли страницы, и затем конвертируем их в изображение по одной
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Закрываем объект PdfConverter
            converter.Close();
        }
```

## See also

Aspose.PDF for .NET позволяет конвертировать PDF-документы в различные форматы, а также конвертировать из других форматов в PDF. Также вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн с помощью приложения Aspose.PDF converter. Ознакомьтесь с разделом [Конвертация](/pdf/net/converting/) для решения ваших задач.