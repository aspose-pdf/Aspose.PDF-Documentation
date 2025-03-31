---
title: Конвертировать PDF в BMP 
linktitle: Конвертировать PDF в BMP
type: docs
weight: 40
url: /ru/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: В этой статье описывается, как конвертировать страницы PDF в изображение BMP, конвертировать все страницы в изображения BMP и конвертировать одну страницу PDF в изображение BMP с помощью Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Класс [BmpDevice](https://reference.aspose.com/pdf/ru/net/aspose.pdf.devices/bmpdevice) позволяет конвертировать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>. Этот класс предоставляет метод под названием [Process](https://reference.aspose.com/pdf/ru/net/aspose.pdf.devices/bmpdevice/methods/process), который позволяет конвертировать конкретную страницу PDF файла в формат изображения Bmp.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

Класс BmpDevice позволяет конвертировать страницы PDF в изображения BMP.
 Этот класс предоставляет метод с именем process(..), который позволяет преобразовать определенную страницу PDF файла в изображение BMP.

## Преобразование страницы PDF в изображение BMP

Чтобы преобразовать страницу PDF в изображение BMP:

1. Создайте объект класса Document, чтобы получить нужную страницу, которую вы хотите преобразовать.
1. Вызовите метод process(..), чтобы преобразовать страницу в BMP.

Следующий пример кода показывает, как преобразовать определенную страницу в изображение BMP.

```java
//Преобразование PDF в BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Создайте объект потока для сохранения выходного изображения
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Создайте объект Resolution
            Resolution resolution = new Resolution(300);

            // Создайте объект BmpDevice с определенным разрешением
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Преобразуйте определенную страницу и сохраните изображение в поток
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Закройте поток
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Преобразование всех страниц PDF в изображения BMP

Чтобы преобразовать все страницы PDF файла в формат BMP, необходимо перебрать каждую отдельную страницу и преобразовать её в формат BMP. В следующем фрагменте кода показано, как перебрать все страницы PDF файла и преобразовать их в BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Перебор всех страниц PDF файла
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Создать объект потока для сохранения выходного изображения
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Создать объект разрешения
            Resolution resolution = new Resolution(300);
            // Создать объект BmpDevice с определённым разрешением
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Преобразовать конкретную страницу и сохранить изображение в поток
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Закрыть поток
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


## Преобразование конкретной области страницы в изображение (DOM)

Мы можем преобразовать PDF-документы в различные форматы изображений, используя объекты устройств изображения Aspose.PDF. Однако иногда возникает необходимость преобразовать конкретную область страницы в формат изображения. Мы можем выполнить это требование в два этапа. Сначала обрезать страницу PDF до нужной области, а затем преобразовать ее в изображение, используя нужный объект устройства изображения.

Следующий фрагмент кода показывает, как преобразовать страницы PDF в изображения.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Получить прямоугольник конкретной области страницы
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // установить значение CropBox в соответствии с прямоугольником нужной области страницы
        document.getPages().get_Item(1).setCropBox(pageRect);
        // сохранить обрезанный документ в поток
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // открыть обрезанный PDF-документ из потока и преобразовать в изображение
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Создать объект Resolution
        Resolution resolution = new Resolution(300);
        // Создать BMP-устройство с указанными атрибутами
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Преобразовать конкретную страницу и сохранить изображение в поток
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```