---
title: Create Bookmarks of All Pages (facades)
type: docs
weight: 10
url: ru/java/create-bookmark/
description: Этот раздел объясняет, как создавать закладки с помощью Aspose.PDF Facades, используя класс PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Create Bookmarks of All Pages (facades)

Для создания закладок для всех страниц необходимо использовать метод createBookmarks без каких-либо параметров. Класс PdfBookmarEditor позволяет создавать закладки для всех страниц PDF-файла. Сначала нужно создать объект класса PdfBookmarkEditor и привязать входной PDF, используя метод bindPdf. Затем необходимо вызвать метод createBookmarks и сохранить выходной PDF-файл, используя метод save.

Следующий фрагмент кода показывает вам:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## Create Bookmarks of All Pages with Properties (facades)

Класс PdfBookmarEditor позволяет создавать закладки для всех страниц PDF-файла и указывать свойства (Цвет, Жирный, Курсив).
 Вы можете сделать это с помощью метода createBookmarks. Сначала вам нужно создать объект класса PdfBookmarkEditor и связать входной PDF с помощью метода bindPdf. Затем вам нужно вызвать метод createBookmarks и сохранить выходной PDF файл с помощью метода save.

Следующий фрагмент кода показывает, как создать закладки для всех страниц с свойствами.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}