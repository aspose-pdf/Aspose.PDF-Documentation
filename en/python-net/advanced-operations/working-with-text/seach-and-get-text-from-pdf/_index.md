---
title: Search and Get Text from Pages of PDF
linktitle: Search and Get Text
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: Learn how to search and extract text from PDF documents in Python using Aspose.PDF for document analysis.
lastmod: "2025-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Search and Get Text from Pages in PDF
Abstract: The article provides an in-depth exploration of text extraction and manipulation capabilities within PDF documents using the Aspose.PDF for Python via .NET library. It introduces the TextFragmentAbsorber class, which allows developers to search through an entire document or specific pages for designated phrases or regular expression patterns. The page outlines various practical scenarios—such as retrieving text content, determining its position (including coordinates and indent values), and extracting font properties like name, size, embed status, and color—from the matched text fragments. Detailed code examples demonstrate the process step-by-step, making it easier for developers to integrate text searching capabilities into their applications.
---

## Search and Get Text from All the Pages of PDF Document

1. Open a PDF Document.
1. Create a Text Absorber.
1. Apply the Absorber to All Pages.
1. Extract and Display Text Properties.

The following code snippet shows you how to search for text from all the pages:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        absorber = ap.text.TextFragmentAbsorber("text")

        # Accept the absorber for all the pages
        document.pages.accept(absorber)

        # Loop through the fragments
        for text_fragment in absorber.text_fragments:
            print(f"Text : {text_fragment.text}")
            print(f"Position : {text_fragment.position}")
            print(f"x_indent : {text_fragment.position.x_indent}")
            print(f"y_indent : {text_fragment.position.y_indent}")
            print(f"Font - Name : {text_fragment.text_state.font.font_name}")
            print(f"Font - is_accessible : {text_fragment.text_state.font.is_accessible}")
            print(f"Font - is_embedded : {text_fragment.text_state.font.is_embedded}")
            print(f"Font - is_subset : {text_fragment.text_state.font.is_subset}")
            print(f"Font Size : {text_fragment.text_state.font_size}")
            print(f"Foreground Color : {text_fragment.text_state.foreground_color}")
```

In case you need to search text inside any particular PDF page, please specify the page number from pages collection of Document instance and call 'accept' method against that page (as shown in code line below).

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        text_fragment_absorber = ap.text.TextFragmentAbsorber("text")
        # Accept the absorber for a particular page
        document.pages[2].accept(text_fragment_absorber)
```

## Search and Get Text Segments from All Pages of PDF Document

1. Opening the PDF Document.
1. Creating a Text Fragment Absorber.
1. Scanning All Pages.
1. Retrieving Extracted Text Fragments.
1. Iterating Through Text Fragments and Segments.
1. Extracting and Printing Detailed Information.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        text_fragment_absorber = ap.text.TextFragmentAbsorber("Figure")
        # Accept the absorber for all the pages
        document.pages.accept(text_fragment_absorber)
        # Get the extracted text fragments
        text_fragment_collection = text_fragment_absorber.text_fragments
        # Loop through the fragments
        for text_fragment in text_fragment_collection:
            for text_segment in text_fragment.segments:
                print(f"Text : {text_segment.text}")
                print(f"Position : {text_segment.position}")
                print(f"x_indent : {text_segment.position.x_indent}")
                print(f"y_indent : {text_segment.position.y_indent}")
                print(f"Font - Name : {text_segment.text_state.font.font_name}")
                print(f"Font - is_accessible : {text_segment.text_state.font.is_accessible}")
                print(f"Font - is_embedded : {text_segment.text_state.font.is_embedded}")
                print(f"Font - is_subset : {text_segment.text_state.font.is_subset}")
                print(f"Font Size : {text_segment.text_state.font_size}")
                print(f"Foreground Color : {text_segment.text_state.foreground_color}")
