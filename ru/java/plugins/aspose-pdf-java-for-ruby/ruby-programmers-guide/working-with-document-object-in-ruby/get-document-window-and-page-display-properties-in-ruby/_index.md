---
title: Получить свойства окна документа и отображения страниц в Ruby
linktitle: Получить свойства окна документа и отображения страниц в Ruby
type: docs
weight: 40
url: /ru/java/get-document-window-and-page-display-properties-in-ruby/
description: Извлекать и настраивать свойства окна документа и отображения страниц в PDF‑файлах с использованием Ruby и Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF — Получить свойства окна документа и отображения страниц

Чтобы получить свойства окна документа и отображения страниц PDF‑документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetDocumentWindow**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get different document properties

# Position of document's window - Default: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Predominant reading order; determine the position of page

# when displayed side by side - Default: L2R

puts "Direction :- " + doc.getDirection().to_s

# Whether window's title bar should display document title.

# If false, title bar displays PDF file name - Default: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Whether to resize the document's window to fit the size of

# first displayed page - Default: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Whether to hide menu bar of the viewer application - Default: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Whether to hide tool bar of the viewer application - Default: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Whether to hide UI elements like scroll bars

# and leaving only the page contents displayed - Default: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# The document's page mode. How to display document on exiting full-screen mode.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# The page layout i.e. single page, one column

puts "PageLayout :-" + doc.getPageLayout().to_s

# How the document should display when opened.

puts "pageMode :-" + doc.getPageMode().to_s
```

## Скачать работающий код

СкачатьВ **Get Document Window and Page Display Properties (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)


