---
title: Importar Marcadores desde XML a un Archivo PDF Existente (fachadas)
type: docs
weight: 30
url: es/java/import-bookmark/
description: Esta sección explica cómo importar marcadores con Aspose.PDF Facades usando la Clase PdfBookmarkEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El método importBookmarksWithXml te permite importar marcadores en un archivo PDF desde un archivo XML.

Para importar marcadores:

1. Crea un objeto PdfBookmarkEditor y vincula el archivo PDF usando el método bindPdf.
1. Llama al método importBookmarksWithXml.
1. Guarda el archivo PDF actualizado usando el método save.

El siguiente fragmento de código muestra cómo importar marcadores desde un archivo XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, la clase PdfBookmarkEditor implementa los métodos exportBookmarksToXML e importBookmarksWithXML con argumentos Stream. Como resultado, los marcadores extraídos se pueden importar desde un objeto stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}