---
title: 새로워진 내용
linktitle: 새로워진 내용
type: docs
weight: 10
url: /ko/python-net/whatsnew/
description: 이 페이지에서는 최근 릴리스에서 소개된, .NET을 통한 Python용 Aspose.PDF 의 가장 인기 있는 새 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2026-06-10"
TechArticle: false
---

## Aspose.PDF 26.3의 새로운 기능

.NET** 26.3을 통한 파이썬용**Aspose.pdf에 다음을 추가했습니다.

PDF 최적화 중 손실 없는 이미지 스트림 재압축최적화 옵션. compressAllContentStreams 속성은 이제 FlateDecode를 사용하여 적합한 이미지 XObject 스트림을 압축하므로 이미지 품질은 그대로 유지하면서 파일 크기를 줄일 수 있습니다.

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

이제 이미지 재압축이 선택된 ImageCompression옵션과 일치합니다. 최적화 중 인코딩 설정을 통해 Jpeg2000 또는 Flate를 사용할 때 이미지 크기 조정, 해상도 제한 및 품질 제어와 함께 보다 일관된 결과를 얻을 수 있습니다.

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

PDF 문서를 이미지 또는 HTML로 저장할 때 주석을 렌더링할 수 있도록 지원하여 외부 PDF 뷰어 공유를 위해 주석이 달린 문서를 내보낼 때 가시적인 검토 마크업을 보존할 수 있습니다.

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

대용량 래스터화 시나리오 (특히 페이지를 비트 톤 TIFF 이미지로 내보낼 때) 의 PDF-TIFF 렌더링 성능이 향상되었습니다.

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

## Aspose.PDF 26.2의 새로운 기능

Aspose.PDF 26.2에서는 RTF에서 PDF로의 변환 지원을 소개합니다.개발자는 이 기능을 사용하여 RTF (리치 텍스트 형식) 문서를 PDF 파일로 직접 변환할 수 있습니다.

RTF는 Microsoft에서 처음 개발한 널리 지원되는 크로스 플랫폼 문서 형식입니다.글꼴, 색상, 굵게, 기울임꼴 텍스트, 포함된 이미지와 같은 기본 서식을 유지하면서 다양한 워드 프로세싱 응용 프로그램 간에 문서를 교환할 수 있도록 설계되었습니다.

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

이 코드 스니펫은 Python용 Aspose.PDF 를 사용하여 PDF 페이지의 기존 내용 뒤에 표를 삽입하는 방법을 보여줍니다.

스크립트는 기존 PDF 문서를 열고 첫 페이지에 있는 현재 내용의 경계 상자를 계산합니다.이 정보를 사용하여 기존 내용이 끝나는 위치를 찾고 새 표를 마지막 요소 아래에 배치하여 표가 시작되기 전에 지정된 여백을 남깁니다.

그런 다음 루프를 사용하여 테이블을 만들고 여러 행과 열로 채웁니다.표 구조와 내용을 설정한 후 해당 표가 페이지의 단락 컬렉션에 추가됩니다.마지막으로 업데이트된 문서는 새 PDF 파일로 저장됩니다.

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

Python용 Aspose.PDF 파일을 사용하여 PDF 문서에서 보이지 않는 텍스트를 감지하고 제거합니다.

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

## Aspose.PDF 26.1의 새로운 기능

.NET** 26.1을 통한 파이썬용**Aspose.pdf에 다음을 추가했습니다.

1. 성능 향상 — 문서에 텍스트를 추가할 때의 성능 저하 및 전반적인 성능 문제를 해결했습니다.
1. 렌더링 정확도 향상 — PDF 왼쪽의 누락된 세로 텍스트를 수정하고 PDF에서 PNG로 변환하는 동안 중국어 문자 렌더링을 수정했습니다.
1. HTML 변환 개선 — 이제 API가 HTML을 PDF로 변환할 때 선 색상을 적용하고 XFA-표준 변환의 텍스트 중복 문제를 수정했습니다.
1. 문서 구조의 버그 수정 — 이제 NumberingStyle이 제목 개체에 제대로 작동하고 PDF-to-HTML에서 강조 표시된 텍스트 색상이 보존됩니다.

## Aspose.PDF 25.12의 새로운 기능

