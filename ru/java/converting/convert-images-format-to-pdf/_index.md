---
title: Конвертировать различные форматы изображений в PDF
linktitle: Конвертировать изображения в PDF
type: docs
weight: 60
url: ru/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как библиотека Aspose.PDF для Java позволяет конвертировать различные форматы изображений в PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF для Java** позволяет конвертировать различные форматы изображений в файлы PDF. Наша библиотека демонстрирует фрагменты кода для конвертации самых популярных форматов изображений, таких как - BMP, CGM, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Конвертация BMP в PDF

Конвертируйте файлы BMP в документ PDF, используя библиотеку **Aspose.PDF для Java**.

Изображения <abbr title="Bitmap Image File">BMP</abbr> - это файлы с расширением .BMP, представляющие файлы растровых изображений, которые используются для хранения цифровых растровых изображений. Эти изображения не зависят от графического адаптера и также называются форматом растровых изображений, не зависящим от устройства (DIB).
Вы можете конвертировать BMP в PDF с помощью API Aspose.PDF для Java.
 Следовательно, вы можете выполнить следующие шаги для преобразования изображений BMP:

1. Инициализируйте новый документ
1. Загрузите образец файла изображения BMP
1. Наконец, сохраните выходной файл PDF

Следующий фрагмент кода следует этим шагам и показывает, как преобразовать BMP в PDF с использованием Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Инициализируйте объект документа
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Загрузите образец файла изображения BMP
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Сохраните выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать BMP в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация BMP в PDF с помощью бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Конвертировать CGM в PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> — это стандарт ISO, который предоставляет векторный 2D-формат файла для хранения и извлечения графической информации. CGM — это формат, не зависящий от устройства. CGM — это формат векторной графики, который поддерживает три разных метода кодирования: двоичный (лучший для скорости чтения программой), основанный на символах (создает наименьший размер файла и позволяет быстрее передавать данные) или кодирование в открытом тексте (позволяет пользователям читать и изменять файл с помощью текстового редактора)

Следующий фрагмент кода показывает, как конвертировать файлы CGM в формат PDF с использованием Aspose.PDF для Java.

