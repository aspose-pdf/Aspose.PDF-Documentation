---
title: Добавление изображений и текста
type: docs
weight: 10
url: ru/net/adding-images-and-text-using-pdffilemend-class/
description: Этот раздел объясняет, как добавлять изображения и текст с помощью класса PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

Класс [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) может помочь вам добавить изображения и текст в существующий PDF-документ в указанном месте. It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index).

Он предоставляет два метода с именами [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) и [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). Метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) позволяет добавлять изображения типа JPG, GIF, PNG и BMP. Метод [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) принимает аргумент типа класса [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) и добавляет его в существующий PDF файл. Изображения и текст могут быть добавлены в прямоугольную область, заданную координатами нижней левой и верхней правой точек. При добавлении изображений вы можете указать либо путь к файлу изображения, либо поток файла изображения. Для того чтобы указать номер страницы, на которую нужно добавить изображение или текст, оба этих метода предоставляют аргумент номера страницы. Таким образом, вы можете не только добавить изображения и текст в указанное место, но и на указанную страницу.

Изображения являются важной частью содержимого PDF документа. 
Манипулирование изображениями в существующем PDF-файле является распространенной задачей для людей, работающих с PDF-файлами. В этой статье мы рассмотрим, как изображения могут быть изменены в существующем PDF-файле с помощью [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) из [Aspose.PDF for .NET](/pdf/net/). Все операции, связанные с изображениями в [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades), были собраны в этой статье.

## Подробности реализации

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) позволяет добавлять новые изображения в существующий PDF-файл.
``` Вы также можете заменить или удалить существующее изображение. Файл PDF также может быть преобразован в изображения. Вы можете либо конвертировать каждую отдельную страницу в одно изображение, либо весь файл PDF в одно изображение. Это позволяет вам форматы, т.е. JPEG, BMP, PNG и TIFF и т.д. Вы также можете извлечь изображения из файла PDF. Вы можете использовать четыре класса [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) для выполнения этих операций, а именно [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Операции с изображениями

В этом разделе мы подробно рассмотрим эти операции с изображениями. Мы также увидим фрагменты кода, демонстрирующие использование связанных классов и методов. Прежде всего, давайте посмотрим на добавление изображения в существующий PDF-файл. Мы можем использовать метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) класса [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) для добавления нового изображения. С помощью этого метода вы можете не только указать номер страницы, на которой вы хотите добавить изображение, но и указать местоположение изображения.

## Добавление изображения в существующий PDF-файл (Facades)

Вы можете использовать метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) класса [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). Метод [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) требует, чтобы изображение было добавлено, указывается номер страницы, на которой нужно добавить изображение, и информация о координатах. После этого сохраните обновленный PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

В следующем примере мы добавляем изображение на страницу, используя imageStream:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Загрузить изображение в поток
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // сохранить выходной файл
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image1.png)

С помощью [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), мы можем наложить одно изображение поверх другого:
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Загрузить изображение в поток
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // сохранить выходной файл
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Добавить изображение](/pdf/net/images/add_image2.png)

Существует несколько способов сохранения изображения в PDF-файл. Мы продемонстрируем один из них в следующем примере:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Загрузить изображение в поток
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // сохранить выходной файл
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Добавление текста в существующий PDF файл (фасады)

Мы можем добавлять текст несколькими способами. Рассмотрим первый. Мы берем [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) и добавляем его на страницу. Затем указываем координаты нижнего левого угла, а после добавляем наш текст на страницу.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Проверьте, как это выглядит:

![Add Text](/pdf/net/images/add_text.png)

Второй способ добавить [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Дополнительно мы указываем прямоугольник, в который должен вписаться наш текст.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
Третий пример предоставляет возможность добавлять текст на указанные страницы. В нашем примере давайте добавим подпись на страницы 1 и 3 документа.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```