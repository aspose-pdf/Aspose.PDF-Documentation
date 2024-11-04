---
title: Crear Marcadores de Todas las Páginas (facades)
type: docs
weight: 10
url: /java/create-bookmark/
description: Esta sección explica cómo crear marcadores con Aspose.PDF Facades usando la Clase PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Crear Marcadores de Todas las Páginas (facades)

Para crear marcadores de todas las páginas, necesitas usar el método createBookmarks sin ningún parámetro. La clase PdfBookmarEditor te permite crear marcadores de todas las páginas de un archivo PDF. Primero, necesitas crear un objeto de la clase PdfBookmarkEditor y enlazar el PDF de entrada usando el método bindPdf. Luego, tienes que llamar al método createBookmarks y guardar el archivo PDF de salida usando el método save.

El siguiente fragmento de código te muestra:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## Crear Marcadores de Todas las Páginas con Propiedades (facades)

La clase PdfBookmarEditor te permite crear marcadores de todas las páginas de un archivo PDF y especificar las propiedades (Color, Negrita, Cursiva).
 Puedes hacer eso con la ayuda del método createBookmarks. Primero, necesitas crear un objeto de la clase PdfBookmarkEditor y vincular el PDF de entrada usando el método bindPdf. Luego, tienes que llamar al método createBookmarks y guardar el archivo PDF de salida usando el método save.

El siguiente fragmento de código te muestra cómo crear marcadores de todas las páginas con propiedades.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}