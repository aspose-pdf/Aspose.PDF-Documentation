---
title: Python で PDF ページを移動する方法
linktitle: PDF ページの移動
type: docs
weight: 100
url: /ja/python-net/move-pages/
description: Python でドキュメント内またはドキュメント間で PDF ページを移動する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でドキュメント間で PDF ページを移動する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF 内のページを移動する方法について説明します。1 ページまたは複数ページを別の文書に移動する方法と、文書と PageCollection API を使用して同じ PDF 内のページの位置を変更する方法を学びます。
---

## ある PDF ドキュメントから別の PDF ドキュメントにページを移動する

Aspose.PDF for Python では、ある PDF から別の PDF にページを移動できます（コピーするだけではありません）。選択したページを元の文書から削除し、新しい PDF ファイルに追加します。

これは、ある本からページを切り取って別の本に貼り付けるようなものです。移動すると、そのページは元のファイルには存在しなくなります。

1. を使用してソース PDF ドキュメントを開きます。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 移動する特定のページ (この場合は 2 ページ) を選択します。これは [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 新しい PDF ドキュメントを作成 (別の PDF ドキュメントをインスタンス化) [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 宛先ドキュメントを使用して、選択したページを新しい PDF ドキュメントに追加します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (たとえば、 `another_document.pages.add(page)`).
1. そのページを使用して元のドキュメントからページを削除します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (たとえば、 `document.pages.delete(index)`).
1. 両方の文書を保存します。

次のコードスニペットは、1 ページを移動する方法を示しています。

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## ある PDF ドキュメントから別の PDF ドキュメントに複数のページを移動する

コピーとは異なり、この操作では選択したページが転送され、ソースファイルからページが削除され、新しい PDF に保存されます。

1. 空の宛先ドキュメントを新規作成 (`Document`).
1. ソース文書から複数のページ (この場合は 1 ページと 3 ページ) を選択します。 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 選択したページをループ処理して、目的のドキュメントに各ページを追加します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 移動したページを含む宛先文書を保存します。
1. それを使用してソース文書から移動したページを削除します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 両方のバージョンを保存するには、変更したソースドキュメントを新しいファイル名で保存します。

次のコードスニペットは、複数のページを移動する方法を示しています。

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## 同じ PDF ドキュメント内の新しい場所へのページの移動

PDFレイアウトを再編成または編集するときによく必要な、特定のページを同じ文書内の別の位置に移動する方法を示します。

1. を使用して入力 PDF ドキュメントをロードします [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 移動したいページ (ページ 2) を選択してください — これは [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. ドキュメントの「」を使用してドキュメントの末尾に追加します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. を使用して元のページを以前の場所から削除します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 変更した文書を新しいファイルとして保存します。

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページを追加する](/pdf/ja/python-net/add-pages/)
- [Python で PDF ページを削除する方法](/pdf/ja/python-net/delete-pages/)
- [Python で PDF ページを抽出](/pdf/ja/python-net/extract-pages/)
