---
title: PDFドキュメントを比較する
linktitle: PDFを比較する
type: docs
weight: 180
url: /ja/net/compare-pdf-documents/
description: 24.7リリース以降、PDFドキュメントの内容を注釈付きで比較し、サイドバイサイドの出力が可能です。
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF for .NETを使用してPDFドキュメントを比較する

PDFドキュメントを扱う際、二つのドキュメントの内容を比較して違いを特定する必要があることがあります。Aspose.PDF for .NETライブラリは、この目的のための強力なツールセットを提供します。この記事では、いくつかの簡単なコードスニペットを使用してPDFドキュメントを比較する方法を探ります。

Aspose.PDFの比較機能を使用すると、二つのPDFドキュメントをページごとに比較することができます。特定のページまたはドキュメント全体を比較することが選択できます。結果として得られる比較ドキュメントは、違いを強調表示し、二つのファイル間の変更点を特定しやすくします。

### 特定のページを比較する

最初のコードスニペットは、二つのPDFドキュメントの最初のページを比較する方法を示しています。

最初のコードスニペットは、2つのPDFドキュメントの最初のページを比較する方法を示しています。

手順：

1. ドキュメントの初期化。
このコードは、それぞれのファイルパス（documentPath1およびdocumentPath2）を使用して2つのPDFドキュメントを初期化することから始まります。パスは現在空の文字列として指定されていますが、実際にはこれを実際のファイルパスに置き換えます。
2. 比較プロセス。
- ページ選択 - 比較は各ドキュメントの最初のページ（'Pages[1]'）に限定されます。
- 比較オプション：

'AdditionalChangeMarks = true'- このオプションは、追加の変更マーカーが表示されることを保証します。これらのマーカーは、現在比較されているページにない場合でも、他のページに存在するかもしれない違いを強調表示します。

'ComparisonMode = ComparisonMode.IgnoreSpaces' - このモードは、比較者にテキスト内のスペースを無視するよう指示し、単語内の変更にのみ焦点を当てます。

3.
```
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### 全文書の比較

二番目のコードスニペットは、二つのPDF文書の全内容を比較する範囲を広げます。

手順:

1. 文書の初期化。
最初の例と同じように、二つのPDF文書がファイルパスで初期化されます。
2. 比較プロセス。
- 全文書比較 - 最初のスニペットとは異なり、このコードは二つの文書の全内容を比較します。
- 比較オプション - 最初のスニペットと同じオプションを使用し、スペースを無視し、追加の変更マークが表示されます。
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

これらのスニペットによって生成された比較結果はPDFドキュメントで、Adobe Acrobatのようなビューアで開くことができます。Adobe Acrobatで二ページ表示を使用すると、変更が並んで表示されます：

- 削除 - これらは左ページに記載されています。
- 挿入 - これらは右ページに記載されています。

'AdditionalChangeMarks'を'true'に設定することで、現在表示されているページに変更がない場合でも、他のページに発生する可能性のある変更のマーカーを表示することもできます。

**Aspose.PDF for .NET**は、特定のページやドキュメント全体を比較する必要がある場合に、強力なツールを提供します。
**Aspose.PDF for .NET** は、特定のページやドキュメント全体を比較する必要がある場合に、強力なPDFドキュメント比較ツールを提供します。
