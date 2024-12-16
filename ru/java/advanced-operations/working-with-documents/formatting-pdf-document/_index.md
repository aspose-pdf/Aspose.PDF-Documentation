---
title: Форматирование PDF документа
linktitle: Форматирование PDF документа
type: docs
weight: 20
url: /ru/java/formatting-pdf-document/
description: Форматирование PDF документа с помощью Aspose.PDF для Java. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2021-06-05"
---

## Получение свойств окна документа и отображения страницы

Эта тема поможет вам понять, как получить свойства окна документа, приложения просмотра и как страницы отображаются.

Чтобы установить эти различные свойства, откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Теперь вы можете получить методы объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), такие как

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Центрировать окно документа на экране. По умолчанию: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Порядок чтения.
 Это определяет, как страницы располагаются при отображении рядом друг с другом. По умолчанию: слева направо.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Отображать заголовок документа на панели заголовка окна документа. По умолчанию: false (заголовок отображается).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Скрыть или отобразить строку меню окна документа. По умолчанию: false (строка меню отображается).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки. По умолчанию: false (элементы интерфейса отображаются).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – Как документ отображается, когда он не отображается в полноэкранном режиме.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – Макет страницы.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – Как документ отображается при первом открытии. Варианты: показать эскизы, полноэкранный режим, показать панель вложений.

Следующий фрагмент кода показывает, как получить свойства, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Получить различные свойства документа
    // Позиция окна документа - По умолчанию: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Основной порядок чтения; определить позицию страницы
    // при отображении рядом - По умолчанию: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Должна ли строка заголовка окна отображать заголовок документа.
    // Если false, строка заголовка отображает имя файла PDF - По умолчанию: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // Должно ли изменяться размер окна документа, чтобы соответствовать
    // размеру первой отображаемой страницы - По умолчанию: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // Должно ли скрываться меню программы просмотра - По умолчанию: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // Должно ли скрываться панель инструментов программы просмотра - По умолчанию: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // Должно ли скрываться элементы интерфейса, такие как полосы прокрутки,
    // оставляя только содержимое страницы - По умолчанию: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // Режим страницы документа. Как отображать документ при выходе
    // из полноэкранного режима.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // Макет страницы, т.е. одна страница, одна колонка
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // Как документ должен отображаться при открытии.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## Установка свойств окна документа и отображения страниц

Эта тема объясняет, как установить свойства окна документа, приложения для просмотра и отображения страниц.

Чтобы установить эти различные свойства:

1. Откройте PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Установите свойства объекта Document.
1. Сохраните обновленный PDF-файл, используя метод Save.

Доступные свойства:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

Следующий фрагмент кода показывает, как установить свойства, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // Установить различные свойства документа
    // указать позиционирование окна документа - По умолчанию: false
    pdfDocument.setCenterWindow(true);
    
    // Основной порядок чтения; определить положение страницы
    // при отображении бок о бок - По умолчанию: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // Указать, должен ли заголовок окна отображать заголовок документа
    // если false, заголовок окна отображает имя PDF файла - По умолчанию: false
    pdfDocument.setDisplayDocTitle(true);
    
    // Указать, нужно ли изменять размер окна документа
    // чтобы соответствовать размеру первой отображаемой страницы - По умолчанию: false
    pdfDocument.setFitWindow(true);
    
    // Указать, нужно ли скрыть строку меню приложения просмотра - По умолчанию:
    // false
    pdfDocument.setHideMenubar(true);
    
    // Указать, нужно ли скрыть панель инструментов приложения просмотра - По умолчанию:
    // false
    pdfDocument.setHideToolBar(true);
    
    // Указать, нужно ли скрыть элементы пользовательского интерфейса, такие как полосы прокрутки
    // и оставить только содержимое страницы - По умолчанию: false
    pdfDocument.setHideWindowUI(true);
    
    // Режим страницы документа. указать, как отображать документ при выходе
    // из полноэкранного режима.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // Указать макет страницы, например, одна страница, одна колонка
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // Указать, как документ должен отображаться при открытии
    // например, показывать миниатюры, полноэкранный режим, показывать панель вложений
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // Сохранить обновленный PDF файл
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## Встраивание шрифтов в существующий PDF файл