```

In order to search and get TextSegments from a particular page of PDF, you need to specify the particular page. Please take a look at the following code lines.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        text_fragment_absorber = ap.text.TextFragmentAbsorber("text")
        # Accept the absorber for a particular page
        document.pages[2].accept(text_fragment_absorber)
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber helps you search and retrieve text, from all the pages, based on a regular expression.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        text_fragment_absorber = ap.text.TextFragmentAbsorber("\\d{4}-\\d{4}")
        # Set text search option to specify regular expression usage
        options = ap.text.TextSearchOptions(True)

        text_fragment_absorber.text_search_options = options

        # Accept the absorber for all the pages
        document.pages.accept(text_fragment_absorber)

        # Loop through the fragments
        for text_fragment in text_fragment_absorber.text_fragments:
            for text_segment in text_fragment.segments:
                print(f"Text : {text_segment.text}")
                print(f"Position : {text_segment.position}")
                print(f"x_indent : {text_segment.position.x_indent}")
                print(f"y_indent : {text_segment.position.y_indent}")
                print(f"Font - Name : {text_segment.text_state.font.font_name}")
                print(f"Font - is_accessible : {text_segment.text_state.font.is_accessible}")
                print(f"Font - is_embedded : {text_segment.text_state.font.is_embedded}")
                print(f"Font - is_subset : {text_segment.text_state.font.is_subset}")
                print(f"Font Size : {text_segment.text_state.font_size}")
                print(f"Foreground Color : {text_segment.text_state.foreground_color}")
```

## Search Text based on Regex and Add Hyperlink

If you want to add hyperlink over a text phrase based on regular expression, first find all the phrases matching that particular regular expression using TextFragmentAbsorber and add hyperlink over these phrases.

To find a phrase and add hyperlink over it:

1. Opening the PDF Document with PdfContentEditor.
1. Searching for the Pattern in a Specific Page.
1. Processing the Matched Text Fragments.
1. Adding Annotations.
1. Saving the Modified PDF.

```python

    import aspose.pdf as ap

    absorber = ap.text.TextFragmentAbsorber("\\d{4}-\\d{4}")
    # Enable regular expression search
    absorber.text_search_options = ap.text.TextSearchOptions(True)
    # Open document
    with ap.facades.PdfContentEditor() as editor:
        # Bind source PDF file
        editor.bind_pdf(path_infile)
        # Accept the absorber for the page
        editor.document.pages[1].accept(absorber)

        # Loop through the fragments
        for text_fragment in absorber.text_fragments:
            text_fragment.text_state.foreground_color = ap.Color.blue
            rect = ap.Rectangle(
                text_fragment.rectangle.llx,
                text_fragment.rectangle.lly,
                text_fragment.rectangle.width + 2,
                text_fragment.rectangle.height + 1,
                True,
            )
            editor.create_web_link(
                rect.to_rect(), "http://www.aspose.com", 1, ap.Color.blue.to_rgb()
            )
            editor.create_line(
                rect.to_rect(),
                "",
                float(text_fragment.rectangle.llx + 1),
                float(text_fragment.rectangle.lly - 1),
                float(text_fragment.rectangle.urx),
                float(text_fragment.rectangle.lly - 1),
                1,
                1,
                ap.Color.blue.to_rgb(),
                "S",
                None,
                None,
            )

        editor.save(path_outfile)
```

## Search and Draw Rectangle around each TextFragment

Aspose.PDF for Python via .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character.

In case of a text paragraph, you may consider using some regular expression to determine the paragraph break and draw a rectangle around it.

Please take a look at the following code snippet. The following code snippet gets coordinates of each character and creates a rectangle around each character.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing
            
    def search_and_draw(self, infile, outfile):
        path_infile = self.data_dir + infile
        path_outfile = self.data_dir + outfile
        # Open PDF document 
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase        
        text_fragment_absorber = ap.text.TextFragmentAbsorber(".")
        text_search_options = ap.text.TextSearchOptions(True)
        text_fragment_absorber.text_search_options = text_search_options
        document.pages.accept(text_fragment_absorber) 
        for text_fragment in text_fragment_absorber.text_fragments:
            self.draw_rectangle_on_page(text_fragment.rectangle, text_fragment.page,
                                   ap.operators.SetRGBColorStroke(drawing.Color.red))
        # Save PDF document        
        document.save(path_outfile)

    def draw_rectangle_on_page(self, rectangle: ap.Rectangle, page: ap.Page, color_stroke: ap.operators.SetRGBColorStroke): 
        if color_stroke is None: 
            color_stroke = ap.operators.SetRGBColorStroke(0.7, 0, 0)
        page.contents.append(ap.operators.GSave())
        page.contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0))
        page.contents.append(color_stroke)
        page.contents.append(ap.operators.Re(rectangle.llx, rectangle.lly, rectangle.width, rectangle.height))
        page.contents.append(ap.operators.ClosePathStroke())    
        page.contents.append(ap.operators.GRestore())
