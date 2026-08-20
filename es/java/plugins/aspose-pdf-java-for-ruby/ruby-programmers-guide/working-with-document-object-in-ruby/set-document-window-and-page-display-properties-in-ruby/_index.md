---
title: Establecer propiedades de visualización de página y ventana de documento en Ruby
linktitle: Establecer propiedades de visualización de página y ventana de documento en Ruby
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
description: Personalice la configuración de visualización de páginas y documentos en archivos PDF utilizando Ruby y Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Establecer propiedades de visualización de página y ventana de documento



Para configurar la ventana del documento y las propiedades de visualización de página del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SetDocumentWindow**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Establecer propiedades de visualización de página y ventana del documento (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
