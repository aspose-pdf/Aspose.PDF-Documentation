---
title: Преобразование HTML в PDF в Java
linktitle: Конвертировать HTML в PDF-файл
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать HTML, MHTML и веб-страницы в PDF на Java с помощью Aspose.PDF, включая настройки мультимедиа, правила страниц CSS, встраивание шрифтов, содержимое SVG и одностраничный вывод.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать HTML в PDF в Java с помощью Aspose.PDF
Abstract: В этой статье объясняется, как конвертировать файлы HTML и MHTML в PDF с помощью Aspose.PDF для Java. В нем рассматривается базовый рабочий процесс преобразования HTML в PDF и показано, как управлять рендерингом с помощью типов мультимедиа, приоритета правил страницы CSS, встроенных шрифтов, содержимого SVG, одностраничного вывода и прямого преобразования с активной веб-страницы.
---
Aspose.PDF для Java может конвертировать локальные файлы HTML, архивированный контент MHTML и живые веб-страницы в документы PDF. Вы можете управлять конвейером преобразования с помощью `HtmlLoadOptions` и `MhtLoadOptions`, чтобы влиять на масштабирование макета, обработку мультимедиа CSS, приоритет правил страниц, встраивание шрифтов, разрешение ресурсов и поведение отрисовки одной страницы.

## Конвертировать HTML в PDF

Используйте этот пример, когда локальный файл HTML необходимо преобразовать непосредственно в документ PDF.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/), чтобы настроить интерпретацию источника HTML во время импорта.
1. Установите для параметра [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) значение `ScaleToPageWidth`, чтобы широкое HTML-содержимое масштабировалось до ширины целевой страницы PDF, а не обрезалось.
1. Откройте исходный HTML-файл, передав его путь и настроенные параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните созданный [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в виде PDF-файла по целевому пути вывода.

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

## Преобразование HTML в PDF с параметрами типа носителя

Используйте этот пример, когда во время преобразования HTML необходимо контролировать обработку медиа-типа CSS.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) для настроек преобразования.
1. Установите для параметра [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) значение `Screen`, если HTML должен отображаться с использованием правил CSS, предназначенных для отображения на экране, а не для печати.
1. Откройте HTML-файл с настроенными параметрами загрузки, чтобы во время преобразования применялись стили, зависящие от медиа-запроса.
1. Сохраните полученный результат [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в формате PDF.

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

## Преобразование HTML в PDF с приоритетом правил страниц CSS

Используйте этот пример, когда правила CSS `@page` должны влиять на окончательный макет страницы PDF.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) перед открытием HTML-файла.
1. Настройте `setPriorityCssPageRule(false)`, когда другие параметры макета должны иметь приоритет над объявлениями CSS `@page` в исходной разметке.
1. Загрузите содержимое HTML в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с настроенными параметрами, чтобы макет страницы был разрешен во время импорта.
1. Сохраните созданный PDF-файл.

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

Используйте этот пример, когда выходной PDF-файл должен сохранить шрифты HTML путем их внедрения.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) для конфигурации импорта HTML.
1. Включите `setEmbedFonts(true)`, чтобы шрифты, разрешенные во время рендеринга HTML, сохранялись в выходном PDF-файле.
1. Откройте исходный HTML-код с этими параметрами загрузки, чтобы сохранить исходную типографику в конечном документе.
1. Сохраните [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в формате PDF с включенными ресурсами встроенных шрифтов.

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

## Рендеринг HTML-контента на одной странице PDF

Используйте этот пример, когда длинный HTML-контент должен храниться на одной странице PDF, а не перемещаться по нескольким страницам.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) для настроек преобразования.
1. Включите `setRenderToSinglePage(true)`, чтобы импортированный HTML-код размещался на одной странице PDF, а не разбивался на несколько страниц.
1. Откройте исходный HTML с настроенными параметрами загрузки и позвольте Aspose.PDF построить макет страницы в виде [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните выходной PDF-файл.

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

## Преобразование HTML, содержащего встроенный SVG

Используйте этот пример, когда источник HTML включает встроенные данные SVG, которые необходимо отобразить в PDF.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) с родительским каталогом HTML-файла в качестве базового пути, чтобы связанные ресурсы можно было последовательно разрешать во время преобразования.
1. Откройте HTML-файл, содержащий встроенную разметку SVG, передав исходный путь и параметры загрузки в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF визуализировать HTML DOM вместе со встроенными элементами SVG в содержимое страницы PDF.
1. Сохраните созданный PDF-документ.

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

Используйте этот пример, когда URL-адрес действующего веб-сайта необходимо отобразить и сохранить в виде PDF-документа.

1. Создайте экземпляр [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) с целевым URL-адресом, чтобы относительные ресурсы, такие как таблицы стилей и изображения, можно было разрешить по этому адресу.
1. Преобразуйте строку URL-адреса в объект `URL` и откройте его входной поток, чтобы получить живой HTML-контент.
1. Создайте [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из потока ответов и настроенных параметров загрузки, чтобы загруженная страница обрабатывалась с правильным базовым URL-адресом.
1. Сохраните обработанную веб-страницу в формате PDF и автоматически закройте ресурсы потока с помощью try-with-resources.

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

## Конвертировать MHTML в PDF

Используйте этот пример, когда архивный файл MHTML необходимо преобразовать в документ PDF.

1. Создайте экземпляр [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/), чтобы указать Aspose.PDF загрузить источник как HTML-контент MIME.
1. Откройте файл `.mht` или `.mhtml`, передав его путь и параметры загрузки MHTML в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF проанализировать заархивированное HTML-содержимое и встроенные ресурсы в модель PDF-документа.
1. Сохраните созданный PDF-файл.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
