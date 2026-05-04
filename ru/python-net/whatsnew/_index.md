---
title: Что нового
linktitle: Что нового
type: docs
weight: 10
url: /python-net/whatsnew/
description: На этой странице представлены самые популярные новые функции в Aspose.PDF for Python via .NET, которые были введены в последних релизах.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-02-24"
TechArticle: false 
---

## Что нового в Aspose.PDF 26.3

В **Aspose.PDF for Python via .NET** 26.3, мы добавили:

Повторное без потери качества сжатие потоков изображений при оптимизации PDF. Свойство OptimizationOptions.CompressAllContentStreams теперь также сжимает подходящие потоки XObject изображений с использованием FlateDecode, способствуя уменьшению размера файла при сохранении качества изображения.

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

Повторное сжатие изображений теперь соответствует выбранному параметру ImageCompressionOptions.Encoding во время оптимизации, обеспечивая более согласованные результаты при использовании Jpeg2000 или Flate, а также при изменении размеров изображений, ограничениях разрешения и управлении качеством.

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

Поддержка рендеринга комментариев при сохранении PDF‑документов в виде изображений или HTML, позволяющая сохранять видимую разметку рецензий при экспорте аннотированных документов для обмена за пределами PDF‑просмотрщиков.

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

Улучшена производительность рендеринга PDF в TIFF для сценариев интенсивной растеризации, особенно при экспорте страниц в двуцветные TIFF‑изображения.

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

## Что нового в Aspose.PDF 26.2

Aspose.PDF 26.2 вводит поддержку преобразования RTF в PDF. Эта функция позволяет разработчикам напрямую преобразовывать документы Rich Text Format (RTF) в PDF‑файлы.

RTF — это широко поддерживаемый кроссплатформенный формат документов, первоначально разработанный компанией Microsoft. Он предназначен для обеспечения обмена документами между различными текстовыми процессорами при сохранении базового форматирования, такого как шрифты, цвета, полужирный и курсивный текст, а также встроенных изображений.

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

Этот фрагмент кода показывает, как вставить таблицу после существующего содержимого на странице PDF с использованием Aspose.PDF for Python.

Скрипт открывает существующий PDF‑документ и вычисляет ограничивающий прямоугольник текущего содержимого на первой странице. Используя эту информацию, он определяет, где заканчивается существующее содержимое, и размещает новую таблицу ниже последнего элемента, оставляя указанное поле перед началом таблицы.

Затем создаётся таблица, которая заполняется несколькими строками и столбцами с помощью цикла. После настройки структуры и содержимого таблицы она добавляется в коллекцию абзацев страницы. В конце обновлённый документ сохраняется как новый PDF‑файл.

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

Обнаружить и удалить невидимый текст из PDF‑документа с использованием Aspose.PDF for Python:

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

## Что нового в Aspose.PDF 26.1

В **Aspose.PDF for Python via .NET** 26.1 мы добавили:

1. Улучшения производительности – устранена плохая производительность при добавлении текста в документы и общие проблемы с производительностью.
1. Повышенная точность рендеринга — исправлена отсутствующая вертикальная печать слева в PDF и скорректировано отображение китайских символов при конвертации PDF в PNG.
1. Улучшено преобразование HTML – API теперь учитывает цвет линии при преобразовании HTML‑в‑PDF и исправлены проблемы наложения текста при конвертации XFA‑в‑Standard.
1. Исправления ошибок структуры документа – NumberingStyle теперь правильно работает с объектами Heading, а PDF-to-HTML теперь сохраняет цвет выделенного текста.

## Что нового в Aspose.PDF 25.12

Преобразовать HTML‑документ в PDF с сохранением информации о логической структуре. Полученный PDF лучше подходит для доступности, тегирования и последующей обработки, зависящей от структурированного содержания документа.

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

Проанализировать цифрово подписанный PDF, чтобы определить и сообщить о содержимом, не покрытом подписями. Использовать это для проверки целостности документа, аудита подписанных PDF и обнаружения изменений после подписи.

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

## Что нового в Aspose.PDF 25.11

Эта функция сравнивает определённую страницу из двух PDF‑документов и производит визуальное сравнение бок о бок. Настраивая параметры сравнения и цвета, она выделяет значимые изменения, игнорируя несущественные различия, такие как пробелы.

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

Удаление скрытых данных и растрирование страниц в версии 25.11.

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

Оптимизация ресурсов с помощью подмножества шрифтов и сжатия потоков контента версии 25.11.

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

## Что нового в Aspose.PDF 25.10

Усиленный контроль видимости слоёв PDF – в этом выпуске представлена возможность программно задавать начальное состояние видимости слоёв PDF и блокировать их, чтобы предотвратить изменения видимости в просмотрщиках PDF.

Новое свойство 'layer.default_state' позволяет задавать значение видимости слоя по умолчанию — видимый или скрытый — с помощью свойства DefaultState. Это обеспечивает тонкий контроль при управлении сложными многоуровневыми PDF‑документами с предсказуемым поведением видимости для пользователя.

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

## Что нового в Aspose.PDF 25.9

В выпуске 25.9 представлены улучшенная доступность, расширенная поддержка соответствия и новые возможности API для работы с помеченными изображениями и стандартами документов.

1. Конвертировать PDF-файлы в формат PDF/E-1.
1. Добавьте помечённые изображения из потоков памяти.

### Преобразовать PDF в формат PDF/E-1

