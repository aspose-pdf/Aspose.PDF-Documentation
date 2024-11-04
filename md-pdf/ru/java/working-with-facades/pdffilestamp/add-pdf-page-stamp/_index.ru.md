---
title: Добавить штамп страницы PDF
type: docs
weight: 10
url: /java/add-pdf-page-stamp/
description: Этот раздел объясняет, как работать с Aspose.PDF Facades, используя класс PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Добавить штамп страницы PDF на все страницы в PDF файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавлять штамп страницы PDF на все страницы PDF файла.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Для того чтобы добавить штамп на страницу PDF, сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вам также нужно создать штамп страницы PDF, используя метод [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т.д., используя объект [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Затем вы можете добавить штамп в файл PDF, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной файл PDF, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить штамп страницы PDF на все страницы в PDF-файле.

```csharp
public static void AddPageStampOnAllPages()
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

            // Добавить штамп в файл PDF
            fileStamp.AddStamp(stamp);

            // Сохранить обновленный файл PDF
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Закрыть fileStamp
            fileStamp.Close();
        }
```

## Добавление штампа на определенные страницы в PDF-файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавить штамп на определенные страницы PDF-файла.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. 

Чтобы добавить штамп на страницу PDF, сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы также должны создать штамп страницы PDF, используя метод [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.  
Вы можете установить другие атрибуты, такие как происхождение, поворот, фон и т.д. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) объект также. Как вы хотите добавить штамп на определенные страницы PDF файла, вам также необходимо установить свойство [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Это свойство требует массив целых чисел, содержащий номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF файл, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной PDF файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить штамп на определенные страницы в PDF файле.

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

        // Добавить номера страниц в PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Добавить номер страницы в PDF файл (facades)

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавлять номера страниц в PDF файл.
 В целях добавления номеров страниц, вам сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Если вы хотите показать номер страницы как «Страница X из N», где X — это текущий номер страницы, а N — общее количество страниц в PDF-файле, вам сначала нужно получить количество страниц, используя свойство getNumberOfpages класса [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Чтобы получить текущий номер страницы, вы можете использовать знак **#** в вашем тексте в любом месте. Вы можете форматировать текст с номером страницы, используя класс [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Если вы хотите начать нумерацию страниц с определенного номера, вы можете установить свойство setStartingNumber. Когда вы будете готовы добавить номер страницы в файл, вам нужно вызвать метод addPageNumber класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной PDF-файл, используя метод Save класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

Следующий фрагмент кода показывает, как добавить номер страницы в PDF-файл.
```java
 public static void AddPageNumberInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Получить общее количество страниц
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Создать форматированный текст для номера страницы
        FormattedText formattedText = new FormattedText("Страница # из " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Установить начальный номер для первой страницы; возможно, вы захотите начать с 2 или более
        fileStamp.setStartingNumber(1);

        // Добавить номер страницы
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Сохранить обновленный PDF файл
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```


### Пользовательский стиль нумерации

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) класс предлагает возможность добавлять информацию о номере страницы как объект штампа в PDF-документ. До этого выпуска класс поддерживал только 1,2,3,4 как стиль нумерации страниц. Однако некоторые клиенты потребовали использовать пользовательский стиль нумерации при размещении штампа с номером страницы в PDF-документе. Для выполнения этого требования было введено свойство [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle), которое принимает значения из перечисления [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle). Ниже указаны значения, предлагаемые в этом перечислении.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Получить общее количество страниц
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Создать отформатированный текст для номера страницы
        FormattedText formattedText = new FormattedText("Страница # из " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Указать стиль нумерации как римские цифры в верхнем регистре
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Установить начальный номер для первой страницы; возможно, вы захотите начать с 2 или более
        fileStamp.setStartingNumber(1);

        // Добавить номер страницы
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Сохранить обновленный PDF-файл
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```