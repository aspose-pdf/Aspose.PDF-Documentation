---
title: Конвертировать PDF в TIFF
linktitle: Конвертировать PDF в TIFF
type: docs
weight: 30
url: /ru/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: В этой статье описывается, как преобразовать страницы PDF‑документа в изображение TIFF. Вы узнаете, как преобразовать все страницы или отдельные страницы в изображения TIFF с помощью Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** делает возможным преобразование страниц PDF в изображения TIFF.

Этот [Класс TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) позволяет конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем Process, который позволяет конвертировать все страницы PDF‑файла в одно изображение TIFF.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Конвертировать страницы PDF в одно изображение TIFF

Aspose.PDF for Android via Java объясняет, как конвертировать все страницы PDF‑файла в одно изображение TIFF:

1. Создайте объект класса Document.
1. Вызовите метод Process для преобразования документа.
1. Чтобы установить свойства выходного файла, используйте класс TiffSettings.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Конвертировать одну страницу в TIFF‑изображение

Aspose.PDF for Android via Java позволяет конвертировать отдельную страницу PDF‑файла в изображение TIFF, используйте перегруженную версию метода Process(..), который принимает номер страницы в качестве аргумента для конвертации. Ниже приведён фрагмент кода, показывающий, как конвертировать первую страницу PDF в формат TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Используйте алгоритм Брэди при конвертации

Aspose.PDF for Android via Java поддерживает функцию конвертации PDF в TIFF с использованием сжатия LZW, а затем с помощью AForge можно применить бинаризацию. Однако один из клиентов запросил, чтобы для некоторых изображений получать пороговое значение с использованием метода Оцу, поэтому они также хотели бы использовать Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

