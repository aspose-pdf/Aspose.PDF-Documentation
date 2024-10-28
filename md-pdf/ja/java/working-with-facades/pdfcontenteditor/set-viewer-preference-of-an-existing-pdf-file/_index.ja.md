---
title: 既存のPDFファイルのビュワー設定を設定する
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: このセクションでは、PdfContentEditorクラスを使用してAspose.PDF Facadesを操作する方法を示します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルのビュワー設定を設定する

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference)クラスは、PDFファイルの表示モードを表します。例えば、ドキュメントウィンドウを画面の中央に配置したり、ビューアアプリケーションのメニューバーを非表示にすることができます。

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスの[ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-)メソッドを使用すると、ビュワー設定を変更することができます。
 そのためには、[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) クラスのオブジェクトを作成し、[bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) メソッドを使用して入力PDFファイルをバインドする必要があります。

その後、任意の設定を行うために [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) メソッドを呼び出すことができます。最後に、Saveメソッドを使用して更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、既存のPDFファイルのビューア設定を変更する方法を示しています。

例えば、パラメータ [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) を指定してウィンドウを中央に配置し、その後 [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) で上部ツールバーを削除し、[PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) でフルスクリーンモードを開きます。
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // ビューアの設定を変更する
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```