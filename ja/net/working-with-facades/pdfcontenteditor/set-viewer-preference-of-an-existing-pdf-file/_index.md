---
title: PDFの表示設定を行う
type: docs
weight: 60
url: ja/net/set-viewer-preference-of-an-existing-pdf-file/
description: このセクションでは、PdfContentEditorクラスを使用して既存のPDFファイルの表示設定を行う方法を示します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルの表示設定を行う

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) クラスはPDFファイルの表示モードを表します。例えば、ドキュメントウィンドウを画面の中央に配置したり、ビューアアプリケーションのメニューバーを隠したりすることができます。

[ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) メソッドは、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラス内で表示設定を変更することを可能にします。 以下のことを行うには、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) メソッドを使用して入力PDFファイルをバインドする必要があります。

その後、任意の設定を行うために [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) メソッドを呼び出すことができます。最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) メソッドを使用して更新されたPDFファイルを保存する必要があります。次のコードスニペットは、既存のPDFファイルでビューア設定を変更する方法を示しています。

例えば、ウィンドウを中央に配置するために [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) パラメータを指定し、[HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) で上部のツールバーを削除し、[PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) で全画面モードを開きます。
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // ビューアの設定を変更
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // 結果をPDFファイルに保存
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```