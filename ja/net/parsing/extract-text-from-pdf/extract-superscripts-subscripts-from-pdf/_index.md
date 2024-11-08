---
title: PDFからスーパースクリプトとサブスクリプトのテキストを抽出
linktitle: スーパースクリプトとサブスクリプトを抽出
type: docs
weight: 30
url: /ja/net/extract-superscripts-subscripts-from-pdf/
description: この記事では、C#のAspose.PDFを使用してPDFからスーパースクリプトとサブスクリプトのテキストを抽出するさまざまな方法について説明します。
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## スーパースクリプトとサブスクリプトのテキストを抽出

PDF文書からテキストを抽出することは一般的なことです。しかし、そのようなテキストを抽出する際に、技術文書や記事に特有な**スーパースクリプトとサブスクリプト**が含まれていても、表示されないことがあります。サブスクリプトまたはスーパースクリプトは、通常のテキスト行の下または上に配置される文字、数字、または文字で、通常は残りのテキストよりも小さいです。

**サブスクリプトとスーパースクリプト**は、公式、数学的表現、化学化合物の仕様で最もよく使用されます。
**下付き文字と上付き文字**は、主に公式、数学的表現、化学化合物の仕様で使用されます。
最近のリリースの1つで、**Aspose.PDF for .NET** ライブラリはPDFからの上付き文字と下付き文字のテキストを抽出するサポートを追加しました。

**TextFragmentAbsorber** クラスを使用して、見つかったテキストで何でもできるようになります。つまり、全てのテキストを単純に使用できます。次のコードスニペットを試してください：

以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

または、**TextFragments** を個別に使用し、座標やサイズによってソートするなど、さまざまな操作を行います。

以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。
以下のコードスニペットは [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
