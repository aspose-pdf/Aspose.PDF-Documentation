---
title: PDF から添付ファイルを抽出
linktitle: 添付ファイルを抽出
type: docs
weight: 50
url: /ja/python-net/extract-attachment/
description: Python と Aspose.PDF を使用して PDF 添付ファイルを操作する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Python で PDF 添付ファイルを管理するための完全ガイド:埋め込みファイルの追加、抽出、処理"
Abstract: PDF 添付ファイルは、補足文書、レポート、画像、その他のリソースを PDF ファイル内に直接保存するために広く使用されています。この記事では、Aspose.PDF を使用して Python で PDF 添付ファイルを処理する方法の概要を説明します。既存の PDF に外部ファイルを埋め込む方法、特定の添付ファイルまたはすべての添付ファイルを抽出する方法、ファイルサイズやタイムスタンプなどのメタデータを調べる方法、FileAttachment アノテーションとして保存されているファイルを復元する方法について説明します。それぞれの例は、添付ワークフローを自動化し、文書の移植性を向上させ、ファイル管理を簡素化する実践的な手法を示しています。エンタープライズ文書システムを構築する場合でも、カスタム自動化スクリプトを構築する場合でも、開発者はこれらの方法を使用して PDF 文書内の埋め込みファイルを効率的に管理できます。
---

## PDF から特定の添付ファイルを抽出

Python と Aspose.PDF を使用して PDF ドキュメントから 1 つの埋め込みファイルを抽出します。添付ファイルを名前で検索し、その内容を取得して別のファイルとして保存します。PDF 内に保存されているレポート、ログ、サポートファイルなどの埋め込み文書にアクセスする場合に便利です。

1. 関数 '単一添付ファイルの抽出 () 'を定義します。
1. PDF ドキュメントを開きます。
1. 添付ファイルを検索します。
1. 添付ファイルの内容を抽出します。

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## 添付ファイルのメタデータを表示

このヘルパー関数は、ファイル仕様オブジェクトからメタデータ情報を出力します。通常、Aspose.PDF を使用して PDF に埋め込まれた添付ファイルを扱うときに使用されます。これにより、開発者はチェックサム、作成日、変更日、ファイルサイズなどの詳細を調べることができます。

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## すべての PDF 添付ファイルの抽出と検査

このコードスニペットは、Python と Aspose.PDF を使用して PDF ドキュメントからすべての埋め込みファイルを抽出する方法を示しています。各添付ファイルを指定されたフォルダーに保存するだけでなく、ファイル名、説明、MIME タイプ、チェックサム、タイムスタンプなどの詳細なメタデータも出力します。PDF ファイルに埋め込まれたコンテンツの監査、エクスポート、または処理に役立ちます。

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## PDF 添付注釈からファイルを抽出

Python と Aspose.PDF を使用して、PDF の添付ファイルアノテーションから埋め込みファイルを抽出します。最初のページで最初の添付注釈を検索し、埋め込まれたファイルを取得して、選択した出力ディレクトリに保存します。これは、PDF に標準の埋め込みファイルコレクションではなく、クリック可能な添付アイコンが含まれている場合に便利です。

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```