---
title: Python で PDF グラフを操作する
linktitle: グラフでの作業
type: docs
weight: 70
url: /ja/python-net/working-with-graphs/
description: Python で PDF ファイルに、円弧、円、曲線、線、長方形、楕円などのグラフや図形を描く方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内のベクトルグラフ形状を描画およびカスタマイズする
Abstract: このセクションでは、.NET 経由で Python 用 Aspose.PDF の Graph クラスを紹介し、PDF ドキュメントで一般的なベクトルシェイプを作成する方法について説明します。円弧、円、曲線、線、四角形、楕円を追加してスタイルを設定する方法と、図形の境界を検証する方法を学びます。
---

## グラフとは

[Aspose.PDF for Python (.NET 経由)](/pdf/ja/python-net/) 提供する [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) PDF ドキュメントでベクターグラフィックを描画するためのクラスです。

`Graph` は段落レベルの要素なので、ページを通じてページに追加します `paragraphs` コレクション。各グラフには `Shapes` 直線、円弧、円、曲線、長方形、楕円などの描画オブジェクトを追加できるコレクション。

このセクションは、チャート、図、イラスト、カスタムページ注釈など、PythonでベクターグラフィックをPDFページに直接描画する必要がある場合に使用します。

## カバーされているグラフシェイプ

では、次のタイプのシェイプがサポートされています。 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス:

- [円弧](/pdf/ja/python-net/add-arc/) -部分円と曲線図要素の円弧セグメントを描画します。
- [サークル](/pdf/ja/python-net/add-circle/) -マーカーや視覚的なハイライト用に円の輪郭や塗りつぶされた円を作成します。
- [カーブ](/pdf/ja/python-net/add-curve/) -カスタムパスとスムーズなグラフィック要素にベジエスタイルのカーブを追加します。
- [ライン](/pdf/ja/python-net/add-line/) -スタイル付きの線や破線を含む直線を描きます。
- [四角形](/pdf/ja/python-net/add-rectangle/) -アウトライン、塗りつぶし、グラデーション、透明の四角形を作成できます。
- [エリプス](/pdf/ja/python-net/add-ellipse/) -楕円形を描き、必要に応じてその中にテキストを追加します。

境界チェックを使用してシェイプの配置を検証することもできます。

- [Python を使用して PDF グラフの形状の境界をチェックする](/pdf/ja/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)

このセクションの例を次の図に示します。

![グラフ内の数字](graphs.png)

