---
title: Преобразовать PDF в BMP
linktitle: Преобразовать PDF в BMP
type: docs
weight: 40
url: /ru/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: В этой статье описывается, как преобразовать страницы PDF в изображение BMP, как преобразовать все страницы в изображения BMP и как преобразовать отдельную страницу PDF в изображение BMP с помощью Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Этот [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) класс позволяет конвертировать страницы PDF в <abbr title="Bitmap Image File">BMP</abbr> изображения. Этот класс предоставляет метод с именем [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) который позволяет преобразовать конкретную страницу PDF‑файла в формат изображения Bmp.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

Класс BmpDevice позволяет конвертировать страницы PDF в BMP‑изображения. Этот класс предоставляет метод с именем process(..), который позволяет конвертировать определённую страницу PDF‑файла в BMP‑изображение.

## Конвертировать страницу PDF в BMP‑изображение

Чтобы конвертировать страницу PDF в BMP‑изображение:

1. Создайте объект класса Document, чтобы получить нужную страницу для конвертации.
1. Вызовите метод process(..), чтобы конвертировать страницу в BMP.

В следующем фрагменте кода показано, как преобразовать конкретную страницу в изображение BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Конвертировать все страницы PDF в BMP-изображения

Чтобы конвертировать все страницы PDF‑файла в формат BMP, необходимо пройтись по ним, получить каждую отдельную страницу и преобразовать её в BMP‑формат. Ниже приведён фрагмент кода, показывающий, как пройтись по всем страницам PDF‑файла и преобразовать их в BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## Преобразовать определённый регион страницы в изображение (DOM)

Мы можем конвертировать PDF‑документы в различные форматы Image, используя объекты image devices из Aspose.PDF. Однако иногда возникает требование конвертировать определённый регион страницы в формат Image. Мы можем выполнить это требование в два шага. Сначала обрезаем страницу PDF до нужного региона, а затем конвертируем её в изображение, используя нужный объект Image device.

Следующий фрагмент кода показывает, как конвертировать страницы PDF в изображения.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
