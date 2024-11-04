---
title: Establecer propiedades de ventana de documento y visualización de página en Ruby
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Establecer propiedades de ventana de documento y visualización de página

Para establecer las propiedades de ventana de documento y visualización de página de un documento Pdf utilizando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SetDocumentWindow**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Establecer diferentes propiedades del documento

# Posición de la ventana del documento - Predeterminado: false

doc.setCenterWindow(true)

# Orden de lectura predominante; determinar la posición de la página

# cuando se muestra lado a lado - Predeterminado: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Si la barra de título de la ventana debe mostrar el título del documento.

# Si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false

doc.setDisplayDocTitle(true)

# Si redimensionar la ventana del documento para ajustar el tamaño de

# la primera página mostrada - Predeterminado: false

doc.setFitWindow(true)

# Si ocultar la barra de menú de la aplicación del visor - Predeterminado: false

doc.setHideMenubar(true)

# Si ocultar la barra de herramientas de la aplicación del visor - Predeterminado: false

doc.setHideToolBar(true)

# Si ocultar elementos de la UI como barras de desplazamiento

# y dejar solo el contenido de la página mostrado - Predeterminado: false

doc.setHideWindowUI(true)

# El modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# El diseño de página, es decir, una sola página, una columna

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# Cómo debe mostrarse el documento al abrirse.

doc.setPageMode()

# Guardar archivo PDF actualizado

doc.save(data_dir + "Set Document Window.pdf")
```


## Descargar Código en Ejecución

Descargar **Establecer Propiedades de Ventana de Documento y Visualización de Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)