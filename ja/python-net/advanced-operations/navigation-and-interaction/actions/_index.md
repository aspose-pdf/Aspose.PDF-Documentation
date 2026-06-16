---
title: Python で PDF アクションを操作する
linktitle: [アクション]
type: docs
weight: 20
url: /ja/python-net/actions/
description: Python を使用して PDF ファイル内のドキュメント、ページ、およびフォームアクションを追加、更新、削除する方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python で PDF ファイルにドキュメント、ページ、フォームアクションを追加
Abstract: この記事では、Aspose.PDF ライブラリを使用して PDF ドキュメント内のアクションを操作する方法について説明します。ドキュメントレベル、ページレベル、フォームレベルのインタラクションについて説明します。PDF アクションはユーザーイベントに応答する定義済みまたはカスタマイズ可能なトリガーで、ナビゲーション、JavaScript の実行、マルチメディアの再生、フォームの送信などを可能にします。このガイドでは、ドキュメントイベントの URL を開く、ページ固有のナビゲーションやズーム効果を作成する、印刷やナビゲーション用のインタラクティブボタンを追加する、フォーム要素を動的に非表示にする、フォームデータを Web エンドポイントに送信するなどのアクションを追加、カスタマイズ、削除する方法を示します。読者は、詳細な Python コード例を通して、ビューアの互換性に関する考慮事項を理解しながら、PDF のインタラクティブ機能を強化し、ワークフローを合理化し、PDF を外部システムと統合する方法を学びます。
---

PDF 内のアクションは、ユーザー操作または文書イベントによってトリガーされる定義済みのタスクです。これらは以下の目的で使用できます。

- 特定のページまたは外部ファイルに移動する
- Web リンクを開く
- マルチメディアコンテンツを再生
- JavaScript を実行
- フォームを送信またはリセットする
- フィールドを表示/非表示
- ズームレベルまたは表示モードの変更

ほとんどすべてのアクションは組み込みパラメータを使用しますが、カスタマイズできるものもあります。たとえば、JavaScript アクションなどです。

## PDF 起動アクションを追加

Python と Aspose.PDF を使用して、JavaScript ベースの起動アクションを PDF ドキュメントに追加します。ドキュメントを開く、保存する、印刷するなどの主要なドキュメントイベントにアクションを割り当てて、サポートされている PDF ビューアでこれらのイベントが発生したときに URL を自動的に起動できるようにします。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## PDF ドキュメントからのアクションの削除

アクションをクリーンアップ (または削除) するには、ハンドラーを次のように設定します `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## PDF ドキュメント内のページへのアクションの追加

ページにも同様のトリガーが用意されています。 `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## アクロフォームのアクション

### ナビゲーションアクションを使用する

PDF 標準では、特定の名前付きアクションのセットが規定されています。このようなアクションの意味は名前によって決まります。
次のコードでは、ナビゲーションにアクションを使用します。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

このコードにより、PDF ドキュメントの各ページにナビゲーションボタンが追加され、ユーザーがページ間を簡単に移動できるようになります。まず、ヘルパーメソッドを使用して入力ファイルと出力ファイルのフルファイルパスを決定します。button_config リストでは、4 種類のナビゲーションボタン ([最初のページ]、[前のページ]、[次のページ]、[最後のページ])、水平位置、トリガーされる定義済みのナビゲーションアクション、および特定のページで各ボタンを読み取り専用にするかどうかを決定するラムダ関数 (たとえば、[最初のページ] ボタンと [前のページ] ボタンは最初のページでは読み取り専用です) が定義されています。

次に、コードが PDF を読み込み、各ページを繰り返し処理します。ページごとにボタン構成をループ処理して、各ボタン用の長方形の領域を作成し、その位置に ButtonField をインスタンス化します。各ボタンには名前が付けられ、その読み取り専用ステータスは現在のページに基づいて設定され、クリックアクションは対応するナビゲーションアクションに割り当てられます。その後、ボタンが PDF フォームフィールドに追加されます。

すべてのボタンをすべてのページに追加すると、変更された文書が保存されます。この処理中にエラーが発生すると、エラーがキャッチされて印刷されます。このアプローチにより、すべてのページに一貫したナビゲーションコントロールが表示されるため、複数ページの PDF の使いやすさが向上します。1 つ微妙な点は、is_readonly_fn ラムダを使ってナビゲーションボタンが意味をなさない場合 (たとえば、最後のページの「次のページ」) にナビゲーションボタンを無効にすることです。これにより、ユーザーの混乱を防ぐことができます。

### 印刷アクションを使用する

