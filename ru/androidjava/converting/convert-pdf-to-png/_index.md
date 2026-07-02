---
title: Конвертировать PDF в PNG
linktitle: Конвертировать PDF в PNG
type: docs
weight: 20
url: /ru/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: На этой странице описывается, как конвертировать страницы PDF в изображение PNG, конвертировать все и отдельные страницы в изображения PNG с помощью Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Используйте библиотеку **Aspose.PDF for Android via Java** для преобразования страниц PDF в <abbr title="Portable Network Graphics">PNG</abbr> Изображения доступным и удобным способом.

Класс PngDevice позволяет конвертировать страницы PDF в изображения PNG. Этот класс предоставляет метод под названием Process, который позволяет преобразовать конкретную страницу PDF‑файла в формат изображения PNG.

## Конвертировать страницы PDF в изображения PNG

Чтобы конвертировать все страницы PDF‑файла в PNG‑файлы, пройдитесь по отдельным страницам и преобразуйте каждую в формат PNG. Ниже показан фрагмент кода, демонстрирующий, как пройтись по всем страницам PDF‑файла и преобразовать каждую в изображение PNG.

{{% alert color="primary" %}} 

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Конвертировать одну страницу PDF в изображение PNG

Передайте индекс страницы в качестве аргумента методу Process(..).
Следующий фрагмент кода показывает шаги по конвертированию первой страницы PDF в формат PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Конвертировать все страницы PDF в PNG‑изображение

Aspose.PDF for Android via Java показывает, как преобразовать все страницы PDF‑файла в изображения:

1. Пройдите по всем страницам в файле.
1. Конвертировать каждую страницу отдельно:
    1. Создайте объект класса Document, чтобы загрузить PDF‑документ.
    1. Получите страницу, которую хотите преобразовать.
    1. Вызовите метод Process, чтобы преобразовать страницу в Png.

В следующем фрагменте кода показано, как преобразовать все страницы PDF в изображения PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Преобразовать отдельную страницу PDF в изображение PNG

Aspose.PDF for Android via Java показывает, как преобразовать отдельную страницу в формат PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
