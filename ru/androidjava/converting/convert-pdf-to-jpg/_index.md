---  
title: Convert PDF to JPG  
linktitle: Convert PDF to JPG  
type: docs  
weight: 10  
url: ru/androidjava/convert-pdf-to-jpg/  
description:  Эта страница описывает, как преобразовать страницы PDF в изображения JPEG, как преобразовать все и отдельные страницы в изображения JPEG с помощью Aspose.PDF для Android через Java.  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

## Преобразование страниц PDF в изображения JPG  

Класс JpegDevice позволяет преобразовывать страницы PDF в изображения JPEG. Этот класс предоставляет метод с именем process(..), который позволяет преобразовать конкретную страницу PDF-файла в изображение JPEG.  

{{% alert color="primary" %}}  

Попробуйте онлайн. Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)  

{{% /alert %}}  

## Преобразование одной страницы PDF в изображение JPG  

Aspose.PDF для Android через Java позволяет преобразовать одну страницу в формат Jpeg.  

Чтобы преобразовать только одну страницу в изображение JPEG:  

1. Создайте объект класса Document, чтобы получить страницу, которую хотите преобразовать.
1. Вызовите метод process(..), чтобы преобразовать страницу в изображение JPEG.

Следующий фрагмент кода показывает шаги по преобразованию первой страницы PDF в формат Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Создайте объект потока для сохранения выходного изображения
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Создайте объект Resolution
            Resolution resolution = new Resolution(300);

            // Создайте объект JpegDevice с определённым разрешением
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Преобразуйте конкретную страницу и сохраните изображение в поток
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Закройте поток
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Конвертировать все страницы PDF в изображения JPG

Aspose.PDF для Android через Java позволяет конвертировать все страницы в PDF-файле в изображения:

1. Переберите все страницы в файле.
1. Конвертируйте каждую страницу отдельно:
    - Создайте объект класса Document для загрузки PDF-документа.
    - Получите страницу, которую хотите конвертировать.
    - Вызовите метод Process, чтобы конвертировать страницу в Jpeg.

Следующий фрагмент кода показывает, как конвертировать все страницы PDF в изображения Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Переберите все страницы PDF-файла
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Создайте объект потока для сохранения выходного изображения
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Создайте объект Resolution
            Resolution resolution = new Resolution(300);
            // Создайте объект JpegDevice с определенным разрешением
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Конвертируйте определенную страницу и сохраните изображение в поток
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


## Преобразование конкретной страницы PDF в изображение JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Получить прямоугольник конкретной области страницы
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // установить значение CropBox в соответствии с прямоугольником желаемой области страницы
        document.getPages().get_Item(1).setCropBox(pageRect);
        // сохранить обрезанный документ в поток
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // открыть обрезанный PDF документ из потока и преобразовать в изображение
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Создать объект Resolution
        Resolution resolution = new Resolution(300);
        // Создать Jpeg устройство с указанными атрибутами
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Преобразовать конкретную страницу и сохранить изображение в поток
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```