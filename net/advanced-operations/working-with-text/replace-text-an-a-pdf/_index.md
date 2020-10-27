---
title: Replace Text in a PDF Document
type: docs
weight: 40
url: /net/replace-text-in-a-pdf-document/
---
# Replace Text in a PDF Document

## Replace Text in all pages of PDF document
>You can try to find in replace the text in the document using Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/redaction](https://products.aspose.app/pdf/redaction)

In order to replace text in all the pages of a PDF document, you first need to use TextFragmentAbsorber to find the particular phrase you want to replace. After that, you need to go through all the TextFragments to replace the text and change any other attributes. Once you have done that, you only need to save the output PDF using the Save method of the Document object. The following code snippet shows you how to replace text in all pages of PDF document.
```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");
            
// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");
            
// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);
            
// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
            
// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Update text and other properties
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// Save resulting PDF document.
pdfDocument.Save(dataDir);
```
## Replace Text in particular page region
In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using TextSearchOptions.Rectangle property and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the Save method of the Document object.  The following code snippet shows you how to replace text in all pages of PDF document.
```
// load PDF file

Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instantiate TextFragment Absorber object

Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// search text within page bound

TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// specify the page region for TextSearch Options

TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// search text from first page of PDF file

pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// iterate through individual TextFragment

foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)

{

    // update text to blank characters

    tf.Text = "";

}

    // save updated PDF file after text replace

pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## Replace Text Based on a Regular Expression
If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. You will have to pass the regular expression as a parameter to the TextFragmentAbsorber constructor. You also need to create TextSearchOptions object which specifies whether the regular expression is being used or not. Once you get the matching phrases in TextFragments, you need to loop through all of them and update as required. Finally, you need to save the updated PDF using the Save method of the Document object. The following code snippet shows you how to replace text based on a regular expression.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");
            
// Create TextAbsorber object to find all the phrases matching the regular expression
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000
            
// Set text search option to specify regular expression usage
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;
            
// Accept the absorber for a single page
pdfDocument.Pages[1].Accept(textFragmentAbsorber);
            
// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
            
// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Update text and other properties
    textFragment.Text = "New Phrase";
    // Set to an instance of an object.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## Replace fonts in existing PDF file
Aspose.PDF for .NET supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document. So instead of replacing the text, only font being used is replaced. One of the overloads of TextFragmentAbsorber constructor accepts TextEditOptions object as an argument and we can use RemoveUnusedFonts value from TextEditOptions.FontReplace enumeration to accomplish our requirements. The following code snippet shows how to replace the font inside PDF document.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Load source PDF file
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Search text fragments and set edit option as remove unused fonts
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Accept the absorber for all the pages
pdfDocument.Pages.Accept(absorber);
// Traverse through all the TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // If the font name is ArialMT, replace font name with Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```
## Text Replacement should automatically re-arrange Page Contents
Aspose.PDF for .NET supports the feature to search and replace text inside the PDF file. However recently some customers encountered issues during text replace when particular TextFragment is replaced with smaller contents and some extra spaces are displayed in resultant PDF or in case the TextFragment is replaced with some longer string, then words overlap existing page contents. So the requirement was to introduce a mechanism that once the text inside a PDF document is replaced, the contents should be re-arranged.

In order to cater above-stated scenarios, Aspose.PDF for .NET has been enhanced so that no such issues appear when replacing text inside PDF file. The following code snippet shows how to replace text inside PDF file and the page contents should be re-arranged automatically.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Load source PDF file
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Create TextFragment Absorber object with regular expression
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Replace each TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Set font of text fragment being replaced
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Set font size
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Replace the text with larger string than placeholder
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Save resultant PDF
doc.Save(dataDir);
```
## Rendering Replaceable Symbols during PDF creation
Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time. Replaceable symbols currently support by new Document Object Model of Aspose.PDF namespace are $P, $p, \n, \r. The $p and $P are used to deal with the page numbering at run time. $p is replaced with the number of the page where the current Paragraph class is in. $P is replaced with the total number of pages in the document. When adding TextFragment to the paragraphs collection of PDF documents, it does not support line feed inside the text. However in order to add text with a line feed, please use TextFragment with TextParagraph:

- use “\r\n” or Environment.NewLine in TextFragment instead of single “\n”;
- create a TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Initialize new TextFragment with text containing required newline markers
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// Set text fragment properties if necessary
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Create TextParagraph object
TextParagraph par = new TextParagraph();

// Add new TextFragment to paragraph
par.AppendLine(textFragment);

// Set paragraph position
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Create TextBuilder object
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Add the TextParagraph using TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## Replaceable symbols in Header/Footer area
Replaceable symbols can also be placed inside the Header/Footer section of PDF file. Please take a look over the following code snippet for details on how to add replaceable symbol in the footer section.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Assign the marginInfo instance to Margin property of sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instantiate a Text paragraph that will store the content to show as header
TextFragment t1 = new TextFragment("report title");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Report_Name");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Create a HeaderFooter object for the section
HeaderFooter hfFoot = new HeaderFooter();
// Set the HeaderFooter object to odd & even footer
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Add a text paragraph containing current page number of total number of pages
TextFragment t3 = new TextFragment("Generated on test date");
TextFragment t4 = new TextFragment("report name ");
TextFragment t5 = new TextFragment("Page $p of $P");

// Instantiate a table object
Table tab2 = new Table();

// Add the table in paragraphs collection of the desired section
hfFoot.Paragraphs.Add(tab2);

// Set with column widths of the table
tab2.ColumnWidths = "165 172 165";

// Create rows in the table and then cells in the rows
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Set the vertical allignment of the text as center alligned
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Add the table in paragraphs collection of the desired section
page.Paragraphs.Add(table);

// Set default cell border using BorderInfo object
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Set table border using another customized BorderInfo object
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Create rows in the table and then cells in the rows
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## Remove Unused Fonts from PDF File
Aspose.PDF for .NET supports the feature to embed fonts while creating a PDF document, as well as the capability to embed fonts in existing PDF files. From Aspose.PDF for .NET 7.3.0, it also lets you remove duplicate or unused fonts from PDF documents.

To replace fonts, use the following approach:

1. Call the [TextFragmentAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) class.
1. Call the TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts parameter. (This removes fonts that have become unused during font replacement).
1. Set font individually for each text fragment.
The following code snippet replaces font for all text fragments of all document pages and removes unused fonts.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Load source PDF file
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterate through all the TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Save updated document
doc.Save(dataDir);
```
## Remove All Text from PDF Document
### Remove All Text using Operators 
In some text operation, you need to remove all text from PDF document and for that, you need to set found text as empty string value usually. The point is that changing the text for multitude text fragments invokes a number of checking and text position adjustment operations. They are essential in the text editing scenarios. The difficulty is that you cannot determine how many text fragments will be removed in the scenario where they are processed in a loop.

Therefore, we recommend using another approach for the scenario of removing all text from PDF pages. Please consider the following code snippet that works very fast.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Loop through all pages of PDF Document
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Select all text on the page
    page.Contents.Accept(operatorSelector);
    // Delete all text
    page.Contents.Delete(operatorSelector.Selected);
}
// Save the document
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```
