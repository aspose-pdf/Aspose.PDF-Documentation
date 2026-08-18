---
title: Преобразование других форматов файлов в PDF в Java
linktitle: Конвертируйте другие форматы файлов в PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать файлы EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD и TeX в PDF на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать другие форматы файлов в PDF в Java
Abstract: В этой статье объясняется, как конвертировать несколько форматов исходных файлов в PDF с помощью Aspose.PDF для Java. Он охватывает рабочие процессы преобразования EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, текста, XML, XPS и XSL-FO с использованием параметров загрузки для конкретного формата и шагов предварительной обработки, где это необходимо.
---
Aspose.PDF для Java поддерживает преобразование форматов документов, разметки и описания страниц в PDF.

## Конвертировать OFD в PDF

Используйте этот пример, когда документ OFD необходимо преобразовать в PDF.

1. Откройте исходный код OFD, передав путь к файлу и [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Пусть Aspose.PDF преобразует пакет OFD в модель документа PDF.
1. Сохраните полученный PDF-файл в целевой путь вывода.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Конвертировать TeX в PDF

Используйте этот пример, когда содержимое TeX должно быть отображено непосредственно в формате PDF.

1. Откройте исходный код TeX, передав путь к файлу и [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать разметку TeX и создавать макет PDF во время загрузки.
1. Сохраните созданный PDF-файл.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PostScript в PDF

Используйте этот пример, когда файл PostScript необходимо преобразовать в документ PDF.

1. Откройте исходный код PostScript с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) в конструкторе [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF преобразовать поток описания страницы PostScript в модель PDF-документа.
1. Сохраните преобразованный PDF-файл.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать EPS в PDF

Используйте этот пример, когда инкапсулированный файл PostScript необходимо преобразовать в PDF.

1. Откройте исходный код EPS с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/), поскольку EPS следует по тому же пути загрузки на основе PostScript.
1. Загрузите файл в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), чтобы содержимое описания страницы было преобразовано во время импорта.
1. Сохраните выходной PDF-файл.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать EPUB в PDF

Используйте этот пример, когда электронную книгу EPUB необходимо преобразовать в PDF.

1. Откройте исходный код EPUB, передав путь к файлу и [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF загрузить структуру электронной книги и преобразовать ее в страницы PDF.
1. Сохраните преобразованный PDF-файл.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать Markdown в PDF

Используйте этот пример, когда содержимое Markdown необходимо отобразить и сохранить в формате PDF.

1. Откройте исходный код Markdown, передав путь к файлу и [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать содержимое Markdown и преобразовать его в содержимое страницы PDF.
1. Сохраните выходной PDF-файл.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование текста в PDF с помощью простого рабочего процесса

Используйте этот пример, когда простой текстовый файл необходимо быстро преобразовать в PDF.

1. Прочтите исходный текст в виде обычного текста с декодированием UTF-8, чтобы текстовое содержимое было доступно в виде строки Java.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Оберните текст в [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и добавьте его в коллекцию абзацев страницы.
1. Сохраните созданный PDF-файл.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование текста в PDF с расширенными параметрами

Используйте этот пример, когда простой текст необходимо преобразовать с дополнительными параметрами макета или кодирования.

1. Считайте все текстовые строки из входного файла, чтобы можно было проверить маркеры разрыва страницы во время преобразования.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и настройте каждый [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) с полями и состоянием текста по умолчанию.
1. Разрешите моноширинный шрифт через [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) и добавьте каждую строку как [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной файл после завершения цикла создания страницы.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PCL в PDF

Используйте этот пример, когда поток печати PCL необходимо преобразовать в PDF.

1. Создайте [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) и включите подавление ошибок синтаксического анализа, когда требуется мягкое поведение при импорте.
1. Откройте исходный код PCL, передав путь к файлу и параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните результат в формате PDF.

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование XML в PDF с помощью XSLT и HTML

Используйте этот пример, когда XML-данные необходимо преобразовать перед окончательным созданием PDF-файла.

1. Преобразуйте источник XML с помощью файла XSLT во временный файл HTML, вызвав специальный метод преобразования.
1. Передайте сгенерированный HTML-файл в существующую функцию преобразования HTML в PDF, чтобы в окончательном PDF-файле использовался стандартный рабочий процесс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/).
1. Удалите временный HTML-файл в блоке `finally` после завершения преобразования.
1. Сохраните созданный PDF-файл.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Конвертировать XPS в PDF

Используйте этот пример, когда документ XPS необходимо преобразовать в PDF.

1. Откройте исходный код XPS, передав путь к файлу и [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать описание страницы XPS во время загрузки документа.
1. Сохраните преобразованный PDF-файл.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать XSL-FO в PDF

Используйте этот пример, когда содержимое XSL-FO должно отображаться в формате PDF.

1. Создайте [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) с путем XSLT, чтобы источник XML можно было преобразовать во время загрузки.
1. Настройте режим обработки ошибок синтаксического анализа, чтобы он выдавался немедленно при обнаружении недопустимого XSL-FO.
1. Откройте исходный код XML в файле [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с этими параметрами загрузки.
1. Сохраните полученный PDF-документ.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Преобразование XML в промежуточный HTML

Используйте этот метод, когда данные XML необходимо преобразовать в HTML перед последним этапом преобразования PDF.

1. Откройте входные файлы XML и XSLT в качестве источников преобразования.
1. Создайте `Transformer` из таблицы стилей XSLT и запустите ее с исходным кодом XML.
1. Запишите преобразованный HTML-файл на диск, чтобы последующая функция преобразования PDF могла его загрузить.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
