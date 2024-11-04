---
title: 设置现有PDF文件的查看器偏好
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: 本节介绍如何使用PdfContentEditor类与Aspose.PDF Facades进行操作。
lastmod: "2021-06-05"
draft: false
---

## 设置现有PDF文件的查看器偏好

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) 类表示PDF文件的显示模式；例如，将文档窗口定位在屏幕中央，隐藏查看器应用程序的菜单栏等。

[ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) 方法在 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类中允许您更改查看器偏好。
 为了做到这一点，你需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类的对象，并使用 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) 方法绑定输入的 PDF 文件。

之后，你可以调用 [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) 方法来设置任何偏好。最后，你需要使用 Save 方法保存更新后的 PDF 文件。下面的代码片段演示了如何在现有 PDF 文件中更改查看器偏好。

例如，我们指定参数 [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW)，用它来居中窗口，然后使用 [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) 去掉顶部工具栏，并通过 [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) 打开全屏模式。
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 更改查看器偏好设置
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```