---
title: PDFドキュメントでのアクションの操作
linktitle: アクション
type: docs
weight: 20
url: /ja/python-net/actions/
description: Aspose.PDF を使用して Python で PDF メタデータ（著者やタイトルなど）を抽出および管理する方法を探ります。
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python を使用した PDF ドキュメントのアクション処理
Abstract: 本記事では、Aspose.PDF ライブラリを使用して PDF ドキュメントのアクションを操作する方法を解説し、ドキュメントレベル、ページレベル、フォームレベルのインタラクションを網羅します。PDF アクションは、ユーザーイベントに応答する事前定義されたまたはカスタマイズ可能なトリガーで、ナビゲーション、JavaScript の実行、マルチメディア再生、フォーム送信などを可能にします。本ガイドでは、ドキュメントイベント時に URL を開く、ページ固有のナビゲーションやズーム効果を作成する、印刷やナビゲーション用のインタラクティブボタンを追加する、フォーム要素を動的に非表示にする、ウェブエンドポイントへフォームデータを送信するなどのアクションの追加、カスタマイズ、削除方法を示します。詳細な Python コード例を通じて、読者は PDF のインタラクティビティを向上させ、ワークフローを効率化し、ビューアの互換性に関する考慮事項を理解しながら外部システムと PDF を統合する方法を学びます。
---

PDF のアクションは、ユーザーの操作やドキュメントイベントによってトリガーされる事前定義されたタスクです。次のような用途に使用できます：

- 特定のページまたは外部ファイルへ移動する
- ウェブリンクを開く
- マルチメディアコンテンツを再生する
- JavaScript を実行する
- フォームを送信またはリセットする
- フィールドを表示/非表示にする
- ズームレベルや表示モードを変更する

ほとんどのアクションは組み込みパラメータを使用しますが、カスタマイズできるものもあります。例として、JavaScript アクションがあります。

## ドキュメントレベルのアクション

### PDF ドキュメントへのアクションの追加

PDF ドキュメントは、ドキュメントを開く際や特定のイベントに応答して実行されるコードを含む、複数のドキュメントレベルアクションをサポートしています。開く時のアクションには `open_action` プロパティを使用し、その他のアクションは `actions` コレクションで管理します。

`open_action` の使用方法を考えてみましょう。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

この例では、`app` オブジェクトの `launchURL` メソッドを呼び出し、デモ目的でウェブサイトを開きます。

他のアクションも同様の方法で追加できますが、若干の変更があります：

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

次のイベントに対してアクションを追加できます： `before_saving`、`before_printing`、`before_closing`、`after_saving`、`after_printing`。

このコードスニペットは、PDF のさまざまなドキュメントレベルイベントに JavaScript アクションを付与する方法を示しています。まず、指定した入力ファイルパスから既存の PDF ドキュメントを読み込みます。`document.open_action` プロパティは、ドキュメントが開かれたときに URL を起動する JavaScript アクションに設定され、PDF ビューアがユーザーのブラウザで `http://localhost:3000/open` を開くよう促します。

次に、2 つの追加 JavaScript アクションをドキュメントの `before_saving` と `before_printing` イベントに割り当てます。これらのアクションは、ユーザーがドキュメントの保存または印刷を試みたときにそれぞれトリガーされ、ブラウザで別々の URL（`/save` または `/print`）を起動します。これは、ユーザーの操作を追跡したり、ウェブベースのワークフローと統合したりするのに役立ちます。

### PDF ドキュメントからのアクションの削除

アクションを削除（またはクリア）するには、ハンドラを `None` に設定するだけです。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## ページレベルのアクション

### PDF ドキュメントのページへのアクションの追加

ページ向けにも同様のトリガーが提供されます： `on_open`、`on_close`。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

このページに 2 つのアクションを追加します。まず、ページが開かれたときにトリガーされる "GoTo" アクションを作成します。このアクションは、特定のズームレベルでページの左上隅へジャンプする明示的な宛先を使用します。次に、ページが閉じられたときに実行される JavaScript アクションを添付し、PDF ビューアにブラウザで特定の URL を開くよう指示します。最後に、変更されたドキュメントを指定された出力パスに保存します。

注意すべき微妙な点はページインデックスです。誤ったインデックスを使用すると予期しない動作やエラーが発生する可能性があります。また、PDF における JavaScript アクションはすべての PDF ビューアでサポートされているわけではないため、この機能がすべての環境で動作するわけではありません。

### PDF ページからのアクションの削除

`remove_actions` を使用してページのアクションを削除します。

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## AcroForms のアクション

### ナビゲーションアクションの使用

PDF 標準では、一部の名前付きアクションが定義されています。これらのアクションの意味は、その名前によって決まります。
以下のコードでは、ナビゲーション用のアクションを使用します。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

このコードは、PDF ドキュメントのすべてのページにナビゲーションボタンを追加し、ユーザーがページ間を簡単に移動できるようにします。まず、ヘルパーメソッドを使用して入力ファイルと出力ファイルのフルパスを決定します。`button_config` リストは、最初のページ、前のページ、次のページ、最後のページの 4 種類のナビゲーションボタンを定義し、それぞれの水平位置、トリガーする事前定義ナビゲーションアクション、および各ボタンが特定のページで読み取り専用にすべきかを判断するラムダ関数を含みます（例として、"First Page" と "Previous Page" ボタンは最初のページで読み取り専用になります）。

