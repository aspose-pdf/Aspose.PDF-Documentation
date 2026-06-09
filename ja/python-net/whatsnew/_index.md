---
title: 新着情報
linktitle: 新着情報
type: docs
weight: 10
url: /ja/python-net/whatsnew/
description: このページでは、最近のリリースで導入された、.NET 経由の Python 用 Aspose.PDF の最も人気の高い新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2026-06-09"
TechArticle: false
---

## Aspose.PDF 26.3 の新機能

**.NET 経由の Python 用 Aspose.pdf ** 26.3 では、以下を追加しました。

PDF 最適化中の無損失イメージストリームの再圧縮。OptimizationOptions.CompressAllContentStreams プロパティでも、対象となる画像 XObject ストリームが flateDecode で圧縮されるようになりました。これにより、画質を損なわずにファイルサイズを小さくすることができます。

```python
import aspose.pdf as ap


def optimize_pdf_with_loss_less_image_stream_recompression(infile, outfile):
    with ap.Document(infile) as document:
        optimize_options = ap.optimization.OptimizationOptions()
        optimize_options.subset_fonts = True
        optimize_options.allow_reuse_page_content = True
        optimize_options.compress_objects = True
        optimize_options.link_duplicate_streams = True
        optimize_options.remove_unused_objects = True
        optimize_options.remove_unused_streams = True
        # Compress content streams and eligible image streams
        optimize_options.compress_all_content_streams = True
        # Optimize PDF document
        document.optimize_resources(optimize_options)
        # Save optimized PDF document
        document.save(outfile)
```

最適化中、画像の再圧縮が、選択した ImageCompressionOptions.encoding 設定と一致するようになりました。これにより、画像のサイズ変更、解像度の制限、および品質制御に加えて、Jpeg2000またはFlateを使用した場合の結果の一貫性が高まります。

```python
import aspose.pdf as ap


def optimize_pdf_images_with_selected_encoding(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as pdf:
        # Configure optimization options
        optimize_options = ap.optimization.OptimizationOptions()
        optimize_options.allow_reuse_page_content = False
        optimize_options.compress_objects = True
        optimize_options.link_duplicate_streams = False
        optimize_options.remove_unused_objects = True
        optimize_options.remove_unused_streams = True
        optimize_options.image_compression_options.compress_images = True
        optimize_options.image_compression_options.resize_images = True
        optimize_options.image_compression_options.max_resolution = 130
        optimize_options.image_compression_options.image_quality = 100
        optimize_options.image_compression_options.encoding = (
            ap.optimization.ImageEncoding.FLATE
        )
        optimize_options.image_compression_options.version = (
            ap.optimization.ImageCompressionVersion.MIXED
        )

        # Optimize PDF document resources
        pdf.optimize_resources(optimize_options)
        # Save optimized PDF document
        pdf.save(outfile)
```

PDF ドキュメントを画像または HTML として保存する際のコメントのレンダリングがサポートされ、注釈付きドキュメントをエクスポートして外部の PDF ビューアで共有する場合に、レビューマークアップが視覚的に表示されるようになります。

```python
import aspose.pdf as ap


def render_comments_to_image_and_html(infile, outfile, output_png):
    # Open PDF document
    with ap.Document(infile) as document:
        # Save the first page to PNG with comments rendered
        device = ap.devices.PngDevice()
        device.process(document.pages[1], output_png)
        # Save the first page to HTML with comments rendered
        options = ap.HtmlSaveOptions()
        options.explicit_list_of_saved_pages = [1]
        options.use_z_order = True
        document.save(outfile, options)
```

特にページをモノクロ TIFF 画像に書き出す場合の、大量のラスタライズシナリオで PDF から TIFF へのレンダリングパフォーマンスが向上しました。

```python
import aspose.pdf as ap


def convert_pdf_to_tiff(infile, data_dir):
    # Open PDF document
    with ap.Document(infile) as document:
        # Create Resolution object
        resolution = ap.devices.Resolution(300)

        # Create TiffSettings object
        tiff_settings = ap.devices.TiffSettings()
        tiff_settings.compression = ap.devices.CompressionType.CCITT4
        tiff_settings.shape = ap.devices.ShapeType.NONE
        tiff_settings.skip_blank_pages = False
        tiff_settings.depth = ap.devices.ColorDepth.FORMAT_1BPP

        # Create TIFF device
        tiff_device = ap.devices.TiffDevice(resolution, tiff_settings)
        for i in range(1, len(document.pages) + 1):
            target_file_name = data_dir + "Asposeout-" + str(i) + ".tif"
            tiff_device.process(document, i, i, target_file_name)
```

## Aspose.PDF 26.2 の新機能

Aspose.PDF 26.2 では RTF から PDF への変換のサポートが導入されました。この機能により、開発者はリッチテキストフォーマット (RTF) 文書を PDF ファイルに直接変換できます。