```

## Highlight each character in PDF documen

Aspose.PDF for Python via .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character. The following code snippet gets coordinates of each character and creates a rectangle around each character.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing
    import io

    # Open PDF document
    with ap.Document(path_infile) as document:
        stream = io.BytesIO()
        conv = ap.facades.PdfConverter(document)
        conv.resolution = ap.devices.Resolution(resolution, resolution)
        conv.get_next_image(stream, drawing.imaging.ImageFormat.png)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(float(scale), float(0), float(0), float(-scale), float(0), float(bmp.height))
                for i in range(len(document.pages)):
                    page = document.pages[1]
                    # Create TextAbsorber object to find all words
                    text_fragment_absorber = ap.text.TextFragmentAbsorber( "[\S]+")
                    text_fragment_absorber.text_search_options.is_regular_expression_used = True
                    page.accept(text_fragment_absorber)
                    # Get the extracted text fragments
                    text_fragment_collection = text_fragment_absorber.text_fragments
                    # Loop through the fragments
                    for text_fragment in text_fragment_collection:
                        if i == 0:
                            gr.draw_rectangle(drawing.Pens.yellow, float(text_fragment.position.x_indent),
                                                float(text_fragment.position.y_indent),
                                                float(text_fragment.rectangle.width),
                                                float(text_fragment.rectangle.height))
                            for seg_num in range(1, len(text_fragment.segments) + 1):
                                segment = text_fragment.segments[seg_num]
                                for char_num in range(1, len(segment.characters)+1):
                                    character_info = segment.characters[char_num]
                                    rect = page.get_page_rect(True)
                                    print(f"TextFragment = {text_fragment.text}" + f" Page URY = {rect.ury}"
                                            + f" TextFragment URY = {text_fragment.rectangle.ury}")
                                    gr.draw_rectangle(drawing.Pens.black, float(character_info.rectangle.llx),
                                                        float(character_info.rectangle.lly),
                                                        float(character_info.rectangle.width),
                                                        float(character_info.rectangle.height))
                                gr.draw_rectangle(drawing.Pens.green, float(segment.rectangle.llx),
                                                    float(segment.rectangle.lly),
                                                    float(segment.rectangle.width),
                                                    float(segment.rectangle.height))
            # Save result
            bmp.save(path_outfile, drawing.imaging.ImageFormat.png)
```

## Add and Search Hidden Text

Sometimes we want to add hidden text in a PDF document and then search hidden text and use its position for post-processing.

1. Creating the PDF Document.
1. Adding a Page and Text Fragments.
1. Marking Text as Invisible.
1. Adding the Fragments to the Page and Saving.
1. Searching and Inspecting the PDF Content.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        page = document.pages.add()
        frag_1 = ap.text.TextFragment("This is common text.")
        frag_2 = ap.text.TextFragment("This is invisible text.")

        # Set text property - invisible
        frag_2.text_state.invisible = True

        page.paragraphs.add(frag_1)
        page.paragraphs.add(frag_2)
        document.save(path_outfile)

    # Search text in the document
    with ap.Document(path_outfile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])

        for fragment in absorber.text_fragments:
            # Do something with fragments
            print(f"Text '{fragment.text}' on pos {fragment.position} invisibility: {fragment.text_state.invisible} ")
```

## Searching bold text

Aspose.PDF for Python via .NET allows users to search documents using font style properties. The 'text_fragment_absorber' can be used for this purpose, as shown in the code sample below.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Search text in the document
    with ap.Document(path_infile) as document:
        # Create TextFragmentAbsorber object to extract text
        text_fragment_absorber = ap.text.TextFragmentAbsorber()
        # Accept the absorber for all document
        text_fragment_absorber.visit(document)
        #  Loop through the fragments
        for text_fragment in text_fragment_absorber.text_fragments:
            # Get the text properties of the text fragment
            text_state = text_fragment.text_state
            # Check if text is bold
            if text_state.font_style == ap.text.FontStyles.BOLD:
                # Print the text from the text fragment
                print(f"Text :- {text_fragment.text}")
```