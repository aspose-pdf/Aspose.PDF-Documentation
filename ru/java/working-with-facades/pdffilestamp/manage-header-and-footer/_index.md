---
title: Управление Заголовком и Нижним Колонтитулом
type: docs
weight: 40
url: ru/java/manage-header-and-footer/
description: В этом разделе объясняется, как управлять заголовком и нижним колонтитулом с использованием Aspose.PDF Facades и класса PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Добавление Заголовка в PDF Файл

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавить заголовок в PDF файл.
 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. 

Чтобы добавить заголовок, сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Вы можете форматировать текст заголовка с использованием класса [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Как только вы будете готовы добавить заголовок в файл, вам нужно вызвать метод [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Вам также необходимо указать как минимум верхнее поле в методе [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Наконец, сохраните выходной PDF файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить заголовок в PDF файл.

```java
 public static void AddHeader() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать форматированный текст для номера страницы
        FormattedText formattedText = new FormattedText("Aspose - Ваши эксперты по форматам файлов!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Добавить заголовок
        fileStamp.addHeader(formattedText, 20);

        // Сохранить обновленный PDF файл
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```

## Добавление нижнего колонтитула в PDF-файл

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавить нижний колонтитул в PDF-файл.
 Чтобы добавить нижний колонтитул, сначала необходимо создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Вы можете форматировать текст нижнего колонтитула с помощью класса [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Когда вы будете готовы добавить нижний колонтитул в файл, вам нужно вызвать метод [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Вам также необходимо указать как минимум нижнее поле в методе [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Наконец, сохраните результат в PDF-файл с помощью метода [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить нижний колонтитул в PDF-файл.

```java
 public static void AddFooter() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать форматированный текст для номера страницы
        FormattedText formattedText = new FormattedText("Aspose - Ваши эксперты по форматам файлов!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Добавить нижний колонтитул
        fileStamp.addFooter(formattedText, 10);

        // Сохранить обновленный PDF-файл
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```

## Add Image in Header of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) класс позволяет добавить изображение в заголовок PDF файла.
 In order to add image in header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. After that, you need to call [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can pass the image to the [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image in header of PDF file.

```java
public static void AddImageHeader() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Добавить заголовок
            fileStamp.addHeader(fs, 10);

            // Сохранить обновленный PDF файл
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Закрыть fileStamp
        fileStamp.close();
    }
```

## Добавить изображение в нижний колонтитул существующего PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавить изображение в нижний колонтитул PDF файла.
 Для того чтобы добавить изображение в нижний колонтитул, сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). После этого, необходимо вызвать метод [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Вы можете передать изображение в метод [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Наконец, сохраните выходной PDF файл с помощью метода [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF файла.

```java
    public static void AddImageFooter() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Добавить нижний колонтитул
            fileStamp.addFooter(fs, 10);

            // Сохранить обновленный PDF файл
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Закрыть fileStamp
        fileStamp.close();
    }
```