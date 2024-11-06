---
title: Convert PDF File
type: docs
weight: 20
url: ru/java/convert-pdf-file/
description: Этот раздел объясняет, как конвертировать PDF файл с использованием Aspose.PDF Facades и класса PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Конвертация страниц PDF в различные форматы изображений (Facades)

Чтобы конвертировать страницы PDF в различные форматы изображений, необходимо создать объект [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) и открыть PDF файл с помощью метода [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

После этого необходимо вызвать метод [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) для выполнения задач инициализации.
 Затем вы можете перебирать все страницы с использованием методов [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) и [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-). Метод getNextImage позволяет вам создать изображение конкретной страницы. Вы также должны передать ImageType этому методу, чтобы создать изображение определенного типа, например, JPEG, GIF или PNG и т.д.

Наконец, вызовите метод close класса [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

Следующий фрагмент кода показывает, как преобразовать страницы PDF в изображения.

```java
public static void ConvertPdfPagesToImages01() {
        // Создать объект PdfConverter
        PdfConverter converter = new PdfConverter();

        // Привязать входной pdf файл
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Инициализировать процесс преобразования
        converter.doConvert();
        
        int count=0;

        // Проверить, существуют ли страницы, и затем преобразовать в изображение по одной
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Закрыть объект PdfConverter
        converter.close();
    }
```

В следующем фрагменте кода мы покажем, как можно изменить некоторые параметры. С помощью [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) мы устанавливаем рамку [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). Также мы можем изменить [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) указав количество точек на дюйм. Следующий [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - режим представления формы. Затем мы указываем [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-), с какого номера страницы начинается преобразование. Мы также можем указать последнюю страницу, задав диапазон.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Создаем объект PdfConverter
        PdfConverter converter = new PdfConverter();

        // Привязываем входной pdf файл
        converter.bindPdf(_dataDir + "sample.pdf");

        // Инициализируем процесс конвертации
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Проверяем, существуют ли страницы, и затем поочередно конвертируем в изображение
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Закрываем объект PdfConverter
        converter.close();
    }
```