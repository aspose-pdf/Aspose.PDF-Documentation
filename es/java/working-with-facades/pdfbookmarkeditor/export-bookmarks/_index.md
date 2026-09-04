---
title: Exportar Marcadores a XML desde un Archivo PDF Existente (facades)
type: docs
weight: 20
url: /es/java/export-bookmark/
description: Esta sección explica cómo exportar marcadores con Aspose.PDF Facades usando la Clase PdfBookmarkEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

El método exportBookmarksToXml te permite exportar marcadores de un archivo PDF a un archivo XML.

{{% /alert %}}

Para exportar marcadores:

1. Crea un objeto PdfBookmarkEditor y vincula el archivo PDF usando el método bindPdf.
1. Llama al método exportBookmarksToXml.

El siguiente fragmento de código te muestra cómo exportar marcadores a un archivo XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF para Java 9.0.0, la clase PdfBookmarkEditor implementa los métodos exportBookmarksToXML e importBookmarksWithXML con argumentos Stream. Como resultado, los marcadores extraídos se pueden guardar en un objeto de flujo.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}