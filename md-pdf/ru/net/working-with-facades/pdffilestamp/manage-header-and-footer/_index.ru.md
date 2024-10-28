---
title: Управление Заголовком и Нижним Колонтитулом
type: docs
weight: 40
url: /net/manage-header-and-footer/
description: Этот раздел объясняет, как управлять заголовком и нижним колонтитулом с помощью Aspose.PDF Facades, используя класс PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Добавить Заголовок в PDF Файл

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) позволяет добавить заголовок в PDF файл. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Чтобы добавить заголовок, сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Вы можете форматировать текст заголовка, используя класс [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). После того как вы будете готовы добавить заголовок в файл, вам нужно вызвать метод [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). Также необходимо указать как минимум верхнее поле в методе [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). Следующий фрагмент кода показывает, как добавить заголовок в PDF файл.

```csharp
 public static void AddHeader()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Создать форматированный текст для номера страницы
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Добавить заголовок
            fileStamp.AddHeader(formattedText, 10);

            // Сохранить обновленный PDF файл
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```
## Добавление нижнего колонтитула в файл PDF

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) позволяет добавить нижний колонтитул в файл PDF. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Для того чтобы добавить нижний колонтитул, сначала необходимо создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Вы можете форматировать текст нижнего колонтитула, используя класс [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Когда вы будете готовы добавить нижний колонтитул в файл, вам нужно вызвать метод [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Вам также нужно указать как минимум нижнее поле в методе [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Следующий фрагмент кода показывает, как добавить нижний колонтитул в PDF файл.

```csharp
 public static void AddFooter()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Создать форматированный текст для номера страницы
            FormattedText formattedText = new FormattedText("Aspose - Ваши эксперты по файловым форматам!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Добавить нижний колонтитул
            fileStamp.AddFooter(formattedText, 10);

            // Сохранить обновленный PDF файл
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```
## Добавить изображение в заголовок существующего PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) позволяет добавить изображение в заголовок PDF файла. Для того чтобы добавить изображение в заголовок, сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). После этого необходимо вызвать метод [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Вы можете передать изображение в метод [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF файла.

```csharp
public static void AddImageHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add Header
                fileStamp.AddHeader(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Close fileStamp
                fileStamp.Close();
            }
        }
```
## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) класс позволяет добавить изображение в нижний колонтитул PDF-файла. В целях добавления изображения в нижний колонтитул, вам сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). После этого, вам нужно вызвать метод [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Вы можете передать изображение в метод [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF файла.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```