PDF ридеры поддерживают [основные 14 шрифтов](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts), чтобы документы отображались одинаково независимо от платформы, на которой они отображаются. Когда PDF содержит шрифт, который не входит в основные шрифты, встраивайте шрифт, чтобы избежать замены шрифта.

Aspose.PDF for Java поддерживает встраивание шрифтов в существующие PDF документы. Вы можете встроить как весь шрифт, так и его подмножество. Чтобы встроить шрифт:

1. Откройте существующий PDF файл, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Используйте класс [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) для встраивания шрифта.
   1. Метод setEmbedded(true) встраивает полный шрифт.
   2. Метод pageFont.isSubset(true) встраивает подмножество шрифта.

Подмножество шрифта встраивает только используемые символы и полезно, когда шрифты используются для коротких предложений или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста.
 Уменьшение подмножества уменьшает размер файла выходного PDF.

Однако, если для основного текста используется пользовательский шрифт, внедрите его полностью.

Следующий фрагмент кода показывает, как внедрить шрифт в файл PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Перебрать все страницы
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Проверить, встраивается ли шрифт
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Проверить объекты форм
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Проверить, встраивается ли шрифт
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Сохранить обновленный PDF файл
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Встраивание шрифтов при создании PDF

Если вам нужно использовать любой шрифт, кроме 14 основных шрифтов, поддерживаемых Adobe Reader, то вы должны встроить описание шрифта при генерации PDF-файла. Если информация о шрифте не встроена, Adobe Reader возьмет её из операционной системы, если она установлена на системе, или он создаст заменяющий шрифт в соответствии с дескриптором шрифта в PDF. Обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт ‘Univers Condensed’ установлен в системе.

Мы используем свойство setEmbedded класса [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) для встраивания информации о шрифте в PDF-файл. Установка значения этого свойства в ‘true’ встроит полный файл шрифта в PDF, зная, что это увеличит размер PDF-файла. Ниже приведен фрагмент кода, который можно использовать для встраивания информации о шрифте в PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Создать объект PDF, вызвав его пустой конструктор
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Создать секцию в объекте Pdf
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" Это пример текста с использованием пользовательского шрифта.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Сохранить обновленный PDF-файл
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Установить имя шрифта по умолчанию при сохранении PDF

Когда PDF-документ содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты на шрифт по умолчанию. Когда шрифт доступен (установлен на устройстве или встроен в документ), в выходном PDF должен использоваться тот же шрифт (не должен заменяться на шрифт по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (а не путь к файлам шрифта). Мы реализовали функцию для установки имени шрифта по умолчанию при сохранении документа как PDF. Следующий фрагмент кода может быть использован для установки шрифта по умолчанию:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Загрузить существующий PDF-документ
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Инициализировать параметры сохранения для формата PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // Установить имя шрифта по умолчанию
    ops.setDefaultFontName(newName);

    // Сохранить PDF-файл
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## Получить все шрифты из PDF-документа

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод **Document.getFontUtilities().getAllFonts()**, предоставляемый классом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы получить все шрифты из существующего PDF-документа:

```java
public static void GetAllFontsFromPDFDocument() {

    // Загрузить существующий PDF-документ
    Document document = new Document(_dataDir + "sample.pdf");

    // Получить все шрифты из документа
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## Получить-установить коэффициент масштабирования PDF-файла

Иногда вам может понадобиться установить или получить коэффициент масштабирования PDF-документа. Вы можете легко выполнить это требование с помощью Aspose.PDF.

Объект [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) позволяет получить значение масштабирования, связанное с PDF-файлом.
 Similarly, it can be used to set a file's Zoom factor.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Загрузить существующий PDF документ
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // установка коэффициента масштабирования документа
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // установка действия для подгонки по ширине страницы
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // установка действия для подгонки по высоте страницы
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // Создать новый объект Document
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Создать объект GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Получить коэффициент масштабирования PDF файла
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Сохранить обновленный PDF файл
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```