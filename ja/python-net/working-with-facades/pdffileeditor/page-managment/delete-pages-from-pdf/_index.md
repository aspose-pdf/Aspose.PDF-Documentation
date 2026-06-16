---
title: PDF からページを削除
type: docs
weight: 20
url: /ja/python-net/delete-pages-from-pdf/
description: Python 用 Aspose.PDF を使用して、PDF ドキュメントから選択したページを削除します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ドキュメントから特定のページを削除する方法
Abstract: Aspose.PDF for Python を使用して PDF ドキュメントから選択したページを削除する方法を説明します。この例は、既存の PDF ファイルから特定のページをプログラムで削除し、削除したページなしで新しい文書を作成する方法を示しています。
---

PDF 文書には、削除する必要のある不要なページや機密ページが含まれている場合があります。Aspose.PDF for Python を使用すると、開発者はファイルを手動で編集しなくても、プログラムで PDF から特定のページを削除できます。

この例では、の delete メソッドを使用する方法を示しています [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) PDF ドキュメントからページを削除するクラス。削除するページ番号を指定することで、不要なページを除外した新しい PDF を作成できます。この機能は、レポートのクリーンアップ、機密情報の削除、カスタム文書抽出の準備に役立ちます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 削除するページを定義します。
1. ページを削除します。

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```