RTF は、マイクロソフトが最初に開発した、広くサポートされているクロスプラットフォームのドキュメント形式です。フォント、色、太字や斜体のテキスト、埋め込み画像などの基本的な書式を維持しながら、さまざまなワープロアプリケーション間で文書を交換できるように設計されています。

```python
import aspose.pdf as ap


def convert_rtf_to_pdf(infile, outfile):
    # Initialize RTF load options
    options = ap.RtfLoadOptions()
    # Open RTF document
    with ap.Document(infile, options) as document:
        # Save PDF document
        document.save(outfile)
```

このコードスニペットは、Aspose.PDF for Python を使用して PDF ページの既存のコンテンツの後に表を挿入する方法を示しています。

このスクリプトは既存の PDF ドキュメントを開き、最初のページの現在のコンテンツのバウンディングボックスを計算します。この情報を使用して既存のコンテンツの終了位置を見つけ、最後の要素の下に新しい表を配置し、表の開始前に指定された余白を残します。

次に、テーブルが作成され、ループを使用して複数の行と列が入力されます。表の構造と内容を設定すると、表はページの段落コレクションに追加されます。最後に、更新された文書は新しい PDF ファイルとして保存されます。

```python
import aspose.pdf as ap


def add_table_after_last_element(infile, outfile):
    # Load source PDF document
    with ap.Document(infile) as document:
        # Initializes a new instance of the Table
        table = ap.Table()
        # Determine the existing content area on the page
        content_area_lly = document.pages[1].calculate_content_b_box().lly
        top_margin = 20
        # Add the table after the existing content, with the 20pt margin before the table.
        table.top = document.pages[1].rect.height - (content_area_lly - top_margin)
        # Set the top margin for the new pages added.
        document.page_info.margin.top = top_margin
        # Create a loop to add 10 rows
        for row_count in range(1, 11):
            # Add row to table
            row = table.rows.add()
            # Add table cells
            row.cells.add("Column (" + str(row_count) + ", 1)")
            row.cells.add("Column (" + str(row_count) + ", 2)")
            row.cells.add("Column (" + str(row_count) + ", 3)")

        # Add table object to first page of input document
        document.pages[1].paragraphs.add(table)
        # Save updated document containing table object
        document.save(outfile)
```

Aspose.PDF for Python を使用して PDF ドキュメントから目に見えないテキストを検出して削除します。

```python
import aspose.pdf as ap


def remove_invisible_text(infile, outfile):
    with ap.Document(infile) as pdf_doc:
        for page in pdf_doc.pages:
            absorber = ap.text.TextFragmentAbsorber()
            page.accept(absorber)
            fragments_to_remove = [
                x
                for x in absorber.text_fragments
                if (
                    x.text_state.invisible
                    or x.text_state.rendering_mode
                    == ap.text.TextRenderingMode.INVISIBLE
                    or (
                        x.text_state.foreground_color is not None
                        and x.text_state.foreground_color.a == 0
                    )
                )
            ]
            for fragment in fragments_to_remove:
                absorber.text_fragments.remove(
                    fragment
                )  # Now properly removes text from document
        pdf_doc.save(outfile)
```

## Aspose.PDF 26.1 の新機能

**.NET 経由の Python 用 Aspose.pdf ** 26.1 では、以下を追加しました。

1. パフォーマンスの向上 — 文書にテキストを追加する際のパフォーマンスの低下と全体的なパフォーマンスの問題を解決しました。
1. レンダリング精度の向上 — PDF の左側で縦書きのテキストが欠落していた問題を修正し、PDF から PNG への変換中に漢字がレンダリングされる問題を修正しました。
1. HTML 変換の改善 — API が HTML から PDF への変換で線の色を考慮するようになり、XFA から標準への変換におけるテキストのオーバーラップの問題が修正されました。
1. 文書構造のバグ修正 — NumberingStyleが見出しオブジェクトで正しく機能するようになり、PDFからHTMLに変換されたテキストの色が保持されるようになりました。

## Aspose.PDF 25.12 の新機能

論理構造情報を保持したまま、HTML 文書を PDF に変換します。作成された PDF は、構造化された文書コンテンツに依存するアクセシビリティ、タグ付け、およびダウンストリーム処理に適しています。

```python
import aspose.pdf as ap


def convert_html_to_pdf_with_logical_structure(self, infile, outfile):
    # Initialize HtmlLoadOptions
    options = ap.HtmlLoadOptions()
    # Convert HTML markup to PDF logical structure elements
    options.create_logical_structure = True
    # Open PDF document
    with ap.Document(infile, options) as document:
        # Save PDF document
        document.save(outfile)
```

デジタル署名された PDF を分析して、署名の対象とならないコンテンツを特定して報告します。文書の整合性の検証、署名済み PDF の監査、署名後の変更の検出に使用できます。

