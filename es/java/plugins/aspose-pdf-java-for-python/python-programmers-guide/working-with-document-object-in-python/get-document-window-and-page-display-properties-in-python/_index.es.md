---
title: Obtener Propiedades de Ventana de Documento y Visualización de Página en Python
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

Para obtener las propiedades de ventana de documento y visualización de página de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **GetDocumentWindow**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener diferentes propiedades del documento
# Posición de la ventana del documento - Predeterminado: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Orden de lectura predominante; determina la posición de la página
# cuando se muestra lado a lado - Predeterminado: L2R
print "Direction :- " + str(doc.getDirection())

# Si la barra de título de la ventana debe mostrar el título del documento.
# Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# Si se debe redimensionar la ventana del documento para ajustarse al tamaño de
# la primera página mostrada - Predeterminado: false
print "FitWindow :- " + str(doc.getFitWindow())

# Si se debe ocultar la barra de menú de la aplicación de visualización - Predeterminado: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Si se debe ocultar la barra de herramientas de la aplicación de visualización - Predeterminado: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Si se deben ocultar elementos de la interfaz de usuario como barras de desplazamiento
# dejando solo el contenido de la página mostrado - Predeterminado: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# El modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# El diseño de la página, es decir, página única, una columna
print "PageLayout :-" + str(doc.getPageLayout())

# Cómo debe mostrarse el documento cuando se abre.
print "pageMode :-" + str(doc.getPageMode())
```


**Descargar Código en Ejecución**

Descarga **Obtener Propiedades de Ventana y Visualización de Página del Documento (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)