---
title: 既存のPDFファイルのビューワープリファレンスを取得する
type: docs
weight: 70
url: ja/java/get-viewer-preference-of-an-existing-pdf-file/
description: このセクションでは、PdfContentEditorクラスを使用してAspose.PDF Facadesを操作する方法を示します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルのビューワープリファレンスを取得する

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) クラスは、PDFファイルの表示モードを表します。例えば、ドキュメントウィンドウを画面の中央に配置したり、ビューアアプリケーションのメニューバーを隠したりすることができます。

設定を読み取るためには、'getViewerPreference'を使用します。このメソッドは、すべての設定が保存されている変数を返します。

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // ビューワープリファレンスを変更する
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("メニューバーが隠されました");
        }
```