---
title: Извлечение необработанного текста из PDF файла
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: /java/extract-text-from-all-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF документов с использованием Aspose.PDF для Java. Из всех страниц, из определенной части, на основе колонок и т.д.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF документа

Извлечение текста из PDF документа — это общая задача. В этом примере вы увидите, как Aspose.PDF для Java позволяет извлекать текст со всех страниц PDF документа. Чтобы извлечь текст со всех страниц PDF:

1. Создайте объект класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Откройте PDF, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и вызовите метод [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. Класс [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) извлекает текст из документа и возвращает его в свойстве **Text**.

Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF-документа.

```java
public static void ExtractFromAllPages(){
    // Путь к каталогу документов.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Открыть документ
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Создать объект TextAbsorber для извлечения текста
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // Применить абсорбер для всех страниц
    pdfDocument.getPages().accept(textAbsorber);
    
    // Получить извлеченный текст
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // Записать строку текста в файл
        writer.write(extractedText);            
        // Закрыть поток
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## Извлечение текста со страниц с использованием TextDevice

Вы можете использовать класс **TextDevice** для извлечения текста из PDF файла. TextDevice использует [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) в своей реализации, таким образом, по сути, они делают одно и то же, но TextDevice был реализован для унификации подхода "Device" для извлечения чего-либо со страницы: ImageDevice, PageDevice и т.д. TextAbsorber может извлекать текст со страницы, всего PDF или XForm, этот TextAbsorber более универсален.

### Извлечение текста со всех страниц

Следующие шаги и фрагмент кода показывают, как извлечь текст из PDF, используя текстовое устройство.

1. Создайте объект класса Document с указанным входным PDF файлом
1. Создайте объект класса TextDevice
1. Используйте объект класса TextExtractOptions для указания параметров извлечения
1. Используйте метод Process класса TextDevice для преобразования содержимого в текст
1. Сохраните текст в выходной файл

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // открыть документ
    Document pdfDocument = new Document("input.pdf");
    // текстовый файл, в который будет сохранен извлеченный текст
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // перебрать все страницы PDF файла
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // создать текстовое устройство
        TextDevice textDevice = new TextDevice();
        // установить параметры извлечения текста - установить режим извлечения текста (Raw или Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // получить текст со страниц PDF и сохранить его в объект OutputStream
        textDevice.process(page, text_stream);
    }
    // закрыть объект потока
    text_stream.close();
}
```


## Извлечение текста из определенной области страницы

Класс [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) предоставляет возможность извлекать текст из определенной или всех страниц PDF-документа. Этот класс возвращает извлеченный текст в свойстве **Text**. Однако, если у нас есть необходимость извлечь текст из определенной области страницы, мы можем использовать свойство **Rectangle** класса [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). Свойство Rectangle принимает объект Rectangle в качестве значения, и с использованием этого свойства мы можем указать область страницы, из которой нам нужно извлечь текст.

Метод [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) страницы вызывается для извлечения текста.
 Создайте объекты классов [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Вызовите метод [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) на отдельной странице, как **Page** Index, объекта **Document**. **Index** — это конкретный номер страницы, с которой необходимо извлечь текст. Вы можете получить текст из свойства **Text** класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Следующий фрагмент кода показывает, как извлечь текст с отдельной страницы.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // открыть документ
    Document doc = new Document("page_0001.pdf");
    // создать объект TextAbsorber для извлечения текста
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // применить абсорбер для первой страницы
    doc.getPages().get_Item(1).accept(absorber);
    // получить извлеченный текст
    String extractedText = absorber.getText();
    // создать writer и открыть файл
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // записать извлеченное содержимое
    writer.write(extractedText);
    // закрыть writer
    writer.close();
}
```

## Извлечение текста на основе колонок

PDF файл может содержать Текст, Изображения, Аннотации, Вложения, Графики и другие элементы, и Aspose.PDF for .NET предлагает возможность добавлять, а также изменять все эти элементы. Этот API замечателен, когда дело касается добавления и извлечения текста из PDF документа, и мы можем столкнуться с ситуацией, когда PDF документ состоит из более чем одной колонки (много-колоночный) PDF документа, и нам нужно извлечь содержимое страницы, сохраняя тот же макет, тогда Aspose.PDF for .NET является правильным выбором для выполнения этого требования. Один из подходов заключается в уменьшении размера шрифта содержимого внутри PDF документа, а затем выполнении извлечения текста. Следующий фрагмент кода показывает шаги по уменьшению размера текста, а затем попытке извлечения текста из PDF документа.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // открыть документ
    Document doc = new Document("page_0001.pdf");
    // создать объект TextAbsorber для извлечения текста
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // принять абсорбер для первой страницы
    doc.getPages().get_Item(1).accept(absorber);
    // получить извлеченный текст
    String extractedText = absorber.getText();
    // создать writer и открыть файл
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // записать извлеченное содержимое
    writer.write(extractedText);
    // закрыть writer
    writer.close();
}
```


### Второй подход - Использование ScaleFactor

В этом новом выпуске мы также внедрили несколько улучшений в TextAbsorber и во внутренний механизм форматирования текста. Таким образом, теперь во время извлечения текста с использованием режима ‘Pure’, вы можете указать опцию ScaleFactor, и это может быть еще одним подходом для извлечения текста из многостолбцового PDF-документа, помимо вышеупомянутого подхода. Этот масштабный коэффициент может быть установлен для настройки сетки, которая используется для внутреннего механизма форматирования текста во время извлечения текста. Указание значений ScaleFactor между 1 и 0.1 (включая 0.1) имеет тот же эффект, что и уменьшение шрифта.

Указание значений ScaleFactor между 0.1 и -0.1 рассматривается как нулевое значение, но это заставляет алгоритм автоматически рассчитывать коэффициент масштабирования, необходимый для извлечения текста. Расчет основан на средней ширине глифа самого популярного шрифта на странице, но мы не можем гарантировать, что в извлеченном тексте ни одна строка столбца не достигнет начала следующего столбца. Обратите внимание, что если значение ScaleFactor не указано, будет использовано значение по умолчанию 1.0. Это означает, что масштабирование не будет выполняться. Если указанное значение ScaleFactor больше 10 или меньше -0.1, будет использовано значение по умолчанию 1.0.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width (about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

Мы предлагаем использовать автоматическое масштабирование (ScaleFactor = 0) при обработке большого количества PDF-файлов для извлечения текстового содержимого. Или вручную установить избыточное уменьшение ширины сетки (примерно ScaleFactor = 0.5). Однако вы не должны определять, необходимо ли масштабирование для конкретных документов или нет. Если вы установите избыточное уменьшение ширины сетки для документа (который в этом не нуждается), извлеченное текстовое содержимое останется полностью адекватным. Пожалуйста, обратите внимание на следующий фрагмент кода.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Установка коэффициента масштабирования на 0.5 достаточно для разделения колонок в большинстве документов
    // Setting of zero allows to algorithm choose scale factor automatically
    // Установка нуля позволяет алгоритму выбирать коэффициент масштабирования автоматически
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

Обратите внимание, что нет прямой взаимосвязи между новым ScaleFactor и старым коэффициентом ручного уменьшения шрифта. Однако, по умолчанию алгоритм учитывает значение размера шрифта, которое уже было уменьшено по некоторым внутренним причинам. Например, уменьшение размера шрифта с 10 до 7 имеет тот же эффект, что и установка коэффициента масштаба на 5/8 (= 0.625).

{{% /alert %}}

## Извлечение выделенного текста из PDF-документа

В различных сценариях извлечения текста из PDF-документа может возникнуть необходимость извлечь только выделенный текст. Для реализации этой функции мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлечь выделенный текст из PDF-документа, фильтруя TextMarkupAnnotation и используя упомянутые методы. Следующий фрагмент кода показывает, как можно извлечь выделенный текст из PDF-документа.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Перебор всех аннотаций
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Фильтрация TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Извлечение фрагментов выделенного текста
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Отображение выделенного текста
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## Доступ к элементам текстового фрагмента и сегмента из XML

Иногда нам необходимо получить доступ к элементам TextFragement или TextSegment при обработке PDF-документов, созданных из XML. Aspose.PDF for .NET предоставляет доступ к таким элементам по имени. Пример кода ниже показывает, как использовать эту функциональность.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```