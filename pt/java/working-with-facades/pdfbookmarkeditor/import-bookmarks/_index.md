---
title: Importar Favoritos de XML para um Arquivo PDF Existente (facades)
type: docs
weight: 30
url: pt/java/import-bookmark/
description: Esta seção explica como importar favoritos com Aspose.PDF Facades usando a Classe PdfBookmarkEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O método importBookmarksWithXml permite que você importe favoritos em um arquivo PDF a partir de um arquivo XML.

Para importar favoritos:

1. Crie um objeto PdfBookmarkEditor e vincule o arquivo PDF usando o método bindPdf.
1. Chame o método importBookmarksWithXml.
1. Salve o arquivo PDF atualizado usando o método save.

O trecho de código a seguir mostra como importar favoritos de um arquivo XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, the PdfBookmarkEditor class implements the exportBookmarksToXML and importBookmarksWithXML methods with Stream arguments. As a result, extracted bookmarks can be imported from a stream object.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}