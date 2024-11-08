---
title: Установка свойств окна документа и отображения страницы в Ruby
type: docs
weight: 100
url: /ru/java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Установка свойств окна документа и отображения страницы

Чтобы установить свойства окна документа и отображения страницы PDF-документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **SetDocumentWindow**.

Ruby Code

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF-документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Установить различные свойства документа

# Положение окна документа - По умолчанию: false

doc.setCenterWindow(true)

# Основной порядок чтения; определяет положение страницы

# при отображении рядом - По умолчанию: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Должен ли заголовок окна отображать заголовок документа.

# Если false, заголовок окна отображает имя PDF-файла - По умолчанию: false

doc.setDisplayDocTitle(true)

# Должно ли окно документа изменяться по размеру для подгонки

# под размер первой отображаемой страницы - По умолчанию: false

doc.setFitWindow(true)

# Должно ли скрываться меню приложения просмотра - По умолчанию: false

doc.setHideMenubar(true)

# Должно ли скрываться панель инструментов приложения просмотра - По умолчанию: false

doc.setHideToolBar(true)

# Должны ли скрываться элементы UI, такие как полосы прокрутки

# и оставаться только содержимое страницы - По умолчанию: false

doc.setHideWindowUI(true)

# Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# Макет страницы, т.е. одна страница, одна колонка

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# Как документ должен отображаться при открытии.

doc.setPageMode()

# Сохранить обновленный PDF-файл

doc.save(data_dir + "Set Document Window.pdf")
```


## Download Running Code

Скачайте **Set Document Window and Page Display Properties (Aspose.PDF)** с любого из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)