---
title: 既存のPDFでの改ページ
type: docs
weight: 30
url: /java/page-break-in-existing-pdf/
description: このセクションでは、PdfFileEditorクラスを使用して既存のPDFでページを分割する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

デフォルトのレイアウトとして、PDFファイル内のコンテンツは左上から右下に向かって追加されます。コンテンツがページの下のマージンを超えると、改ページが発生します。しかし、要件に応じて改ページを挿入する必要がある場合があります。この要件を達成するために、[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスに AddPageBreak(...) メソッドが追加されています。

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- srcは元のドキュメント/ドキュメントへのパス/元のドキュメントを含むストリームです
- destはドキュメントが保存されるドキュメント/パス/ストリームです
- PageBreakはページブレークオブジェクトの配列です。ページブレークを配置するページのインデックスとページ上のページブレークの垂直位置の2つのプロパティがあります。

## 例1 (ページブレークを追加)

```java
   public static void PageBrakeExample01() {
        // Documentのインスタンスを作成
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // 空のDocumentのインスタンスを作成
        Document dest = new Document();
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // 結果のファイルを保存
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## 例 2

```java
  public static void PageBrakeExample02() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## 例 3

```java
 public static void PageBrakeExample03() {
        // ストリームを作成
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```