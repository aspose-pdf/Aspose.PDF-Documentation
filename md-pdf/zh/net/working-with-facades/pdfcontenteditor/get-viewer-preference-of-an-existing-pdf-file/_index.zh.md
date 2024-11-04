---
title: 获取 PDF 文件的查看器偏好设置
type: docs
weight: 70
url: /net/get-viewer-preference-of-an-existing-pdf-file/
description: 本节展示如何使用 PdfContentEditor 类获取现有 PDF 文件的查看器偏好设置。
lastmod: "2021-06-05"
draft: false
---

## 获取现有 PDF 文件的查看器偏好设置

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) 类表示 PDF 文件的显示模式；例如，将文档窗口定位在屏幕中央，隐藏查看器应用程序的菜单栏等。

为了读取设置，我们使用 [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference) 类。此方法返回一个保存所有设置的变量。

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 更改查看器偏好设置
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("菜单栏已隐藏");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("页面模式全屏");
        }
```