---
title: Python で PDF ページを回転させる
linktitle: PDF ページの回転
type: docs
weight: 110
url: /ja/python-net/rotate-pages/
description: Python で PDF ページを回転させたり、ページの向きを変更したりする方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使って PDF 内のページを回転させる方法
Abstract: この記事では、Python を使用して既存の PDF ファイル内のページの向きをプログラムで更新または変更する方法について説明します。.NET 経由で Aspose.PDF for Python を使用すると、ページの MediaBox プロパティを調整することで、ユーザーは横向きと縦向きを簡単に切り替えることができます。この記事には、PDF ドキュメント内のページを繰り返し処理する方法、MediaBox のサイズと位置を変更する方法、および必要に応じた CropBox を調整する方法を示す Python コードスニペットが含まれています。さらに、「rotate」メソッドを使用してページの回転角度を設定して目的の向きにする方法についても説明します。最後に、更新した PDF ファイルを保存します。
---

このトピックでは、Python を使用して既存の PDF ファイル内のページのページの向きをプログラムで更新または変更する方法について説明します。

このページは、ページの向きを縦向きと横向きに切り替えたり、既存のPDFコンテンツに回転角度を適用したりする必要がある場合に使用します。

## ページの向きを変更

この関数は PDF のすべてのページを回転させます [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Python 用の Aspose.PDF を使用すると時計回りに 90 度になります。
スキャンした文書が横向きになっているなど、ページの向きの問題を修正するのに役立ちます。元の PDF は変更されず、回転したバージョンは新しいファイルとして保存されます。

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページサイズを変更する方法](/pdf/ja/python-net/change-page-size/)
- [Python で PDF ページをトリミングする方法](/pdf/ja/python-net/crop-pages/)
- [Python で PDF ページのプロパティを取得および設定する方法](/pdf/ja/python-net/get-and-set-page-properties/)