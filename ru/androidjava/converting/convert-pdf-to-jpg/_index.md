---
title: Конвертировать PDF в JPG
linktitle: Конвертировать PDF в JPG
type: docs
weight: 10
url: /ru/androidjava/convert-pdf-to-jpg/
description:  На этой странице описывается, как конвертировать страницы PDF в изображения JPEG, конвертировать все и отдельные страницы в изображения JPEG с помощью Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Конвертировать страницы PDF в изображения JPG

Класс JpegDevice позволяет конвертировать страницы PDF в изображения JPEG. Этот класс предоставляет метод с именем process(..), который позволяет конвертировать определённую страницу PDF‑файла в изображение JPEG.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Преобразовать отдельную страницу PDF в изображение JPG

Aspose.PDF for Android via Java позволяет вам преобразовать отдельную страницу в формат Jpeg.

Чтобы преобразовать только одну страницу в изображение JPEG:

1. Создайте объект класса Document, чтобы получить страницу, которую вы хотите конвертировать.
1. Вызовите метод process(..), чтобы преобразовать страницу в изображение JPEG.

Следующий фрагмент кода показывает шаги для преобразования первой страницы PDF в формат JPEG.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Конвертировать все страницы PDF в изображение JPG

Aspose.PDF for Android via Java позволяет конвертировать все страницы PDF‑файла в изображения:

1. Пройдите по всем страницам в файле.
1. Конвертировать каждую страницу отдельно:
    - Создайте объект класса Document для загрузки PDF‑документа.
    - Получите страницу, которую хотите конвертировать.
    - Вызовите метод Process, чтобы преобразовать страницу в JPEG.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в изображения Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
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
            JpegDevice JpegDevice = new JpegDevice(resolution);

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

## Преобразовать определённую страницу PDF в изображение JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
