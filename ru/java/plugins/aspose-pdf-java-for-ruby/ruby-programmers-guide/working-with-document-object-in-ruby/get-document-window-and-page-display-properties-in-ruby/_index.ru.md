---
title: Получение свойств окна документа и отображения страницы в Ruby
type: docs
weight: 40
url: /java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получение свойств окна документа и отображения страницы

Чтобы получить свойства окна документа и отображения страницы PDF-документа, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetDocumentWindow**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF-документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Получить различные свойства документа

# Позиция окна документа - По умолчанию: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Основной порядок чтения; определить позицию страницы

# при отображении рядом - По умолчанию: L2R

puts "Direction :- " + doc.getDirection().to_s

# Должна ли строка заголовка окна отображать заголовок документа.

# Если false, строка заголовка отображает имя файла PDF - По умолчанию: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Нужно ли изменять размер окна документа, чтобы он соответствовал размеру

# первой отображаемой страницы - По умолчанию: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Нужно ли скрывать строку меню приложения просмотра - По умолчанию: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Нужно ли скрывать панель инструментов приложения просмотра - По умолчанию: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Нужно ли скрывать элементы интерфейса, такие как полосы прокрутки,

# и отображать только содержимое страницы - По умолчанию: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# Макет страницы, например, одна страница, одна колонка

puts "PageLayout :-" + doc.getPageLayout().to_s

# Как документ должен отображаться при открытии.

puts "pageMode :-" + doc.getPageMode().to_s
```


## Скачать Исполняемый Код

Скачайте **Получение Свойств Окна Документа и Отображения Страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)