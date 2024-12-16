---
title: Обработка PDF документа 
linktitle: Обработка PDF документа
type: docs
weight: 30
url: /ru/php-java/manipulate-pdf-document/
description: Эта статья содержит информацию о том, как проверить PDF документ на соответствие стандарту PDF A, как работать с ОГС, как установить срок действия PDF, и как определить прогресс генерации PDF файла.
lastmod: "2024-06-05"
---

## Проверка PDF документа на соответствие стандарту PDF A (A 1A и A 1B)

Чтобы проверить PDF документ на совместимость с PDF/A-1a или PDF/A-1b, используйте метод [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Этот метод позволяет указать имя файла, в котором будет сохранен результат, и требуемый тип валидации из перечисления [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A или PDF_A_1B.

Формат выходного XML является пользовательским форматом Aspose.
 The XML содержит коллекцию тегов с именем Problem; каждый тег содержит детали конкретной проблемы. Атрибут ObjectID тега Problem представляет ID конкретного объекта, с которым связана данная проблема. Атрибут Clause представляет соответствующее правило в спецификации PDF.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Проверить PDF на соответствие PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Работа с оглавлением

### Добавление оглавления в существующий PDF

Чтобы добавить оглавление в существующий PDF файл, используйте класс [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) в пакете com.aspose.pdf. Пакет com.aspose.pdf может как создавать новые, так и изменять существующие PDF файлы. Чтобы добавить оглавление в существующий PDF, используйте пакет com.aspose.pdf.

Этот фрагмент кода PHP использует Aspose.PDF для добавления оглавления (TOC) в существующий PDF документ:

```php
    // Открыть документ
    $document = new Document($inputFile);

    // Получить доступ к первой странице PDF файла
    $tocPage = $document->getPages()->insert(1);

    // Создать объект для представления информации об оглавлении
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Установить заголовок для оглавления
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Создать строковые объекты, которые будут использоваться как элементы оглавления
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Создать объект Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Указать целевую страницу для объекта heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Целевая страница
        $heading2->setTop($page->getRect()->getHeight());

        // Координата назначения
        $segment2->setText($titles[$i]);

        // Добавить заголовок на страницу, содержащую оглавление
        $tocPage->getParagraphs()->add($heading2);
    }
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

### Установить разные TabLeaderType для разных уровней TOC

Aspose.PDF также позволяет устанавливать разные TabLeaderType для разных уровней TOC. Вам нужно установить свойство LineDash FormatArray с соответствующим значением перечисления TabLeaderType следующим образом.

```php
    // Открыть документ
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // установить LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Добавить раздел списка в коллекцию разделов PDF документа
    $tocPage->setTocInfo($tocInfo);

    // Определите формат списка четырех уровней, установив левый отступ и
    // настройки формата текста для каждого уровня
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Создать раздел в PDF документе
    $page = $document->getPages()->add();

    // Добавить четыре заголовка в разделе
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Sample Heading" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Добавить заголовок в таблицу содержания.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```


### Скрыть номера страниц в оглавлении

В случае, если вы не хотите отображать номера страниц вместе с заголовками в оглавлении, вы можете использовать свойство [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) класса [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) как false. Пожалуйста, проверьте следующий фрагмент кода, чтобы скрыть номера страниц в содержании:

```php
    // Открыть документ
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Создать объект для представления информации о содержании
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Установить заголовок для оглавления
    $tocInfo->setTitle($title);

    // Добавить раздел списка в коллекцию разделов документа Pdf
    $tocPage->setTocInfo($tocInfo);

    // Определить формат списка из четырех уровней, установив отступы слева и
    // настройки формата текста каждого уровня

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Добавить четыре заголовка в раздел
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("this is heading of level " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```


### Настройка номеров страниц при добавлении оглавления

Часто требуется настроить нумерацию страниц в оглавлении при добавлении оглавления в документ PDF. Например, может потребоваться добавить некоторый префикс перед номером страницы, такой как P1, P2, P3 и так далее. В таком случае Aspose.PDF для PHP через Java предоставляет свойство PageNumbersPrefix класса TocInfo, которое можно использовать для настройки номеров страниц, как показано в следующем примере кода.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить доступ к первой странице PDF файла
    $tocPage = $document->getPages()->insert(1);

    // Создать объект для представления информации об оглавлении
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Установить заголовок для оглавления
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Создать строковые объекты, которые будут использованы как элементы оглавления
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Создать объект заголовка
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Указать целевую страницу для объекта заголовка
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Целевая страница
        $heading2->setTop($page->getRect()->getHeight());

        // Целевая координата
        $segment2->setText($titles[$i]);

        // Добавить заголовок на страницу, содержащую оглавление
        $tocPage->getParagraphs()->add($heading2);
    }
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```


## Добавление слоев в PDF файл

Слои могут использоваться в PDF документах разными способами. У вас может быть многоязычный файл, который вы хотите распространить, и хотите, чтобы текст на каждом языке отображался на разных слоях, а дизайн фона появлялся на отдельном слое. Вы также можете создавать документы с анимацией, которая появляется на отдельном слое. Один из примеров может быть добавление лицензионного соглашения к вашему файлу, и вы не хотите, чтобы пользователь просматривал содержимое, пока он не согласится с условиями соглашения.

Aspose.PDF для PHP через Java поддерживает добавление слоев в PDF файлы.

Чтобы работать со слоями в PDF файлах, используйте следующие члены API.

Класс [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) представляет собой слой и содержит следующие свойства:

- **Name** – имя слоя.
- **Id** – идентификатор слоя.
- **Contents** – список операторов слоя.

После того как объекты [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) были определены, добавьте их в коллекцию слоев объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Код ниже показывает, как добавить слои в PDF документ.

```php
    // Открыть документ
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Красная линия");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Зеленая линия");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Синяя линия");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Установить срок действия PDF

Функция истечения срока действия PDF устанавливает, как долго PDF-файл будет действительным. В определенный день, если кто-то попытается получить к нему доступ, появится всплывающее окно с объяснением, что файл устарел и им нужен новый.

Aspose.PDF позволяет установить срок действия при создании и редактировании PDF-файлов.

Пример кода ниже показывает, как установить дату истечения срока действия для PDF-файла. Вам нужно использовать JavaScript, так как файлы, сохраненные сторонними компонентами (например, OwnerGuard), не могут быть просмотрены на других рабочих станциях без этой утилиты.

PDF-файл может быть создан с использованием PDF OwnerGuard, используя существующий файл с указанной датой истечения срока. Но новый файл может быть открыт только на рабочей станции, где установлен PDF OwnerGuard. Рабочие станции без PDF OwnerGuard выдадут ExpirationFeatureError. Например, PDF Reader откроет файл, если OwnerGuard установлен, но Adobe Acrobat вернет ошибку.

```php

    // Открыть документ
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('Файл устарел. Вам нужен новый.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```