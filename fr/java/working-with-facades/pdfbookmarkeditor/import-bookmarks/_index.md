---
title: Importer des Signets à partir de XML dans un Fichier PDF Existant (façades)
type: docs
weight: 30
url: fr/java/import-bookmark/
description: Cette section explique comment importer des signets avec Aspose.PDF Facades en utilisant la classe PdfBookmarkEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La méthode importBookmarksWithXml vous permet d'importer des signets dans un fichier PDF à partir d'un fichier XML.

Pour importer des signets :

1. Créez un objet PdfBookmarkEditor et liez le fichier PDF en utilisant la méthode bindPdf.
1. Appelez la méthode importBookmarksWithXml.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode save.

Le fragment de code suivant montre comment importer des signets à partir d'un fichier XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, la classe PdfBookmarkEditor implémente les méthodes exportBookmarksToXML et importBookmarksWithXML avec des arguments Stream. En conséquence, les signets extraits peuvent être importés à partir d'un objet stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}