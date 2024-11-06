---
title: 新着情報
linktitle: 新着情報
type: docs
weight: 10
url: ja/python-net/whatsnew/
description: このページでは、Aspose.PDF for Python via .NETの最近のリリースで導入された最も人気のある新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Aspose.PDF 23.12の新機能

Aspose.PDF 23.12から、新しい変換機能が追加されました：

- PDFからMarkdownへの変換を実装

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- OFDからPDFへの変換を実装

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Python 3.6のサポートが終了しました。

## Aspose.PDF 23.11の新機能

23.11以降、隠しテキストを削除することが可能になりました。以下のコードスニペットを使用できます：

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # このオプションは、隠しテキストの置換後に他のテキストフラグメントが移動するのを防ぐために使用できます。
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```

## Aspose.PDF 23.8の新機能

23.8バージョン以降、増分更新検出の追加をサポートしています。

PDFドキュメントにおける増分更新検出の機能が追加されました。
 この関数は、ドキュメントがインクリメンタルアップデートで保存された場合に 'true' を返します。それ以外の場合は 'false' を返します。

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

また、23.8はネストされたチェックボックスフィールドを扱う方法をサポートしています。多くの記入可能なPDFフォームには、ラジオグループとして機能するチェックボックスフィールドがあります:

- 複数値チェックボックスフィールドを作成:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # 最初のチェックボックスグループオプションの値を設定
    checkbox.export_value = "option 1"
    # 既存のものの下に新しいオプションを追加
    checkbox.add_option("option 2")
    # 指定された矩形に新しいオプションを追加
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # 追加されたチェックボックスを選択
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- 複数値チェックボックスの値を取得および設定する:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # 許可された値は AllowedStates コレクションから取得できます
    # Value プロパティを使用してチェックボックスの値を設定します
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # 前に設定された値、例: "option 1"
    # 値は AllowedStates の任意の要素である必要があります
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # 値を "Off" に設定するか、Checked を false に設定することでチェックを外します
    checkbox.value = "Off"
    # または、代わりに:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- ユーザークリック時にチェックボックスの状態を更新する:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # 例えば、マウスクリックの座標
    # オプション 1: ページ上の注釈を確認する
    page = document.pages[5]
    for annotation in page.annotations:
        if(annotation.rect.contains(point)):
            widget = cast(ap.annotations.WidgetAnnotation, annotation)
            checkbox = cast(ap.forms.CheckboxField, widget.parent)
            if(annotation.active_state == "Off"):
                checkbox.value = widget.get_checked_state_name()
            else:
                checkbox.value = "Off"
        break
    # オプション 2: AcroForm 内のフィールドを確認する
    for widget in document.form:
        field = cast(ap.forms.Field, widget)
        if(field == None):
            continue
        checkBoxFound = False
        for annotation in field:
            if(annotation.rect.contains(point)):
                checkBoxFound = True
                if(annotation.active_state=="Off"):
                    annotation.parent.value = annotation.get_checked_state_name()
                else:
                    annotation.parent.value = "Off"
            if(checkBoxFound):
                break
```


## Aspose.PDF 23.7の新機能

バージョン23.7では、形状抽出の追加をサポートしています：

```python

    import aspose.pdf as ap

    input1_file = DIR_INPUT + "input_1.pdf"
    input2_file = DIR_INPUT + "input_2.pdf"

    source = ap.Document(input1_file)
    dest = ap.Document(input2_file)

    graphic_absorber = ap.vector.GraphicsAbsorber()
    graphic_absorber.visit(source.pages[1])
    area = ap.Rectangle(90, 250, 300, 400, True)
    dest.pages[1].add_graphics(graphic_absorber.elements, area)
```

また、テキストを追加するときのオーバーフローの検出機能もサポートされています：

```python

    import aspose.pdf as ap

    output_file = DIR_OUTPUT + "output.pdf"
    doc = ap.Document()
    paragraph_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan."
    fragment = ap.text.TextFragment(paragraph_content)
    rectangle = ap.Rectangle(100, 600, 500, 700, False)
    paragraph = ap.text.TextParagraph()
    paragraph.vertical_alignment = ap.VerticalAlignment.TOP
    paragraph.formatting_options.wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.rectangle = rectangle
    is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    while is_fit_rectangle == False:
        fragment.text_state.font_size -= 0.5
        is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    paragraph.append_line(fragment)
    builder = ap.text.TextBuilder(doc.pages.add())
    builder.append_paragraph(paragraph)
    doc.save(output_file)
```


