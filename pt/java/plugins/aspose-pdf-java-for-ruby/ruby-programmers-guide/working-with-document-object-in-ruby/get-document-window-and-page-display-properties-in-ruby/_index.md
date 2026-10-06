---
title: Obter propriedades da janela de documento e exibição de página em Ruby
linktitle: Obter propriedades da janela de documento e exibição de página em Ruby
type: docs
weight: 40
url: /pt/java/get-document-window-and-page-display-properties-in-ruby/
description: Recuperar e personalizar propriedades da janela de documento e exibição de página em arquivos PDF usando Ruby e Aspose.PDF.
lastmod: "2026-10-06"
---
## Aspose.PDF - obter propriedades da janela de documento e exibição de página

Para obter propriedades da janela de documento e exibição de página de um documento Pdf usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **GetDocumentWindow**.

Código Ruby

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

## Baixar o exemplo de código

Download **Obtenha Propriedades da Janela do Documento e da Exibição da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)
