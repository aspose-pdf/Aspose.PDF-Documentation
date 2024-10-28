---
title: Exportar Favoritos para XML de um Arquivo PDF Existente (facades)
type: docs
weight: 20
url: /java/export-bookmark/
description: Esta seção explica como exportar favoritos com Aspose.PDF Facades usando a Classe PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

O método exportBookmarksToXml permite exportar favoritos de um arquivo PDF para um arquivo XML.

{{% /alert %}}

Para exportar favoritos:

1. Crie um objeto PdfBookmarkEditor e vincule o arquivo PDF usando o método bindPdf.
1. Chame o método exportBookmarksToXml.

O trecho de código a seguir mostra como exportar favoritos para um arquivo XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, a classe PdfBookmarkEditor implementa os métodos exportBookmarksToXML e importBookmarksWithXML com argumentos Stream. Como resultado, os marcadores extraídos podem ser salvos em um objeto de fluxo.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}