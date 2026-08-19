---
title: Конвертировать другие форматы файлов в PDF на Java
linktitle: Конвертировать другие форматы файлов в PDF
type: docs
weight: 80
url: /ru/java/convert-other-files-to-pdf/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать файлы EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD и TeX в PDF на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать другие форматы файлов в PDF на Java
Abstract: В этой статье объясняется, как конвертировать несколько исходных форматов файлов в PDF с помощью Aspose.PDF for Java. Она охватывает рабочие процессы конвертации EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, текст, XML, XPS и XSL-FO с использованием специфических для формата параметров загрузки и предварительных этапов при необходимости.
---
Aspose.PDF for Java поддерживает преобразование из форматов документов, разметки и описания страниц в PDF.

## Конвертировать OFD в PDF

Используйте этот пример, когда документ OFD должен быть преобразован в PDF.

1. Откройте источник OFD, передав путь к файлу и [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF разобрать пакет OFD в модель документа PDF.
1. Сохраните полученный PDF в целевой путь вывода.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Преобразуйте TeX в PDF

Используйте этот пример, когда содержимое TeX должно быть напрямую преобразовано в PDF.

1. Откройте исходный файл TeX, передав путь к файлу и [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF интерпретировать разметку TeX и формировать макет PDF при загрузке.
1. Сохраните сгенерированный PDF.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PostScript в PDF

Используйте этот пример, когда файл PostScript должен быть преобразован в документ PDF.

1. Откройте исходный PostScript с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF преобразовать поток описания страниц PostScript в модель документа PDF.
1. Сохраните преобразованный PDF‑файл.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте EPS в PDF

Используйте этот пример, когда файл Encapsulated PostScript нужно преобразовать в PDF.

1. Откройте EPS‑источник с помощью [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) потому что EPS следует тому же пути загрузки на основе PostScript.
1. Загрузите файл в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) поэтому содержимое описания страницы преобразуется при импорте.
1. Сохраните выходной PDF.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать EPUB в PDF

Используйте этот пример, когда EPUB‑книга должна быть преобразована в PDF.

1. Откройте исходный EPUB, передав путь к файлу и [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
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

## Преобразуйте Markdown в PDF

Используйте этот пример, когда контент в формате Markdown должен быть отрендерен и сохранён как PDF.

1. Откройте исходный файл Markdown, передав путь к файлу и [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF интерпретировать содержимое Markdown и отрисовать его в содержимое страниц PDF.
1. Сохраните выходной файл PDF.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте текст в PDF с простым рабочим процессом

Используйте этот пример, когда обычный текстовый файл нужно быстро преобразовать в PDF.

1. Прочитайте исходный текстовый файл с декодированием UTF-8, чтобы содержимое текста было доступно в виде строки Java.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Объедините текст в [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и добавить его в коллекцию абзацев страницы.
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

## Конвертировать текст в PDF с расширенными параметрами

Используйте этот пример, когда обычный текст должен быть преобразован с дополнительными параметрами макета или кодировки.

1. Прочитайте все строки текста из входного файла, чтобы можно было проверить маркеры разрыва страниц во время конвертации.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и настройте каждый [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) с полями и состоянием текста по умолчанию.
1. Разрешить моноширинный шрифт через [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) и добавить каждую строку как [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
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

## Конвертировать PCL в PDF

Используйте этот пример, когда поток печати PCL должен быть преобразован в PDF.

1. Создайте [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) и включить подавление ошибок разбора, когда требуется мягкое поведение импорта.
1. Откройте источник PCL, передав путь к файлу и параметры загрузки в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
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

## Преобразуйте XML в PDF с помощью XSLT и HTML

Используйте этот пример, когда данные XML должны быть преобразованы перед окончательной генерацией PDF.

1. Преобразуйте XML‑источник с помощью XSLT‑файла во временный HTML‑файл, вызвав специализированный метод преобразования.
1. Передайте сгенерированный HTML‑файл в существующую функцию преобразования HTML в PDF, чтобы итоговый PDF использовал стандарт [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) Workflow.
1. Удалите временный HTML‑файл в `finally` блок после завершения конверсии.
1. Сохраните сгенерированный файл PDF.

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

## Преобразуйте XPS в PDF

Используйте этот пример, когда документ XPS должен быть преобразован в PDF.

1. Откройте источник XPS, передавая путь к файлу и [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
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

## Преобразуйте XSL-FO в PDF

Используйте этот пример, когда содержимое XSL-FO должно быть отрендерено в PDF.

1. Создайте [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) с путем XSLT, чтобы XML‑источник мог быть преобразован во время загрузки.
1. Настройте режим обработки ошибок разбора так, чтобы при обнаружении недопустимого XSL-FO сразу генерировать исключение.
1. Откройте XML-источник в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с этими параметрами загрузки.
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

## Преобразуйте XML в промежуточный HTML

Используйте этот метод, когда данные XML должны быть преобразованы в HTML перед окончательным шагом конвертации в PDF.

1. Откройте файлы XML и XSLT ввода в качестве источников преобразования.
1. Создайте `Transformer` из XSLT‑стилевого листа и запустить его на XML‑источнике
1. Запишите преобразованный HTML‑файл на диск, чтобы функция последующего преобразования в PDF могла его загрузить.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```

