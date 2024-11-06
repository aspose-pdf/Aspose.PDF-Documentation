---
title: Получение Свойств Окна Документа и Отображения Страницы в PHP
type: docs
weight: 30
url: ru/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получение Свойств Окна Документа и Отображения Страницы

Чтобы получить свойства окна документа и отображения страницы PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **GetDocumentWindow**.

Код PHP

```php

# Открыть PDF-документ.
$doc = new Document($dataDir . "input1.pdf");

# Получить различные свойства документа
# Положение окна документа - По умолчанию: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Основной порядок чтения; определяет положение страницы
# при отображении рядом - По умолчанию: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Должна ли строка заголовка окна отображать заголовок документа.
# Если false, строка заголовка отображает имя PDF файла - По умолчанию: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# Должно ли изменяться размер окна документа, чтобы соответствовать размеру
# первой отображаемой страницы - По умолчанию: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Должно ли скрываться меню приложения просмотра - По умолчанию: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Должно ли скрываться панель инструментов приложения просмотра - По умолчанию: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Должны ли скрываться элементы интерфейса, такие как полосы прокрутки
# и оставлять только содержимое страницы - По умолчанию: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# Макет страницы, т.е. одна страница, одна колонка
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# Как документ должен отображаться при открытии.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Скачать Рабочий Код**

Скачайте **Получить Свойства Окна Документа и Отображения Страницы (Aspose.PDF)** с любого из ниже перечисленных социальных платформ для кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)