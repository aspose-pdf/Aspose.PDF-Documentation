---
title: Optimize, Compress or Reduce PDF Size in Java
linktitle: Optimize PDF Document
type: docs
weight: 40
url: ru/java/optimize-pdf/
description: Оптимизируйте PDF файл, уменьшите все изображения, уменьшите размер PDF, удалите встроенные шрифты, удалите неиспользуемые объекты с помощью Java.
lastmod: "2021-06-05"
---

PDF-документ иногда может содержать дополнительные данные. Уменьшение размера PDF-файла поможет вам оптимизировать передачу данных по сети и хранение. Это особенно удобно для публикации на веб-страницах, обмена в социальных сетях, отправки по электронной почте или архивирования в хранилище. Мы можем использовать несколько методов для оптимизации PDF:

- Оптимизация содержимого страниц для онлайн-просмотра
- Уменьшение или сжатие всех изображений
- Включение повторного использования содержимого страниц
- Объединение дублирующихся потоков
- Удаление встроенных шрифтов
- Удаление неиспользуемых объектов
- Удаление или упрощение полей формы
- Удаление или упрощение аннотаций

## Оптимизация PDF-документа для Интернета

Оптимизация или линеаризация относится к процессу подготовки PDF-файла для онлайн-просмотра с использованием веб-браузера.
 Aspose.PDF поддерживает этот процесс.

