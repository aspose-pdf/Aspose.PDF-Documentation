---
title: 向现有PDF文件添加书签操作
type: docs
weight: 20
url: /zh/java/adding-bookmark-actions/
description: 本节解释如何使用Aspose.PDF Facades向现有PDF文件添加书签操作。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类位于com.aspose.pdf.facades包中，提供了向PDF文件添加书签操作的灵活性。您可以创建一个链接，并执行与在PDF查看器中执行菜单项相对应的序列操作。该类还提供为文档事件创建附加操作的功能。

以下代码示例演示如何向PDF文档添加书签操作。
 如果你点击这个标签，将执行所需的操作。借助书签，点击它，我们执行所需的操作。然后创建一个 [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-)，设置文本的参数、颜色，指明书签的名称，并指明页码。最后一个动作是使用 "GoTo" 完成的，它允许你从任何地方跳转到我们需要的页面。

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // 将结果PDF保存到文件中
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```