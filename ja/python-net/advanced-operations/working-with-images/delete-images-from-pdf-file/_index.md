---
title: Python を使用して PDF ファイルから画像を削除する
linktitle: 画像を削除する
type: docs
weight: 20
url: /ja/python-net/delete-images-from-pdf-file/
description: Python で PDF ファイルから特定の画像またはすべての画像を削除する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルから画像を削除する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントから画像を削除する方法を説明します。特定の画像リソースを削除する方法と、選択したページからすべての画像を削除する方法について説明します。
---

このページは、不要なグラフィックを削除したり、PDF サイズを小さくしたり、文書から機密性の高いビジュアルコンテンツを消去したりする必要がある場合に使用します。

## PDF ファイルからの画像の削除

次の手順を使用して、ページから 1 つの画像を削除します。

1. ソース PDF を以下のようにロードします。 `ap.Document(infile)`.
1. ページと画像リソースインデックスを選択します。
1. で画像を削除する `resources.images.delete(index)`.
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## ページからすべての画像を削除する

この例を使用して、特定のページからすべての画像を削除します。

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## 関連画像トピック

- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [既存の PDF ファイル内の画像の置換](/pdf/ja/python-net/replace-image-in-existing-pdf-file/)
- [PDF ファイルからの画像の抽出](/pdf/ja/python-net/extract-images-from-pdf-file/)
- [既存の PDF ファイルへの画像の追加](/pdf/ja/python-net/add-image-to-existing-pdf-file/)