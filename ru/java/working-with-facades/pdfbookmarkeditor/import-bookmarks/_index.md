---
title: Импорт закладок из XML в существующий PDF файл (facades)
type: docs
weight: 30
url: ru/java/import-bookmark/
description: В этом разделе объясняется, как импортировать закладки с помощью Aspose.PDF Facades, используя класс PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Метод importBookmarksWithXml позволяет импортировать закладки в файл PDF из файла XML.

Для импорта закладок:

1. Создайте объект PdfBookmarkEditor и свяжите PDF файл, используя метод bindPdf.
1. Вызовите метод importBookmarksWithXml.
1. Сохраните обновленный файл PDF, используя метод save.

Следующий фрагмент кода показывает, как импортировать закладки из XML файла.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, класс PdfBookmarkEditor реализует методы exportBookmarksToXML и importBookmarksWithXML с аргументами типа Stream. В результате извлеченные закладки могут быть импортированы из объекта потока.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}