```python
import aspose.pdf as ap


def extract_unsigned_content(self, infile):
    # Open PDF document
    with ap.Document(infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create an instance of UnsignedContentAbsorber
            unsigned_content = ap.security.UnsignedContentAbsorber(signature)
            # Try to get unsigned content
            result = unsigned_content.try_get_content()
            # Print information about unsigned content
            print(result.message)
            print(result.coverage)
            print(result.unsigned_content.pages.length)
            print(result.unsigned_content.forms.length)
```

## Aspose.PDF 25.11 の新機能

この関数は、2 つの PDF ドキュメントの特定のページを比較し、視覚的な差分を並べて生成します。比較オプションと色をカスタマイズすることで、空白などのわずかな違いは無視しながら、意味のある変更箇所を強調表示します。

```python
import aspose.pdf as ap


def comparing_specific_pages(self, infile1, infile2, outfile):
    # Open PDF documents
    with ap.Document(infile1) as document1:
        with ap.Document(infile2) as document2:
            options = ap.comparison.SideBySideComparisonOptions()
            options.additional_change_marks = True
            options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES
            options.delete_color = ap.Color.dark_gray
            options.insert_color = ap.Color.light_yellow
            # Compare
            ap.comparison.SideBySidePdfComparer.compare(
                document1.pages[1], document2.pages[1], outfile, options
            )
```

25.11 バージョンでの隠しデータの削除とページのラスタライズ

```python
import aspose.pdf as ap


def clear_hidden_data(self, infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        # Create preconfigured “all-enabled” options (except conversion to images):
        options = ap.security.hiddendatasanitization.HiddenDataSanitizationOptions.all()
        # Additionally enable page conversion to images with a specified DPI:
        options.convert_pages_to_images = True
        options.image_dpi = 200
        # Create the sanitizer with the specified options
        sanitizer = ap.security.hiddendatasanitization.HiddenDataSanitizer(options)
        # Sanitize the document
        sanitizer.sanitize(document)
        # Save the sanitized PDF document
        document.save(outfile)
```

フォントサブセットとコンテンツストリーム圧縮によるリソースの最適化 25.11 バージョン。

```python
import aspose.pdf as ap


def optimize_resources_with_font_subsetting(self, infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        # Configure optimization options
        optimize_options = ap.optimization.OptimizationOptions()
        optimize_options.subset_fonts = True
        optimize_options.allow_reuse_page_content = True
        optimize_options.compress_objects = True
        optimize_options.link_duplicate_streams = True
        optimize_options.remove_unused_objects = True
        optimize_options.remove_unused_streams = True
        optimize_options.compress_all_content_streams = True
        # Optimize PDF document
        document.optimize_resources(optimize_options)
        # Save the optimized PDF document
        document.save(outfile)
    # Display file size reduction
    original_file = os.path.getsize(infile)
    optimized_file = os.path.getsize(outfile)
    print(
        f"Original file size: {original_file} bytes. Optimized file size: {optimized_file} bytes."
    )
```

## Aspose.PDF 25.10 の新機能

PDF レイヤーの可視性制御の強化 — このリリースでは、PDF レイヤーの初期表示状態をプログラムで定義し、PDF ビューアーでの表示が変化しないようにロックする機能が導入されました。

新しい「layer.default_state」プロパティでは、DefaultState プロパティを使用してレイヤーのデフォルトの可視性を表示または非表示に設定できます。これにより、複雑なレイヤー化された PDF 文書の管理をきめ細かく制御でき、ユーザーの可視性動作も予測可能になります。

```python
import aspose.pdf as ap


def manage_layer_visibility(self, infile, outfile):
    # Create a new PDF document
    with ap.Document() as document:
        # Add a page to the document
        page = document.pages.add()
        page.set_page_size(500, 500)
        # Load an image from a file stream
        with io.FileIO(infile, "r") as stream:
            # Create a new layer with an ID and a name
            layer = ap.Layer("1", "testlayer")
            # Set the initial visibility state of the layer to hidden
            layer.default_state = ap.DefaultState.HIDDEN
            # Add the image to the page's resources
            image_name = page.resources.images.add(stream)
            # Add operators to the layer's contents to display the image
            layer.contents.append(ap.operators.GSave())
            layer.contents.append(ap.operators.ConcatenateMatrix(500, 0, 0, 500, 0, 0))
            layer.contents.append(ap.operators.Do(image_name))
            layer.contents.append(ap.operators.GRestore())
            # Lock the layer to prevent its visibility from being changed in the PDF viewer
            layer.lock()
            # Add the layer to the page
            page.layers.append(layer)
        # Save the PDF document
        document.save(outfile)
```

## Aspose.PDF 25.9 の新機能

25.9リリースでは、アクセシビリティの向上、コンプライアンスサポートの強化、タグ付き画像や文書標準を扱うための新しいAPI機能が導入されています。

1. PDF を PDF/E-1 フォーマットに変換します。
1. メモリストリームからタグ付き画像を追加します。

### PDF を PDF/E-1 フォーマットに変換

