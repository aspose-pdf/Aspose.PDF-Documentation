---
title: Экспорт закладок в XML из существующего PDF файла (фасады)
type: docs
weight: 20
url: /java/export-bookmark/
description: Этот раздел объясняет, как экспортировать закладки с помощью Aspose.PDF Facades, используя класс PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

Метод exportBookmarksToXml позволяет экспортировать закладки из PDF файла в XML файл.

{{% /alert %}}

Чтобы экспортировать закладки:

1. Создайте объект PdfBookmarkEditor и свяжите PDF файл, используя метод bindPdf.
1. Вызовите метод exportBookmarksToXml.

Следующий фрагмент кода показывает, как экспортировать закладки в XML файл.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, класс PdfBookmarkEditor реализует методы exportBookmarksToXML и importBookmarksWithXML с аргументами Stream. В результате извлеченные закладки могут быть сохранены в объект потока.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}