PDF フォームを使用する場合、そのような PDF ドキュメントを印刷する必要があることがよくあります。この操作は PDF リーダーを使用して実行できますが、特別なボタンを使用して文書から直接実行したほうが便利な場合もあります。

実際、これは名前付きアクションの使用方法のもう1つの例です。これから使用します。 `PredefinedAction.FILE_PRINT` ([ファイル] → [印刷] メニュー項目の使用をシミュレート)。ただし、次の方法も使用できます `PredefinedAction.PRINT` または `PredefinedAction.PRINT_DIALOG`、あなた自身の目的に応じて。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

このコードスニペットは、PDF ドキュメントの最初のページに「印刷」ボタンを追加する方法を示しています。まず、指定された入力ファイルパスから PDF を読み込み、最初のページ (document.pages [1]) を選択します。

ページ上のボタンの位置とサイズには、長方形の領域が定義されます。次に、この場所に「PrintButton」という名前のボタンフィールドが作成され、その表示値が「Print」に設定されます。ボタンは、クリックすると (具体的にはマウスボタンを離したときに)、定義済みの「ファイルを印刷」アクションがトリガーされ、PDF ビューアに印刷ダイアログを開くように促すように構成されています。

ボタンの見栄えを良くするために、幅を 1 単位に設定した境界線を作成してボタンに割り当てます。その後、ボタンは最初のページの PDF フォームフィールドに追加されます。最後に、変更された文書は出力ファイルパスに保存されます。この方法により、PDF 内から文書を直接印刷する便利な方法が得られます。この機能の有効性は、PDF ビューアがインタラクティブなフォームフィールドと定義済みのアクションをサポートしているかどうかにかかっていることに注意してください。

### 「非表示」アクションを使用する

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

このコードスニペットは、クリックすると文書内のすべてのチェックボックスフィールドを非表示にするボタンを PDF の最初のページに追加します。まず、ヘルパーメソッドを使用して入力ファイルパスと出力ファイルパスをすべて解決します。PDF が読み込まれ、以下のインスタンスのフォームフィールドをフィルタリングしてすべてのチェックボックスフィールドを収集します。 `ap.CheckboxField`.

新しいボタンのページ上部付近の位置には、長方形の領域が定義されます。この場所に「HideButton」という名前のボタンフィールドが作成され、「チェックボックスを非表示」というラベルが付けられます。ボタンは (マウスボタンを離して) クリックすると HideAction がトリガーされ、収集されたすべてのチェックボックスが非表示になるように構成されています。

次に、ボタンが最初のページのフォームフィールドに追加され、変更された PDF が出力ファイルに保存されます。この処理中にエラーが発生した場合、エラーは検出されて印刷されます。この機能により、PDF 内のすべてのチェックボックスをすばやく非表示にできるので、文書の外観やワークフローをカスタマイズするのに役立ちます。

### 送信アクションを適用中

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

この関数は PDF フォームの最初のページに「送信」ボタンを追加し、ユーザーがフォームデータを指定の Web エンドポイントに送信できるようにします。まず、入力 PDF ファイルと出力 PDF ファイルのフルパスを作成し、Aspose.PDF ライブラリを使用して入力 PDF を読み込みます。

A `SubmitFormAction` ボタンがクリックされたときの動作を定義するために作成されます。アクションの URL はを使用して設定されます。 `FileSpecification` を指しています http://localhost:3000/submit, つまり、フォームデータはこの URL に送信されます。flags プロパティは組み合わされます。 `EXPORT_FORMAT` そして `SUBMIT_COORDINATES`フォームデータが標準形式でエクスポートされ、ボタンクリックの座標が送信に含まれていることを確認します。

ページ上のボタンの位置とサイズには、長方形の領域が定義されます。最初のページのこの場所に「SubmitButton」という名前のボタンフィールドが作成され、その表示値は「Submit」に設定されます。送信アクションはボタンのマウスリリースイベントに割り当てられるため、ユーザーがボタンをクリックするとアクションがトリガーされます。

最後に、ボタンが最初のページのフォームフィールドに追加され、変更された PDF が出力ファイルに保存されます。この処理中にエラーが発生した場合、エラーは検出されて印刷されます。このアプローチは、PDF ユーザーがフォームデータをサーバーエンドポイントに直接送信するためのユーザーフレンドリーな方法を提供します。

## 関連ナビゲーショントピック

- [Python を使用した PDF でのナビゲーションとインタラクション](/pdf/ja/python-net/navigation-and-interaction/)
- [Python を使用して PDF 内のブックマークを操作する](/pdf/ja/python-net/bookmarks/)
- [Python を使用して PDF 内のリンクを操作する](/pdf/ja/python-net/links/)
