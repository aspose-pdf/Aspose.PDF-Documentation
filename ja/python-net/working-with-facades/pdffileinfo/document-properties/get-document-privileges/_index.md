---
title: ドキュメント権限を取得
type: docs
weight: 10
url: /ja/python-net/get-document-privileges/
description: Aspose.PDF for Python を使用して PDF ドキュメントの権限をプログラムで確認する方法を学びましょう。このチュートリアルでは、PDFFileInfo クラスを使用して、印刷、コピー、権限の変更など、文書のセキュリティ設定を読み取る方法を説明します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF ドキュメントの権限を取得する
Abstract: PDF ドキュメントには、フォームの印刷、コピー、変更、入力などの操作を制限するセキュリティ制限がある場合があります。これらの権限にプログラムからアクセスすることで、開発者は PDF にどのような操作を許可するかを決定できます。このガイドでは、PDFFileInfo クラスを使用して PDF のドキュメント権限を取得し、Python で表示する方法を説明します。
---

PDF 権限は、ユーザーが文書に対してできることとできないことを制御します。一般的な権限には以下が含まれます。

- 文書を印刷する
- コンテンツをコピーする
- 注釈または内容の変更
- フォームフィールドへの入力
- スクリーンリーダーを使用する
- 文書の組み立てまたは結合

Aspose.PDF for Python では、以下を使用してこれらの設定をプログラムで調べることができます。 [PDF ファイル情報](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) クラス。これは、自動化されたワークフローで複数の PDF を操作したり、コンプライアンスを検証したり、アプリケーションでの文書処理を制御したりする場合に特に便利です。

1. PDF ファイルをロードします。
1. そのドキュメント権限を取得します。
1. ドキュメントに許可されているアクションを表示します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