次にコードは PDF を読み込み、各ページを反復します。各ページについて、ボタン設定をループし、各ボタンの矩形領域を作成してその位置に `ButtonField` をインスタンス化します。各ボタンに名前を付け、現在のページに基づいて読み取り専用ステータスを設定し、クリックアクションを対応するナビゲーションアクションに割り当てます。その後、ボタンは PDF フォームフィールドに追加されます。

すべてのページにすべてのボタンが追加された後、変更されたドキュメントが保存されます。処理中にエラーが発生した場合はキャッチされ、出力されます。このアプローチにより、すべてのページが一貫したナビゲーションコントロールを持ち、マルチページ PDF の使い勝手が向上します。微妙な点として、`is_readonly_fn` ラムダを使用して意味がなくなるナビゲーションボタン（例：最後のページの "Next Page"）を無効化することで、ユーザーの混乱を防ぎます。

### 印刷アクションの使用

PDF フォームを使用する場合、これらの PDF ドキュメントを印刷する必要があることがよくあります。このアクションは PDF リーダーを使用して実行できますが、特別なボタンを使ってドキュメントから直接実行する方が便利なこともあります。

実際、これは名前付きアクションの使用例のもう一つです。`PredefinedAction.FILE_PRINT`（File→Print メニュー項目の使用をシミュレート）を使用しますが、用途に応じて `PredefinedAction.PRINT` や `PredefinedAction.PRINT_DIALOG` も使用できます。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

このコードスニペットは、PDFドキュメントの最初のページに「Print」ボタンを追加する方法を示しています。指定された入力ファイルパスからPDFをロードし、最初のページ（document.pages[1]）を選択することから始まります。

ページ上のボタンの位置とサイズのために長方形の領域が定義されます。その位置に ButtonField が作成され、名前は "printButton" とし、表示値を "Print" に設定します。ボタンは、クリックされたとき（具体的にはマウスボタンが離されたとき）に事前定義された "Print File" アクションをトリガーするように構成され、PDFビューアに印刷ダイアログを開かせます。

ボタンの外観を強化するために、幅1ユニットのボーダーを作成しボタンに割り当てます。その後、ボタンを最初のページの PDF フォームフィールドに追加します。最後に、変更されたドキュメントを出力ファイルパスに保存します。このアプローチは、ユーザーに PDF 内から直接ドキュメントを印刷する便利な方法を提供します。なお、この機能の有効性は、PDFビューアがインタラクティブなフォームフィールドと事前定義アクションをサポートしているかどうかに依存します。

### Hideアクションの使用

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

このコードスニペットは、PDF の最初のページにボタンを追加し、クリックされるとドキュメント内のすべてのチェックボックスフィールドを非表示にします。ヘルパーメソッドを使用して完全な入力および出力ファイルパスを解決することから始めます。PDF をロードし、フォームフィールドを `ap.CheckboxField` のインスタンスでフィルタリングしてすべてのチェックボックスフィールドを収集します。

ページ上部付近に新しいボタンの位置を示す長方形の領域が定義されます。その位置に ButtonField が作成され、名前は "HideButton"、ラベルは "Hide Checkboxes" とします。ボタンは、クリックされたとき（マウスボタンが離されたとき）に、収集したすべてのチェックボックスを非表示にする HideAction をトリガーするように構成されます。

その後、ボタンは最初のページのフォームフィールドに追加され、変更された PDF が出力ファイルに保存されます。このプロセス中にエラーが発生した場合、捕捉されて出力されます。この機能は、PDF 内のすべてのチェックボックスをすばやく非表示にする方法をユーザーに提供し、ドキュメントの外観やワークフローをカスタマイズする際に役立ちます。

### Submitアクションの適用

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

この関数は、PDF フォームの最初のページに "Submit" ボタンを追加し、ユーザーがフォームデータを指定された Web エンドポイントに送信できるようにします。まず、入力および出力 PDF ファイルの完全なパスを構築し、次に Aspose.PDF ライブラリを使用して入力 PDF をロードします。

`SubmitFormAction` が作成され、ボタンがクリックされたときの動作を定義します。アクションの url は `FileSpecification` を使用して http://localhost:3000/submit を指すように設定され、この URL にフォームデータが送信されます。flags プロパティは `EXPORT_FORMAT` と `SUBMIT_COORDINATES` を組み合わせ、フォームデータが標準形式でエクスポートされ、ボタンクリックの座標が送信に含まれることを保証します。

ページ上のボタンの位置とサイズのために長方形の領域が定義されます。最初のページのその位置に ButtonField が作成され、名前は "SubmitButton"、表示値は "Submit" に設定されます。Submit アクションはボタンのマウスリリースイベントに割り当てられ、ユーザーがボタンをクリックしたときにアクションがトリガーされます。

最後に、ボタンは最初のページのフォームフィールドに追加され、変更された PDF が出力ファイルに保存されます。このプロセス中にエラーが発生した場合は捕捉されて出力されます。このアプローチは、PDF ユーザーがフォームデータをサーバーエンドポイントに直接送信できるユーザーフレンドリーな方法を提供します。