## Aspose.PDF 23.6の新機能

HTML、Epubページのタイトルを設定する機能をサポート:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- これが追加されました

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Aspose.PDF 23.5の新機能

バージョン23.5からRedactionAnnotation FontSizeオプションの追加をサポートしています。このタスクを解決するには、次のコードスニペットを使用してください:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # 特定のページ領域に対するRedactionAnnotationインスタンスを作成
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # 削除注釈上に印刷されるテキスト
    annot.overlay_text = "(Unknown)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # 削除注釈上にオーバーレイテキストを繰り返す
    annot.repeat = False
    # 新しいプロパティがあります！
    annot.font_size = 20
    # 最初のページの注釈コレクションに注釈を追加
    doc.pages[1].annotations.add(annot, False)
    # 注釈をフラットにし、ページ内容を削除します（つまり、削除された注釈の下のテキストと画像を削除します）
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


Python 3.5のサポートは終了しました。Python 3.11のサポートが追加されました。

## Aspose.PDF 23.3の新機能

バージョン23.3では、画像に解像度を追加するサポートが導入されました。この問題を解決するために、2つの方法が使用できます：

```python

    import aspose.pdf as ap

    input_file = DIR_INPUT + "input.jpg"
    table = ap.Table()
    table.column_widths = "600"
    image = ap.Image()
    image.is_apply_resolution = True
    image.file = input_file
    for i in range(0, 2):
        row = table.rows.add()
        cell = row.cells.add()
        cell.paragraphs.add(image)

    page.paragraphs.add(table)
```

画像はスケールされた解像度で配置されます。または、FixedWidthまたはFixedHeightプロパティをIsApplyResolutionと組み合わせて設定することができます。

## Aspose.PDF 23.1の新機能

バージョン23.1以降、PrinterMark注釈の作成をサポートしています。

プリンターマークは、複数版のジョブのコンポーネントを識別し、生産中に一貫した出力を維持するのを助けるために、生産担当者がページに追加するグラフィックスシンボルまたはテキストです。
 印刷業界で一般的に使用される例には以下が含まれます：

- プレートを整列させるための登録ターゲット
- 色とインク密度を測定するためのグレースケールとカラーバー
- 出力メディアがどこでトリミングされるかを示すカットマーク

色とインク密度を測定するためのカラーバーオプションの例を示します。基本的な抽象クラスPrinterMarkAnnotationがあり、そこからColorBarAnnotationという子クラスが派生しています - これがこれらのストライプをすでに実装しています。例を確認しましょう：

```python

    import aspose.pdf as ap

    out_file = DIR_OUTPUT  + "ColorBarTest.pdf"
    doc = ap.Document()
    page = doc.pages.add()
    page.trim_box = ap.Rectangle(20, 20, 580, 820, True)
    add_annotations(page)
    doc.save(out_file)


def add_annotations(page: ap.Page):
    rect_black = ap.Rectangle(100, 300, 300, 320, True)
    rect_cyan = ap.Rectangle(200, 600, 260, 690, True)
    rect_magenta = ap.Rectangle(10, 650, 140, 670, True)
    color_bar_black = ap.annotations.ColorBarAnnotation(page, rect_black, ap.annotations.ColorsOfCMYK.BLACK)
    color_bar_cyan = ap.annotations.ColorBarAnnotation(page, rect_cyan, ap.annotations.ColorsOfCMYK.CYAN)
    color_ba_magenta = ap.annotations.ColorBarAnnotation(page, rect_magenta, ap.annotations.ColorsOfCMYK.BLACK)
    color_ba_magenta.color_of_cmyk = ap.annotations.ColorsOfCMYK.MAGENTA
    color_bar_yellow = ap.annotations.ColorBarAnnotation(page, ap.Rectangle(400, 250, 450, 700, True), ap.annotations.ColorsOfCMYK.YELLOW)
    page.annotations.add(color_bar_black, False)
    page.annotations.add(color_bar_cyan, False)
    page.annotations.add(color_ba_magenta, False)
    page.annotations.add(color_bar_yellow, False)
```
Also support the vector images extraction. ベクター画像の抽出もサポートします。以下のコードを使用してベクターグラフィックスを検出し、抽出してみてください。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```