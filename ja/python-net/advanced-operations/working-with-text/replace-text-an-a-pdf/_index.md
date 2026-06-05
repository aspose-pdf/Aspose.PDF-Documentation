---
title: PythonでPDFのテキストを置換
linktitle: PDFのテキストを置換
type: docs
weight: 40
url: /ja/python-net/replace-text-in-pdf/
description: Python を使用して PDF ファイルのテキストを置換する方法を学びます。ページ跨ぎのテキスト置換、ページ領域に限定した変更、正規表現の使用、テキストの削除を含みます。
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルのテキストを置換および削除する
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントのテキストを置換する方法を示します。すべてのページにわたるテキスト置換、ページ領域の置換、正規表現マッチング、フォント置換、テキストレイアウトの調整、そして表示テキストまたは非表示テキストの削除についてカバーしています。
---

このページでは、Aspose.PDF for Python via .NET を使用して **Python で PDF のテキストを置換する方法** を示します。

テキスト値の更新、不要なコンテンツの削除、特定ページ領域のテキスト置換、または複数のPDFページにわたるテキスト置換ルールの適用が必要な場合は、これらの例を使用してください。

## PythonでPDFのテキストを置換

### PDFドキュメントの全ページのテキストを置換する

{{% alert color="primary" %}}

