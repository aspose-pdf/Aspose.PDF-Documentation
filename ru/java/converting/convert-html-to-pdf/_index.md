---
title: Преобразование HTML в PDF на Java
linktitle: Преобразование HTML в файл PDF
type: docs
weight: 40
url: /ru/java/convert-html-to-pdf/
lastmod: "2026-09-16"
description: Узнайте, как конвертировать HTML, MHTML и веб-страницы в PDF на Java с помощью Aspose.PDF, включая настройки типов носителей, правила CSS‑страниц, встраивание шрифтов, содержимое SVG и вывод на одну страницу.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать HTML в PDF на Java с помощью Aspose.PDF
Abstract: Эта статья объясняет, как конвертировать файлы HTML и MHTML в PDF с использованием Aspose.PDF for Java. Она охватывает базовый процесс HTML-to-PDF и показывает, как управлять рендерингом с помощью типов носителей, приоритетов правил CSS‑страницы, встроенных шрифтов, SVG‑контента, вывода на одну страницу и прямого преобразования с веб-страницы.
---
Aspose.PDF for Java может конвертировать локальные HTML‑файлы, архивированный контент MHTML и веб-страницы в PDF‑документы. Вы можете управлять конвейером конвертации с помощью `HtmlLoadOptions` и `MhtLoadOptions` для влияния на масштабирование макета, обработку CSS‑медиа, приоритет правил страниц, встраивание шрифтов, разрешение ресурсов и поведение одностраничного рендеринга.

## Преобразование HTML в PDF

Используйте этот пример, когда локальный HTML‑файл необходимо напрямую преобразовать в PDF‑документ.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) для настройки того, как HTML‑источник интерпретируется при импорте.
1. Установите [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) в значение `ScaleToPageWidth`, при этом широкое HTML‑содержимое масштабируется до ширины целевой страницы PDF вместо обрезки.
1. Откройте исходный HTML‑файл, передав его путь и настроенные параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните созданный [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) как PDF‑файл по целевому пути вывода.

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование HTML в PDF с настройкой типа носителя

Используйте этот пример, когда обработку типа носителя CSS необходимо контролировать во время преобразования HTML.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) настроек конвертации.
1. Установите [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) в значение `Screen`, когда HTML должен отображаться с использованием CSS‑правил, предназначенных для экранного отображения, а не для печати.
1. Откройте HTML‑файл с настроенными параметрами загрузки, чтобы стили, зависящие от media‑query, применялись во время конвертации.
1. Сохраните результат [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) как PDF‑файл.

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование HTML в PDF с настройкой приоритета правил CSS для страниц

Используйте этот пример, когда правила CSS `@page` должны влиять на итоговый макет страниц PDF.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) перед открытием HTML‑файла.
1. Настройте `setPriorityCssPageRule(false)`, когда другие настройки макета должны иметь приоритет над объявлениями CSS `@page` в исходной разметке.
1. Загрузите HTML‑содержимое в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с настроенными параметрами, чтобы макет страницы был определён при импорте.
1. Сохраните сгенерированный файл PDF.

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование HTML в PDF со встроенными шрифтами

Используйте этот пример, когда результирующий PDF должен сохранять шрифты HTML, встраивая их.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) конфигурации импорта HTML.
1. Включите `setEmbedFonts(true)`, при этом шрифты, определённые во время рендеринга HTML, сохраняются в выходном PDF.
1. Откройте HTML‑источник с этими параметрами загрузки, чтобы сохранить оригинальную типографику в итоговом документе.
1. Сохраните [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в виде PDF с включёнными встроенными ресурсами шрифтов.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Отображение HTML на одной странице PDF

Используйте этот пример, когда длинный HTML‑контент должен быть размещён на одной странице PDF, а не растекаться на несколько страниц.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) настроек конвертации.
1. Включите `setRenderToSinglePage(true)`, при этом импортированный HTML размещается на одной странице PDF, а не разбивается на несколько страниц.
1. Откройте исходный HTML с настроенными параметрами загрузки и позвольте Aspose.PDF построить макет страницы в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните выходной PDF‑файл.

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование HTML со встроенным SVG

Используйте этот пример, когда HTML‑источник содержит встроенные данные SVG, которые необходимо отобразить в PDF.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) с родительским каталогом HTML‑файла в качестве базового пути, чтобы связанные ресурсы могли быть последовательно разрешены во время преобразования.
1. Откройте HTML‑файл, содержащий встроенную разметку SVG, передав путь к источнику и параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF рендерить HTML DOM вместе со встроенными SVG‑элементами в содержимое страницы PDF.
1. Сохраните сгенерированный PDF‑документ.

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование веб-страницы в PDF

Используйте этот пример, когда содержимое по URL-адресу веб-страницы должен быть отрисован и сохранён как PDF‑документ.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) с целевым URL, чтобы относительные ресурсы, такие как таблицы стилей и изображения, могли быть разрешены относительно этого адреса.
1. Преобразуйте строку URL в объект `URL` и откройте его поток ввода, чтобы получить актуальное HTML-содержимое.
1. Создайте [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из потока ответа и настроенных параметров загрузки, чтобы загруженная страница обрабатывалась с правильным базовым URL.
1. Сохраните отрендеренную веб-страницу в виде PDF-файла и автоматически закройте ресурсы потоков с помощью конструкции try-with-resources.

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## Преобразование MHTML в PDF

Используйте этот пример, когда архивный файл MHTML должен быть преобразован в документ PDF.

1. Создайте экземпляр [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/), чтобы указать Aspose.PDF загружать источник как MIME HTML‑контент.
1. Откройте файл `.mht` или `.mhtml`, передавая его путь и параметры загрузки MHTML в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF разобрать архивированный HTML‑контент и его встроенные ресурсы в модель документа PDF.
1. Сохраните сгенерированный файл PDF.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
