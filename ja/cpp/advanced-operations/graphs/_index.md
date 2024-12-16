---
title: PDFでのグラフの操作
linktitle: グラフの操作
type: docs
weight: 70
url: /ja/cpp/graphs/
description: この記事では、グラフとは何か、塗りつぶされた長方形オブジェクトの作成方法、グラフオブジェクト内にテキストを追加する方法、PDFにラインオブジェクトを追加する方法などについて説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## グラフとは何か

PDFドキュメントにグラフを追加することは、Adobe Acrobat Writerやその他のPDF処理アプリケーションを使用する際に開発者によくあるタスクです。PDFアプリケーションで使用できるグラフには多くの種類があります。
[Aspose.PDF for C++](/pdf/ja/cpp/) もPDFドキュメントにグラフを追加することをサポートしています。この目的のために、Graphクラスが提供されています。Graphは段落レベルの要素であり、PageインスタンスのParagraphsコレクションに追加することができます。Graphインスタンスには、Shapesのコレクションが含まれています。

[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) クラスでサポートされている形状の種類は次のとおりです:

- [Arc](/pdf/ja/cpp/add-arc/) - フラグと呼ばれることもあるが、隣接する頂点の順序対を指し、場合によっては有向線とも呼ばれることがあります。
- [Circle](/pdf/ja/cpp/add-circle/) - データをセクターに分割した円を使用してデータを表示します。円グラフ（パイチャートとも呼ばれる）を使用して、データが全体またはグループの一部をどのように表しているかを示します。
- [Curve](/pdf/ja/cpp/add-curve/) - 射影直線の連結和であり、それぞれの直線は通常の二重点で他の三つの直線と交わります。
- [Line](/pdf/ja/cpp/add-line) - 折れ線グラフは連続データを表示するのに使用され、時間の経過とともに傾向を示す場合、将来の出来事を予測するのに役立つことがあります。
- [Rectangle](/pdf/ja/cpp/add-rectangle/) - グラフで見ることができる多くの基本的な形状の一つであり、問題を解決するのに非常に役立つことがあります。
- [Ellipse](/pdf/ja/cpp/add-ellipse/) - 平面上の点の集合で、楕円形の曲線を形成します。

上記の詳細は以下の図にも示されています:

![Figures in Graphs](graph.png)