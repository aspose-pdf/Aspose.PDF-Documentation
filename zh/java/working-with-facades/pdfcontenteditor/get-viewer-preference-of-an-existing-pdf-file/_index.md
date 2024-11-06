---
title: 获取现有PDF文件的查看器偏好
type: docs
weight: 70
url: zh/java/get-viewer-preference-of-an-existing-pdf-file/
description: 本节展示如何使用PdfContentEditor类与Aspose.PDF Facades一起工作。
lastmod: "2021-06-05"
draft: false
---

## 获取现有PDF文件的查看器偏好

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) 类表示PDF文件的显示模式；例如，将文档窗口定位在屏幕中央，隐藏查看器应用程序的菜单栏等。

为了读取设置，我们使用'getViewerPreference'。此方法返回一个变量，其中保存了所有设置。

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 更改查看器偏好设置
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Menu bar hided");
        }
```