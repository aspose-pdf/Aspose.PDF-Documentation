---
title: PythonでPDFをHTMLに変換
linktitle: PDFをHTML形式に変換
type: docs
weight: 50
url: /ja/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: このトピックでは、Aspose.PDF for Python via .NET ライブラリを使用して PDF ファイルを HTML 形式に変換する方法を示します。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PythonでPDFをHTMLに変換する方法
Abstract: この記事では、Python を使用して PDF ファイルを HTML に変換する包括的なガイドを提供します。特に Aspose.PDF for Python via .NET ライブラリを通じて行います。プログラムで変換を実現するために必要な手順を概説し、ソース PDF から `Document` オブジェクトを作成し、`HtmlSaveOptions` を使用してドキュメントを HTML 形式で保存することを強調しています。記事には、変換プロセスを示す簡潔な Python コードスニペットが含まれています。さらに、ユーザーが機能と変換品質を確認できるオンラインツールである Aspose.PDF の「PDF to HTML」アプリケーションも紹介しています。記事は関連トピックを網羅する構成となっており、Python を使用した PDF から HTML への変換について十分に理解できるようになっています。
---

## PDF を HTML に変換

**Aspose.PDF for Python via .NET** は、さまざまなファイル形式を PDF ドキュメントに変換したり、PDF ファイルをさまざまな出力形式に変換したりする多くの機能を提供します。この記事では、PDF ファイルを <abbr title="HyperText Markup Language">HTML</abbr> に変換する方法について説明します。Python の数行のコードだけで PDF を HTML に変換できます。ウェブサイトを作成したり、オンライン フォーラムにコンテンツを追加したりする場合、PDF を HTML に変換する必要があるかもしれません。PDF を HTML に変換する方法の一つは、Python をプログラムで使用することです。

{{% alert color="success" %}}
**PDF をオンラインで変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html) を提供しており、機能と品質を調査できます。

[![Aspose.PDF 無料アプリで PDF を HTML に変換](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

手順: PythonでPDFをHTMLに変換

1. ソース PDF ドキュメントを使用して [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトのインスタンスを作成します。
1. [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) に保存するために、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 指定フォルダーに画像を保存して PDF を HTML に変換

この関数は、Aspose.PDF for Python via .NET を使用して PDF ファイルを HTML 形式に変換します。抽出されたすべての画像は、HTML ファイルに埋め込む代わりに指定されたフォルダーに保存されます。

1. HTML 保存オプションを構成します。
1. 外部画像として HTML を保存します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF をマルチページ HTML に変換

この関数は、PDF ファイルをマルチページ HTML に変換します。各 PDF ページが個別の HTML ファイルとしてエクスポートされます。これにより、出力のナビゲーションが容易になり、大きな PDF の読み込み時間が短縮されます。

1. 'ap.Document' を使用してソース PDF をロードします。
1. 'HtmlSaveOptions' を作成し、'set split_into_pages' を設定します。
1. ページを別々のファイルに分割して、ドキュメントを HTML として保存します。
1. 確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 指定フォルダーに SVG 画像を保存して PDF を HTML に変換

この関数は、PDF を HTML 形式に変換し、すべての画像を SVG ファイルとして指定フォルダーに保存します。HTML に直接埋め込む代わりです。

1. 'ap.Document' を使用してソース PDF をロードします。
1. 'HtmlSaveOptions' を作成し、'set special_folder_for_svg_images' を対象フォルダーに設定します。
1. 外部 SVG 画像としてドキュメントを HTML に保存します。
1. 確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を HTML に変換し、圧縮 SVG 画像を保存

このスニペットは、PDF を HTML 形式に変換し、すべての画像を指定フォルダーに SVG ファイルとして保存し、ファイルサイズを削減するために圧縮します。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'HtmlSaveOptions' を作成し、
- 'special_folder_for_svg_images' を設定して、SVG 画像を外部に保存します。
- 'compress_svg_graphics_if_any' を有効にして、SVG 画像を圧縮します。
1. 圧縮された外部 SVG 画像としてドキュメントを HTML に保存します。
1. 確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 埋め込みラスター画像の制御で PDF を HTML に変換

このスニペットは、PDF を HTML 形式に変換し、ラスター画像を PNG ページ背景として埋め込みます。このアプローチにより、画像の品質とページレイアウトが HTML 内で保持されます。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'HtmlSaveOptions' を作成し、'raster_images_saving_mode' を 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND' に設定します。
1. ラスタ画像を埋め込んだ状態でドキュメントを HTML として保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を本文のみの HTML ページに変換

この関数は PDF を HTML 形式に変換し、余分な 'html' や 'head' タグのない 'body-only' コンテンツを生成し、出力を別々のページに分割します。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'HtmlSaveOptions' を作成し、設定します：
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' を使用して 'body' コンテンツのみを生成します。
- 'split_into_pages' を使用して各 PDF ページごとに別々の HTML ファイルを作成します。
1. 指定したオプションでドキュメントを HTML として保存します。
1. 確認メッセージを表示します。

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を透明テキストレンダリングで HTML に変換

この関数は PDF を HTML 形式に変換し、影付きテキストを含むすべてのテキストを透明にレンダリングします。これにより視覚的忠実度を保ちつつ、出力 HTML で柔軟なスタイリングが可能になります。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'HtmlSaveOptions' を作成し、設定します：
- 'save_transparent_texts' を使用して通常のテキストを透明にレンダリングします。
- 'save_shadowed_texts_as_transparent_texts' を使用して影付きテキストを透明にレンダリングします。
1. 透明テキストレンダリングでドキュメントを HTML として保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF をドキュメントレイヤーレンダリングで HTML に変換

この関数は PDF を HTML 形式に変換し、マークされたコンテンツを出力 HTML の別々のレイヤーに変換することでドキュメントのレイヤーを保持します。これにより、注釈、背景、オーバーレイなどのレイヤー要素が正確にレンダリングされます。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'HtmlSaveOptions' を作成し、レイヤーを保持するために 'convert_marked_content_to_layers' を有効にします。
1. レイヤー化されたコンテンツでドキュメントを HTML として保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


