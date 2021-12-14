---
title: Replace Text in PDF 
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from PDF. Aspose.PDF allows replacing text in a particular region or with a regular expression.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Sometimes a task appears to correct or replace text in a PDF document. Trying to do it manually will be a daunting task, so here is the solution to that problem.

Honestly, editing a PDF file is not an easy task. So, a situation, where you need to find and replace one word with another while editing a PDF file, will be very difficult as it will take you a long time to do it. In addition, you may encounter many problems with your output, such as formatting or broken fonts. If you want to easily find and replace text in PDF files, we recommend that you use the Aspose.Pdf library software as it will get the job done in minutes.

In this article, we will show you how to successfully find and replace text in your PDF files using Aspose.PDF for C++.

## Replace Text in all pages of PDF document

{{% alert color="primary" %}}

You can try to find in replace the text in the document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

In order to replace text in all the pages of a PDF document, you first need to use TextFragmentAbsorber to find the particular phrase you want to replace. After that, you need to go through all the TextFragments to replace the text and change any other attributes. Once you have done that, you only need to save the output PDF using the Save method of the Document object. The following code snippet shows you how to replace text in all pages of PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {
    
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Replace Text in particular page region

In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using TextSearchOptions.Rectangle property and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the Save method of the Document object.  The following code snippet shows you how to replace text in all pages of PDF document.

```cpp
void ReplaceTextInParticularRegion() {
    
    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // instantiate TextFragment Absorber object
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // search text within page bound
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // specify the page region for TextSearch Options
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // search text from first page of PDF file
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // iterate through individual TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // replace text with "---"
        tf->set_Text(u"---");
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Replace Text Based on a Regular Expression

If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. You will have to pass the regular expression as a parameter to the TextFragmentAbsorber constructor. You also need to create TextSearchOptions object which specifies whether the regular expression is being used or not. Once you get the matching phrases in TextFragments, you need to loop through all of them and update as required. Finally, you need to save the updated PDF using the Save method of the Document object. The following code snippet shows you how to replace text based on a regular expression.

```cpp
void ReplaceTextWithRegularExpression() {
    
    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Replace fonts in existing PDF file

Aspose.PDF for C++ supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document. So instead of replacing the text, only font being used is replaced. One of the overloads of TextFragmentAbsorber constructor accepts TextEditOptions object as an argument and we can use RemoveUnusedFonts value from TextEditOptions.FontReplace enumeration to accomplish our requirements. The following code snippet shows how to replace the font inside PDF document.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Search text fragments and set edit option as remove unused fonts
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // Accept the absorber for all pages of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // traverse through all the TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // if the font name is ArialMT, replace font name with Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

In the next code snippet, you will see how to use non-English font when replacing text:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Lets to change every of word "PDF" to some Japan text with specific font
    // MSGothic that might be installed in the OS
    // Also, it may be another font that supports hieroglyphs
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Create instance of Text Search options
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Accept the absorber for all pages of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Save the updated document
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## Text Replacement should automatically re-arrange Page Contents

Aspose.PDF for C++ supports finding and replacing text within a PDF file. Recently, however, some clients have run into problems when replacing text, where a particular TextFragment is replaced with smaller content and some extra whitespace is displayed in the resulting PDF, or if the TextFragment is replaced with some longer string, then the words overlap the existing page content. Thus, it was required to introduce a mechanism that, after replacing the text inside the PDF document, rearranged its content.

To serve the aforementioned scenarios, Aspose.PDF for C++ has been improved so that such issues do not occur when replacing text within a PDF file. The following code snippet demonstrates how to replace text within a PDF file and the page content should be reordered automatically.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Create TextFragment Absorber object with regular expression
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // You also can specify the ReplaceAdjustment.WholeWordsHyphenation option to
    // wrap text on the next or current line if the current line becomes too long or
    // short after replacement:    
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Accept the absorber for all pages of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Replace each TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Set font of text fragment being replaced
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Set font size
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Replace the text with larger string than placeholder
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Save resultant PDF
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Rendering Replaceable Symbols during PDF creation

Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time. Replaceable symbols currently support by new Document Object Model of Aspose.PDF namespace are `$P`, `$p,` `\n`, `\r`. The `$p` and `$P` are used to deal with the page numbering at run time. `$p` is replaced with the number of the page where the current Paragraph class is in. `$P` is replaced with the total number of pages in the document. When adding `TextFragment` to the paragraphs collection of PDF documents, it does not support line feed inside the text. However in order to add text with a line feed, please use `TextFragment` with `TextParagraph`:

- use "\r\n" or Environment.NewLine in TextFragment instead of single "\n";
- create a TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.

```cpp
void RenderingReplaceableSymbols() {
    
    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->Add();

    // Initialize new TextFragment with text containing required newline markers
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Set text fragment properties if necessary
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Create TextParagraph object
    auto par = MakeObject<TextParagraph>();

    // Add new TextFragment to paragraph
    par->AppendLine(textFragment);

    // Set paragraph position
    par->set_Position(MakeObject<Position>(100, 600));

    // Create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(page);

    // Add the TextParagraph using TextBuilder
    textBuilder->AppendParagraph(par);

    document->Save(_dataDir + u"RenderingReplaceableSymbols_out.pdf");
}
```

## Replaceable symbols in Header/Footer area

The replaceable symbol can also be placed inside the header/footer section of the PDF file. Review the following code snippet to see how to add a replaceable symbol to a footer section.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Assign the marginInfo instance to Margin property of PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instantiate a Text paragraph that will store the content to show as header
    auto t1 = MakeObject<TextFragment>("report title");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Report_Name");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Create a HeaderFooter object for the section
    auto hfFoot = MakeObject<HeaderFooter>();

    // Set the HeaderFooter object to odd & even footer
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Add a text paragraph containing current page number of total number of pages
    auto t3 = MakeObject<TextFragment>("Generated on test date");
    auto t4 = MakeObject<TextFragment>("report name ");
    auto t5 = MakeObject<TextFragment>("Page $p of $P");

    // Instantiate a table object
    auto tab2 = MakeObject<Table>();

    // Add the table in paragraphs collection of the desired section
    hfFoot->get_Paragraphs()->Add(tab2);

    // Set with column widths of the table
    tab2->set_ColumnWidths(u"165 172 165");

    // Create rows in the table and then cells in the rows
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Set the vertical allignment of the text as center alligned
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Add the table in paragraphs collection of the desired section
    page.getParagraphs().add(table);

    // Set default cell border using BorderInfo object
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Set table border using another customized BorderInfo object
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Create rows in the table and then cells in the rows
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ is a compilation of every Java component offered by Aspose. It is compiled on a"
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"Using Aspose.Total for C++ developers can create a wide range of applications.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Remove All Text from PDF Document

### Remove All Text using Operators

In some text operations, you need to remove all text from the PDF document, and for that, you usually need to set the found text as an empty string value. The fact is that changing the text for a set of text fragments causes a number of operations to check and adjust the position of the text. They are required in text editing scripts. The difficulty lies in the fact that you cannot determine how many chunks of text will be deleted in the script where they are processed in the loop.

Therefore, we recommend using a different approach for the scenario of removing all text from PDF pages.

The following code snippet shows how to resolve this task fast.

```cpp
void RemoveAllTextUsingOperators() {
    
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Loop through all pages of PDF Document
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Select all text on the page
        page->get_Contents()->Accept(operatorSelector);
        // Delete all text
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Save the document
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```
