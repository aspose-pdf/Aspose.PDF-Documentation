---
title: Получение и Установка Свойств Страницы
type: docs
weight: 30
url: ru/java/get-and-set-page-properties/
description: Эта тема объясняет, как получить номера в PDF-файле, получить свойства страницы и определить цвет страницы с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
---

Aspose.PDF для Java позволяет вам читать и устанавливать свойства страниц в PDF-файле в ваших Java-приложениях. Этот раздел показывает, как получить количество страниц в PDF-файле, получить информацию о свойствах страницы PDF, таких как цвет, и установить свойства страницы.

## Получение Количества Страниц в PDF Файле

При работе с документами вам часто нужно знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF-файле:

1. Откройте PDF-файл с использованием класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Затем используйте свойство Count коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (из объекта Document), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц в PDF-файле.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Получить количество страниц
        System.out.println("Количество страниц : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Получение количества страниц без сохранения документа

Пока PDF-файл не сохранен и все элементы фактически не размещены внутри PDF-файла, мы не можем получить количество страниц для конкретного документа (поскольку мы не можем быть уверены в количестве страниц, на которых все элементы будут размещены).
 Однако начиная с выпуска Aspose.PDF for Java 10.1.0, мы ввели метод с именем [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--), который предоставляет возможность получить количество страниц в PDF-документе без сохранения файла. Таким образом, мы можем получить информацию о количестве страниц на лету. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // Для полных примеров и файлов данных, пожалуйста, перейдите на
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // создание экземпляра Document
        Document doc = new Document();
        // добавление страницы в коллекцию страниц PDF-файла
        Page page = doc.getPages().add();
        // создание цикла для добавления 300 экземпляров TextFragment
        for (int i = 0; i < 300; i++)
            // добавление TextFragment в коллекцию параграфов первой страницы PDF
            page.getParagraphs().add(new TextFragment("Pages count test"));
        // обработка параграфов для получения информации о количестве страниц
        doc.processParagraphs();
        System.out.println("Количество страниц в PDF = " + doc.getPages().size());
    }
```

## Получение Свойств Страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, поля обрезки, обрезка и обрезка по меткам. Aspose.PDF позволяет получить доступ к этим свойствам.

### **Понимание Свойств Страницы: Различия между Artbox, BleedBox, CropBox, MediaBox, TrimBox и свойством Rect**

- **Медиабокс**: Медиабокс — это самая большая рамка страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, медиабокс определяет физический размер носителя, на котором отображается или печатается PDF-документ.
- **Рамка обрезки**: Если документ имеет обрезку, то PDF также будет иметь рамку обрезки.
 Bleed — это количество цвета (или иллюстрации), которое выходит за край страницы. Оно используется для того, чтобы при печати и обрезке документа до нужного размера ("обрезка") краска доходила до самого края страницы. Даже если страница обрезается с отклонением от меток обрезки, на странице не появятся белые края.
- **Trim box**: Trim box указывает на конечный размер документа после печати и обрезки.
- **Art box**: Art box — это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка страницы используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box — это размер "страницы", при котором ваш PDF-документ отображается в Adobe Acrobat. В обычном режиме отображается только содержимое crop box в Adobe Acrobat.
  Для подробного описания этих свойств прочитайте спецификацию Adobe.Pdf, особенно раздел 10.10.1 Page Boundaries.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Картинка ниже иллюстрирует эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Доступ к свойствам страницы

Класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) предоставляет все свойства, связанные с определенной страницей PDF. Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Оттуда возможно получить доступ как к отдельным объектам страницы, используя их индекс, так и перебрать коллекцию с помощью цикла foreach, чтобы получить все страницы. После того как доступ к отдельной странице получен, мы можем получить её свойства. В следующем фрагменте кода показано, как получить свойства страницы.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Получить коллекцию страниц
        PageCollection pageCollection = pdfDocument.getPages();

        // Получить конкретную страницу
        Page pdfPage = pageCollection.get_Item(1);

        // Получить свойства страницы
        System.out.printf("\n ArtBox : Высота = " + pdfPage.getArtBox().getHeight() + ", Ширина = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Высота = " + pdfPage.getBleedBox().getHeight() + ", Ширина = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Высота = " + pdfPage.getCropBox().getHeight() + ", Ширина = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Высота = " + pdfPage.getMediaBox().getHeight() + ", Ширина = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Высота = " + pdfPage.getTrimBox().getHeight() + ", Ширина = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Высота = " + pdfPage.getRect().getHeight() + ", Ширина = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Номер страницы :- " + pdfPage.getNumber());
        System.out.printf("\n Поворот :-" + pdfPage.getRotate());
    }
```

## Определение Цвета Страницы

Класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) предоставляет свойства, связанные с конкретной страницей в PDF-документе, включая информацию о том, какой тип цвета - RGB, черно-белый, градации серого или неопределенный - используется на странице.

Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Свойство [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) указывает цвет элементов на странице. Чтобы получить или определить цветовую информацию для конкретной страницы PDF, используйте свойство [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) объекта класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Следующий фрагмент кода показывает, как перебрать отдельные страницы PDF-файла, чтобы получить информацию о цвете.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Перебрать все страницы PDF-файла
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Получить информацию о типе цвета для конкретной страницы PDF
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Страница # -" + pageCount + " черно-белая..");
                break;
            case 1:
                System.out.println("Страница # -" + pageCount + " в градациях серого...");
                break;
            case 0:
                System.out.println("Страница # -" + pageCount + " в RGB..");
                break;
            case 3:
                System.out.println("Цвет страницы # -" + pageCount + " не определен..");
                break;
            }
        }
    }
}
```