논리적 구조 정보를 보존하면서 HTML 문서를 PDF로 변환합니다.생성된 PDF는 구조화된 문서 내용에 의존하는 접근성, 태그 지정 및 다운스트림 처리에 더 적합합니다.

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

디지털 서명된 PDF를 분석하여 서명이 포함되지 않은 콘텐츠를 식별하고 보고할 수 있습니다.이를 사용하여 문서 무결성을 검증하고, 서명된 PDF를 감사하고, 서명 후 수정을 감지할 수 있습니다.

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

## Aspose.PDF 25.11의 새로운 기능

이 함수는 두 PDF 문서의 특정 페이지를 비교하여 나란히 표시되는 시각적 차이를 생성합니다.비교 옵션과 색상을 사용자 정의하여 공백과 같은 중요하지 않은 차이는 무시하고 의미 있는 변경 사항을 강조할 수 있습니다.

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

25.11 버전에서 숨겨진 데이터를 제거하고 페이지를 래스터화합니다.

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

글꼴 서브세팅 및 콘텐츠 스트림 압축 25.11 버전으로 리소스 최적화

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

## Aspose.PDF 25.10의 새로운 기능

향상된 PDF 레이어 가시성 제어 — 이번 릴리스에서는 PDF 뷰어에서 가시성이 변경되지 않도록 PDF 레이어의 초기 가시성 상태를 프로그래밍 방식으로 정의하고 잠그는 기능을 도입했습니다.

새로운 'layer.default_state' 속성을 사용하면 DefaultState 속성을 사용하여 레이어의 기본 가시성을 표시하거나 숨길 수 있습니다.이를 통해 사용자 가시성 동작을 예측할 수 있는 복잡한 계층화된 PDF 문서를 세밀하게 관리할 수 있습니다.

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

## Aspose.PDF 25.9의 새로운 기능

25.9 릴리스에는 향상된 접근성, 향상된 규정 준수 지원, 태그가 지정된 이미지 및 문서 표준 작업을 위한 새로운 API 기능이 도입되었습니다.

1. PDF를 PDF/E-1 형식으로 변환합니다.
1. 메모리 스트림에서 태그가 지정된 이미지를 추가합니다.

### PDF를 PDF/E-1 형식으로 변환

