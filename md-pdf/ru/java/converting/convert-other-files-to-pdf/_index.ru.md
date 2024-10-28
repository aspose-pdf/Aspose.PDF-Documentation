---
title: Конвертировать различные форматы файлов в PDF
linktitle: Конвертировать другие форматы файлов в PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать другие форматы файлов в PDF документ.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Конвертация EPUB в PDF

**Aspose.PDF для Java** позволяет просто конвертировать файлы EPUB в формат PDF.

<abbr title="electronic publication">EPUB</abbr> (сокращение от электронная публикация) — это бесплатный и открытый стандарт для электронных книг от Международного форума цифровых публикаций (IDPF). Файлы имеют расширение .epub. EPUB разработан для переформатируемого контента, что означает, что ридер EPUB может оптимизировать текст для конкретного устройства отображения.

Для того чтобы конвертировать файлы EPUB в формат PDF, Aspose.PDF для Java имеет класс под названием [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions), который используется для загрузки исходного файла EPUB.
 После этого объект передается в качестве аргумента для инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), так как это помогает движку рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода показывает процесс преобразования файла EPUB в формат PDF.

1. Создайте [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) для EPUB.
2. Инициализируйте объект [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. Сохраните выходной PDF документ.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Создайте LoadOptions для EPUB
        EpubLoadOptions options = new EpubLoadOptions();

        // Инициализируйте объект document
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Сохраните выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн приложение ["EPUB в PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация EPUB в PDF с бесплатным приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Конвертируйте Markdown в PDF

**Эта функция поддерживается версией 19.6 или выше.**

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн приложение ["Markdown в PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация Markdown в PDF с бесплатным приложением](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown — это инструмент для конвертации текста в HTML для веб-авторов.
 Markdown позволяет вам писать в формате простого текста, который легко читать и писать, а затем преобразовывать его в структурно корректный XHTML (или HTML).

Следующий фрагмент кода показывает, как использовать эту функциональность с Aspose.PDF для Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Инициализировать объект опций загрузки Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // Создать объект Document
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Сохранить выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Convert PCL to PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) — это язык принтера Hewlett-Packard, разработанный для доступа к стандартным функциям принтера. Уровни PCL с 1 по 5e/5c — это языки, основанные на командах, которые используют управляющие последовательности, обрабатываемые и интерпретируемые в порядке их получения. На уровне потребителя потоки данных PCL генерируются драйвером принтера. Вывод PCL также может быть легко сгенерирован пользовательскими приложениями.

{{% alert color="success" %}}
**Попробуйте преобразовать PCL в PDF онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PCL в PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Преобразование PCL в PDF с бесплатным приложением](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**В настоящее время поддерживаются только PCL5 и более старые версии.**

|**Наборы команд**|**Поддержка**|**Исключения**|**Описание**|

| :- | :- | :- | :- |
|Команды управления заданиями|+|Режим двусторонней печати|Управление процессом печати: количество копий, выходной лоток, односторонняя/двусторонняя печать, отступы слева и сверху и т. д.|
|Команды управления страницей|+|Команда пропуска перфорации|Указание размера страницы, полей, ориентации страницы, расстояний между строками и символами и т. д.|
|Команды позиционирования курсора|+| |Указание позиции курсора и, следовательно, начала текста, растровых или векторных изображений и деталей.|

|Команды выбора шрифта|+|<p>1. Команда прозрачной печати данных.</p><p>2. Встроенные мягкие шрифты. В текущей версии вместо создания мягкого шрифта наша библиотека выбирает подходящий шрифт из существующих "жестких" TrueType шрифтов, установленных на целевой машине. <br>   Пригодность определяется отношением ширины к высоте. <br>   Эта функция работает только для Bitmap и TrueType шрифтов и не гарантирует, что текст, напечатанный с мягким шрифтом, будет соответствовать тексту в исходном файле. <br>   Поскольку коды символов в мягком шрифте могут не совпадать с кодами по умолчанию.</p><p>3. Пользовательские наборы символов.</p>|Позволяет загружать мягкие (встроенные) шрифты из PCL файла и управлять ими в памяти.|
|Команды растровой графики|+|Только черно-белые|Позволяет загружать растровые изображения из PCL файла в память, задавать параметры растра <br>такие как ширина, высота, тип сжатия, разрешение и т.д.|
|Команды цвета|+| |Позволяет окрашивать все печатные объекты.|
|Команды модели печати|+| |Позволяет заполнять текст, растровые изображения и прямоугольные области растровыми предопределенными и пользовательскими узорами, задавать режим прозрачности для узоров и исходного растрового изображения.
 <br>Предопределенные узоры — это штриховка, перекрестная штриховка и тонирование.|
|Команды заполнения прямоугольной области|+| |Позволяют создавать и заполнять прямоугольные области узорами.|
|HP-GL/2 команды векторной графики|+|Команды экранированного вектора (SV), режима прозрачности (TR), прозрачных данных (TD), RO (поворот системы координат), команды масштабируемых или растровых шрифтов (SB), наклона символов (SL) и дополнительного пространства (ES) не реализованы, а команды DV (определение переменной текстовой траектории) реализованы в бета-версии.|<p>- Позволяют загружать HP-GL/2 векторные изображения из PCL-файла в память. Vector image has an origin at the lower-left corner of the printable area, can be scaled, translated, rotated and clipped.</p><p>- Векторное изображение имеет начало координат в нижнем левом углу печатной области, может быть масштабировано, перемещено, повернуто и обрезано.</p><p>- Векторное изображение может содержать текст, в виде меток, и геометрические фигуры, такие как прямоугольник, круг, эллипс, линия, дуга, кривая Безье и сложные фигуры, составленные из простых.</p><p>- Замкнутые фигуры, включая буквы меток, могут быть заполнены сплошной заливкой или векторным узором.</p><p>- Узор может быть штриховкой, перекрестной штриховкой, затенением, растровым пользовательским, PCL штриховкой или перекрестной штриховкой и PCL пользовательским. Узор PCL является растровым. Метки могут быть индивидуально повернуты, масштабированы и направлены в четырех направлениях: вверх, вниз, влево и вправо. Направления влево и вправо предполагают расположение букв одна за другой. Направления вверх и вниз предполагают расположение букв одна под другой.</p>|
|Macross|―| |Позволяет загружать последовательность команд PCL в память и использовать эту последовательность много раз, например, для печати заголовка страницы или установки одного форматирования для набора страниц.|
|Unicode text|―| |Позволяет печатать не-ASCII символы. Не реализовано из-за отсутствия файлов с <br>Unicode текстом|
|PCL6 (PCL-XL)| |Реализовано только в бета-версии из-за отсутствия тестовых файлов. Встроенные шрифты также не поддерживаются. Расширение JetReady не поддерживается, так как невозможно иметь спецификацию JetReady.|Бинарный формат файла.|

### Преобразование PCL файла в формат PDF

Для преобразования из PCL в PDF, [Aspose.PDF for Java](https://products.aspose.com/pdf/java) имеет класс [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Этот объект затем передается в качестве аргумента при инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает движку рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода показывает процесс преобразования файла PCL в формат PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Известные проблемы

1. Происхождение текстовых строк и изображений может незначительно отличаться от таковых в исходном PCL файле, если направление печати не 0º. То же самое относится к векторным изображениям, если система координат векторного графика повернута (предшествует команда RO).
2. Происхождение меток в векторных изображениях может отличаться от таковых в исходном PCL файле, если на метки влияет последовательность команд: Происхождение метки (LO), Определение пути переменного текста (DV), Абсолютное направление (DI) или Относительное направление (DR).
3. Текст может быть неправильно прочитан, если он должен быть отображен с помощью Bitmap или TrueType мягкого (встроенного) шрифта, потому что в настоящее время эти шрифты поддерживаются только частично (см. исключения в таблице "Поддерживаемые функции"). В этой ситуации текст может быть правильно прочитан только в том случае, если коды символов в мягком шрифте соответствуют стандартным. Стиль прочитанного текста также может отличаться от такового в исходном PCL файле, потому что не обязательно задавать стиль в заголовке мягкого шрифта.

1. Если разобранный PCL файл содержит шрифты Intellifont или Universal soft, будет выброшено исключение, потому что шрифты Intellifont и Universal не поддерживаются.  
1. Если разобранный PCL файл содержит макрокоманды, результат разбора будет существенно отличаться от исходного файла, потому что макрокоманды не поддерживаются.

## Конвертация текста в PDF

**Aspose.PDF для Java** предоставляет возможность конвертировать текстовые файлы в формат PDF. В этой статье мы демонстрируем, как легко и эффективно мы можем конвертировать текстовый файл в PDF, используя Aspose.PDF.

Когда вам нужно конвертировать текстовый файл в PDF, сначала прочитайте исходный текстовый файл в некотором ридере. Мы использовали StringBuilder для чтения содержимого текстового файла. Создайте объект Document и добавьте новую страницу в коллекцию Pages. Создайте новый объект TextFragment и передайте объект StringBuilder в его конструктор. Добавьте новый абзац в коллекцию Paragraphs, используя объект TextFragment, и сохраните полученный PDF-файл, используя метод Save класса Document.
**Попробуйте преобразовать ТЕКСТ в PDF онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование ТЕКСТА в PDF с бесплатным приложением](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Преобразование текстового файла в PDF

```java
package com.aspose.pdf.examples;
/**
 * Преобразование TXT в PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Инициализация объекта документа

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Создание экземпляра объекта Document, вызвав его пустой конструктор
        Document pdfDocument = new Document();

        // Добавление новой страницы в коллекцию Pages документа
        Page page = pdfDocument.getPages().add();

        // Создание экземпляра TextFragment и передача текста из объекта reader в его
        // конструктор в качестве аргумента
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Добавление нового текстового абзаца в коллекцию paragraphs и передача объекта
        // TextFragment
        page.getParagraphs().add(text);

        // Сохранение результирующего PDF файла
        pdfDocument.save(pdfDocumentFileName);
    }
```


### Преобразование предварительно форматированного текстового файла в PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Чтение текстового файла как массива строк
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Создание экземпляра объекта Document, вызвав его пустой конструктор
        Document pdfDocument = new Document();

        // Добавление новой страницы в коллекцию Pages объекта Document
        Page page = pdfDocument.getPages().add();

        // Установка левых и правых полей для лучшего представления
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // проверка, содержит ли строка символ "перевод страницы"
            // см. https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Создание экземпляра TextFragment и
                // передача строки в его
                // конструктор в качестве аргумента
                TextFragment text = new TextFragment(line);

                // Добавление нового текстового абзаца в коллекцию абзацев и передача объекта TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## Конвертация XPS в PDF

**Aspose.PDF for Java** поддерживает функцию конвертации файлов <abbr title="XML Paper Specification">XPS</abbr> в формат PDF. Ознакомьтесь с этой статьей, чтобы решить ваши задачи.

XPS, XML Paper Specification, это формат файла от Microsoft, используемый для интеграции создания и просмотра документов в Windows. С помощью Aspose.PDF for Java возможно конвертировать файлы XPS в PDF, портативный формат файла от Adobe.

Формат файла в основном представляет собой заархивированный XML-файл, который в первую очередь используется для распространения и хранения. Его очень трудно редактировать, и он в основном реализован Microsoft.

Чтобы конвертировать файл XPS в PDF с использованием [Aspose.PDF for Java](https://products.aspose.com/pdf/java), используйте класс [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Этот код используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Позже этот объект передается в качестве аргумента во время инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает механизму рендеринга PDF определить формат входного документа.

Как в XP, так и в Windows 7, вы должны найти предварительно установленный XPS-принтер, если посмотрите в Панели управления, а затем в Принтерах. Чтобы создавать XPS-файлы, вы можете использовать этот принтер в качестве выходного устройства. В Windows 7 вы можете просто дважды щелкнуть файл, чтобы открыть его в просмотрщике XPS. Вы также можете скачать [просмотрщик XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) с веб-сайта Microsoft.

Следующий фрагмент кода показывает процесс преобразования XPS-файла в формат PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Инициализация объекта документа

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // Создание объекта LoadOption с использованием опции загрузки XPS
        LoadOptions options = new XpsLoadOptions();

        // Создание объекта Document, вызывая его пустой конструктор
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // Сохранение результирующего PDF-файла
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат XPS в PDF онлайн**

Aspose.PDF для Java представляет вам бесплатное онлайн-приложение ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация XPS в PDF с бесплатным приложением](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Конвертация PostScript в PDF

**Aspose.PDF для Java** поддерживает функции преобразования файлов PostScript в формат PDF. Одной из функций Aspose.PDF является возможность установить набор папок шрифтов, которые будут использоваться во время конвертации.

Для того чтобы конвертировать файл PostScript в формат PDF, Aspose.PDF для Java предлагает класс [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions), который используется для инициализации объекта LoadOptions. Позже этот объект может быть передан в качестве аргумента конструктору объекта Document, что поможет PDF Rendering Engine определить формат исходного документа.


Следующий фрагмент кода может быть использован для преобразования файла PostScript в формат PDF:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // Инициализировать объект документа

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Создать объект Document
        Document document = new Document(psDocumentFileName, options);

        // Сохранить выходной PDF документ
        document.save(pdfDocumentFileName);
    }
```

Кроме того, вы можете задать набор папок шрифтов, которые будут использоваться во время преобразования:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Создать объект Document
        Document document = new Document(psDocumentFileName, options);

        // Сохранить выходной PDF документ
        document.save(pdfDocumentFileName);
    }
```


## Преобразование XML в PDF

Формат XML используется для хранения структурированных данных. Существует несколько способов преобразования <abbr title="Extensible Markup Language">XML</abbr> в PDF в Aspose.PDF.

{{% alert color="success" %}}
**Попробуйте преобразовать XML в PDF онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["XML в PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), где вы можете попробовать изучить функциональность и качество работы.

[![Aspose.PDF Преобразование XML в PDF с помощью бесплатного приложения](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Рассмотрите вариант использования XML-документа на основе стандарта XSL-FO.

### Преобразование XSL-FO в PDF

Преобразование файлов XSL-FO в PDF можно реализовать с использованием объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) с [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * Преобразование XML в PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Инициализация объекта документа

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Создание экземпляра объекта Document, вызвав его пустой конструктор
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // Сохранение итогового PDF файла
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### Преобразование XSL-FO в PDF с заданной стратегией обработки ошибок

```java
// Инициализация объекта документа

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// Установка стратегии обработки ошибок
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// Создание объекта Document, вызвав его пустой конструктор
Document document = new Document(xmlDocumentFileName, options);

// Сохранение результирующего PDF файла
document.save(documentFileName);
document.close();
```

## Преобразование LaTeX/TeX в PDF

Формат файла LaTeX представляет собой текстовый формат с разметкой в производной от TeX семье языков LaTeX, и LaTeX является производным форматом системы TeX.
 LaTeX (ˈleɪtɛk/ лай-тек или ла-тек) — это система подготовки документов и язык разметки документов. Он широко используется для общения и публикации научных документов во многих областях, включая математику, физику и информатику. Также он играет важную роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как санскрит и арабский, включая критические издания. LaTeX использует программу набора текста TeX для форматирования своего вывода и сам написан на языке макросов TeX.

**Aspose.PDF for Java** поддерживает функцию преобразования файлов TeX в формат PDF, и для выполнения этого требования пакет com.aspose.pdf имеет класс под названием [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions), который предоставляет возможности загрузки файлов LaTex и отображения вывода в формате PDF, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Следующий фрагмент кода показывает процесс преобразования LaTex файла в формат PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Создать объект опции загрузки Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Создать объект документа
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Сохранить выходной PDF документ
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Попробуйте преобразовать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попробовать изучить функциональность и качество его работы.
[![Aspose.PDF Конвертация LaTeX/TeX в PDF с бесплатным приложением](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}