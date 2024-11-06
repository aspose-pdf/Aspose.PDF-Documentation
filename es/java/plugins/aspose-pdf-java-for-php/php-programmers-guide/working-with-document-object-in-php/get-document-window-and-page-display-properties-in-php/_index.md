---
title: Obtener Propiedades de Ventana de Documento y Visualización de Página en PHP
type: docs
weight: 30
url: es/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Propiedades de Ventana de Documento y Visualización de Página

Para obtener las Propiedades de Ventana de Documento y Visualización de Página del documento Pdf utilizando **Aspose.PDF Java para PHP**, simplemente invoca la clase **GetDocumentWindow**.

Código PHP

```php

# Abrir un documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtener diferentes propiedades del documento
# Posición de la ventana del documento - Predeterminado: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Orden de lectura predominante; determina la posición de la página
# cuando se muestra lado a lado - Predeterminado: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Si la barra de título de la ventana debe mostrar el título del documento.
# Si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# Si se debe cambiar el tamaño de la ventana del documento para ajustarse al tamaño de
# la primera página mostrada - Predeterminado: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Si se debe ocultar la barra de menú de la aplicación de visualización - Predeterminado: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Si se debe ocultar la barra de herramientas de la aplicación de visualización - Predeterminado: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Si se deben ocultar elementos de la interfaz de usuario como barras de desplazamiento
# dejando solo el contenido de la página mostrado - Predeterminado: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# El modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# El diseño de la página, es decir, página única, una columna
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# Cómo se debe mostrar el documento al abrirlo.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Descargar Código en Ejecución**

Descargar **Obtener Propiedades de Ventana de Documento y Visualización de Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)