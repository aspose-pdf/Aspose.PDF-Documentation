---
title: Rotate Text Inside PDF
type: docs
weight: 50
url: /net/rotate-text-inside-pdf/
---
# Rotate Text Inside PDF

## Rotate Text Inside PDF using Rotation Property
By using the Rotation property of TextFragment Class, you can rotate text at various angles. The text rotation can be used in different scenarios of document generation. You can specify the rotation angle in degrees to rotate the text as per your requirement. Please check the following different scenarios, in which you can implement text rotation.

## Implement Rotation using TextFragment and TextBuilder
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Initialize document object
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Create text fragment
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// Set text properties
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Create rotated text fragment
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// Set text properties
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Create rotated text fragment
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// Set text properties
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// create TextBuilder object
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Append the text fragment to the PDF page
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Save document
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
view rawExamples-CSharp-AsposePDF-Text-RotateTextUsingTextFragment-RotateTextUsingTextFragment.cs hosted with ❤ by GitHub
Implement Rotation using TextParagraph and TextBuilder (Rotated Fragments)
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Initialize document object
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Create text fragment
TextFragment textFragment1 = new TextFragment("rotated text");
// Set text properties
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Set rotation
textFragment1.TextState.Rotation = 45;
// Create text fragment
TextFragment textFragment2 = new TextFragment("main text");
// Set text properties
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Create text fragment
TextFragment textFragment3 = new TextFragment("another rotated text");
// Set text properties
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Set rotation
textFragment3.TextState.Rotation = -45;
// Append the text fragments to the paragraph
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Create TextBuilder object
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Append the text paragraph to the PDF page
textBuilder.AppendParagraph(paragraph);
// Save document
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```
## Implement Rotation using TextFragment and Page.Paragraphs
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Initialize document object
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Create text fragment
TextFragment textFragment1 = new TextFragment("main text");
// Set text properties
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Create text fragment
TextFragment textFragment2 = new TextFragment("rotated text");
// Set text properties
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Set rotation
textFragment2.TextState.Rotation = 315;
// Create text fragment
TextFragment textFragment3 = new TextFragment("rotated text");
// Set text properties
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Set rotation
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Save document
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```
## Implement Rotation using TextParagraph and TextBuilder (Whole Paragraph Rotated)
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Initialize document object
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Specify rotation
    paragraph.Rotation = i * 90 + 45;
    // Create text fragment
    TextFragment textFragment1 = new TextFragment("Paragraph Text");
    // Create text fragment
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Create text fragment
    TextFragment textFragment2 = new TextFragment("Second line of text");
    // Set text properties
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Create text fragment
    TextFragment textFragment3 = new TextFragment("And some more text...");
    // Set text properties
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Create TextBuilder object
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Append the text fragment to the PDF page
    textBuilder.AppendParagraph(paragraph);
}
// Save document
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```
