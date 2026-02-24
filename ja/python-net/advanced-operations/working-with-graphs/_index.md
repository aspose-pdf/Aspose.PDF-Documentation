---
title: Python を使用した PDF でのグラフ操作
linktitle: グラフの操作
type: docs
weight: 70
url: /ja/python-net/working-with-graphs/
description: この記事では、グラフとは何か、塗りつぶし矩形オブジェクトの作成方法、その他の機能について説明します
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF へのグラフ追加
Abstract: この記事では、Adobe Acrobat Writer や同様の PDF 処理ツールを使用する開発者にとって一般的な要件である、PDF 文書へのグラフの統合について説明します。Aspose.PDF for Python via .NET の Graph クラスを紹介し、さまざまな種類の形状を PDF 文書に追加できるようにしてこの作業を容易にします。Graph クラスは段落レベルの要素で、Page インスタンスの Paragraphs コレクションに追加でき、Arc、Circle、Curve、Line、Rectangle、Ellipse などの形状コレクションをサポートします。各形状は固有の目的を持ち、例えば Arc は隣接性を表し、Circle はデータの一部を示し、Curve は連結した線を描写し、Line は連続データのトレンドを表示し、Rectangle は空間的な問題を解決し、Ellipse は楕円形を形成します。この記事では、これらの形状の視覚的な表現も提供し、理解を助けます。
---

## グラフとは何か

PDF 文書にグラフを追加することは、Adobe Acrobat Writer やその他の PDF 処理アプリケーションで作業する開発者にとって非常に一般的なタスクです。PDF アプリケーションで使用できるグラフの種類は多数あります。
[Aspose.PDF for Python via .NET](/pdf/python-net/) も PDF 文書へのグラフ追加をサポートしています。この目的のために Graph クラスが提供されています。Graph は段落レベルの要素で、Page インスタンスの Paragraphs コレクションに追加できます。Graph インスタンスは Shapes のコレクションを含みます。

次の形状タイプは [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラスでサポートされています：

- [Arc](/pdf/python-net/add-arc/) - 時にはフラグとも呼ばれ、隣接する頂点の順序付けられたペアですが、時には有向線とも呼ばれます。
- [Circle](/pdf/python-net/add-circle/) - 円をセクタに分割してデータを表示します。円グラフ（パイチャートとも呼ばれる）を使用して、データが全体やグループの一部をどのように表すかを示します。
- [Curve](/pdf/python-net/add-curve/) - 投影直線の連結された合成で、各直線は普通の二重点で他の三本の直線と交わります。
- [Line](/pdf/python-net/add-line) - 折れ線グラフは連続データを表示するために使用され、時間経過によるトレンドを示す際に将来の出来事を予測するのに役立ちます。
- [Rectangle](/pdf/python-net/add-rectangle/) - グラフで見られる基本的な形状の一つで、問題解決に非常に役立ちます。
- [Ellipse](/pdf/python-net/add-ellipse/) - 平面上の点の集合で、楕円形や曲線の形を作ります。

上記の詳細は、以下の図でも示されています：

![グラフの図](graphs.png)


