---
title: 添加书签到 PDF 文件
type: docs
weight: 20
url: zh/net/how-to-create-nested-bookmarks/
description: 本节说明如何使用 PdfContentEditor 类创建嵌套书签。
lastmod: "2021-06-05"
draft: false
---

书签为您提供了在 PDF 文档中跟踪/链接到特定页面的选项。[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) 类在 [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) 中提供了一个功能，允许您在现有 PDF 文件中以复杂但直观的方式在给定页面或所有页面上创建自己的书签。

## 实现细节

除了创建简单书签，有时您还需要以章节的形式创建书签，在章节书签内嵌套各个书签，这样当您点击章节的 + 号时，书签展开后可以看到其中的页面，如下图所示。
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("书签 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // 将结果 PDF 保存到文件
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```