В версии 25.9 библиотеки Aspose.PDF for Python доступно преобразование формата PDF/E-1. Дополнительную информацию об этом формате можно найти на [Документация по форматам файлов](https://docs.fileformat.com/pdf/e/).

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

### Добавить Tagged Images из потока

Добавление помеченных изображений из потока в PDF. Версия 25.9 поддерживает расширенную доступность PDF‑документов, позволяя добавить изображение из потоковой памяти и пометить его альтернативным текстом.

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

## Что нового в Aspose.PDF 25.8

Это обновление добавляет большую гибкость в управлении макетом и безопасностью документов.

1. Создайте помеченные таблицы содержания (TOC).
1. Изменить размер страниц PDF с масштабированием содержимого.
1. Применить пунктирные границы к таблицам.

### Создать помеченное оглавление (TOC)

Автоматически генерировать доступные оглавления (TOC) в Tagged PDF. Создание полностью доступного оглавления (TOC) в PDF позволяет читателям эффективно перемещаться по документу и обеспечивает соответствие требованиям PDF/UA-1 по доступности.

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

### Изменение размеров страниц с масштабированием содержимого

Изменить размер страниц PDF, сохраняя макет и пропорционально масштабируя содержимое. При работе с PDF вам может потребоваться изменить размер страниц или масштабировать содержимое, чтобы оно соответствовало новым размерам.

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

### Применить пунктирные границы к таблицам

Добавьте таблицы с пользовательскими стилями границ, используя пунктирные линии. Этот пример демонстрирует, как применить пользовательские стили границ — такие как пунктирные или точечные линии — к таблицам в PDF‑документе, используя Aspose.PDF for Python via .NET.

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

## Что нового в Aspose.PDF 25.7

Выпуск 25.7 ориентирован на улучшенную поддержку аннотаций, подгонку текста и управление цифровыми подписями.

1. Поместите текст внутри фигур.
1. Зашифруйте PDF-файлы с использованием публичного сертификата.
1. Добавить облачные и полигональные аннотации.

### Шифровать PDF с публичным сертификатом

Защитите свои PDF-файлы шифрованием на основе публичных сертификатов. Шифрование с использованием публичного сертификата позволяет зашифровать PDF для конкретных получателей, гарантируя, что только владельцы соответствующих закрытых ключей смогут открыть и прочитать документ.

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

### Вписать текст в прямоугольник

Автоматически масштабировать текст, чтобы он помещался в заданный прямоугольник. При обновлении или расширении текста в PDF он может выйти за пределы исходного абзаца.

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

### Добавить облачные полигональные аннотации

Улучшите процессы рецензирования PDF с помощью облачных или полигональных аннотаций. Полигональные аннотации позволяют выделять или подчеркивать определённые области в PDF, используя геометрические фигуры.

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

## Что нового в Aspose.PDF 25.6

Основные возможности этой версии:

1. Поддержка альтернативного текста изображения.
1. Доступ к информации о лицензии.
1. Стилизованные аннотации свободного текста.
1. Настраиваемый внешний вид цифровой подписи.

### Поддержка альтернативного текста изображения

Устанавливайте и получайте альтернативный текст для изображений, чтобы улучшить доступность для средств чтения с экрана.

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

### Доступ к информации о лицензии

Получить детальные метаданные лицензии (лицензионный пользователь, дата истечения) через LicenseInfo.

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

### Оформленные аннотации свободного текста

Используйте SetTextStyle, чтобы применять стили, такие как полужирный, курсив, подчёркнутый, или очистить существующее форматирование текста аннотации.

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

### Настраиваемый внешний вид цифровой подписи

Добавьте изображения, измените шрифты и наложите графику подписи поверх фонового контента для улучшения брендинга или согласованности дизайна.

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

## Что нового в Aspose.PDF 25.5

Последнее обновление Aspose.PDF вводит несколько мощных улучшений, которые повышают доступность документов, совместимость и безопасность. Теперь разработчики могут извлекать цифровые сертификаты непосредственно из подписанных PDF‑файлов, позволяя проводить расширенную проверку и проверки соответствия.

1. Извлечь сертификаты из подписей PDF.
1. Создавайте структурированные упорядоченные списки в Tagged PDFs.
1. Проверьте подписи с помощью сертификатов открытого ключа.
1. Преобразовать динамические формы XFA в PDF‑файлы AcroForm.
1. Замена шрифтов в PDF - конвертация в XPS.

### Извлечь сертификаты из подписей PDF

Получить встроенные сертификаты с помощью 'extract_certificate()'.

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

### Создать структурированные упорядоченные списки в Tagged PDF

Создавайте доступные нумерованные списки (с вложенными элементами) в помеченных документах.

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

### Проверка подписей с использованием сертификатов открытого ключа

Проверять цифровые подписи с использованием внешних сертификатов публичных ключей.

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

### Преобразовать динамические формы XFA в PDF‑файлы AcroForm

Стандартизировать формы XFA с параметром 'ignore_needs_rendering'.

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

### Замена шрифтов в PDF - преобразование в XPS

Заменять отсутствующие Font на запасный шрифт по умолчанию (например, «Courier New»).

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

## Что нового в Aspose.PDF 25.4

### Автоматическое тегирование при конвертации PDF/A

Преобразовать PDF в PDF/A-1b с автоматическим созданием логической структуры для повышения доступности.

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
