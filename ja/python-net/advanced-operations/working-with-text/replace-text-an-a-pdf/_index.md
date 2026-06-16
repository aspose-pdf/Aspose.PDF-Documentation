---
title: PDF 内のテキストを Python に置き換える
linktitle: PDF 内のテキストを置換
type: docs
weight: 40
url: /ja/python-net/replace-text-in-pdf/
description: ページ間のテキストの置換、ページ領域への変更の制限、正規表現の使用、テキストの削除など、PDF ファイル内のテキストを Python に置き換える方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内のテキストを置換および削除する
Abstract: この記事では、PDF ドキュメント内のテキストを .NET 経由で Python 用 Aspose.PDF に置き換える方法を説明します。全ページにわたるテキスト置換、ページ領域置換、正規表現マッチング、フォント置換、テキストレイアウト調整、表示または非表示テキストの削除について説明します。
---

このページでは、.NET 経由で Aspose.PDF for Python を使用して **PDF 内のテキストを Python に置き換える** 方法を説明します。

これらの例は、テキスト値の更新、不要なコンテンツの削除、特定のページ領域のテキストの置換、複数の PDF ページにわたるテキスト置換ルールの適用が必要な場合に使用します。

## PDF 内のテキストを Python に置き換える

### PDF ドキュメントのすべてのページのテキストを置換

{{% alert color="primary" %}}

