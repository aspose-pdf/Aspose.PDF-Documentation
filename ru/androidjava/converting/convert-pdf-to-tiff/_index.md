---
title: Convert PDF to TIFF 
linktitle: Convert PDF to TIFF  
type: docs
weight: 30
url: /ru/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: Эта статья описывает, как преобразовать страницы в PDF-документе в изображение TIFF. Вы узнаете, как конвертировать все или отдельные страницы в изображения TIFF с помощью Aspose.PDF для Android через Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для Android через Java** позволяет конвертировать страницы PDF в изображения TIFF.

[Класс TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) позволяет конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем Process, который позволяет конвертировать все страницы в PDF-файле в одно изображение TIFF.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конверсии Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Преобразование страниц PDF в одно изображение TIFF

Aspose.PDF для Android с использованием Java объясняет, как преобразовать все страницы в PDF-файле в одно изображение TIFF:

1. Создайте объект класса Document.
1. Вызовите метод Process для преобразования документа.
1. Чтобы задать свойства выходного файла, используйте класс TiffSettings.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать объект Resolution
        Resolution resolution = new Resolution(300);

        // Создать объект TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Создать устройство TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Преобразовать конкретную страницу и сохранить изображение в поток
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Преобразование отдельной страницы в изображение TIFF

Aspose.PDF для Android через Java позволяет преобразовать конкретную страницу в PDF-файле в изображение TIFF, используя перегруженную версию метода Process(..), который принимает номер страницы в качестве аргумента для преобразования. Следующий фрагмент кода показывает, как преобразовать первую страницу PDF в формат TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Создать объект Resolution
        Resolution resolution = new Resolution(300);

        // Создать объект TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Создать устройство TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Преобразовать конкретную страницу и сохранить изображение в поток
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## Используйте алгоритм Брэдли при преобразовании

Aspose.PDF для Android через Java поддерживает возможность преобразования PDF в TIFF с использованием сжатия LZW, и затем с применением AForge можно применить бинаризацию. Однако один из клиентов запросил, чтобы для некоторых изображений они могли получить пороговое значение с использованием метода Оцу, поэтому они также хотели бы использовать алгоритм Брэдли.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Не реализовано в Aspose.PDF для Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Не реализовано в Aspose.PDF для Android
        throw new NotImplementedException();
    }
```