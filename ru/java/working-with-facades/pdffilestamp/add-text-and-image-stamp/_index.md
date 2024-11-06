---
title: Добавить текстовый и графический штамп
type: docs
weight: 20
url: ru/java/add-text-and-image-stamp/
description: В этом разделе объясняется, как добавить текстовый и графический штамп с использованием com.aspose.pdf.facades через класс PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Добавление текстового штампа на все страницы PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавлять текстовый штамп на все страницы PDF файла.
 Чтобы добавить текстовый штамп, сначала вам нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы также можете создать текстовую метку, используя метод BindLogo класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы можете установить другие атрибуты, такие как происхождение, вращение, фон и т.д., используя объект [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Затем вы можете добавить метку в PDF-файл, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной PDF-файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить текстовую метку на все страницы в PDF-файле.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать метку
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Добавить метку в PDF-файл
        fileStamp.addStamp(stamp);

        // Сохранить обновленный PDF-файл
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```

## Добавление текстового штампа на определенные страницы PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавлять текстовый штамп на определенные страницы PDF файла.
 Для того чтобы добавить текстовую печать, сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы также должны создать текстовый штамп, используя метод [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы можете установить другие атрибуты, такие как origin, rotation, background и т.д. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) объект также. Как вы хотите добавить текстовый штамп на конкретные страницы PDF файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Это свойство требует массив целых чисел, содержащий номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF файл, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной PDF файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить текстовый штамп на конкретные страницы в PDF файле.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать штамп
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Установить конкретные страницы
        stamp.setPages(new int[] { 2 });

        // Добавить штамп в PDF файл
        fileStamp.addStamp(stamp);

        // Сохранить обновленный PDF файл
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```

## Добавить штамп изображения на все страницы в PDF файле

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавить штамп изображения на все страницы PDF файла.
 Чтобы добавить штамп изображения, сначала необходимо создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вам также нужно создать штамп изображения, используя метод [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Вы можете установить другие атрибуты, такие как происхождение, поворот, фон и т.д., используя объект [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Затем вы можете добавить штамп в PDF файл, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните результат в PDF файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить штамп изображения на все страницы в PDF файле.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать штамп
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Добавить штамп в PDF файл
        fileStamp.addStamp(stamp);

        // Сохранить обновленный PDF файл
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```

### Контроль качества изображения при добавлении в виде штампа

При добавлении изображения в виде объекта штампа, вы также можете контролировать качество изображения. Для выполнения этого требования добавлено свойство Quality для класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Оно указывает качество изображения в процентах (допустимые значения от 0 до 100).

## Добавление штампа изображения на определенные страницы PDF файла

Класс [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) позволяет добавлять штамп изображения на определенные страницы PDF файла.
 Чтобы добавить штамп изображения, сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) и [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) метод класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.  
Вы можете установить другие атрибуты, такие как начало, вращение, фон и т.д. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) объект также. Как вы хотите добавить штамп изображения на определенные страницы PDF-файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) класса [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Это свойство требует целочисленный массив, содержащий номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF-файл, используя метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Наконец, сохраните выходной PDF-файл, используя метод [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) класса [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Следующий фрагмент кода показывает, как добавить штамп изображения на определенные страницы в PDF-файле.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Создать объект PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Открыть документ
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Создать штамп
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Установить определенные страницы
        stamp.setPages(new int[] { 2 });

        // Добавить штамп в PDF-файл
        fileStamp.addStamp(stamp);

        // Сохранить обновленный PDF-файл
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Закрыть fileStamp
        fileStamp.close();
    }
```