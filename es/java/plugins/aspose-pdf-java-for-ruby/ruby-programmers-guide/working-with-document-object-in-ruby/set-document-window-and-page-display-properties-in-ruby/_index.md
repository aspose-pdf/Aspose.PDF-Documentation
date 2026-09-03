---
title: Establecer propiedades de la ventana del documento y de visualización de página en Ruby
linktitle: Establecer propiedades de la ventana del documento y de visualización de página en Ruby
type: docs
weight: 100
url: /es/java/set-document-window-and-page-display-properties-in-ruby/
description: Personalizar la configuración de visualización del documento y de la página en PDFs usando Ruby y Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Establecer propiedades de la ventana del documento y de visualización de página

Para establecer las propiedades de la ventana del documento y de visualización de página del documento Pdf usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **SetDocumentWindow**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Set different document properties

# Position of document's window - Default: false

doc.setCenterWindow(true)

# Predominant reading order; determine the position of page

# when displayed side by side - Default: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Whether window's title bar should display document title.

# If false, title bar displays PDF file name - Default: false

doc.setDisplayDocTitle(true)

# Whether to resize the document's window to fit the size of

# first displayed page - Default: false

doc.setFitWindow(true)

# Whether to hide menu bar of the viewer application - Default: false

doc.setHideMenubar(true)

# Whether to hide tool bar of the viewer application - Default: false

doc.setHideToolBar(true)

# Whether to hide UI elements like scroll bars

# and leaving only the page contents displayed - Default: false

doc.setHideWindowUI(true)

# The document's page mode. How to display document on exiting full-screen mode.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# The page layout i.e. single page, one column

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# How the document should display when opened.

doc.setPageMode()

# Save updated PDF file

doc.save(data_dir + "Set Document Window.pdf")
```

## Descargar Código en Ejecución

DescargarВ **Establecer ventana del documento y propiedades de visualización de página (Aspose.PDF)**В deВ cualquiera de los sitios de código social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