Aspose.PDF を使用してオンラインでテキスト検索と置換を試すことができます [編集アプリ](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

既存のPDF文書の内容を更新または修正する場合、たとえば製品名の変更、タイプミスの修正、複数ページにわたる用語の更新など、テキストの置換は一般的な要件です。

.NET 経由の Python Aspose.PDF は、テキストの検索と置換をプログラムで行うための強力で効率的な方法を提供します。 [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) クラス。

この例は、PDF ドキュメント全体で特定のフレーズ（この場合は「Black cat」）のすべての出現箇所を検索し、それらを新しいフレーズ（「White dog」）に置き換える方法を示しています。

1. 検索フレーズと置換フレーズを指定します。検索するテキストと置換したいテキストを設定します。
1. PDF ドキュメントをロードします。
1. テキストアブソーバーを作成します。テキストフラグメントアブソーバーは検索フレーズで初期化されます。ドキュメントをスキャンして、指定されたフレーズのすべてのインスタンスを検索します。
1. アブソーバーをすべてのページに適用します。これにより、すべてのページが繰り返し処理され、フレーズに一致するテキストフラグメントが収集されます。
1. 見つかった各フラグメントを交換してください。「黒猫」のすべてのインスタンスを「白犬」に変更する必要があります。
1. 更新した PDF を保存します。

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

### 特定のページ領域のテキストを置換

場合によっては、文書全体を検索する代わりに、PDF ページの特定の領域内のテキストのみを置換する必要がある場合があります。たとえば、ヘッダー、フッター、または既知の位置にある表セルの更新などです。

.NET ライブラリ経由の Python 用 Aspose.PDF は、以下を利用してこの機能を有効にします。 [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 地域ベースのテキスト検索と組み合わせて。

この例は、特定のページの定義された長方形の領域内にあるターゲットフレーズのすべての出現箇所を検索して置換する方法を示しています。

1. 検索フレーズと置換フレーズを指定します。
1. PDF ドキュメントをロードします。
1. 検索用のテキストアブソーバーを作成します。TextFragmentAbsorber を初期化して目的のテキストを見つけます。
1. 検索エリアを制限します。長方形はページの X 座標と Y 座標の範囲を指定します。
1. 特定のページにアブソーバーを適用します。これにより、検索が実行され、指定した領域内の一致するテキストフラグメントが収集されます。
1. 見つかったテキストを置換します。定義した領域で「doc」が出現するたびに「DOC」になります。
1. 更新した PDF を保存します。

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

### フォントサイズを変更せずにテキストのサイズを変更およびシフト

PDF 内のテキストを置換する場合、フォントサイズを変更せずに、新しいテキストを特定の領域に収めたり再配置したりしたい場合があります。
Aspose.PDF for Python via .NET には、元のフォントサイズをそのまま維持したまま、テキストのレイアウトと間隔を調整するオプションが用意されています。

1. PDF ドキュメントをロードします。
1. 「TextFragmentAbsorber」を使用して、ページ上のすべてのテキストフラグメントを収集します。
1. 変更するフラグメントを選択します。
1. テキスト矩形をシフトしてサイズを変更します。
1. テキストの間隔を調整します。変更した四角形内にテキストが収まるように間隔調整を有効にします。
1. フラグメントテキストを置き換えます。
1. 更新した PDF を保存します。

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

### PDF の段落のサイズ変更とシフト

PDF で作業する場合、ページレイアウトと視覚的に一致させながら、段落を置き換えたり拡張したりする必要がある場合があります。Aspose.PDF では、フォントサイズを変更せずに、段落の境界となる四角形のサイズを変更したり、新しいテキストに合わせて間隔を調整したりできます。

1. PDF ドキュメントをロードします。
1. 「TextFragmentAbsorber」を使用して、ページ上のすべてのテキストフラグメントを収集します。
1. 変更するフラグメントを選択します。
1. 段落のサイズを変更して移動します。ページのメディアボックスを使用して境界を決定し、四角形を調整します。
1. 間隔を調整。これにより、フォントサイズを変更する代わりに、単語/文字間の間隔が変更されます。
1. フラグメントテキストを置き換えます。
1. 変更した PDF を保存します。

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

### テキストを置換してターゲット領域いっぱいに自動的にフォントを拡大

PDF 内のテキストを置き換えながら、フォントのサイズを自動的に変更して特定の四角形領域いっぱいに拡大します。.NET ライブラリ経由の Aspose.PDF for Python を使用すると、新しいテキストコンテンツが定義されたバウンディングボックス内に完全に収まるように、コードがフォントサイズと間隔を動的に調整し、手動でフォントを計算しなくても済みます。

1. PDF をロードします。
1. テキストフラグメントをキャプチャします。
1. 特定のフラグメントを選択します。
1. ターゲット長方形を定義します。
1. テキスト調整オプションを有効にします。
1. テキストを置換。
1. 文書を保存します。

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

### テキストを置換して長方形に収める

必要に応じて自動的にフォントサイズを小さくして、新しいコンテンツが元のテキストの長方形の領域に収まるようにしながら、PDF ドキュメント内のテキストを置き換えます。

.NET ライブラリ経由の Aspose.PDF for Python を使用すると、この関数はテキストレイアウトとフォントサイズの両方を動的に調整し、オーバーフローを防ぎながらドキュメント構造を維持します。

1. TextFragmentAbSorber オブジェクトを作成して、最初のページからすべてのテキストフラグメントを抽出します。
1. 特定のテキストフラグメントにアクセスします。
1. 置換領域を設定します。
1. テキスト調整オプションを設定します。次の 2 つのキー置換オプションを設定します。
    -フォントサイズ調整-新しいテキストが長すぎる場合、「SHRINK_TO_FIT」は自動的にフォントサイズを縮小します。
    -間隔調整-「ADJUST_SPACE_WIDTH」は間隔を均等に保ちます。
1. テキストを置換します。
1. 変更した PDF を保存します。

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

### プレースホルダーテキストの自動置換と PDF レイアウトの再配置

PDF 内のプレースホルダーテキスト (テンプレートやフォームなど) を、名前や会社情報などの実際のデータに置き換えます。
カスタムフォーマット (フォント、色、サイズ) を適用しながら、新しいテキストに合わせてページレイアウトを自動的に調整します。

1. PDF をインポートしてロードします。
1. プレースホルダー用のテキストアブソーバーを作成します。
1. アブソーバーをすべてのページに適用します。
1. 見つかったテキストフラグメントをループスルーします。
1. カスタムテキストフォーマットを適用します。
1. 更新した文書を保存します。

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

### 正規表現に基づいてテキストを置換

PDF 文書を扱う場合、電話番号やコード、日付のような形式など、特定の語句ではなくパターンに従ったテキストを置き換える必要がある場合があります。

.NET 経由の Aspose.PDF for Python では、TextFragmentAbSorber クラスの正規表現 (regex) を使用してこのような置換を実行できます。

この例は、テキストパターン (この場合は、1234-5678 など ####-### の形式に一致する任意のテキスト) を検索し、フォーマットされた文字列 'ABC1-2XZY' に置き換える方法を示しています。また、置換後のテキストのフォント、色、サイズをカスタマイズする方法も示します。

次のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

1. PDF ドキュメントをロードします。
1. 正規表現ベースのテキストアブソーバーを作成します。テキストフラグメントアブソーバーを正規表現パターンで初期化します。
1. 正規表現モードを有効にする。'True' パラメーターは正規表現検索モードを有効にします。
1. アブソーバーをページに適用します。これにより、定義された正規表現パターンに一致するすべてのテキストフラグメントがページからスキャンされます。
1. 各マッチを新しいテキストに置き換え、カスタムスタイルを適用します。
1. 変更した文書を保存します。

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

## フォントの置換または未使用のフォントの削除

### 既存の PDF ファイル内のフォントの置換

場合によっては、PDF 全体でフォントを標準化または更新する必要があります。たとえば、古いフォントや独自のフォントを、よりアクセスしやすいフォントに置き換える場合などです。Aspose.PDF for Python via .NET ライブラリを使用すると、プログラムでフォントの検出と置換を行うことができるため、一貫したタイポグラフィと文書の互換性を確保できます。

この例は、PDF ドキュメント全体で特定のフォント（「Arial-BoldMT」など）のすべてのインスタンスを別のフォント（たとえば、「Verdana」）に置き換える方法を示しています。

次のコードスニペットは、PDF ドキュメント内のフォントを置き換える方法を示しています。

1. PDF ドキュメントを開きます。
1. テキストフラグメントアブソーバーを初期化します。
1. Absorberを使用して、ドキュメント内のすべてのページからテキストフラグメントを抽出します。
1. フォントの識別と置換。このスクリプトは、フラグメントの現在のフォントが「Arial-BoldMT」かどうかをチェックします。true の場合、FontRepository.find_Font () メソッドを使用して「Verdana」フォントに置き換えます。
1. 変更した文書を保存します。

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

時間が経つにつれて、PDF 文書には未使用のフォントや埋め込みフォントが蓄積され、ファイルサイズが大きくなり、処理が遅くなることがあります。これらの未使用のフォントは、特にサイズの大きいまたは複雑な PDF を扱う場合、テキストを編集したり置換したりしても残ることがよくあります。

.NET ライブラリ経由の Aspose.PDF for Python には、TextEditOptions クラスを使用してこのような冗長フォントを効率的に削除する方法が用意されています。これにより、文書が最適化されるだけでなく、表示されているテキストに実際に適用されているフォントのみが使用されるようになります。

'remove_unused_fonts () 'メソッドは、冗長なフォントデータを削除することで PDF ファイルを最適化するシンプルで強力な方法です。

この例は、以下の方法を示しています。

- PDF をスキャンして未使用のフォントを探します。
- 安全に取り外してください。
- アクティブなテキストフラグメントを一貫したフォント（Times New Romanなど）に再割り当てします。

1. PDF ドキュメントを開きます。
1. テキスト編集オプションを設定します。これにより、表示されているテキストで現在使用されていない埋め込みフォントをすべて削除するようにエンジンに指示されます。
1. オプション付きのテキストアブソーバーを作成します。TextFragmentAbsorber は文書からテキストフラグメントを抽出して編集します。
1. 標準フォントを再割り当てします。アブソーバーがすべてのフラグメントを収集したら、それらを繰り返し処理して一貫性のあるフォントを適用します。
1. クリーンアップした PDF を保存します。

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

### PDF からテキストを削除

画像、図形、レイアウト構造はそのままに、PDFファイルからすべてのテキストコンテンツを削除します。
TextFragmentAbSorber を使用すると、コードは文書全体を効率的にスキャンし、各ページで見つかったすべてのテキストフラグメントを削除します。

1. PDF ドキュメントをロードします。
1. TextFragmentAbSorber オブジェクトは、PDF 内のテキストフラグメントを検出して処理するために作成されます。
1. すべてのテキストコンテンツを削除します。メソッド 'absorber.remove_all_text () 'は、読み込まれたドキュメントからすべてのテキスト要素を削除し、テキスト以外のコンポーネントはそのまま残します。
1. 更新した文書を保存します。

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

Aspose.PDF の TextFragmentAbsorber クラスを使用して、PDF ドキュメントの 1 ページからすべてのテキストを削除します。
文書全体の削除とは異なり、この方法ではページレベルのテキストクリーンアップが実行され、選択したページからのみテキストが削除され、他のページはすべて削除されません。

1. PDF ファイルをロードします。
1. テキストフラグメントアブソーバーインスタンスを作成します。
1. 最初のページからすべてのテキストを削除します。
1. 変更した PDF を保存します。

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

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の長方形領域からすべてのテキストを削除します。
この方法では、ページ全体を消去する代わりに、対象を絞ったテキスト削除が実行されるため、影響を受けるページの部分を正確に制御できます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを作成します。
1. ターゲット領域 (長方形) を定義します。
1. 指定された領域からテキストを削除します。
1. ドキュメントの残りの部分を保存します。
1. 変更した PDF を保存します。

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

### PDF ドキュメントからすべての隠しテキストを削除する

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の長方形領域からすべてのテキストを削除します。
この方法では、ページ全体を消去する代わりに、対象を絞ったテキスト削除が実行されるため、影響を受けるページの部分を正確に制御できます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを作成します。
1. ターゲット領域 (長方形) を定義します。
1. 指定された領域からテキストを削除します。
1. ドキュメントの残りの部分を保存します。
1. 変更した PDF を保存します。

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

## 関連テキストトピック

- [Python を使用して PDF 内のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [PDF へのテキストの追加](/pdf/ja/python-net/add-text-to-pdf-file/)
- [Python で PDF テキストを検索して抽出する](/pdf/ja/python-net/search-and-get-text-from-pdf/)
- [Python で PDF テキストをフォーマットする](/pdf/ja/python-net/text-formatting-inside-pdf/)
