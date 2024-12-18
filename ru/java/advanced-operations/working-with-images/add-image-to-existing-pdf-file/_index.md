---
title: Добавить изображение в существующий PDF файл
linktitle: Добавить изображение
type: docs
weight: 10
url: /ru/java/add-image-to-existing-pdf-file/
description: Этот раздел описывает, как добавить изображение в существующий PDF файл с использованием Java библиотеки.
lastmod: "2021-06-05"
---

Каждая страница PDF содержит свойства Resources и Contents. Ресурсы могут быть изображениями и формами, например, в то время как содержимое представлено набором PDF операторов. Каждый оператор имеет свое имя и аргумент. В этом примере используются операторы для добавления изображения в PDF файл.

Чтобы добавить изображение в существующий PDF файл:

- Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и откройте входной PDF документ.
- Получите страницу, на которую вы хотите добавить изображение.
- Добавьте изображение в коллекцию [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) страницы.
- Используйте операторы для размещения изображения на странице:
- Используйте оператор GSave, чтобы сохранить текущее графическое состояние.

- Используйте оператор [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix), чтобы указать, где должно быть размещено изображение.
- Используйте оператор [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do), чтобы нарисовать изображение на странице.
- Наконец, используйте оператор [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore), чтобы сохранить обновленное графическое состояние.
- Сохраните файл.

Следующий фрагмент кода показывает, как добавить изображение в PDF-документ.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Открыть документ
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Установить координаты
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Получить страницу, на которую нужно добавить изображение
        Page page = pdfDocument1.getPages().get_Item(1);

        // Загрузить изображение в поток
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Добавить изображение в коллекцию изображений ресурсов страницы
        page.getResources().getImages().add(imageStream);

        // Используя оператор GSave: этот оператор сохраняет текущее графическое состояние
        page.getContents().add(new GSave());

        // Создать объекты Rectangle и Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Используя оператор ConcatenateMatrix (конкатенация матрицы): определяет, как
        // изображение должно быть размещено
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Используя оператор Do: этот оператор рисует изображение
        page.getContents().add(new Do(ximage.getName()));

        // Используя оператор GRestore: этот оператор восстанавливает графическое состояние
        page.getContents().add(new GRestore());

        // Сохранить новый PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Закрыть поток изображения
        imageStream.close();
    }
```


## Добавление изображения из BufferedImage в PDF

Начиная с выпуска Aspose.PDF for Java 9.5.0, мы внедрили поддержку добавления изображения из экземпляра BufferedImage в PDF документ. Для поддержки этого требования реализован метод: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
Вы можете использовать любой InputStream, а не только объект FileInputStream для добавления изображения. Так что, используя объект java.io.ByteArrayInputStream, вам не нужно сохранять какие-либо файлы в системе:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## Добавление изображения в существующий PDF файл (Фасады)

Существует также альтернативный, более простой способ добавить изображение в PDF файл. Вы можете использовать метод AddImage класса [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). Метод AddImage требует указания изображения для добавления, номера страницы, на которой нужно добавить изображение, и информации о координатах. После этого сохраните обновленный PDF файл, используя метод Close.

Следующий фрагмент кода показывает, как добавить изображение в существующий PDF файл.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Открыть документ
        PdfFileMend mender = new PdfFileMend();

        // Создать объект PdfFileMend для добавления текста
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Добавить изображение в PDF файл
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Сохранить изменения
        mender.save(_dataDir + "AddImage_out.pdf");

        // Закрыть объект PdfFileMend
        mender.close();
    }
```


## Добавление ссылки на одно изображение несколько раз в PDF документе

Иногда возникает необходимость использовать одно и то же изображение несколько раз в PDF документе. Добавление нового экземпляра увеличивает размер итогового PDF документа. Мы добавили новый метод XImageCollection.add(XImage), который поддерживает объект Ximage для добавления в коллекцию изображений. Этот метод позволяет добавить ссылку на тот же PDF объект, что и оригинальное изображение, оптимизируя размер PDF документа.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## Определение, является ли изображение внутри PDF цветным или черно-белым

К изображениям могут применяться различные типы сжатия для уменьшения их размера. Тип сжатия, применяемый к изображению, зависит от его цветового пространства, т.е. если изображение цветное (RGB), то применяется сжатие JPEG2000, а если оно черно-белое, то следует применять сжатие JBIG2/JBIG2000. Поэтому определение типа каждого изображения и использование соответствующего типа сжатия создаст наилучший/оптимизированный результат.

PDF файл может содержать текст, изображение, график, вложение, аннотацию и т.д., и если исходный PDF файл содержит изображения, мы можем определить цветовое пространство изображения и применить соответствующее сжатие для уменьшения размера PDF файла. Следующий фрагмент кода показывает шаги для определения, является ли изображение внутри PDF цветным или черно-белым.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // перебор всех страниц PDF файла
            for (Page page : (Iterable<Page>) document.getPages()) {
                // создание экземпляра поглотителя размещения изображений
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* Тип цвета */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Черно-белое изображение");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Цветное изображение");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Ошибка при чтении файла = " + document.getFileName());
        }
    }
}
```