Чтобы оптимизировать PDF для отображения в интернете:

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Используйте метод [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Сохраните оптимизированный документ, используя метод save(..).

Следующий фрагмент кода показывает, как оптимизировать PDF-документ для интернета.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Оптимизация для интернета
        pdfDocument.optimize();

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Уменьшение размера PDF-файла

Эта тема объясняет шаги по оптимизации/уменьшению размера PDF-файла. Aspose.PDF API предоставляет класс [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions), который дает возможность оптимизировать выходной PDF, удаляя ненужные объекты и сжимая PDF-файлы с изображениями. Оба этих варианта подробно описаны в следующих разделах.

### Удаление ненужных объектов
Мы можем оптимизировать размер PDF-документов, удаляя дублирующиеся и неиспользуемые объекты. Следующий фрагмент кода показывает, как это сделать.

```java
public static void ReduceSizePDF() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Оптимизировать PDF-документ. Однако, обратите внимание, что этот метод не может гарантировать
        // сокращение документа
        pdfDocument.optimizeResources();

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Сжатие всех изображений

If the source PDF file contains images, consider compressing the images and setting their quality. In order to enable image compression, pass true as an argument to the setCompressImages(..) method. All the images in a document will be re-compressed. The compression is defined by the setImageQuality(..) method, which is the value of the quality in percent. 100% is unchanged quality and image size. To decrease image size, pass an argument of less than 100 to the setImageQuality(..) method.

Если исходный PDF-файл содержит изображения, рассмотрите возможность сжатия изображений и установки их качества. Чтобы включить сжатие изображений, передайте true в качестве аргумента методу setCompressImages(..). Все изображения в документе будут повторно сжаты. Сжатие определяется методом setImageQuality(..), который задает значение качества в процентах. 100% - это неизменное качество и размер изображения. Чтобы уменьшить размер изображения, передайте аргумент меньше 100 в метод setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Инициализировать OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Установить опцию CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Установить опцию ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Оптимизировать PDF-документ с использованием OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```

Другой способ - изменить размер изображений с более низким разрешением. В этом случае мы должны установить ResizeImages в true и MaxResolution в соответствующее значение.

```java
public static void ShrinkingCompressing2() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Инициализировать OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Установить опцию CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Установить опцию ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Установить опцию ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Установить опцию MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Оптимизировать PDF-документ с использованием OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Начало : " + clock.instant());

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Инициализировать OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Установить опцию CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Установить опцию ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Установить версию сжатия изображений на быструю
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Оптимизировать PDF документ используя OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
        System.out.println("Конец : " + clock1.instant());
    }
```

## Удаление неиспользуемых объектов

PDF-документ иногда содержит PDF-объекты, которые не ссылаются ни на один другой объект в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а скорее уменьшает его размер.

```java
    public static void RemovingUnusedObjects() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);

    }
```
## Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов.
 Эти потоки не являются "неиспользуемыми объектами", потому что они ссылаются из словаря ресурсов страницы. Это может произойти в случаях, когда изображение было удалено со страницы, но не из ресурсов страницы. Также такая ситуация часто возникает, когда страницы извлекаются из документа, а страницы документа имеют "общие" ресурсы, то есть один и тот же объект Resources. Содержимое страницы анализируется для определения, используется ли поток ресурсов или нет. Неиспользуемые потоки удаляются. Иногда это уменьшает размер документа.

```java
public static void RemovingUnusedStream() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
        
    }
```
## Связывание Дублирующихся Потоков

Иногда документ содержит несколько идентичных потоков ресурсов (например, изображения). Это может произойти, например, когда документ соединяется сам с собой. Выходной документ содержит две независимые копии одного и того же потока ресурсов. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остается только одна копия, ссылки изменяются соответствующим образом и копии объекта удаляются. Иногда это уменьшает размер документа.

```java
    public static void LinkingDuplicateStream() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Оптимизация PDF документа с использованием OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```

Кроме того, мы можем использовать настройку AllowReusePageContent. Если это свойство установлено в true, содержимое страницы будет повторно использоваться при оптимизации документа для идентичных страниц.

```java
public static void AllowReusePageContent() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Оптимизация PDF-документа с использованием OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```
## Удаление встроенных шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифта размещены в документе.
 Преимущество заключается в том, что документ можно просматривать независимо от того, установлен ли шрифт на компьютере пользователя или нет. Однако встраивание шрифтов увеличивает размер документа. Метод удаления встроенных шрифтов удаляет все встроенные шрифты. Это уменьшает размер документа, но документ может стать нечитаемым, если нужный шрифт не установлен.

```java
    public static void UnembedFonts() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Оптимизировать PDF документ, используя параметры оптимизации
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```

## Удаление или упрощение аннотаций

Аннотации можно удалить, если они не нужны. Когда они необходимы, но не требуют дополнительного редактирования, их можно "сгладить". Оба эти метода уменьшат размер файла.

```java
    public static void FlatteningAnnotations() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }

```
## Удаление полей формы

Если PDF-документ содержит AcroForms, мы можем попытаться уменьшить размер файла, сгладив поля формы.

```java
    public static void RemovingFormFields() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Сгладить формы
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }

```
## Преобразование PDF из цветового пространства RGB в градации серого

PDF-файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вы можете столкнуться с необходимостью преобразования PDF из цветового пространства RGB в градации серого, чтобы ускорить процесс печати этих PDF-файлов. Кроме того, при преобразовании файла в градации серого уменьшается размер документа, но при этом может снизиться качество документа. В настоящее время эта функция поддерживается функцией Pre-Flight в Adobe Acrobat, но когда речь идет об автоматизации офисных процессов, Aspose.PDF является идеальным решением, предоставляющим такие возможности для манипуляции с документами.

Для выполнения этого требования можно использовать следующий фрагмент кода.

```java
    public static void ConvertRGBtoGrayscale() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode Сжатие

Aspose.PDF для Java предоставляет поддержку сжатия FlateDecode для функциональности оптимизации PDF. Следующий фрагмент кода показывает, как использовать эту опцию в оптимизации для хранения изображений с сжатием FlateDecode:

```java
    public static void FlateDecodeCompression() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Оптимизировать PDF документ с использованием OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```
## Хранение изображения в XImageCollection 

Aspose.PDF для Java предоставляет возможность хранения новых изображений в [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) с использованием сжатия FlateDecode.
 Чтобы включить эту опцию, вы можете использовать флаг ImageFilterType.Flate. Следующий фрагмент кода показывает, как использовать эту функциональность:

```java
    public static void StoreImageInXImageCollection() {
        // Инициализация документа
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Загрузка изображения в поток
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Установка координат
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Использование оператора ConcatenateMatrix (объединение матриц): определяет, как изображение должно быть размещено
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```