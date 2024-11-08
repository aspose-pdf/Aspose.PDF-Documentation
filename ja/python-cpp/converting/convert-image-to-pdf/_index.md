---
title: Pythonで画像をPDFに変換する
linktitle: 画像をPDFファイルに変換する
type: docs
weight: 10
url: /ja/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: このトピックでは、Aspose.PDF for Python via C++ライブラリを使用して画像をPDFに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

私たちのライブラリは、最も一般的な画像形式であるJPEGを変換するためのコードスニペットを示しています。Aspose.PDF for Python via C++を使用して、以下の手順でJPG画像をPDFに非常に簡単に変換できます。

## 画像をPDFに変換する

Aspose.PDF for C++を使用して、以下の手順でJPG画像をPDFに非常に簡単に変換できます。

1. PILライブラリを使用して入力画像ファイルを開く
1. 画像の幅と高さを取得する
1. AsposePDFPythonWrappersライブラリを使用して新しいDocumentインスタンスを作成する
1. 画像の固定の高さと幅を設定する
1. ドキュメントに新しいページを追加する
1. ページに画像を追加する
1. 'document.save'メソッドで出力PDFを保存する

以下のコードスニペットは、Python via C++を使用してJPG画像をPDFに変換する方法を示しています。

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# データファイルのディレクトリパスを設定
dataDir = os.path.join(os.getcwd(), "samples")

# 入力ファイルのパスを設定
input_file = os.path.join(dataDir, "sample.jpg")

# 出力ファイルのパスを設定
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# PILライブラリを使用して入力画像ファイルを開く
pil_img = Image.open(input_file)

# 画像の幅と高さを取得
width, height = pil_img.size

# AsposePDFPythonWrappersライブラリを使用して新しいDocumentインスタンスを作成
document = apw.Document()

# AsposePDFPythonWrappersライブラリを使用して新しいImageインスタンスを作成
image = apw.Image()

# 画像のファイルパスを設定
image.file = input_file

# 画像の固定高さと幅を設定
image.fix_height = height
image.fix_width = width

# ドキュメントに新しいページを追加
page = document.pages.add()

# ページに画像を追加
page.paragraphs.add(image)

# 出力ファイルパスにドキュメントを保存
document.save(output_file)
```