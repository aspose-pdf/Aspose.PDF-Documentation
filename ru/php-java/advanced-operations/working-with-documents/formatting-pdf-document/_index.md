---
title: Форматирование PDF документа 
linktitle: Форматирование PDF документа
type: docs
weight: 20
url: ru/php-java/formatting-pdf-document/
description: Форматируйте PDF документ с помощью Aspose.PDF для PHP через Java. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2024-06-05"
---

## Получение свойств окна документа и отображения страницы

Эта тема поможет вам понять, как получить свойства окна документа, приложения для просмотра и как отображаются страницы.

Чтобы установить эти различные свойства, откройте PDF файл, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Теперь вы можете получить методы объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), такие как

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Центрировать окно документа на экране. По умолчанию: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Порядок чтения.
 Это определяет, как страницы располагаются при отображении рядом друг с другом. По умолчанию: слева направо.  
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Отображать заголовок документа в строке заголовка окна документа. По умолчанию: false (заголовок отображается).  
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – Получает флаг, указывающий, следует ли скрывать строку меню, когда документ активен.  
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – Получает флаг, указывающий, следует ли скрывать панель инструментов, когда документ активен.  
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – Получает флаг, указывающий, должны ли элементы пользовательского интерфейса быть скрыты, когда документ активен.  

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – Получает режим страницы, указывающий, как отображать документ при выходе из полноэкранного режима.  - [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – Макет страницы.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – Получает режим страницы, указывая, как документ должен отображаться при открытии.

Следующий фрагмент кода показывает, как получить свойства, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // Открыть документ
    $document = new Document($inputFile);

    // Получить различные свойства документа
    // Позиция окна документа - По умолчанию: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Основной порядок чтения; определяет позицию страницы
    // при отображении рядом - По умолчанию: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Должна ли строка заголовка окна отображать заголовок документа.
    // Если false, строка заголовка отображает имя PDF файла - По умолчанию: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Нужно ли изменять размер окна документа, чтобы он соответствовал размеру
    // первой отображаемой страницы - По умолчанию: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Нужно ли скрыть строку меню в приложении для просмотра - По умолчанию: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Нужно ли скрыть панель инструментов в приложении для просмотра - По умолчанию: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Нужно ли скрыть элементы пользовательского интерфейса, такие как полосы прокрутки,
    // оставляя отображенным только содержимое страницы - По умолчанию: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // Режим страницы документа. Как отображать документ при выходе
    // из полноэкранного режима.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // Макет страницы, например, одна страница, одна колонка
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // Как должен отображаться документ при открытии.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## Установка свойств окна документа и отображения страницы

Эта тема объясняет, как установить свойства окна документа, приложения для просмотра и отображения страницы.

Чтобы установить эти различные свойства:

1. Откройте PDF-файл с использованием класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Установите свойства объекта Document.
3. Сохраните обновленный PDF-файл с использованием метода Save.

Доступные методы:

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

```php

    // Открыть документ
    $document = new Document($inputFile);
    // Установить различные свойства документа
    // указать, чтобы окно документа было позиционировано - По умолчанию: false
    $document->setCenterWindow(true);
    // Основной порядок чтения; определить положение страницы
    // при отображении рядом - По умолчанию: L2R
    $document->setDirection(Direction::$R2L);
    // Указать, следует ли отображать заголовок документа в строке заголовка окна
    // если false, строка заголовка отображает имя PDF файла - По умолчанию: false
    $document->setDisplayDocTitle(true);
    // Указать, следует ли изменять размер окна документа для соответствия размеру
    // первой отображаемой страницы - По умолчанию: false
    $document->setFitWindow(true);
    // Указать, следует ли скрывать строку меню приложения просмотра - По умолчанию:
    // false
    $document->setHideMenubar(true);
    // Указать, следует ли скрывать панель инструментов приложения просмотра - По умолчанию:
    // false
    $document->setHideToolBar(true);
    // Указать, следует ли скрывать элементы интерфейса, такие как полосы прокрутки
    // оставляя только содержимое страницы - По умолчанию: false
    $document->setHideWindowUI(true);
    // Режим страницы документа. указать, как отображать документ при выходе из
    // полноэкранного режима.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Указать макет страницы, т.е. одна страница, одна колонка
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Указать, как документ должен отображаться при открытии
    // т.е. показать миниатюры, полноэкранный режим, показать панель вложений
    $document->setPageMode(PageMode::$UseThumbs);
    // Сохранить обновленный PDF файл
    $document->save($outputFile);
    $document->close();

```


## Встраивание шрифтов в существующий PDF файл

PDF-ридеры поддерживают [основные 14 шрифтов](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts), чтобы документы отображались одинаково независимо от платформы, на которой документ отображается. Когда PDF содержит шрифт, который находится вне основных шрифтов, встраивайте шрифт, чтобы избежать замены шрифта.

Aspose.PDF для PHP через Java поддерживает встраивание шрифтов в существующие PDF-документы. Вы можете встроить полный шрифт или его часть. Чтобы встроить шрифт:

1. Откройте существующий PDF-файл с использованием класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Используйте класс [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) для встраивания шрифта.
   1. Метод setEmbedded(true) встраивает полный шрифт.
   1. Метод [isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) встраивает часть шрифта.

Частичное встраивание шрифта включает только те символы, которые используются, и полезно, когда шрифты используются для коротких предложений или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста.
 Использование подмножества уменьшает размер выходного PDF-файла.

Однако, если для основного текста используется пользовательский шрифт, встроите его полностью.

Следующий фрагмент кода показывает, как встроить шрифт в PDF-файл.

```php

    // Открыть документ
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // Проверить, встроен ли шрифт
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Проверить объекты формы
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // Проверить, встроен ли шрифт
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // Сохранить обновленный PDF-файл
    $document->save($outputFile);
    $document->close();
```

## Встраивание шрифтов при создании PDF

Если вам нужно использовать любой шрифт, кроме 14 основных шрифтов, поддерживаемых Adobe Reader, то вы должны встроить описание шрифта при создании PDF файла. Если информация о шрифте не встроена, Adobe Reader возьмет ее из операционной системы, если она установлена в системе, или создаст заменяющий шрифт в соответствии с дескриптором шрифта в PDF. Обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт 'Univers Condensed' установлен в системе.

Мы используем свойство setEmbedded класса [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) для встраивания информации о шрифте в PDF файл. Установка значения этого свойства в ‘true’ встроит полный файл шрифта в PDF, зная, что это увеличит размер PDF файла. Ниже приведен фрагмент кода, который можно использовать для встраивания информации о шрифте в PDF.

```php

    // Создать объект PDF, вызвав его пустой конструктор
    $document = new Document();

    // Создать секцию в объекте Pdf
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("Это пример текста с использованием пользовательского шрифта.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // Сохранить обновленный PDF файл
    $document->save($outputFile);
    $document->close();
```


## Установить имя шрифта по умолчанию при сохранении PDF

Когда PDF-документ содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты шрифтом по умолчанию. Когда шрифт доступен (установлен на устройстве или встроен в документ), выходной PDF должен содержать тот же шрифт (не должен заменяться шрифтом по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (не путь к файлам шрифтов). Мы реализовали функцию для установки имени шрифта по умолчанию при сохранении документа в формате PDF. Следующий фрагмент кода можно использовать для установки шрифта по умолчанию:

```php

    // Загрузить существующий PDF-документ
    $document = new Document($inputFile);
    $newName = "Arial";

    // Инициализировать параметры сохранения для формата PDF
    $ops = new PdfSaveOptions();

    // Установить имя шрифта по умолчанию
    $ops->setDefaultFontName($newName);

    // Сохранить PDF-файл
    $document->save($outputFile, $ops);
    // Закрыть обновленный PDF-файл
    $document->close();
```

## Получить все шрифты из PDF-документа

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод **Document.getFontUtilities().getAllFonts()**, предоставленный в классе [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF документа:

```php

    // Загрузить существующий PDF документ
    $document = new Document($inputFile);

    // Получить все шрифты из документа
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Сохранить обновленный PDF файл
    $document->close();
```

## Получение и установка коэффициента масштабирования PDF файла

Иногда требуется установить или получить коэффициент масштабирования PDF документа. Вы можете легко выполнить это требование с помощью Aspose.PDF.

Объект [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) позволяет получить значение масштабирования, связанное с PDF файлом. Аналогично, он может быть использован для установки коэффициента масштабирования файла.

```php

    // Загрузить существующий PDF документ
    $document = new Document($inputFile);

    // Создать объект GoToAction
    $action = $document->getOpenAction();

    // Получить коэффициент масштабирования PDF файла
    $responseData = $action->getDestination()->getZoom();

    // Сохранить обновленный PDF файл
    $document->close();  
```

Следующий фрагмент кода показывает, как получить коэффициент масштабирования PDF-файла.

```php

    // Загрузить существующий PDF-документ
    $document = new Document($inputFile);
    $zoom = 0.5;
    // установка коэффициента масштабирования документа
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // установка действия для подгонки по ширине страницы
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // установка действия для подгонки по высоте страницы
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Сохранить обновленный PDF-файл
    $document->save($outputFile);
    $document->close();  
```