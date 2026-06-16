---
title: N-Up PDF ドキュメントを作成
type: docs
weight: 10
url: /ja/python-net/create-n-up-pdf-document/
description: Aspose.PDF for Python を使用して潜在的なエラーを安全に処理しながら N-Up PDF ドキュメントを作成する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で N アップ PDF レイアウトを作成する
Abstract: Python 用 Aspose.PDF を使用して N-Up PDF レイアウトを生成する方法を学びましょう。この例は、PDFFileEditor クラスの「make_n_up」または「try_make_n_up」メソッドを使用して、PDF ドキュメントの複数のページを 1 ページに結合する方法を示しています。
---

N-Up レイアウトは、PDF ドキュメントの複数のページを 1 ページにグリッド形式で配置します。このレイアウトは、複数のページを一度に表示できるプレゼンテーション、配布資料、またはレポートの印刷によく使用されます。

Aspose.PDF for Python を使用すると、開発者は、各出力ページに表示される元のページ数を決定する行と列の数を指定することで、N-Up 文書をすばやく作成できます。

このコードスニペットでは、の 'make_n_up' メソッド [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class は、入力 PDF のページを 2 × 2 グリッドに配置します。つまり、出力ドキュメントの 1 ページに 4 つの元のページが表示されます。

以下の例では、レイアウトは 2 行 2 列で、1 シートあたり 4 ページになっています。

1. ソース PDF ファイルを開きます。
1. PDF ファイルエディターのインスタンスを作成します。
1. N-Up レイアウトの行と列の数を指定します。
1. ページが結合された新しい PDF を生成します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

.NET 経由の Python 用 Aspose.PDF では、PDFFileEditor クラスを使用して N アップレイアウトを生成できます。'try_make_n_up' メソッドは make_n_up と同様に機能しますが、操作が失敗したときに例外を発生させる代わりに、プロセスが成功したかどうかを示すブール値を返します。

N-Up レイアウトは、行と列で定義されたグリッドを使用して、複数の PDF ページを 1 ページに配置します。

'try_make_n_up' メソッドを使用すると、この操作をより安全に実行できます。理由は次のとおりです。

- レイアウトが正常に作成された場合は True を返します。
- 操作が失敗した場合は False を返します。
- 例外が発生してもプログラムの実行は中断されません

以下の例では、文書は 2 × 2 のグリッドを使用して配置され、各出力ページに 4 つのオリジナルページが配置されます。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
