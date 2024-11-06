---
title: 创建所有页面的书签 (facades)
type: docs
weight: 10
url: zh/java/create-bookmark/
description: 本节说明如何使用 PdfBookmarEditor 类通过 Aspose.PDF Facades 创建书签。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 创建所有页面的书签 (facades)

为了创建所有页面的书签，您需要使用不带任何参数的 createBookmarks 方法。PdfBookmarEditor 类允许您为 PDF 文件的所有页面创建书签。首先，您需要创建一个 PdfBookmarkEditor 类的对象，并使用 bindPdf 方法绑定输入 PDF。然后，您必须调用 createBookmarks 方法，并使用 save 方法保存输出 PDF 文件。

以下代码片段展示了：

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## 创建具有属性的所有页面书签 (facades)

PdfBookmarEditor 类允许您为 PDF 文件的所有页面创建书签并指定属性（颜色、粗体、斜体）。
 你可以通过使用 createBookmarks 方法来实现这一点。首先，你需要创建一个 PdfBookmarkEditor 类的对象，并使用 bindPdf 方法绑定输入的 PDF。然后，你需要调用 createBookmarks 方法，并使用 save 方法保存输出的 PDF 文件。

以下代码片段向你展示了如何创建具有属性的所有页面的书签。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}