---
title: Pythonを使用してPDFにテキストを追加する
linktitle: PDFにテキストを追加
type: docs
weight: 10
url: /python-net/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加する方法、HTMLフラグメントを追加する方法、またはカスタムOTFフォントを使用する方法を学びます。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFにテキストを追加する",
    "alternativeHeadline": "PDFにテキストを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add text to pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "この記事では、Python用Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加する方法、HTMLフラグメントを追加する方法、またはカスタムOTFフォントを使用する方法を学びます。"
}
</script>


## テキストの追加

1. Aspose.PDFを使用して入力PDFドキュメントを開きます。
1. テキストを追加したい特定のページを選択します。
1. TextFragmentオブジェクトを作成します。テキストフラグメントは「main text」という内容で作成されます。このフラグメントはページの座標(100, 600)に配置されます。
1. テキストプロパティの設定。フォントサイズ、フォントタイプ（Times New Roman）、背景色（ライトグレー）、前景色（赤）など、テキストのさまざまなプロパティが設定されます。
1. TextBuilderオブジェクトを作成します。選択したページでTextBuilderオブジェクトがインスタンス化されます。
1. テキストフラグメントを追加します。以前に作成されたテキストフラグメントは、TextBuilderオブジェクトを使用してPDFページに追加されます。
1. [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出し、出力PDFファイルを保存します。

以下のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています：

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 特定のページを取得
    page = document.pages[1]

    # テキストフラグメントを作成
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # テキストプロパティを設定
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # TextBuilderオブジェクトを作成
    builder = ap.text.TextBuilder(page)

    # テキストフラグメントをPDFページに追加
    builder.append_text(text_fragment)

    # 結果のPDFドキュメントを保存。
    document.save(output_pdf)             
```


## ストリームからフォントを読み込む

次のコードスニペットは、PDFドキュメントにテキストを追加する際にストリームオブジェクトからフォントを読み込む方法を示しています。

```python

    import aspose.pdf as ap

    # 入力PDFファイルを読み込む
    document = ap.Document()
    document.pages.add()
    # ドキュメントの最初のページ用にテキストビルダーオブジェクトを作成
    text_builder = ap.text.TextBuilder(document.pages[1])
    # サンプル文字列を持つテキストフラグメントを作成
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # TrueTypeフォントをストリームオブジェクトに読み込む
        font_stream = open(input_ttf, "rb")
        # テキスト文字列のフォント名を設定する
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # テキストフラグメントの位置を指定する
        text_fragment.position = ap.text.Position(10, 10)
        # テキストをTextBuilderに追加し、PDFファイル上に配置できるようにする
        text_builder.append_text(text_fragment)
        # 結果のPDFドキュメントを保存する。
        document.save(output_pdf)
```


## TextParagraphを使用してテキストを追加する

次のコードスニペットは、[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)クラスを使用してPDFドキュメントにテキストを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document()
    # Documentオブジェクトのページコレクションにページを追加
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # テキスト段落を作成
    paragraph = ap.text.TextParagraph()
    # 以降の行のインデントを設定
    paragraph.subsequent_lines_indent = 20
    # TextParagraphを追加する場所を指定
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # ワードラップモードを指定
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # テキストフラグメントを作成
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # フラグメントを段落に追加
    paragraph.append_line(fragment1)
    # 段落を追加
    builder.append_paragraph(paragraph)

    # 結果のPDFドキュメントを保存
    document.save(output_pdf)
```


## テキストセグメントにハイパーリンクを追加

このコードは、PDFドキュメント内で動的かつインタラクティブなコンテンツを作成する方法を示しており、外部リソースへのハイパーリンクを含みます。

PDFページは、1つ以上のTextFragmentオブジェクトで構成されている場合があり、各TextFragmentオブジェクトは1つ以上の[TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/)インスタンスを持つことができます。

この要件を達成するには、次のコードスニペットを試してください:

```python

    import aspose.pdf as ap

    # ドキュメントインスタンスを作成
    document = ap.Document()
    # PDFファイルのページコレクションにページを追加
    page1 = document.pages.add()
    # TextFragmentインスタンスを作成
    tf = ap.text.TextFragment("サンプルテキストフラグメント")
    # TextFragmentの水平位置を設定
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # サンプルテキストでテキストセグメントを作成
    segment = ap.text.TextSegment(" ... テキストセグメント1...")
    # TextFragmentのセグメントコレクションにセグメントを追加
    tf.segments.append(segment)
    # 新しいTextSegmentを作成
    segment = ap.text.TextSegment("Googleへのリンク")
    # TextFragmentのセグメントコレクションにセグメントを追加
    tf.segments.append(segment)
    # TextSegmentにハイパーリンクを設定
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # テキストセグメントの前景色を設定
    segment.text_state.foreground_color = ap.Color.blue
    # テキストの書式をイタリックに設定
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # 別のTextSegmentオブジェクトを作成
    segment = ap.text.TextSegment("ハイパーリンクのないTextSegment")
    # TextFragmentのセグメントコレクションにセグメントを追加
    tf.segments.append(segment)
    # ページオブジェクトの段落コレクションにTextFragmentを追加
    page1.paragraphs.add(tf)
    # 結果のPDFドキュメントを保存
    document.save(output_pdf)
```


## OTF フォントを使用する

Aspose.PDF for Python via .NET は、PDFファイルの内容を作成/操作する際にカスタム/TrueTypeフォントを使用する機能を提供しており、ファイルの内容をデフォルトのシステムフォント以外のフォントで表示できます。

```python

    import aspose.pdf as ap

    # 新しいドキュメントインスタンスを作成
    document = ap.Document()
    # PDFファイルのページコレクションにページを追加
    page = document.pages.add()
    # サンプルテキストでTextFragmentインスタンスを作成
    fragment = ap.text.TextFragment("OTFフォントでのサンプルテキスト")
    # または、システムディレクトリ内のOTFフォントのパスを指定することもできます
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # PDFファイル内にフォントを埋め込むことを指定し、正しく表示されるようにします。
    # 特定のフォントがターゲットマシンにインストール/存在していなくても
    fragment.text_state.font.is_embedded = True
    # Pageインスタンスの段落コレクションにTextFragmentを追加
    page.paragraphs.add(fragment)
    # 結果のPDFドキュメントを保存
    document.save(output_pdf)
```


## DOMを使用してHTML文字列を追加する

次のPythonコードは、Aspose.PDFライブラリを利用して、HTMLフラグメントを含むPDFドキュメントを作成します。

1. Documentをインスタンス化します。Documentクラスのインスタンスが作成され、PDFドキュメントを表します。
1. PDFドキュメントにページを追加します。
1. HTMLコンテンツを持つHtmlFragmentオブジェクトをインスタンス化します。
1. HTMLフラグメントのマージンを設定します。この場合、下部のマージンは10ポイントに、上部のマージンは200ポイントに設定されます。
1. ページにHTMLフラグメントを追加します。
1. PDFファイルを保存します。

```python

    import aspose.pdf as ap

    # Documentオブジェクトをインスタンス化
    doc = ap.Document()
    # PDFファイルのページコレクションにページを追加
    page = doc.pages.add()
    # HTMLコンテンツを持つHtmlFragmentをインスタンス化
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # 下部マージン情報を設定
    title.margin.bottom = 10
    # 上部マージン情報を設定
    title.margin.top = 200
    # ページの段落コレクションにHTMLフラグメントを追加
    page.paragraphs.add(title)
    # PDFファイルを保存
    doc.save(output_pdf)
```


### フットノートのカスタムラインスタイル

次の例では、PDFページの下部にフットノートを追加し、カスタムラインスタイルを定義する方法を示します。

```python

    import aspose.pdf as ap

    # Documentインスタンスの作成
    doc = ap.Document()
    # PDFのページコレクションにページを追加
    page = doc.pages.add()
    # GraphInfoオブジェクトの作成
    graph = ap.GraphInfo()
    # 線の幅を2に設定
    graph.line_width = 2
    # グラフオブジェクトの色を設定
    graph.color = ap.Color.red
    # ダッシュ配列の値を3に設定
    graph.dash_array = [3]
    # ダッシュフェーズの値を1に設定
    graph.dash_phase = 1
    # ページのフットノートラインスタイルをグラフに設定
    page.note_line_style = graph
    # TextFragmentインスタンスの作成
    text = ap.text.TextFragment("Hello World")
    # TextFragmentのフットノートの値を設定
    text.foot_note = ap.Note("テストテキスト1のフットノート")
    # ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page.paragraphs.add(text)
    # 2つ目のTextFragmentを作成
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # 2つ目のテキストフラグメントのフットノートを設定
    text.foot_note = ap.Note("テストテキスト2のフットノート")
    # PDFファイルの段落コレクションに2つ目のテキストフラグメントを追加
    page.paragraphs.add(text)
    # 結果のPDFドキュメントを保存
    doc.save(output_pdf)
```


### フットノートラベルをカスタマイズする

次のコードスニペットは、フットノートを含むテキストフラグメントを持つPDFドキュメントを作成する方法を示しています。

デフォルトでは、フットノート番号は1から始まる増分です。しかし、カスタムフットノートラベルを設定する必要がある場合があります。この要件を達成するために、次のコードスニペットを使用してください。

```python

    import aspose.pdf as ap

    # Documentインスタンスを作成
    document = ap.Document()
    # PDFのページコレクションにページを追加
    page = document.pages.add()
    # GraphInfoオブジェクトを作成
    graph = ap.GraphInfo()
    # 線の幅を2に設定
    graph.line_width = 2
    # グラフオブジェクトの色を設定
    graph.color = ap.Color.red
    # ダッシュ配列の値を3に設定
    graph.dash_array = [3]
    # ダッシュフェーズの値を1に設定
    graph.dash_phase = 1
    # ページのフットノートラインスタイルをグラフとして設定
    page.note_line_style = graph
    # TextFragmentインスタンスを作成
    text = ap.text.TextFragment("Hello World")
    # TextFragmentにフットノートを設定
    text.foot_note = ap.Note("フットノートはテストテキスト1用です")
    # フットノートにカスタムラベルを指定
    text.foot_note.text = " Aspose"
    # ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page.paragraphs.add(text)
    # 結果として得られるPDFドキュメントを保存
    document.save(output_pdf)
```


## フットノートに画像と表を追加する

このコードは、Aspose.PDF for Pythonを使用して、画像、テキスト、および表を含む複雑なフットノートを含むテキストフラグメントを持つPDFドキュメントを作成する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # 結果のPDFドキュメントを保存します。
    document.save(output_pdf)
```

## エンドノートの作成方法

エンドノートは、読者を論文の最後の特定の場所に参照させる情報源の引用であり、そこで引用または言及された情報や言葉の出典を見つけることができます。
 引用符や要約された文、または要約された資料を使用する場合、引用文の後に上付き数字が続きます。

以下のコードは、Aspose.PDF for Pythonを使用してPDFドキュメントにエンドノート付きのテキストフラグメントを追加する方法を示しています：

```python

    import aspose.pdf as ap

    # Documentインスタンスを作成
    document = ap.Document()
    # PDFのページコレクションにページを追加
    page = document.pages.add()
    # TextFragmentインスタンスを作成
    text = ap.text.TextFragment("Hello World")
    # TextFragmentにエンドノートの値を設定
    text.end_note = ap.Note("サンプルエンドノート")
    # FootNoteにカスタムラベルを指定
    text.end_note.text = " Aspose"
    # ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page.paragraphs.add(text)
    # 結果のPDFドキュメントを保存
    document.save(output_pdf)
```

## インライン段落としてのテキストと画像

PDFファイルのデフォルトのレイアウトはフローレイアウト（左上から右下）です。 したがって、PDFファイルに追加される新しい要素はすべて右下のフローに追加されます。しかし、さまざまなページ要素、つまり画像とテキストを同じレベル（次々と）で表示する必要がある場合があります。一つのアプローチとして、テーブルインスタンスを作成し、両方の要素を個々のセルオブジェクトに追加することができます。しかし、別のアプローチとしてインライン段落を使用することもできます。画像とテキストのIsInLineParagraphプロパティをtrueに設定することで、これらの段落は他のページ要素とインラインとして表示されます。

次のコードスニペットは、PDFファイルにテキストと画像をインライン段落として追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Documentインスタンスをインスタンス化する
    document = ap.Document()
    # Documentインスタンスのpagesコレクションにページを追加する
    page = document.pages.add()
    # TextFragmentを作成する
    text = ap.text.TextFragment("Hello World.. ")
    # ページオブジェクトのparagraphsコレクションにテキストフラグメントを追加する
    page.paragraphs.add(text)
    # 画像インスタンスを作成する
    image = ap.Image()
    # 画像をインライン段落として設定し、それが直後に現れるようにする
    # 前の段落オブジェクト（TextFragment）の
    image.is_in_line_paragraph = True
    # 画像ファイルパスを指定する
    image.file = input_jpg
    # 画像の高さを設定する（オプション）
    image.fix_height = 30
    # 画像の幅を設定する（オプション）
    image.fix_width = 100
    # ページオブジェクトのparagraphsコレクションに画像を追加する
    page.paragraphs.add(image)
    # 異なる内容でTextFragmentオブジェクトを再初期化する
    text = ap.text.TextFragment(" Hello Again..")
    # TextFragmentをインライン段落として設定する
    text.is_in_line_paragraph = True
    # 新しく作成したTextFragmentをページのparagraphsコレクションに追加する
    page.paragraphs.add(text)
    # 結果のPDFドキュメントを保存する。
    document.save(output_pdf)
```

## テキストを追加する際の文字間隔を指定する

次のコードスニペットは、文字間隔を増やしたテキスト断片を含むPDFドキュメントを生成する方法を示しています。

テキストは、TextFragmentインスタンスを使用してPDFファイルの段落コレクション内に追加することも、TextParagraphオブジェクトを使用して追加することもでき、TextStampクラスを使用してPDF内にテキストをスタンプすることもできます。

### TextBuilderとTextFragmentを使用する

```python

    import aspose.pdf as ap

    # Documentインスタンスを作成
    document = ap.Document()
    # Documentのページコレクションにページを追加
    document.pages.add()
    # TextBuilderインスタンスを作成
    builder = ap.text.TextBuilder(document.pages[1])
    # サンプルコンテンツでテキストフラグメントインスタンスを作成
    wide_fragment = ap.text.TextFragment("文字間隔を広げたテキスト")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # TextFragmentの文字間隔を指定
    wide_fragment.text_state.character_spacing = 2.0
    # TextFragmentの位置を指定
    wide_fragment.position = ap.text.Position(100, 650)
    # TextFragmentをTextBuilderインスタンスに追加
    builder.append_text(wide_fragment)
    # 結果のPDFドキュメントを保存
    document.save(output_pdf)
```


### Using TextParagraph

```python

    import aspose.pdf as ap

    # Document インスタンスを作成
    document = ap.Document()
    # Document の pages コレクションにページを追加
    document.pages.add()
    # TextBuilder インスタンスを作成
    builder = ap.text.TextBuilder(document.pages[1])
    # TextParagraph インスタンスをインスタンス化
    paragraph = ap.text.TextParagraph()
    # フォント名とサイズを指定するために TextState インスタンスを作成
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # 文字間隔を指定
    state.character_spacing = 1.5
    # テキストを TextParagraph オブジェクトに追加
    tt = "これは文字間隔のある段落です"
    paragraph.append_line(tt, state)
    # TextParagraph の位置を指定
    paragraph.position = ap.text.Position(100, 550)
    # TextParagraph を TextBuilder インスタンスに追加
    builder.append_paragraph(paragraph)
    # 結果として得られる PDF ドキュメントを保存
    document.save(output_pdf)
```

### Using TextStamp

```python

    import aspose.pdf as ap

    # Document インスタンスを作成
    document = ap.Document()
    # Document の pages コレクションにページを追加
    page = document.pages.add()
    # サンプルテキストで TextStamp インスタンスをインスタンス化
    stamp = ap.TextStamp("これは文字間隔のあるテキストスタンプです")
    # Stamp オブジェクトのフォント名を指定
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # TextStamp のフォントサイズを指定
    stamp.text_state.font_size = 12
    # 文字間隔を 1 に指定
    stamp.text_state.character_spacing = 1
    # Stamp の x_indent を設定
    stamp.x_indent = 100
    # Stamp の y_indent を設定
    stamp.y_indent = 500
    # ページインスタンスにテキストスタンプを追加
    stamp.put(page)
    # 結果として得られる PDF ドキュメントを保存
    document.save(output_pdf)
```


## マルチカラムPDFドキュメントを作成する

[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) は、PDFドキュメントのページ内に複数のカラムを作成する機能も提供しています。マルチカラムのPDFファイルを作成するためには、FloatingBoxクラスを使用します。このクラスは、FloatingBox内のカラムの数を指定するためのcolumn_infoプロパティを提供しており、column_spacingとwidthプロパティを使用してカラム間の間隔やカラムの幅を指定することもできます。

カラム間隔とはカラム間のスペースを指し、デフォルトのカラム間隔は1.25cmです。カラムの幅が指定されていない場合、[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) はページサイズとカラム間隔に基づいて各カラムの幅を自動的に計算します。

以下に、Graphsオブジェクト（Line）を使用して2つのカラムを作成する例を示します。それらはFloatingBoxのparagraphsコレクションに追加され、次にPageインスタンスのparagraphsコレクションに追加されます。

```python

    import aspose.pdf as ap

    document = ap.Document()
    # PDFファイルの左マージン情報を指定
    document.page_info.margin.left = 40
    # PDFファイルの右マージン情報を指定
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # セクションオブジェクトの段落コレクションに線を追加
    page.paragraphs.add(graph1)

    # 線の座標を指定
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # HTMLタグを含むテキストの文字列変数を作成
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> お金の詐欺を避ける方法</<strong> "
        + "</font>"
    )
    # HTMLテキストを含むテキスト段落を作成
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # セクションに4つのカラムを追加
    box.column_info.column_count = 2
    # カラム間の間隔を設定
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # 線を描くためのグラフオブジェクトを作成
    graph2 = ap.drawing.Graph(50, 10)
    # 線の座標を指定
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # セクションオブジェクトの段落コレクションに線を追加
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # PDFファイルを保存
    document.save(output_pdf)
```


## カスタムタブストップを使用する

このPythonコードスニペットは、タブストップを使用してテーブル構造をシミュレートするテキストフラグメントを含むPDFドキュメントを作成する方法を示しています。

ここでは、カスタムTABストップを設定する例を示します。

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "これはTABストップを使用してテーブルを形成する例です", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## PDFに透明なテキストを追加する方法

PDFファイルには、画像、テキスト、グラフ、添付ファイル、注釈オブジェクトが含まれており、TextFragmentを作成する際に、前景色、背景色の情報やテキストの書式を設定することができます。Aspose.PDF for Python via .NETは、アルファカラーチャネルを使用してテキストを追加する機能をサポートしています。

次のコードスニペットは、透明な色でテキストを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Documentインスタンスを作成
    document = ap.Document()
    # PDFファイルのページコレクションにページを作成
    page = document.pages.add()

    # サンプル値を持つTextFragmentインスタンスを作成
    text = ap.text.TextFragment(
        "透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト 透明なテキスト "
    )
    # アルファチャネルから色オブジェクトを作成
    color = ap.Color.from_argb(30, 0, 255, 0)
    # テキストインスタンスに色情報を設定
    text.text_state.foreground_color = color
    # ページインスタンスの段落コレクションにテキストを追加
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## フォントの行間を指定する

すべてのフォントには抽象的な四角形があり、その高さは同じフォントサイズの行間の意図された距離です。この四角形は em スクエアと呼ばれ、グリフのアウトラインが定義されるデザイングリッドです。入力フォントの多くの文字には、フォントの em スクエアの境界外に配置されるポイントがあるため、フォントを正しく表示するためには特別な設定を使用する必要があります。

次のコードスニペットは、PDF を読み込み、特定の行間を持つテキストフラグメントを TrueType フォントで追加し、変更された PDF ドキュメントを保存します。

```python

    import aspose.pdf as ap

    # 入力 PDF ファイルを読み込む
    document = ap.Document()
    # LineSpacingMode.FULL_SIZE を使用して TextFormattingOptions を作成する
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # サンプル文字列でテキストフラグメントを作成する
    text_fragment = ap.text.TextFragment("Hello world")

    # TrueType フォントをストリームオブジェクトに読み込む
    font_stream = open(input_ttf, "rb")
    # テキスト文字列のフォント名を設定する
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # テキストフラグメントの位置を指定する
    text_fragment.position = ap.text.Position(100, 600)
    # 現在のフラグメントの TextFormattingOptions を事前定義されたものに設定する（LineSpacingMode.FULL_SIZE を指す）
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # 結果の PDF ドキュメントを保存する
    document.save(output_pdf)
```


## テキスト幅を動的に取得する

このPythonコードスニペットは、Aspose.PDFでフォントオブジェクトとテキスト状態オブジェクトから得られる文字列の測定値を比較します:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("予期しないフォント文字列の測定!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("予期しないフォント文字列の測定!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("フォントと状態の文字列測定が一致しません!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>