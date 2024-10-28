---
title: Добавление заголовка и нижнего колонтитула в PDF 
linktitle: Добавить заголовок и нижний колонтитул
type: docs
weight: 70
url: /java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF для Java позволяет добавлять заголовки и нижние колонтитулы в ваш PDF файл с помощью класса TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Штампы PDF часто используются в контрактах, отчетах и ограниченных материалах, чтобы подтвердить, что документы были проверены и помечены как "прочитано", "квалифицировано" или "конфиденциально" и т.д. В этой статье будет показано, как мы можем добавить штампы изображений и текстовые штампы в PDF документы, используя **Aspose.PDF для Java**.

Если вы будете читать приведенные выше фрагменты кода построчно, вы должны обнаружить, что синтаксис и логика кода довольно просты для понимания.

## Добавление текста в заголовок PDF файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) для добавления текста в заголовок PDF файла.
 TextStamp класс предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить текст в заголовок, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить текст в заголовок PDF.

Вам нужно установить свойство TopMargin таким образом, чтобы оно корректировало текст в области заголовка вашего PDF. Также необходимо установить HorizontalAlignment в Center и VerticalAlignment в Top.

Следующий фрагмент кода показывает, как добавить текст в заголовок PDF файла с помощью Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // Путь к директории с документами.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Создать заголовок
        TextStamp textStamp = new TextStamp("Header Text");

        // Установить свойства штампа
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Добавить заголовок на все страницы
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Сохранить обновленный документ
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Добавление текста в нижний колонтитул PDF файла

Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул PDF файла. Класс TextStamp предоставляет свойства, необходимые для создания текстового штампа, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить текст в нижний колонтитул, вам нужно создать объект Document и объект TextStamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы для добавления текста в нижний колонтитул PDF.

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF файла с помощью Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Создать нижний колонтитул
        TextStamp textStamp = new TextStamp("Footer Text");
        // Установить свойства штампа
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Добавить нижний колонтитул на все страницы
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Сохранить обновленный PDF файл
        pdfDocument.save(_dataDir);
    }
```


## Добавление изображения в заголовок PDF-файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) для добавления изображения в заголовок PDF-файла. Класс ImageStamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект ImageStamp с использованием необходимых свойств. После этого вы можете вызвать метод [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) страницы, чтобы добавить изображение в заголовок PDF-файла.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Открыть документ
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Создать заголовок
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Установить свойства штампа
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Добавить заголовок на все страницы
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Сохранить обновленный PDF-файл
pdfDocument.save(_dataDir);
}
```


Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF файла с помощью Java.

## Добавление изображения в нижний колонтитул PDF файла

Вы можете использовать класс Image Stamp для добавления изображения в нижний колонтитул PDF файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить изображение в нижний колонтитул, вам нужно создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в нижний колонтитул PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство BottomMargin таким образом, чтобы оно настраивало изображение в области нижнего колонтитула вашего PDF. Также необходимо установить [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) на `Center` и [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) на `Bottom`.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF файла с помощью Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Создать нижний колонтитул
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Установить свойства штампа
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Добавить нижний колонтитул на все страницы
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Сохранить обновленный PDF файл
        pdfDocument.save(_dataDir);
    }
```

## Добавление различных заголовков в один PDF файл

Мы знаем, что можем добавить TextStamp в раздел Заголовка/Нижнего колонтитула документа, используя свойства TopMargin или Bottom Margin, но иногда может возникнуть необходимость добавить несколько заголовков/нижних колонтитулов в один PDF документ.
 **Aspose.PDF для Java** объясняет, как это сделать.

Для выполнения этого требования мы создадим отдельные объекты [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) (количество объектов зависит от количества необходимых заголовков/нижних колонтитулов) и добавим их в PDF-документ. Мы также можем указать различную информацию о форматировании для каждого отдельного объекта штампа. В следующем примере мы создали объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и три объекта [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp), а затем использовали метод [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) страницы для добавления текста в раздел заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с помощью Aspose.PDF для Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // Открыть исходный документ
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Создать три штампа
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // Установить выравнивание штампа (разместить штамп в верхней части страницы, по центру по горизонтали)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Указать стиль шрифта как жирный
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Установить цвет текста переднего плана как красный
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Указать размер шрифта как 14
        stamp1.getTextState().setFontSize(14);

        // Теперь нам нужно установить вертикальное выравнивание второго объекта штампа как верхнее
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Установить горизонтальное выравнивание штампа как центрированное
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Установить коэффициент масштабирования для объекта штампа
        stamp2.setZoom (10);

        // Установить форматирование третьего объекта штампа
        // Указать информацию о вертикальном выравнивании для объекта штампа как ВЕРХ
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Установить горизонтальное выравнивание для объекта штампа как центрированное
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // Установить угол поворота для объекта штампа
        stamp3.setRotateAngle(35);
        // Установить розовый как цвет фона для штампа
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // Изменить информацию о шрифте для штампа на Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // Первый штамп добавляется на первую страницу;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // Второй штамп добавляется на вторую страницу;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // Третий штамп добавляется на третью страницу.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Сохранить обновленный PDF файл
        pdfDocument.save(_dataDir);
    }

}
```