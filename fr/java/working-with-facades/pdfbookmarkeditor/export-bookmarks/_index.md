---
title: Exporter les Signets vers XML depuis un Fichier PDF Existant (facades)
type: docs
weight: 20
url: /fr/java/export-bookmark/
description: Cette section explique comment exporter des signets avec Aspose.PDF Facades en utilisant la classe PdfBookmarkEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

La méthode exportBookmarksToXml vous permet d'exporter des signets d'un fichier PDF vers un fichier XML.

{{% /alert %}}

Pour exporter des signets :

1. Créez un objet PdfBookmarkEditor et liez le fichier PDF en utilisant la méthode bindPdf.
2. Appelez la méthode exportBookmarksToXml.

Le snippet de code suivant vous montre comment exporter des signets vers un fichier XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF pour Java 9.0.0, la classe PdfBookmarkEditor implémente les méthodes exportBookmarksToXML et importBookmarksWithXML avec des arguments Stream. En conséquence, les signets extraits peuvent être enregistrés dans un objet stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}