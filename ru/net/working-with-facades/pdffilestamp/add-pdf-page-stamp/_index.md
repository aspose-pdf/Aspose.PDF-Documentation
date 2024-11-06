---
title: Добавить штамп на страницу PDF
type: docs
weight: 10
url: ru/net/add-pdf-page-stamp/
description: Этот раздел объясняет, как работать с Aspose.PDF Facades, используя класс PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Добавить штамп на страницу PDF на всех страницах в PDF файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавить штамп на страницу PDF на всех страницах PDF файла. Чтобы добавить штамп на страницу PDF, сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вам также нужно создать штамп страницы PDF, используя метод [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т.д., используя объект [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Затем вы можете добавить штамп в файл PDF, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной файл PDF, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить штамп страницы PDF на всех страницах в PDF-файле.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Добавление штампа страницы PDF на определенные страницы в PDF-файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавлять штамп страницы PDF на определенные страницы PDF-файла. В целях добавления штампа на страницу PDF, сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the PDF page stamp using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.

Вам также необходимо создать штамп страницы PDF, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т.д. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) объект также. Как вы хотите добавить штамп страницы PDF на определенные страницы PDF файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Это свойство требует целочисленного массива, содержащего номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF файл, используя метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить штамп страницы PDF на определенные страницы в PDF файле.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Создать штамп
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Добавить штамп в PDF файл
            fileStamp.AddStamp(stamp);

            // Сохранить обновленный PDF файл
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }

        // Добавить номера страниц PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```
## Добавить номер страницы в PDF файл

Класс [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) позволяет добавлять номера страниц в PDF файл. 
Для того чтобы добавить номера страниц, вам сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp).
``` If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

Если вы хотите показать номер страницы как «Страница X из N», где X — это текущий номер страницы, а N — общее количество страниц в PDF-файле, то сначала вам нужно получить количество страниц, используя свойство [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) класса [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Для получения текущего номера страницы вы можете использовать знак **#** в любом месте вашего текста. Вы можете форматировать текст номера страницы, используя класс [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Если вы хотите начать нумерацию страниц с определенного номера, вы можете установить свойство [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). После того как вы будете готовы добавить номер страницы в файл, вам нужно вызвать метод [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). Наконец, сохраните выходной PDF файл, используя метод [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). Следующий фрагмент кода показывает, как добавить номер страницы в PDF файл.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Получить общее количество страниц
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Создать отформатированный текст для номера страницы
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Установить начальный номер для первой страницы; вы можете начать с 2 или более
            fileStamp.StartingNumber = 1;

            // Добавить номер страницы
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Сохранить обновленный PDF файл
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```
### Пользовательский стиль нумерации

Класс PdfFileStamp предлагает возможность добавлять информацию о номере страницы как объект штампа в PDF-документ. До этого выпуска класс поддерживал только 1,2,3,4 как стиль нумерации страниц. Однако некоторые клиенты запросили использование пользовательского стиля нумерации при размещении штампа номера страницы внутри PDF-документа. Для выполнения этого требования было введено свойство [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle), которое принимает значения из перечисления [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Ниже указаны значения, предлагаемые в этом перечислении.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // Создать объект PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Открыть документ
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Получить общее количество страниц
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Создать отформатированный текст для номера страницы
            FormattedText formattedText = new FormattedText($"Страница # из {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Указать стиль нумерации как римские цифры в верхнем регистре
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // Установить начальный номер для первой страницы; можно начать с 2 или более
            fileStamp.StartingNumber = 1;

            // Добавить номер страницы
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Сохранить обновленный PDF файл
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```