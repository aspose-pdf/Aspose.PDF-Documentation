---
title: 设置PDF的查看器偏好
type: docs
weight: 60
url: zh/net/set-viewer-preference-of-an-existing-pdf-file/
description: 本节介绍如何使用PdfContentEditor类设置现有PDF文件的查看器偏好。
lastmod: "2021-06-05"
draft: false
---

## 设置现有PDF文件的查看器偏好

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference)类表示PDF文件的显示模式；例如，将文档窗口置于屏幕中央，隐藏查看器应用程序的菜单栏等。

[ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference)方法在[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)类中允许您更改查看器偏好。 为了做到这一点，您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) 方法绑定输入的 PDF 文件。

之后，您可以调用 [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) 方法设置任何偏好。最后，您必须使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存更新的 PDF 文件。以下代码片段向您展示如何在现有 PDF 文件中更改查看器偏好。

例如，我们指定参数 [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) 使窗口居中，然后使用 [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) 移除顶部工具栏，并使用 [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) 打开全屏模式。
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 更改查看器首选项
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // 将结果PDF保存到文件
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```