Aspose.PDF for Python ライブラリの 25.9 バージョンでは、PDF/E-1 形式への変換が可能です。この形式の詳細については、以下を参照してください。 [ファイルフォーマットドキュメント](https://docs.fileformat.com/pdf/e/).

```python
import aspose.pdf as ap


def convert_pdf_to_pdf_e(self, infile, outfile):
    """PDF/E-1 Standard Support: Added the capability to convert PDF files to the PDF/E-1 format and to validate
    the output files for compliance with the standard."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set up the PDF/E-1 format with PdfFormatConversionOptions
        options = ap.PdfFormatConversionOptions(
            ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
        )
        # Convert to PDF/E-1 compliant document
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```

### ストリームからタグ付き画像を追加する

PDF のストリームからタグ付き画像を追加します。25.9 バージョンでは、メモリストリームから画像を追加して代替テキストでタグ付けすることで、PDF ドキュメントのアクセシビリティが強化されています。

```python
import aspose.pdf as ap


def add_tagged_image_from_stream(self, image_file, outfile):
    """Enhanced Accessibility for Tagged Images: possible to add alternative text to images loaded from a memory stream."""

    path_image = self.data_dir + image_file
    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:
        page = document.pages.add()
        # Tag the document for accessibility
        tagged_content = document.tagged_content
        tagged_content.set_title("Tagged Image from Stream")
        tagged_content.set_language("en-US")
        # Add an image from a stream to the page
        image_stream = io.FileIO(path_image, "r")
        page.add_image(image_stream, ap.Rectangle(100, 600, 300, 800, True), None, True)
        # Get the added image and set its alternative text
        img = page.resources.images[1]
        img.try_set_alternative_text("Aspose Logo", page)
        # Save the document
        document.save(path_outfile)
```

## Aspose.PDF 25.8 の新機能

この更新により、レイアウトとドキュメントのセキュリティ管理がより柔軟になります。

1. タグ付き目次 (TOC) を作成します。
1. コンテンツのスケーリングでPDFページのサイズを変更します。
1. テーブルに破線を適用します。

### タグ付き目次 (TOC) の作成

タグ付き PDF でアクセシブルな目次 (TOC) を自動的に生成します。完全にアクセシブルな PDF の目次 (TOC) を作成すると、読者は文書を効率的にナビゲートでき、アクセシビリティが PDF/UA-1 に準拠していることを確認できます。

```python
import aspose.pdf as ap


def create_pdf_with_toc_page(self, outfile):
    """
    Supports generating fully accessible Tagged Table of Contents (TOC) pages with proper navigation to
    corresponding sections, ensuring PDF/UA-1 compliance.
    """

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Add the TOC element to the document structure tree
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Save PDF document
        document.save(path_outfile)
```

### コンテンツスケーリングによるページのサイズ変更

レイアウトを維持したまま、コンテンツを均等に拡大縮小しながら PDF ページのサイズを変更します。PDF を扱う場合、新しいサイズに合わせてページのサイズを変更したり、コンテンツを拡大縮小したりする必要がある場合があります。

```python
import aspose.pdf as ap


def resize_page(
    self, document, page_number, target_width, target_height, width, height, outfile
):
    """
    Resize and scale page content using PdfFileEditor.ResizeContents.

    A high-level helper that scales and/or resizes the rendered content streams of one or more pages
    without performing a full content reflow. Use this to make existing page contents larger or smaller,
    fit content into a different page box, or uniformly scale content for printing or display.

    Parameters (recommended)
    ------------------------
    pdf_editor : Aspose.Pdf.Facades.PdfFileEditor
        The PdfFileEditor instance that exposes the ResizeContents API.
    page_numbers : int | Iterable[int] | slice, optional
        Page index (1-based) or collection of page indices to process. If omitted or None, all pages
        in the document are processed.
    scale : float, optional
        Uniform scale factor to apply to content (e.g., 0.5 reduces content to 50%). Mutually exclusive
        with target_width/target_height unless keep_aspect_ratio is explicitly handled.
    target_width : float, optional
        Desired content width in PDF points (1 point = 1/72 inch). When provided, content will be scaled
        to match this width (subject to keep_aspect_ratio and fit_mode).
    target_height : float, optional
        Desired content height in PDF points.
    keep_aspect_ratio : bool, default True
        If True, preserve the original aspect ratio when scaling to a target width or height.
    fit_mode : {'fit', 'fill', 'stretch'}, default 'fit'
        'fit'   — scale so content fits entirely inside the target box, preserving aspect ratio;
        'fill'  — scale so the target box is completely covered (may crop content);
        'stretch' — scale independently in X and Y (may distort).
    margins : tuple(float, float, float, float), optional
        (left, top, right, bottom) margins in points to preserve inside the target box.
    preserve_annotations : bool, default True
        When True, attempt to preserve annotations/forms/interactive elements; some annotations may
        require special handling after scaling.
    preserve_transparency : bool, default True
        Preserve transparency settings of page contents where possible.

    Returns
    -------
    bool
        True if the operation completed successfully. Some implementations operate in-place and may
        return a status rather than a new document object.

    Raises
    ------
    ValueError
        If parameters are invalid (e.g., scale <= 0 or both scale and conflicting target dimensions).
    IOError
        If input/output streams cannot be read or written.
    PdfProcessingError
        If the PDF content streams cannot be interpreted or transformed by the editor.

    Notes
    -----
    - All size and margin values are in PDF points (1/72 inch). Convert from inches or millimeters
      before calling if necessary.
    - This API scales content streams and their transform matrices; it does not reflow text or rebuild
      page layout. Text encoded as vectors will scale; text drawn by layout engines may not reflow.
    - Complex page objects such as XObjects, forms, and annotations may require additional post-processing.
    - For raster-output use-cases (images/screenshots), consider exporting to an image at a target DPI
      instead of scaling content streams.
    - When targeting printing, compute target page size in points from the physical paper size and DPI.

    Example (conceptual)
    --------------------
    # Scale pages 1-3 to 50%:
    editor = PdfFileEditor(input_stream, output_stream)
    editor.ResizeContents(page_numbers=[1,2,3], scale=0.5)
    editor.Save()

    # Fit page content into a letter-sized box while preserving aspect ratio:
    editor.ResizeContents(page_numbers=None, target_width=612, target_height=792, fit_mode='fit')

    See also
    --------
    PdfFileEditor.ResizeContents : Low-level API that performs content scaling and transform adjustments.
    """

    path_outfile = self.data_dir + outfile

    margin_width = (target_width - width) / 2
    margin_height = (target_height - height) / 2

    # Set the parameters
    param = ap.facades.PdfFileEditor.ContentsResizeParameters.page_resize(width, height)
    param.top_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_height)
    param.bottom_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(
        margin_height
    )
    param.left_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_width)
    param.right_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(
        margin_width
    )
    param.change_media_box = True

    # Do resize
    ap.facades.PdfFileEditor().resize_contents(document, [page_number], param)

    document.save(path_outfile)
```

### テーブルに破線枠を適用

破線を使用してカスタムボーダースタイルのテーブルを追加します。この例は、.NET 経由の Aspose.PDF for Python を使用して、PDF ドキュメント内の表に破線や点線などのカスタム枠スタイルを適用する方法を示しています。

```python
import aspose.pdf as ap


def create_table_with_dashed_border(self, outfile):
    """Support style  for table borders, allowing you to set dashed, dotted, or custom border styles for tables."""

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:
        page = document.pages.add()
        table = ap.Table()
        graph_info = ap.GraphInfo()
        graph_info.dash_array = [10, 10]
        graph_info.dash_phase = 5
        graph_info.line_width = 3
        table.border = ap.BorderInfo(ap.BorderSide.BOX, graph_info)
        row = table.rows.add()
        row.cells.add("Dashed border cell")

        page.paragraphs.add(table)

        document.save(path_outfile)
```

## Aspose.PDF 25.7 の新機能

25.7 リリースでは、注釈サポート、テキストフィッティング、およびデジタル署名管理の強化に重点が置かれています。

1. テキストを図形の内側に収める。
1. 公開証明書を使用して PDF を暗号化します。
1. クラウドとポリゴンのアノテーションを追加します。

### 公開証明書で PDF を暗号化

公開証明書に基づく暗号化で PDF を保護します。公開証明書暗号化により、特定の受信者向けに PDF を暗号化し、対応する秘密鍵の所有者のみが文書を開いて読むことができるようになります。

```python
import aspose.pdf as ap


def pub_sec_encryption(self, outfile, pub_cert, crypto_algorithm):
    """Support for public certificate encryption, allowing PDFs to be encrypted so that only specified certificate
    holders can open the document."""

    # The path to the recipient certificate
    path_outfile = self.data_dir + outfile
    path_cert = self.data_dir + pub_cert

    # Create the PDF document
    with ap.Document() as document:
        # Add an info
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"

        # Add a page and add some text
        page = document.pages.add()
        text = ap.text.TextFragment("Hello World!")
        page.paragraphs.add(text)

        # Load certificate
        with open(path_cert, "rb") as f:
            cert_data = f.read()

        # Encrypt the PDF document
        document.encrypt(ap.Permissions.PRINT_DOCUMENT, crypto_algorithm, [cert_data])

        # Save the PDF document. A private key certificate must be installed in the storage to open the document
        # by Adobe Acrobat.
        document.save(path_outfile)
```

### テキストを四角形に収める

定義された長方形の内側に収まるようにテキストを自動的に拡大縮小します。PDF 内のテキストを更新または展開すると、元の段落の境界を超えることがあります。

```python
import re
import aspose.pdf as ap


def fit_text_into_rectangle(self, infile, outfile):
    """New functionality to fit expanded text content within the bounds of a paragraph’s original rectangle,
    adjusting font size and spacing automatically."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Extract the paragraph text (or provide the specific text you want to replace)
        text_absorber = ap.text.TextAbsorber()
        text_absorber.visit(document)
        paragraph_text = text_absorber.text
        paragraph_text = paragraph_text.replace("\n", " ")

        # Search for the text fragment
        searchable_content = re.sub(" ", r"\\s+", paragraph_text)
        text_fragment_absorber = ap.text.TextFragmentAbsorber(
            searchable_content, ap.text.TextSearchOptions(True)
        )
        document.pages.accept(text_fragment_absorber)
        text_fragment = text_fragment_absorber.text_fragments[1]
        # Use the text fragment’s rectangle as the target replacement area
        text_fragment.replace_options.rectangle = text_fragment.rectangle
        # Enable font size reduction to fit the text within the specified area
        text_fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        # Optionally adjust spacing to justify the text width
        text_fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        # Duplicate the paragraph content and assign it to the text fragment
        text_fragment.text = paragraph_text + " " + paragraph_text
        # Save PDF document
        document.save(path_outfile)
```

### クラウドポリゴン注釈を追加

クラウドまたはポリゴンスタイルの注釈でPDFレビューワークフローを強化します。多角形注釈を使うと、幾何学的図形を使って PDF 内の特定の領域を強調したり強調したりできます。

```python
import aspose.pdf as ap


def add_cloud_polygon_annotation(self, outfile):
    """The ability to apply “Cloudy” border effects to polygon annotations for enhanced visual appearance."""

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:
        page = document.pages.add()
        # Add Cloud Polygon (rectangle)
        left = 100.0
        top = 270.0
        right = 420.0
        bottom = 80.0
        cloud_polygon = ap.annotations.PolygonAnnotation(
            page,
            ap.Rectangle(left, top, right, bottom, True),
            [
                ap.Point(left, top),
                ap.Point(right, top),
                ap.Point(right, bottom),
                ap.Point(left, bottom),
            ],
        )
        cloud_polygon.color = ap.Color.blue
        border = ap.annotations.Border(cloud_polygon)
        border.width = 3
        border.effect = ap.annotations.BorderEffect.CLOUDY
        cloud_polygon.border = border
        page.annotations.append(cloud_polygon)
        # Add another Cloud Polygon
        cloud_polygon = ap.annotations.PolygonAnnotation(
            page,
            ap.Rectangle(400, 400, 580, 600, True),
            [
                ap.Point(400, 450),
                ap.Point(450, 300),
                ap.Point(520, 300),
                ap.Point(580, 500),
                ap.Point(500, 600),
            ],
        )
        cloud_polygon.color = ap.Color.dark_green
        cloud_polygon.interior_color = ap.Color.aqua
        border = ap.annotations.Border(cloud_polygon)
        border.width = 3
        border.effect = ap.annotations.BorderEffect.CLOUDY
        cloud_polygon.border = border
        page.annotations.append(cloud_polygon)
        # Save PDF document
        document.save(path_outfile)
```

## Aspose.PDF 25.6 の新機能

このリリースの主な機能:

1. 画像代替テキストのサポート。
1. ライセンス情報へのアクセス。
1. スタイル付きのフリーテキスト注釈。
1. カスタマイズ可能なデジタル署名の外観。

### 画像代替テキストサポート

スクリーンリーダーのアクセシビリティを向上させるために、画像の代替テキストを設定および取得します。

```python
import aspose.pdf as ap


def get_set_alternative_text_for_image(self, infile, outfile):
    """To get and set the alternative text for images"""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Alternative text to be given to the image
        alt_text = "Alternative text for image"
        # Image for which alternative text will be set and get
        x_image = document.pages[1].resources.images[1]
        # Try to set alternative text for an image
        result = x_image.try_set_alternative_text(alt_text, document.pages[1])
        # If set is successful, then get the alternative text for the image
        if result:
            alt_texts = x_image.get_alternative_text(document.pages[1])
        # Save PDF document
        document.save(path_outfile)
```

### ライセンス情報へのアクセス

LicenseInfoから詳細なライセンスメタデータ (ライセンスユーザー、有効期限) を取得します。

```python
import aspose.pdf as ap


def get_license_info_example(self, infile):
    """A new way to access license information programmatically through the LicenseInfo property of the License class"""

    path_infile = self.data_dir + infile

    # Initialize license object
    lic = ap.License()
    # Set license
    lic.set_license(path_infile)
    # Get license info.
    lic_license_info = lic.license_info
    print(lic_license_info.licensed_to)
    print(lic_license_info.subscription_expiry)
```

### スタイル付きフリーテキスト注釈

SetTextStyle を使用すると、太字、斜体、下線などのスタイルを注釈テキストに適用したり、既存の書式をクリアしたりできます。

```python
import aspose.pdf as ap


def add_free_annotation_and_set_styles(self, outfile):
    """Extended formatting capabilities for annotation text through the SetTextStyle method family of the
    FreeTextAnnotation class"""

    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document() as document:
        # Add new page
        page = document.pages.add()
        # Instantiate DefaultAppearance object
        default_appearance = ap.annotations.DefaultAppearance(
            "Arial", 16, drawing.Color.blue
        )
        # Create annotation
        free_text = ap.annotations.FreeTextAnnotation(
            page, ap.Rectangle(20, 600, 400, 650, True), default_appearance
        )
        # Specify the contents of annotation
        free_text.contents = "Text of FreeTextAnnotation with different styles"
        # Add annotation to annotations collection of page
        page.annotations.append(free_text)
        # Set styles for annotation text
        free_text.set_text_style(0, 4, ap.annotations.RichTextFontStyles.ITALIC)
        free_text.set_text_style(
            8,
            26,
            ap.annotations.RichTextFontStyles.UNDERLINE
            | ap.annotations.RichTextFontStyles.BOLD,
        )
        free_text.set_text_style(27, 86, ap.annotations.RichTextFontStyles.BOLD)
        free_text.set_text_style(
            42,
            45,
            ap.annotations.RichTextFontStyles.CLEAR_EXISTING
            | ap.annotations.RichTextFontStyles.UNDERLINE,
        )
        # Save PDF document
        document.save(path_outfile)
```

### カスタマイズ可能なデジタル署名の外観

画像を追加したり、フォントを変更したり、背景コンテンツ上に署名グラフィックを重ねたりすることで、ブランディングやデザインの一貫性を高めることができます。

```python
import aspose.pdf as ap


def customization_features_for_digital_sign(
    self, infile, outfile, image_file, pfx_file
):
    """Enhanced digital signature appearance allowing signature images to appear over background text."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_image = self.data_dir + image_file
    path_pfx = self.data_dir + pfx_file

    with ap.facades.PdfFileSignature() as pdf_file_signature:
        # Bind PDF document
        pdf_file_signature.bind_pdf(path_infile)
        # Create a rectangle for signature location
        rect = drawing.Rectangle(10, 10, 300, 50)
        # Create any of the three signature types
        signature = ap.forms.PKCS7Detached(path_pfx, "12345")
        # Create signature appearance
        signature_custom_appearance = ap.forms.SignatureCustomAppearance()
        signature_custom_appearance.font_size = 6
        signature_custom_appearance.font_family_name = "Times New Roman"
        signature_custom_appearance.digital_signed_label = "Signed by:"
        signature_custom_appearance.is_foreground_image = True
        # Set signature appearance
        signature.custom_appearance = signature_custom_appearance
        # Set signature appearance
        pdf_file_signature.signature_appearance = path_image
        pdf_file_signature.sign(1, True, rect, signature)
        #  Save PDF document
        pdf_file_signature.save(path_outfile)
```

## Aspose.PDF 25.5 の新機能

最新の Aspose.PDF 更新では、ドキュメントのアクセシビリティ、互換性、およびセキュリティを向上させるいくつかの強力な機能強化が導入されています。開発者は署名付き PDF ファイルからデジタル証明書を直接抽出できるようになり、高度な検証とコンプライアンスチェックが可能になりました。

1. PDF 署名から証明書を抽出します。
1. タグ付き PDF に構造化された順序付きリストを作成します。
1. 公開鍵証明書で署名を検証します。
1. ダイナミック XFA フォームをアクロフォーム PDF に変換します。
1. PDF でのフォントの置換-XPS 変換

### PDF 署名から証明書を抽出

「extract_certificate ()」を使用して埋め込まれた証明書を取得します。

```python
import aspose.pdf as ap


def extract_certificate(self, infile):
    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            for signature_name in signature_names:
                # Extract certificate
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print(certificate[0] is not None)
```

### タグ付き PDF での構造化された順序付きリストの作成

タグ付けされた文書内に、アクセシブルな番号付きリスト (入れ子になった項目を含む) を生成します。

```python
import aspose.pdf as ap


def create_ordered_list(self, outfile):
    path_outfile = self.data_dir + outfile

    # Create or open PDF document
    with ap.Document() as document:
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        root_list = content.create_list_element()
        span_for_lbl_1 = content.create_span_element()
        span_for_lbl_1.set_text("1. ")
        position_settings = ap.tagged.PositionSettings()
        position_settings.is_in_line_paragraph = True
        span_for_lbl_1.adjust_position(position_settings)
        span_for_body_1 = content.create_span_element()
        span_for_body_1.set_text("bread")
        span_for_body_1.adjust_position(position_settings)
        lbl_1 = content.create_list_lbl_element()
        lbl_1.append_child(span_for_body_1, True)
        l_body_1 = content.create_list_l_body_element()
        l_body_1.append_child(span_for_lbl_1, True)
        li_1 = content.create_list_li_element()
        li_1.append_child(lbl_1, True)
        li_1.append_child(l_body_1, True)
        root_list.append_child(li_1, True)
        span_for_lbl_2 = content.create_span_element()
        span_for_lbl_2.set_text("2. ")
        span_for_body_2 = content.create_span_element()
        span_for_body_2.set_text("milk")
        span_for_body_2.adjust_position(position_settings)
        lbl_2 = content.create_list_lbl_element()
        lbl_2.append_child(span_for_lbl_2, True)
        l_body_2 = content.create_list_l_body_element()
        l_body_2.append_child(span_for_body_2, True)
        li_2 = content.create_list_li_element()
        li_2.append_child(lbl_2, True)
        li_2.append_child(l_body_2, True)
        root_list.append_child(li_2, True)
        nested_list_depth_1 = content.create_list_element()
        span_for_lbl_3_1 = content.create_span_element()
        span_for_lbl_3_1.set_text("3.1. ")
        position_settings_lbl_3_1 = ap.tagged.PositionSettings()
        position_settings_lbl_3_1.is_in_line_paragraph = False
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        position_settings_lbl_3_1.margin = margin_info
        span_for_lbl_3_1.adjust_position(position_settings_lbl_3_1)
        span_for_body_3_1 = content.create_span_element()
        span_for_body_3_1.set_text("apples")
        span_for_body_3_1.adjust_position(position_settings)
        lbl_3_1 = content.create_list_lbl_element()
        lbl_3_1.append_child(span_for_lbl_3_1, True)
        l_body_3_1 = content.create_list_l_body_element()
        l_body_3_1.append_child(span_for_body_3_1, True)
        li_3_1 = content.create_list_li_element()
        li_3_1.append_child(lbl_3_1, True)
        li_3_1.append_child(l_body_3_1, True)
        nested_list_depth_1.append_child(li_3_1, True)
        span_for_lbl_3_2 = content.create_span_element()
        span_for_lbl_3_2.set_text("3.2. ")
        span_for_lbl_3_2.adjust_position(position_settings_lbl_3_1)
        span_for_body_3_2 = content.create_span_element()
        span_for_body_3_2.set_text("banana")
        span_for_body_3_2.adjust_position(position_settings)
        lbl_3_2 = content.create_list_lbl_element()
        lbl_3_2.append_child(span_for_lbl_3_2, True)
        l_body_3_2 = content.create_list_l_body_element()
        l_body_3_2.append_child(span_for_body_3_2, True)
        li_3_2 = content.create_list_li_element()
        li_3_2.append_child(lbl_3_2, True)
        li_3_2.append_child(l_body_3_2, True)
        nested_list_depth_1.append_child(li_3_2, True)
        span_for_lbl_3 = content.create_span_element()
        span_for_lbl_3.set_text("3. ")
        span_for_body_3 = content.create_span_element()
        span_for_body_3.set_text("fruits")
        span_for_body_3.adjust_position(position_settings)
        lbl_3 = content.create_list_lbl_element()
        lbl_3.append_child(span_for_lbl_3, True)
        l_body_3 = content.create_list_l_body_element()
        l_body_3.append_child(span_for_body_3, True)
        li_3 = content.create_list_li_element()
        li_3.append_child(lbl_3, True)
        li_3.append_child(l_body_3, True)
        l_body_3.append_child(nested_list_depth_1, True)
        root_list.append_child(li_3, True)
        root_element.append_child(root_list, True)
        # Save Tagged PDF Document
        document.save(path_outfile)
```

### 公開鍵証明書による署名の検証

外部の公開鍵証明書を使用してデジタル署名を検証します。

```python
import aspose.pdf as ap


def verify_with_public_key_certificate1(self, certificate, infile):
    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

### ダイナミック XFA フォームをアクロフォーム PDF に変換

「無視_needs_render」を使用して XFA フォームを標準化します。

```python
import aspose.pdf as ap


def convert_xfa_form_with_ignore_needs_rendering(self, infile, outfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

### PDF でのフォントの置換-XPS 変換

見つからないフォントをデフォルトの代替フォントに置き換えます (例:「Courier New」)。

```python
import aspose.pdf as ap


def replace_font_when_converting_pdf_to_xps(self, infile, outfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Create XpsSaveOptions instance
    xps_save_options = ap.XpsSaveOptions()
    # use_embedded_true_type_fonts option specifies whether to use embedded TrueType fonts
    xps_save_options.use_embedded_true_type_fonts = False
    # The specified default font will be used if the embedded font name cannot be found in the system
    xps_save_options.default_font = "Courier New"
    # Open PDF document
    doc = ap.Document(path_infile)
    # Save the resultant XPS
    doc.save(path_outfile, xps_save_options)
```

## Aspose.PDF 25.4 の新機能

### PDF/A 変換中の自動タグ付け

PDFをPDF/A-1bに変換し、論理構造を自動的に作成してアクセシビリティを向上させます。

```python
import aspose.pdf as ap


def convert_to_pdfa_with_automatic_tagging(self, infile, outfile, outlogfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_outlogfile = self.data_dir + outlogfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(
            path_outlogfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
        )
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = (
            ap.HeadingRecognitionStrategy.AUTO
        )
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```
