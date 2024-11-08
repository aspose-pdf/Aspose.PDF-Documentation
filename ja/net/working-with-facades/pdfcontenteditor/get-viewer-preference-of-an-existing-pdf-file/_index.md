---
title: 既存のPDFファイルのビューアプリファレンスを取得する
type: docs
weight: 70
url: /ja/net/get-viewer-preference-of-an-existing-pdf-file/
description: このセクションでは、PdfContentEditorクラスを使用して既存のPDFファイルのビューアプリファレンスを取得する方法を示します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルのビューアプリファレンスを取得する

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) クラスは、PDFファイルの表示モードを表します。例えば、ドキュメントウィンドウを画面の中央に配置したり、ビューアアプリケーションのメニューバーを非表示にすることなどです。

設定を読み取るために [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference) クラスを使用します。このメソッドは、すべての設定が保存されている変数を返します。

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // ビューアプリファレンスを変更する
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("メニューバーが非表示");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("ページモード全画面");
        }
```