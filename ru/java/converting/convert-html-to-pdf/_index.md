---
title: Преобразовать HTML в PDF на Java
linktitle: Преобразовать HTML в PDF файл
type: docs
weight: 40
url: /ru/java/convert-html-to-pdf/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать HTML, MHTML и веб-страницы в PDF на Java с помощью Aspose.PDF, включая настройки media, правила CSS для страниц, встраивание шрифтов, содержимое SVG и одностраничный вывод.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать HTML в PDF на Java с помощью Aspose.PDF
Abstract: В этой статье объясняется, как преобразовать файлы HTML и MHTML в PDF с помощью Aspose.PDF for Java. Описывается базовый процесс преобразования HTML в PDF и показывается, как управлять рендерингом с помощью медиатипов, приоритетов правил CSS‑страницы, встроенных шрифтов, SVG‑контента, вывода в один лист и прямого преобразования из живой веб‑страницы.
---
Aspose.PDF for Java может конвертировать локальные HTML‑файлы, архивированный контент MHTML и живые веб‑страницы в PDF‑документы. Вы можете управлять процессом конвертации с помощью `HtmlLoadOptions` и `MhtLoadOptions` для влияния на масштабирование макета, обработку медиa‑запросов CSS, приоритет правил страницы, встраивание шрифтов, разрешение ресурсов и поведение рендеринга одной страницы.

## Преобразуйте HTML в PDF

Используйте этот пример, когда локальный HTML‑файл должен быть напрямую преобразован в PDF‑документ.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр для настройки того, как интерпретируется HTML‑исходник при импорте.
1. Установите [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) к `ScaleToPageWidth` поэтому широкое HTML‑содержание масштабируется до ширины целевой страницы PDF, а не обрезается.
1. Откройте исходный HTML‑файл, передав его путь и настроенные параметры загрузки в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Сохраните сгенерированное [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в виде PDF‑файла по целевому пути вывода.

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

## Преобразуйте HTML в PDF с вариантами типа медиа

Используйте этот пример, когда обработка типа медиа CSS должна контролироваться при преобразовании HTML.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр для настроек преобразования.
1. Установите [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) к `Screen` когда HTML должен отображаться с использованием CSS‑правил, предназначенных для отображения на экране, а не для печати.
1. Откройте HTML‑файл с настроенными параметрами загрузки, чтобы стили, зависящие от медиа‑запросов, применялись во время конвертации.
1. Сохраните полученный [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в виде PDF‑файла.

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

## Преобразуйте HTML в PDF с приоритетом правила CSS page

Используйте этот пример при работе с CSS `@page` правила должны влиять на окончательный макет страниц PDF.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр перед открытием HTML‑файла.
1. Настройте `setPriorityCssPageRule(false)` когда другие настройки макета должны иметь приоритет над CSS `@page` объявления в исходной разметке.
1. Загрузите HTML‑контент в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с настроенными параметрами, чтобы макет страницы был определён во время импорта.
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

## Преобразуйте HTML в PDF с внедрёнными шрифтами

Используйте этот пример, когда результирующий PDF должен сохранять шрифты HTML путем их встраивания.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр конфигурации импорта HTML.
1. Включите `setEmbedFonts(true)` поэтому шрифты, определённые при рендеринге HTML, сохраняются в итоговом PDF.
1. Откройте исходный HTML с этими параметрами загрузки, чтобы сохранить оригинальную типографику в окончательном документе.
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

## Отобразите HTML‑контент на одной странице PDF

Используйте этот пример, когда длинный HTML‑контент следует удерживать на одной странице PDF вместо разбивки на несколько страниц.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр для настроек преобразования.
1. Включите `setRenderToSinglePage(true)` поэтому импортированный HTML размещается на одной странице PDF, а не разбивается на несколько страниц.
1. Откройте исходный HTML с настроенными параметрами загрузки и позвольте Aspose.PDF построить макет страницы в a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните выходной файл PDF.

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

## Преобразуйте HTML, содержащий встроенный SVG

Используйте этот пример, когда исходный HTML содержит встроенные данные SVG, которые необходимо отобразить в PDF.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр с родительским каталогом HTML‑файла в качестве базового пути, чтобы связанные ресурсы могли разрешаться последовательно во время конвертации.
1. Откройте HTML‑файл, содержащий встроенную разметку SVG, передав путь к источнику и параметры загрузки в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF отрисовывать DOM HTML вместе с встроенными элементами SVG в содержимое страницы PDF.
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

## Преобразуйте веб-страницу в PDF

Используйте этот пример, когда живой веб‑URL должен быть отрендерен и сохранён как PDF‑документ.

1. Создайте [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) экземпляр с целевым URL, чтобы относительные ресурсы, такие как таблицы стилей и изображения, могли разрешаться относительно этого адреса.
1. Преобразуйте строку URL в `URL` объект и открыть его входной поток, чтобы получить живой HTML‑контент.
1. Создайте [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из потока ответа и настроенных вариантов загрузки, чтобы загруженная страница обрабатывалась с правильным базовым URL.
1. Сохраните отрисованную веб-страницу в файл PDF и автоматически закройте ресурсы потоков с помощью try-with-resources.

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

## Преобразуйте MHTML в PDF

Используйте этот пример, когда необходимо преобразовать архивный файл MHTML в документ PDF.

1. Создайте [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) экземпляр, чтобы указать Aspose.PDF загрузить источник как MIME HTML‑контент.
1. Откройте `.mht` или `.mhtml` файл, передавая его путь и параметры загрузки MHTML в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF разобрать архивированное HTML‑содержание и его встроенные ресурсы в модель документа PDF.
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


