---  
title: Добавление текстового и изображенного штампа  
type: docs  
weight: 20  
url: ru/net/add-text-and-image-stamp/  
description: Этот раздел объясняет, как добавить текстовый и изображенный штамп с помощью Aspose.PDF Facades, используя класс PdfFileStamp.  
lastmod: "2021-06-05"  
draft: false  
---  

## Добавление текстового штампа на все страницы PDF файла  

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) класс позволяет добавить текстовый штамп на все страницы PDF файла. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Чтобы добавить текстовый штамп, сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вам также необходимо создать штамп текста, используя метод [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т.д., используя объект [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить текстовый штамп на всех страницах PDF-файла.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Создать штамп
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Добавить штамп в PDF-файл
            fileStamp.AddStamp(stamp);

            // Сохранить обновленный PDF-файл
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```
## Добавить текстовый штамп на определенные страницы в PDF-файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавить текстовый штамп на определенные страницы PDF-файла. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Для добавления текстового штампа сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вы также должны создать текстовую печать, используя метод [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Вы можете установить другие атрибуты, такие как начальная точка, вращение, фон и т.д. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) объект также. Как вы хотите добавить текстовый штамп на определенные страницы PDF-файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Это свойство требует массив целых чисел, содержащий номера страниц, на которых вы хотите добавить штамп. Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить текстовый штамп на определенные страницы в PDF-файле.
## Добавить штамп изображения на все страницы PDF-файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавить штамп изображения на все страницы PDF-файла. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Чтобы добавить изображение штампа, сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).  Вам также необходимо создать штамп изображения, используя метод [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т. д., используя также объект [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить штамп изображения на все страницы в PDF-файле.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Создать штамп
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Установить конкретные страницы
            stamp.Pages = new int[] { 2 };

            // Добавить штамп в PDF-файл
            fileStamp.AddStamp(stamp);

            // Сохранить обновленный PDF-файл
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```
### Контроль качества изображения при добавлении в виде штампа

При добавлении изображения в виде объекта штампа, вы также можете контролировать качество изображения. Для выполнения этого требования добавлено свойство Quality для класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Оно указывает качество изображения в процентах (допустимые значения 0..100).

## Добавление штампа изображения на конкретные страницы PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавить штамп изображения на конкретные страницы PDF файла. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Чтобы добавить штамп изображения, сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вы также должны создать штамп изображения, используя метод [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.

Вы можете установить другие атрибуты, такие как origin, rotation, background и т. д. используя объект [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) также. Поскольку вы хотите добавить изображение штампа на определенные страницы PDF файла, вам также необходимо установить свойство [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Это свойство требует массив целых чисел, содержащий номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF файл, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить изображение штампа на определенные страницы в PDF файле.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```