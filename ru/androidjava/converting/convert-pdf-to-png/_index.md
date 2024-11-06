---
title: Convert PDF to PNG 
linktitle: Convert PDF to PNG 
type: docs
weight: 20
url: ru/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: Эта страница описывает, как конвертировать страницы PDF в изображения PNG, конвертировать все и отдельные страницы в изображения PNG с помощью Aspose.PDF для Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Используйте библиотеку **Aspose.PDF for Android via Java** для преобразования страниц PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr> доступным и удобным способом.

Класс PngDevice позволяет конвертировать страницы PDF в изображения PNG. Этот класс предоставляет метод под названием Process, который позволяет конвертировать определенную страницу PDF-файла в формат изображения PNG.

## Конвертация страниц PDF в изображения PNG

Чтобы конвертировать все страницы PDF-файла в файлы PNG, пройдитесь по отдельным страницам и конвертируйте каждую в формат PNG. Следующий фрагмент кода показывает, как пройти по всем страницам PDF-файла и конвертировать каждую в изображение PNG.

{{% alert color="primary" %}}

Пробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Конвертируйте одну страницу PDF в изображение PNG

Передайте индекс страницы в качестве аргумента методу Process(..).
Следующий фрагмент кода показывает шаги для конвертации первой страницы PDF в формат PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Создайте объект потока для сохранения выходного изображения
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Создайте объект Resolution
            Resolution resolution = new Resolution(300);

            // Создайте объект PngDevice с определенным разрешением
            PngDevice PngDevice = new PngDevice(resolution);

            // Конвертируйте конкретную страницу и сохраните изображение в поток
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Закройте поток
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Преобразование всех страниц PDF в изображение PNG

Aspose.PDF для Android через Java показывает, как преобразовать все страницы в PDF-файле в изображения:

1. Переберите все страницы в файле.
1. Преобразуйте каждую страницу по отдельности:
    1. Создайте объект класса Document для загрузки PDF-документа.
    1. Получите страницу, которую хотите преобразовать.
    1. Вызовите метод Process, чтобы преобразовать страницу в Png.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в изображения PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Переберите все страницы PDF-файла
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Создайте объект потока для сохранения выходного изображения
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Создайте объект разрешения
            Resolution resolution = new Resolution(300);
            // Создайте объект JpegDevice с определенным разрешением
            PngDevice JpegDevice = new PngDevice(resolution);

            // Преобразуйте конкретную страницу и сохраните изображение в потоке
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Закройте поток
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


## Преобразование определенной страницы PDF в изображение PNG

Aspose.PDF для Android через Java показывает, как преобразовать определенную страницу в формат PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Получить прямоугольник определенной области страницы
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // установить значение CropBox в соответствии с прямоугольником желаемой области страницы
        document.getPages().get_Item(1).setCropBox(pageRect);
        // сохранить обрезанный документ в поток
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // открыть обрезанный PDF документ из потока и преобразовать в изображение
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Создать объект разрешения
        Resolution resolution = new Resolution(300);
        // Создать устройство Jpeg с указанными атрибутами
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Преобразовать определенную страницу и сохранить изображение в поток
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```