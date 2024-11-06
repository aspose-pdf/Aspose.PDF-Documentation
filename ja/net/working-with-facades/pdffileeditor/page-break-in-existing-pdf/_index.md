---
title: 既存のPDFにおける改ページ
type: docs
weight: 30
url: ja/net/page-break-in-existing-pdf/
description: このセクションでは、PdfFileEditorクラスを使用して既存のPDFでページを分割する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

デフォルトのレイアウトとして、PDFファイル内のコンテンツは左上から右下に追加されます。コンテンツがページの下部余白を超えると、改ページが発生します。ただし、要件に応じて改ページを挿入する必要がある場合があります。この要件を達成するために、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスにAddPageBreak(...)というメソッドが追加されています。

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak)

- srcはドキュメントのソース/ドキュメントへのパス/ソースドキュメントを持つストリームです
- destはドキュメントが保存される宛先ドキュメント/パス/ドキュメントが保存されるストリームです
- PageBreakはページブレークオブジェクトの配列です。ページブレークを配置するページのインデックスとページ上のページブレークの垂直位置の2つのプロパティを持っています。

## 例 1 (ページブレークを追加)

```csharp
public static void PageBrakeExample01()
{
    // Documentインスタンスをインスタンス化
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // 空のDocumentインスタンスをインスタンス化
    Document dest = new Document();
    // PdfFileEditorオブジェクトを作成
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // 結果のファイルを保存
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## 例 2

```csharp
public static void PageBrakeExample02()
{
    // PdfFileEditorオブジェクトを作成
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## 例 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```