파이썬용 Aspose.PDF 라이브러리의 25.9 버전에서는 PDF/E-1 형식 변환이 가능합니다.이 형식에 대한 자세한 내용은 에서 확인할 수 있습니다. [파일 형식 문서](https://docs.fileformat.com/pdf/e/).

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

### 스트림에서 태그가 지정된 이미지 추가

스트림의 태그가 지정된 이미지를 PDF로 추가합니다. 25.9 버전은 메모리 스트림에서 이미지를 추가하고 대체 텍스트로 태그를 지정하여 PDF 문서의 향상된 접근성을 지원합니다.

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

## Aspose.PDF 25.8의 새로운 기능

이 업데이트는 레이아웃 및 문서 보안 관리에 더 많은 유연성을 추가합니다.

1. 태그가 지정된 목차 (TOC) 를 생성합니다.
1. 콘텐츠 스케일링으로 PDF 페이지 크기를 조정합니다.
1. 테이블에 파선 테두리를 적용합니다.

### 태그가 있는 목차 (TOC) 만들기

태그가 있는 PDF에서 액세스 가능한 목차 (TOC) 를 자동으로 생성합니다.PDF에서 완전히 액세스할 수 있는 목차 (TOC) 를 만들면 독자가 문서를 효율적으로 탐색할 수 있고 접근성에 대한 PDF/UA-1 준수를 보장할 수 있습니다.

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

### 콘텐츠 스케일링으로 페이지 크기 조정

레이아웃을 유지하고 콘텐츠의 크기를 비례적으로 조정하면서 PDF 페이지 크기를 조정할 수 있습니다.PDF로 작업할 때 새 크기에 맞게 페이지 크기를 조정하거나 콘텐츠 크기를 조정해야 할 수 있습니다.

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

### 테이블에 파선 테두리 적용

파선을 사용하여 사용자 지정 테두리 스타일로 테이블을 추가합니다.이 예제에서는 .NET을 통해 Aspose.PDF for Python을 사용하여 PDF 문서의 테이블에 대시선 또는 점선과 같은 사용자 지정 테두리 스타일을 적용하는 방법을 보여줍니다.

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

## Aspose.PDF 25.7의 새로운 기능

25.7 릴리스는 더 나은 주석 지원, 텍스트 맞춤 및 디지털 서명 관리에 중점을 둡니다.

1. 도형 안에 텍스트를 맞춥니다.
1. 공인 인증서를 사용하여 PDF를 암호화합니다.
1. 클라우드 및 폴리곤 주석을 추가합니다.

### 공개 인증서로 PDF 암호화

공인 인증서 기반 암호화로 PDF를 보호하세요.공개 인증서 암호화를 사용하면 특정 수신자에 대해 PDF를 암호화하여 해당 개인 키 소유자만 문서를 열고 읽을 수 있습니다.

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

### 사각형 안에 텍스트 맞추기

정의된 사각형 안에 맞게 텍스트 크기를 자동으로 조정합니다.PDF에서 텍스트를 업데이트하거나 확장할 때 텍스트가 원래 단락 경계를 초과할 수 있습니다.

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

### 클라우드 폴리곤 주석 추가

클라우드 또는 폴리곤 스타일 주석을 사용하여 PDF 검토 워크플로우를 개선합니다.다각형 주석을 사용하면 기하학적 모양을 사용하여 PDF의 특정 영역을 강조하거나 강조할 수 있습니다.

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

## Aspose.PDF 25.6의 새로운 기능

이번 릴리즈의 주요 기능:

1. 이미지 대체 텍스트 지원.
1. 라이선스 정보 액세스.
1. 스타일이 적용된 자유 텍스트 주석.
1. 사용자 지정 가능한 디지털 서명 모양.

### 이미지 대체 텍스트 지원

이미지의 대체 텍스트를 설정하고 검색하여 화면 판독기의 접근성을 개선합니다.

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

### 라이선스 정보 액세스

LicenseInfo를 통해 자세한 라이선스 메타데이터 (라이선스 사용자, 만료일) 를 검색합니다.

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

### 스타일이 적용된 자유 텍스트 주석

SetTextStyle을 사용하여 굵게, 기울임꼴, 밑줄 또는 기존 서식 지우기와 같은 스타일을 주석 텍스트에 적용할 수 있습니다.

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

### 사용자 지정 가능한 디지털 서명 모양

이미지를 추가하고, 글꼴을 변경하고, 배경 콘텐츠 위에 시그니처 그래픽을 겹쳐 브랜딩 또는 디자인 일관성을 향상하세요.

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

## Aspose.PDF 25.5의 새로운 기능

최신 Aspose.PDF 업데이트에는 문서 접근성, 호환성 및 보안을 향상시키는 몇 가지 강력한 개선 사항이 도입되었습니다.이제 개발자는 서명된 PDF 파일에서 직접 디지털 인증서를 추출하여 고급 검증 및 규정 준수 검사를 수행할 수 있습니다.

1. PDF 서명에서 인증서를 추출합니다.
1. 태그가 있는 PDF에서 구조화된 정렬 목록 만들기.
1. 공개 키 인증서로 서명을 확인합니다.
1. 동적 XFA 양식을 아크로폼 PDF로 변환합니다.
1. PDF의 글꼴 교체 - XPS 변환

### PDF 서명에서 인증서 추출

'extract_certificate () '를 사용하여 내장된 인증서를 검색합니다.

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

### 태그가 있는 PDF에서 구조화된 순서 목록 만들기

태그가 지정된 문서 내에 액세스 가능한 번호가 매겨진 목록 (중첩된 항목 포함) 을 생성합니다.

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

### 공개 키 인증서로 서명 확인

외부 공개 키 인증서를 사용하여 디지털 서명의 유효성을 검사합니다.

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

### 동적 XFA 양식을 아크로폼 PDF로 변환

'무시_필요_렌더링'을 사용하여 XFA 양식을 표준화하세요.

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

### PDF에서 글꼴 바꾸기 - XPS 변환

누락된 글꼴을 기본 대체 글꼴로 대체합니다 (예: “Courier New”).

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

## Aspose.PDF 25.4의 새로운 기능

### PDF/A 변환 시 자동 태깅

자동 논리적 구조 생성을 통해 PDF를 PDF/A-1b로 변환하여 접근성을 개선합니다.

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
