---
title: Obtener Propiedades de Ventana de Documento y Visualización de Página en Ruby
type: docs
weight: 40
url: /es/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Propiedades de Ventana de Documento y Visualización de Página

Para obtener las propiedades de ventana de documento y visualización de página de un documento Pdf utilizando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **GetDocumentWindow**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtener diferentes propiedades del documento

# Posición de la ventana del documento - Predeterminado: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Orden de lectura predominante; determina la posición de la página

# cuando se muestra lado a lado - Predeterminado: L2R

puts "Direction :- " + doc.getDirection().to_s

# Si la barra de título de la ventana debería mostrar el título del documento.

# Si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Si redimensionar la ventana del documento para ajustar el tamaño de

# la primera página mostrada - Predeterminado: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Si ocultar la barra de menú de la aplicación del visor - Predeterminado: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Si ocultar la barra de herramientas de la aplicación del visor - Predeterminado: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Si ocultar elementos de la interfaz de usuario como barras de desplazamiento

# y dejar solo el contenido de la página mostrado - Predeterminado: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# El modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# La disposición de la página, es decir, página única, una columna

puts "PageLayout :-" + doc.getPageLayout().to_s

# Cómo debería mostrarse el documento cuando se abre.

puts "pageMode :-" + doc.getPageMode().to_s
```


## Descargar Código en Ejecución

Descargar **Obtener Propiedades de Ventana de Documento y Visualización de Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)