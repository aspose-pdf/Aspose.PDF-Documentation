---
title: スタンプからテキストを抽出する方法を学ぶ
type: docs
weight: 60
url: ja/net/extract-text-from-stamps/
description: Aspose.PDF for .NETの特別機能を使用して、スタンプ注釈からテキストを抽出する方法を学びます
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## スタンプ注釈からテキストを抽出する

Aspose.PDF for NETでは、スタンプ注釈からテキストを抽出することができます。PDFのスタンプ注釈からテキストを抽出するためには、以下の手順を使用できます。

1. `Document` クラスのオブジェクトを作成する
1. ページの注釈リストから所望の `Annotation` を取得する
1. `TextAbsorber` クラスの新しいオブジェクトを定義する
1. テキストを取得するために TextAbsorber の visit メソッドを使用する

次のコードスニペットは [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