1. Создайте класс [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. Создайте экземпляр класса [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) с указанием имени исходного файла и параметров.
1. Сохраните документ с нужным именем файла.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Создайте CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // Инициализируйте объект документа
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Сохраните выходной документ PDF
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## Конвертация DICOM в PDF

<abbr title="Цифровая обработка и связь в медицине">DICOM</abbr> — это стандарт для обработки, хранения, печати и передачи информации в медицинской визуализации. Он включает в себя определение формата файла и протокол сетевой связи.

Aspose.PDF для Java позволяет преобразовать файлы DICOM в формат PDF, посмотрите следующий пример кода:

1. Загрузите изображение в поток
1. Инициализируйте [объект Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Загрузите образец DICOM файла изображения
1. Сохраните выходной PDF документ

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Загрузите изображение в поток
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Инициализируйте объект документа
        Document document = new Document();
        document.getPages().add();
        
        // Загрузите образец DICOM файла изображения
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Сохраните выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Попробуйте конвертировать DICOM в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["DICOM в PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация DICOM в PDF с использованием бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертация EMF в PDF

Формат расширенного метафайла (<abbr title="Enhanced metafile format">EMF</abbr>) хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут воспроизвести сохраненное изображение после разбора на любом выходном устройстве.

У нас есть несколько подходов для конвертации EMF в PDF.

## Использование класса Image

Документ PDF состоит из страниц, и каждая страница содержит один или несколько объектов параграфа. Параграф может быть текстом, изображением, таблицей, плавающей рамкой, графиком, заголовком, полем формы или вложением.

Чтобы конвертировать файл изображения в формат PDF, заключите его в параграф.

Возможно преобразование изображений, находящихся на физическом носителе на локальном жестком диске, найденных по веб-URL или в экземпляре потока.

Чтобы добавить изображение:

1. Создайте объект класса com.aspose.pdf.Image.
1. Добавьте изображение в коллекцию [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) экземпляра страницы.
1. Укажите путь или источник изображения.
    - Если изображение находится на жестком диске, укажите путь с помощью метода [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Если изображение находится в FileInputStream, передайте объект, содержащий изображение, в метод [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Следующий фрагмент кода демонстрирует, как загрузить объект изображения, установить поля страницы, разместить изображение на странице и сохранить результат в формате PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Преобразование EMF в PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Создание объекта документа
        Document doc = new Document();
        // Добавление страницы в коллекцию страниц документа
        Page page = doc.getPages().add();
        // Загрузка исходного файла изображения в объект Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Установка полей, чтобы изображение поместилось и т.д.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Создание объекта изображения
        Image image1 = new Image();
        // Добавление изображения в коллекцию параграфов раздела
        page.getParagraphs().add(image1);
        // Установка потока файла изображения
        image1.setImageStream(fs);
        // Сохранение результирующего PDF-файла
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // смотрите код ниже
    } 
}
```


### Добавить изображение из BufferedImage

Aspose.PDF для Java также предлагает возможность загрузки изображения из экземпляра Stream, где изображение может быть загружено в объект BufferedImage и помещено в коллекцию абзацев Pdf файла.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // добавить страницу в коллекцию страниц Pdf файла
    Page page = doc.getPages().add();
    // создать экземпляр изображения
    Image image1 = new Image();
    // создать экземпляр BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // записать буферизованное изображение в экземпляр OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // добавить изображение в коллекцию абзацев первой страницы
    page.getParagraphs().add(image1);
    // установить поток изображения как OutputStream, содержащий буферизованное изображение
    image1.setImageStream(bais);
    // сохранить полученный PDF файл
    doc.save("BufferedImage.pdf");
}
```


## Добавление изображения с использованием операторов PDF

Каждый объект страницы PDF содержит методы [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) и [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). Ресурсы могут быть изображениями и формами, например, в то время как контент представлен набором операторов PDF. Каждый оператор имеет свое собственное имя и аргумент.

В этом примере используются операторы для добавления изображения в PDF файл.

Чтобы добавить изображение в существующий PDF файл:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и откройте входной PDF документ.
2. Получите страницу, на которую хотите добавить изображение.
3. Добавьте изображение в коллекцию [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) страницы.
4. Используйте операторы, чтобы разместить изображение на странице:
   1. Используйте оператор GSave, чтобы сохранить текущее графическое состояние.
   2. Используйте оператор ConcatenateMatrix, чтобы указать, где должно быть размещено изображение.

1. Используйте оператор Do, чтобы нарисовать изображение на странице.
   1. В завершение, используйте оператор GRestore, чтобы сохранить обновленное графическое состояние.
1. Сохраните файл.

Следующий фрагмент кода показывает, как добавить изображение в PDF-документ.

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Откройте документ
Document pdfDocument1 = new Document("input.pdf");

// Установите координаты
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Получите страницу, на которую вы хотите добавить изображение
Page page = pdfDocument1.getPages().get_Item(1);

// Загрузите изображение в поток
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Добавьте изображение в коллекцию изображений ресурсов страницы
page.getResources().getImages().add(imageStream);

// Использование оператора GSave: этот оператор сохраняет текущее графическое состояние
page.getContents().add(new Operator.GSave());

// Создайте объекты Rectangle и Matrix
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть расположено изображение
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Использование оператора Do: этот оператор рисует изображение
page.getContents().add(new Operator.Do(ximage.getName()));

// Использование оператора GRestore: этот оператор восстанавливает графическое состояние
page.getContents().add(new Operator.GRestore());

// Сохраните новый PDF
pdfDocument1.save("Updated_document.pdf");

// Закройте поток изображения
imageStream.close();
```


{{% alert color="success" %}}
**Попробуйте преобразовать EMF в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация EMF в PDF с использованием бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Преобразование JPG в PDF

Не нужно ломать голову над тем, как преобразовать JPG в PDF, потому что библиотека Apose.PDF для Java имеет лучшее решение.

Вы можете очень легко преобразовать JPG изображения в PDF с помощью Aspose.PDF для Java, следуя этим шагам:

1. Инициализируйте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Загрузите изображение JPG и добавьте его в абзац
1. Сохраните выходной PDF

Пример кода ниже показывает, как преобразовать изображение JPG в PDF с использованием Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Инициализировать объект документа
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Загрузить образец файла изображения JPEG
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // Сохранить выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Попробуйте конвертировать JPG в PDF онлайн**

Aspose представляет вам бесплатное онлайн приложение ["JPG в PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация JPG в PDF с использованием бесплатного приложения](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Конвертация PNG в PDF

**Aspose.PDF для Java** поддерживает функцию конвертации изображений PNG в формат PDF. Ознакомьтесь с следующим примером кода для реализации вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файла изображения, который использует без потерь сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в изображение PDF, используя следующие шаги:

1. Загрузите входное изображение PNG
1. Считайте значения высоты и ширины
1. Создайте новый документ и добавьте страницу
1. Установите размеры страницы
1. Сохраните выходной файл

Кроме того, приведенный ниже пример кода показывает, как конвертировать PNG в PDF в ваших Java приложениях:

```java
package com.aspose.pdf.examples;

/**
 * Конвертация PNG в PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Инициализация объекта документа
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Загрузите образец BMP файла изображения
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // Сохраните выходной PDF документ
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PNG в PDF с использованием бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертация SVG в PDF

Scalable Vector Graphics (SVG) - это семейство спецификаций файлового формата на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

SVG-изображения и их поведение определяются в текстовых XML-файлах.
 Это означает, что они могут быть найдены, индексированы, скриптованы и, при необходимости, сжаты. Как файлы XML, изображения SVG могут быть созданы и отредактированы с помощью любого текстового редактора, но чаще всего удобнее создавать их с помощью графических программ, таких как Inkscape.

## Как конвертировать файл SVG в формат PDF

Чтобы преобразовать файлы SVG в PDF, используйте класс с именем [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Позже этот объект передается в качестве аргумента во время инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает движку рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода показывает процесс преобразования файла SVG в формат PDF.

```java
// Инициализация объекта документа

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["SVG в PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация SVG в PDF с бесплатным приложением](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Конвертация TIFF в PDF

**Aspose.PDF для Java** поддерживает формат файла, будь то однорамочное или многорамочное изображение <abbr title="Tag Image File Format">TIFF</abbr>. Это означает, что вы можете конвертировать изображение TIFF в PDF в ваших Java приложениях.

TIFF или TIF, Tagged Image File Format, представляет собой растровые изображения, предназначенные для использования на различных устройствах, которые соответствуют этому стандарту формата файла.
 TIFF изображение может содержать несколько кадров с разными изображениями. Формат файла Aspose.PDF также поддерживается, будь то однофреймовое или многофреймовое TIFF изображение. Таким образом, вы можете конвертировать TIFF изображение в PDF в ваших Java приложениях. Поэтому мы рассмотрим пример конвертации многостраничного TIFF изображения в многостраничный PDF документ с помощью следующих шагов:

1. Создайте экземпляр класса Document
1. Загрузите входное TIFF изображение
1. Наконец, сохраните изображение как PDF страницу

Кроме того, следующий фрагмент кода показывает, как конвертировать многостраничное или многофреймовое TIFF изображение в PDF:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Преобразование TIFF в PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // Инициализация объекта документа
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Сохранение выходного PDF документа
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```