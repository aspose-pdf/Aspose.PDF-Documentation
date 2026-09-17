---
title: Преобразование других форматов файлов в PDF на Java
linktitle: Преобразование других форматов файлов в PDF
type: docs
weight: 80
url: /ru/java/convert-other-files-to-pdf/
lastmod: "2026-09-16"
description: Узнайте, как конвертировать файлы EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD и TeX в PDF на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать другие форматы файлов в PDF на Java
Abstract: В этой статье объясняется, как преобразовать несколько исходных форматов файлов в PDF с помощью Aspose.PDF for Java. Описываются рабочие процессы конвертации EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, текста, XML, XPS и XSL-FO с использованием опций загрузки, специфичных для формата, и предварительных шагов при необходимости.
---
Aspose.PDF for Java поддерживает преобразование из форматов документов, разметки и описания страниц в PDF.

## Преобразование OFD в PDF

Используйте этот пример, когда документ OFD должен быть преобразован в PDF.

1. Откройте источник OFD, передавая путь к файлу и [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF разобрать пакет OFD в модель документа PDF.
1. Сохраните полученный PDF по целевому пути.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Преобразование TeX в PDF

Используйте этот пример, когда содержимое TeX должно быть напрямую отрендерено в PDF.

1. Откройте исходный файл TeX, передав путь к файлу и [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать разметку TeX и построить макет PDF при загрузке.
1. Сохраните сгенерированный PDF.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PostScript в PDF

Используйте этот пример, когда файл PostScript должен быть преобразован в документ PDF.

1. Откройте исходный PostScript с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) в конструкторе [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF преобразовать поток описания страниц PostScript в модель документа PDF.
1. Сохраните преобразованный файл PDF.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование EPS в PDF

Используйте этот пример, когда файл Encapsulated PostScript необходимо преобразовать в PDF.

1. Откройте EPS‑источник с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/), поскольку EPS следует тому же пути загрузки, основанному на PostScript.
1. Загрузите файл в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), при этом содержимое описания страницы преобразуется во время импорта.
1. Сохраните выходной PDF.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование EPUB в PDF

Используйте этот пример, когда необходимо преобразовать электронную книгу EPUB в PDF.

1. Откройте источник EPUB, передав путь к файлу и [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF загрузить структуру электронной книги и преобразовать её в страницы PDF.
1. Сохраните преобразованный PDF.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование Markdown в PDF

Используйте этот пример, когда содержимое Markdown должно быть отрисовано и сохранено в PDF.

1. Откройте исходный Markdown, передав путь к файлу и [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать содержимое Markdown и отобразить его в содержимое страницы PDF.
1. Сохраните выходной PDF-файл.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Простой способ преобразования текста в PDF

Используйте этот пример, когда необходимо быстро преобразовать текстовый файл в PDF.

1. Прочитайте исходный обычный текст с декодированием UTF-8, чтобы содержимое текста было доступно в виде строки Java.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Оберните текст в [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и добавьте его в коллекцию абзацев страницы.
1. Сохраните сгенерированный PDF.

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

## Преобразование текста в PDF с дополнительными параметрами

Используйте этот пример, когда обычный текст должен быть преобразован с дополнительными параметрами макета или кодирования.

1. Прочитайте все строки текста из входного файла, чтобы можно было проверить маркеры разрыва страниц во время конвертации.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и настройте поля и параметры текста по умолчанию для каждой страницы [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Найдите моноширинный шрифт с помощью [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) и добавьте каждую строку как [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной файл после завершения цикла построения страниц.

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

## Преобразование PCL в PDF

Используйте этот пример, когда поток печати PCL необходимо преобразовать в PDF.

1. Создайте [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) и включите подавление ошибок разбора, если импорт должен продолжаться при их возникновении.
1. Откройте источник PCL, передав путь к файлу и параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните результат как PDF.

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

Используйте этот пример, когда данные XML должны быть преобразованы перед окончательной генерацией PDF.

1. Преобразуйте XML‑исходник с помощью файла XSLT во временный HTML‑файл, вызвав специальный метод преобразования.
1. Передайте сгенерированный HTML‑файл в существующую функцию преобразования HTML в PDF, чтобы итоговый PDF создавался стандартным способом с помощью [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/).
1. Удалите временный HTML‑файл в блоке `finally` после завершения конвертации.
1. Сохраните сгенерированный PDF-файл.

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

## Преобразование XPS в PDF

Используйте этот пример, когда XPS‑документ необходимо преобразовать в PDF.

1. Откройте источник XPS, передав путь к файлу и [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать описание страницы XPS во время загрузки документа.
1. Сохраните преобразованный PDF.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование XSL-FO в PDF

Используйте этот пример, когда содержимое XSL-FO должно быть преобразовано в PDF.

1. Создайте [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) с путём XSLT, чтобы XML‑источник можно было преобразовать при загрузке.
1. Настройте режим обработки ошибок разбора так, чтобы при обнаружении неверного XSL-FO сразу генерировалось исключение.
1. Откройте XML-источник в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с этими параметрами загрузки.
1. Сохраните полученный PDF‑документ.

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

Используйте этот метод, когда XML‑данные необходимо преобразовать в HTML перед окончательным шагом конвертации в PDF.

1. Откройте XML- и XSLT-файлы ввода в качестве источников преобразования.
1. Создайте `Transformer` из таблицы стилей XSLT и примените его к исходному XML.
1. Запишите преобразованный HTML‑файл на диск, чтобы последующая функция преобразования в PDF могла загрузить его.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