Aspose.PDF を使用して、オンラインでテキスト検索と置換を試すことができます。 [レダクションアプリ](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

テキストの置換は、既存の PDF ドキュメントの内容を更新または修正する際の一般的な要件です — たとえば、製品名の変更、誤字の修正、または複数ページにわたる用語の更新などがあります。

Aspose.PDF for Python via .NET は、テキストをプログラムで検索および置換するための強力かつ効率的な方法を提供します [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) クラス。

この例は、特定のフレーズ（この場合、"Black cat"）のすべての出現箇所を見つけ、PDF ドキュメント全体で新しいフレーズ（"White dog"）に置き換える方法を示しています。

1. 検索および置換フレーズを指定します。検索したいテキストと置換したいテキストを設定してください。
1. PDFドキュメントを読み込む。
1. Text Absorber を作成します。TextFragmentAbsorber は検索フレーズで初期化されます。それは、文書内の指定されたフレーズのすべての出現箇所をスキャンします。
1. Absorberをすべてのページに適用します。これにより、すべてのページを反復処理し、フレーズに一致するテキストフラグメントを収集します。
1. 見つかった各フラグメントを置き換えてください。"Black cat" のすべてのインスタンスは "White dog" に変更する必要があります。
1. 更新された PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 特定のページ領域のテキストを置換する

場合によっては、文書全体を検索するのではなく、PDF ページの特定の領域内だけでテキストを置換する必要があることがあります。例えば、既知の位置にあるヘッダー、フッター、または表のセルを更新する場合です。

Aspose.PDF for Python via .NET ライブラリは、この機能を利用して [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 領域ベースのテキスト検索と組み合わせて。

この例では、特定のページの定義された矩形領域内でターゲットフレーズのすべての出現箇所を検索して置換する方法を示しています。

1. 検索および置換フレーズを指定してください。
1. PDFドキュメントを読み込む。
1. 検索用の Text Absorber を作成します。目的のテキストを見つけるために TextFragmentAbsorber を初期化します。
1. 検索領域を制限します。矩形はページ上の x および y 座標の制限を指定します。
1. Absorber を特定のページに適用します。これにより、検索が実行され、指定された領域内の一致するテキストフラグメントが収集されます。
1. 検出されたテキストを置き換えます。定義された領域内の 'doc' のすべての出現が 'DOC' になります。
1. 更新された PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### フォントサイズを変更せずにテキストをリサイズしてシフト

PDF のテキストを置き換える際、フォントサイズを変更せずに新しいテキストを特定の領域内に収めたり位置を調整したりしたい場合があります。
Aspose.PDF for Python via .NET は、元の Font サイズをそのままに保ちながら、テキストのレイアウトと間隔を調整するオプションを提供します。

1. PDFドキュメントを読み込む。
1. ページ上のすべてのテキストフラグメントを 'TextFragmentAbsorber' で収集します。
1. 変更するフラグメントを選択してください。
1. テキスト矩形を移動してサイズを変更します。
1. テキスト間隔を調整する。変更された矩形内にテキストが収まるように、間隔調整を有効にします。
1. フラグメントテキストを置き換える。
1. 更新された PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### PDF内の段落をサイズ変更して移動する

PDF を扱う際、段落を置き換えたり拡張したりしながら、ページレイアウトと視覚的に揃えておく必要があることがあります。Aspose.PDF を使用すると、段落のバウンディング矩形のサイズを変更し、間隔を調整して新しいテキストに合わせることができ、フォントサイズを変更せずに済みます。

1. PDFドキュメントを読み込む。
1. ページ上のすべてのテキストフラグメントを収集するために 'TextFragmentAbsorber' を使用します。
1. 変更するフラグメントを選択してください。
1. 段落のサイズ変更とシフト。ページのメディアボックスを使用して境界を決定し、矩形を調整します。
1. スペーシングを調整します。これにより、フォントサイズを変更するのではなく、単語や文字間の間隔が変更されます。
1. フラグメントテキストを置き換える。
1. 変更されたPDFを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### テキストを置換し、フォントを自動的に拡大して対象領域を埋める

PDFのテキストを置き換え、特定の矩形領域に合わせてフォントを自動的にリサイズおよび拡張します。Aspose.PDF for Python via .NET ライブラリを使用すると、コードはフォントサイズと間隔を動的に調整し、新しいテキスト コンテンツが定義されたバウンディング ボックスにぴったり収まるようにします — 手動でフォント計算を行う必要はありません。

1. PDFを読み込む。
1. テキストフラグメントをキャプチャする。
1. 特定のフラグメントを選択。
1. ターゲット矩形を定義する。
1. テキスト調整オプションを有効にする。
1. テキストを置き換える。
1. ドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### テキストを置き換えて矩形に合わせる

PDFドキュメント内のテキストを置き換える際、必要に応じてフォントサイズを自動的に縮小し、新しいコンテンツが元のテキストの矩形領域内に収まるようにします。

Aspose.PDF for Python via .NET ライブラリを使用して、この関数はテキストのレイアウトとフォントサイズの両方を動的に調整し、ドキュメント構造を保持しながらオーバーフローを防止します。

1. 最初のページからすべてのテキストフラグメントを抽出するために、TextFragmentAbsorber オブジェクトを作成します。
1. 特定のテキストフラグメントにアクセスする。
1. 置換領域を設定します。
1. テキスト調整オプションを構成します。2つの主要な置換オプションを設定します:
    - フォントサイズ調整 - 'SHRINK_TO_FIT' は新しいテキストが長すぎる場合に自動的にフォントサイズを縮小します。
    - スペース調整 - 'ADJUST_SPACE_WIDTH' は間隔を比例的に保ちます。
1. テキストを置き換える。
1. 変更されたPDFを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### プレースホルダー テキストを自動的に置き換え、PDFレイアウトを再配置する

PDF（例えばテンプレートやフォーム）内のプレースホルダー文字列を、名前や企業情報などの実際のデータに置き換える。
新しいテキストに合わせてページレイアウトを自動的に調整し、カスタム書式設定（フォント、色、サイズ）を適用します。

1. PDFをインポートしてロードします。
1. プレースホルダー用の Text Absorber を作成する。
1. Absorber をすべてのページに適用する。
1. 見つかったテキストフラグメントをループ処理する。
1. カスタムテキスト書式設定を適用する。
1. 更新されたドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### 正規表現に基づいてテキストを置換する

PDF文書を扱う際、特定のフレーズではなくパターンに従うテキストを置換する必要がある場合があります。例えば、電話番号、コード、または日付形式のようなものです。

Aspose.PDF for Python via .NET は、TextFragmentAbsorber クラスを使用して正規表現（regex）によるこのような置換を実行できます。

この例では、テキストパターン（この場合、####-#### の形式に一致する任意のテキスト、例: 1234-5678）を見つけて、フォーマットされた文字列 'ABC1-2XZY' に置き換える方法を示しています。また、置き換えたテキストのフォント、色、サイズをカスタマイズする方法も示しています。

次のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

1. PDFドキュメントを読み込む。
1. 正規表現ベースの Text Absorber を作成します。正規表現パターンで TextFragmentAbsorber を初期化します。
1. 正規表現モードを有効にします。'True' パラメーターは正規表現検索モードを有効にします。
1. Absorber をページに適用します。これは、定義された正規表現パターンに一致するすべてのテキストフラグメントをページからスキャンします。
1. 各一致項目を新しいテキストに置き換え、カスタムスタイリングを適用します。
1. 変更されたドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## フォントを置き換えるか、未使用のフォントを削除する

### 既存のPDFファイルのFontを置き換える

場合によっては、PDF全体のフォントを標準化または更新する必要があります。たとえば、古いまたは専有フォントを、よりアクセスしやすいフォントに置き換えるといったケースです。Aspose.PDF for Python via .NET ライブラリを使用すると、プログラムでフォントを検出および置換でき、タイポグラフィの一貫性と文書の互換性を確保できます。

この例は、PDF ドキュメント全体で特定のフォント（例: 'Arial-BoldMT'）のすべてのインスタンスを別のフォント（例: 'Verdana'）に置き換える方法を示しています。

以下のコードスニペットは、PDF ドキュメント内のフォントを置き換える方法を示しています:

1. PDF ドキュメントを開く。
1. TextFragmentAbsorberを初期化します。
1. Absorber を使用して、文書のすべてのページからテキスト フラグメントを抽出します。
1. フォントの識別と置換。スクリプトはフラグメントの現在のフォントが ‘Arial-BoldMT’ かどうかを確認します。true の場合、FontRepository.find_font() メソッドを使用して ‘Verdana’ フォントに置き換えます。
1. 変更されたドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 未使用のフォントを削除する

時間が経つにつれて、PDF ドキュメントは未使用または埋め込まれたフォントが蓄積し、ファイルサイズが増大し、処理が遅くなることがあります。これらの未使用フォントは、テキストの編集や置換を行った後でも残ることが多く、特に大規模または複雑な PDF を扱う際に顕著です。

Aspose.PDF for Python via .NET ライブラリは、TextEditOptions クラスを使用してこのような冗長フォントを削除する効率的な方法を提供します。これにより、ドキュメントが最適化されるだけでなく、実際に可視テキストに適用されているフォントのみが使用されることが保証されます。

「'remove_unused_fonts()' メソッドは、冗長なフォントデータを削除することで PDF ファイルを最適化するシンプルながら強力な方法です。」

この例では、次のことを示します:

- PDF の未使用フォントをスキャンする。
- 安全に削除してください。
- アクティブなテキストフラグメントを一貫したFont（例: Times New Roman）に再割り当てします。

1. PDF ドキュメントを開く。
1. テキスト編集オプションを構成します。これは、エンジンに対して、表示テキストで現在使用されていない埋め込みフォントをすべて削除するよう指示します。
1. オプション付きで Text Absorber を作成します。TextFragmentAbsorber は、文書からテキストフラグメントを抽出して編集できます。
1. 標準フォントを再割り当てします。吸収器がすべてのフラグメントを収集したら、それらを反復処理し、一貫したフォントを適用します。
1. クリーンされた PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## すべてのテキストを削除

### PDFからテキストを削除する

PDFファイルからすべてのテキストコンテンツを削除し、画像、図形、レイアウト構造はそのまま保持する。
TextFragmentAbsorber を使用することにより、コードは文書全体を効率的にスキャンし、各ページで見つかったすべてのテキストフラグメントを削除します。

1. PDFドキュメントを読み込む。
1. PDF 内のテキストフラグメントを検出および処理するために、TextFragmentAbsorber オブジェクトが作成されます。
1. すべてのテキストコンテンツを削除します。メソッド 'absorber.remove_all_text()' は、読み込まれたドキュメントからすべてのテキスト要素を削除し、テキスト以外のコンポーネントはそのまま残します。
1. 更新されたドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 特定のページからすべてのテキストを削除する

Aspose.PDF の TextFragmentAbsorber クラスを使用して、PDF ドキュメントの単一ページからすべてのテキストを削除します。
全文書の削除とは異なり、このメソッドはページレベルのテキストクリーンアップを実行し、選択されたページからのみテキストを削除し、他のすべてのページはそのままにします。

1. PDFファイルを読み込む。
1. TextFragmentAbsorber のインスタンスを作成します。
1. 最初のページからすべてのテキストを削除します。
1. 変更されたPDFを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### PDFページの特定の領域からすべてのテキストを削除する

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の矩形領域からすべてのテキストを削除します。
ページ全体をクリアするのではなく、このメソッドは対象テキストの削除を実行し、ページのどの部分が影響を受けるかを正確に制御できます。

1. PDFドキュメントを読み込む。
1. TextFragmentAbsorber を作成します。
1. 対象領域（矩形）を定義する。
1. 指定された領域からテキストを削除します。
1. ドキュメントの残り部分を保持する。
1. 変更されたPDFを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### PDF文書からすべての隠しテキストを削除する

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の矩形領域からすべてのテキストを削除します。
ページ全体をクリアするのではなく、このメソッドは対象テキストの削除を実行し、ページのどの部分が影響を受けるかを正確に制御できます。

1. PDFドキュメントを読み込む。
1. TextFragmentAbsorber を作成します。
1. 対象領域（矩形）を定義する。
1. 指定された領域からテキストを削除します。
1. ドキュメントの残り部分を保持する。
1. 変更されたPDFを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## 関連テキスト トピック

- [Python を使って PDF のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [PDFにテキストを追加する](/pdf/ja/python-net/add-text-to-pdf-file/)
- [PythonでPDFテキストを検索し抽出する](/pdf/ja/python-net/search-and-get-text-from-pdf/)
- [PythonでPDFテキストをフォーマットする](/pdf/ja/python-net/text-formatting-inside-pdf/)
