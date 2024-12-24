---
title: Replace Text in PDF
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /net/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "The Replace Text in PDF feature in Aspose.PDF for .NET allows users to efficiently locate and replace text across an entire PDF document or within specific page regions. It supports advanced capabilities, including text replacement based on regular expressions, automatic rearranging of page content after replacements, and the ability to remove unused fonts, enhancing the document editing experience",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Learn more about various ways of replacing and removing text from Aspose.PDF for .NET library."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Replace Text in all pages of PDF document

{{% alert color="primary" %}}

You can try to find in replace the text in the document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

In order to replace text in all the pages of a PDF document, you first need to use TextFragmentAbsorber to find the particular phrase you want to replace. After that, you need to go through all the TextFragments to replace the text and change any other attributes. Once you have done that, you only need to save the output PDF using the Save method of the Document object. The following code snippet shows you how to replace text in all pages of PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages(string folderPath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(folderPath + "ReplaceTextAll.pdf"))
	{
		// Create TextAbsorber object to find all instances of the input search phrase
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

		// Accept the absorber for all the pages
		document.Pages.Accept(absorber);

		// Get the extracted text fragments
		var textFragmentCollection = absorber.TextFragments;

		// Loop through the fragments
		foreach (var textFragment in textFragmentCollection)
		{
			// Update text and other properties
			textFragment.Text = "TEXT";
			textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
			textFragment.TextState.FontSize = 22;
			textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
			textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
		}

		// Save resulting PDF document
		document.Save(folderPath + "ReplaceTextAll_out.pdf");
	}
}
```

## Replace Text in particular page region

In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using TextSearchOptions.Rectangle property and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the Save method of the Document object.  The following code snippet shows you how to replace text in all pages of PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion(string inputFilePath, string outputFilePath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(inputFilePath))
	{
		// instantiate TextFragment Absorber object
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

		// search text within page bound
		absorber.TextSearchOptions.LimitToPageBounds = true;

		// specify the page region for TextSearch Options
		absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

		// search text from first page of PDF file
		document.Pages[1].Accept(absorber);

		// iterate through individual TextFragment
		foreach (var textFragment in absorber.TextFragments)
		{
			// update text to blank characters
			textFragment.Text = "";
		}

		// save updated PDF file after text replace
		document.Save(outputFilePath);
	}
}
```

## Replace Text Based on a Regular Expression

If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. You will have to pass the regular expression as a parameter to the TextFragmentAbsorber constructor. You also need to create TextSearchOptions object which specifies whether the regular expression is being used or not. Once you get the matching phrases in TextFragments, you need to loop through all of them and update as required. Finally, you need to save the updated PDF using the Save method of the Document object. The following code snippet shows you how to replace text based on a regular expression.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression(string inputFilePath, string outputFilePath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(inputFilePath))
	{

		// Create TextAbsorber object to find all the phrases matching the regular expression
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

		// Set text search option to specify regular expression usage
		absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

		// Accept the absorber for a single page
		document.Pages[1].Accept(absorber);

		// Get the extracted text fragments
		var collection = absorber.TextFragments;

		// Loop through the fragments
		foreach (var textFragment in collection)
		{
			// Update text and other properties
			textFragment.Text = "New Phrase";
			// Set to an instance of an object.
			textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
			textFragment.TextState.FontSize = 22;
			textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
			textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
		}

		document.Save(outputFilePath);
	}
}
```

## Replace fonts in existing PDF file

Aspose.PDF for .NET supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document. So instead of replacing the text, only font being used is replaced. One of the overloads of TextFragmentAbsorber constructor accepts TextEditOptions object as an argument and we can use RemoveUnusedFonts value from TextEditOptions.FontReplace enumeration to accomplish our requirements. The following code snippet shows how to replace the font inside PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts(string inputFilePath, string outputFilePath)
{
	// Load source PDF file
	using (var document = new Aspose.Pdf.Document(inputFilePath))
	{
		// Create text edit options
		var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

		// Search text fragments and set edit option as remove unused fonts
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

		// Accept the absorber for all the pages
		document.Pages.Accept(absorber);

		// Traverse through all the TextFragments
		foreach (var textFragment in absorber.TextFragments)
		{
			// If the font name is ArialMT, replace font name with Arial
			if (textFragment.TextState.Font.FontName == "Arial,Bold")
			{
				textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
			}
		}

		// Save updated document
		document.Save(outputFilePath);
	}
}
```

## Text Replacement should automatically re-arrange Page Contents

Aspose.PDF for .NET supports the feature to search and replace text inside the PDF file. However recently some customers encountered issues during text replace when particular TextFragment is replaced with smaller contents and some extra spaces are displayed in resultant PDF or in case the TextFragment is replaced with some longer string, then words overlap existing page contents. So the requirement was to introduce a mechanism that once the text inside a PDF document is replaced, the contents should be re-arranged.

In order to cater above-stated scenarios, Aspose.PDF for .NET has been enhanced so that no such issues appear when replacing text inside PDF file. The following code snippet shows how to replace text inside PDF file and the page contents should be re-arranged automatically.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents(string folderPath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(folderPath + "ExtractTextPage.pdf"))
	{

		// Create TextFragment Absorber object with regular expression
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
		document.Pages.Accept(absorber);

		// Replace each TextFragment
		foreach (var textFragment in absorber.TextFragments)
		{
			// Set font of text fragment being replaced
			textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
			// Set font size
			textFragment.TextState.FontSize = 12;
			textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
			// Replace the text with larger string than placeholder
			textFragment.Text = "This is a Larger String for the Testing of this issue";
		}

		// Save resultant PDF
		document.Save(folderPath + "RearrangeContentsUsingTextReplacement_out.pdf");
	}
}
```

## Rendering Replaceable Symbols during PDF creation

Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time. Replaceable symbols currently support by new Document Object Model of Aspose.PDF namespace are `$P`, `$p,` `\n`, `\r`. The `$p` and `$P` are used to deal with the page numbering at run time. `$p` is replaced with the number of the page where the current Paragraph class is in. `$P` is replaced with the total number of pages in the document. When adding `TextFragment` to the paragraphs collection of PDF documents, it does not support line feed inside the text. However in order to add text with a line feed, please use `TextFragment` with `TextParagraph`:

- Use "\r\n" or Environment.NewLine in TextFragment instead of single "\n".
- Create a TextParagraph object. It will add text with line splitting.
- Add the TextFragment with TextParagraph.AppendLine.
- Add the TextParagraph with TextBuilder.AppendParagraph.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols(string folderPath)
{
	// Create document
	using (var document = new Aspose.Pdf.Document())
	{
		var page = document.Pages.Add();

		// Initialize new TextFragment with text containing required newline markers
		Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

		// Set text fragment properties if necessary
		textFragment.TextState.FontSize = 12;
		textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
		textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
		textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

		// Create TextParagraph object
		var par = new Aspose.Pdf.Text.TextParagraph();

		// Add new TextFragment to paragraph
		par.AppendLine(textFragment);

		// Set paragraph position
		par.Position = new Aspose.Pdf.Text.Position(100, 600);

		// Create TextBuilder object
		var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

		// Add the TextParagraph using TextBuilder
		textBuilder.AppendParagraph(par);
		
		// Save document
		document.Save(folderPath + "RenderingReplaceableSymbols_out.pdf");
	}
}
```

## Replaceable symbols in Header/Footer area

Replaceable symbols can also be placed inside the Header/Footer section of PDF file. Please take a look over the following code snippet for details on how to add replaceable symbol in the footer section.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea(string folderPath)
{
	// Create document
	using (var document = new Aspose.Pdf.Document())
	{
		var page = document.Pages.Add();

		// Create margin info
		var marginInfo = new Aspose.Pdf.MarginInfo();
		marginInfo.Top = 90;
		marginInfo.Bottom = 50;
		marginInfo.Left = 50;
		marginInfo.Right = 50;
		// Assign the marginInfo instance to Margin property of sec1.PageInfo
		page.PageInfo.Margin = marginInfo;

		var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
		page.Header = headerFooterFirst;
		headerFooterFirst.Margin.Left = 50;
		headerFooterFirst.Margin.Right = 50;

		// Instantiate a Text paragraph that will store the content to show as header
		var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
		fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
		fragment1.TextState.FontSize = 16;
		fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
		fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
		fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
		fragment1.TextState.LineSpacing = 5f;
		headerFooterFirst.Paragraphs.Add(fragment1);

		var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
		fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
		fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
		fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
		fragment2.TextState.LineSpacing = 5f;
		fragment2.TextState.FontSize = 12;
		headerFooterFirst.Paragraphs.Add(fragment2);

		// Create a HeaderFooter object for the section
		var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

		// Set the HeaderFooter object to odd & even footer
		page.Footer = headerFooterFoot;
		headerFooterFoot.Margin.Left = 50;
		headerFooterFoot.Margin.Right = 50;

		// Add a text paragraph containing current page number of total number of pages
		var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
		var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
		var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

		// Instantiate a table object
		var table2 = new Aspose.Pdf.Table();

		// Add the table in paragraphs collection of the desired section
		headerFooterFoot.Paragraphs.Add(table2);

		// Set with column widths of the table
		table2.ColumnWidths = "165 172 165";

		// Create rows in the table and then cells in the rows
		var row3 = table2.Rows.Add();

		row3.Cells.Add();
		row3.Cells.Add();
		row3.Cells.Add();

		// Set the vertical allignment of the text as center alligned
		row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
		row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
		row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

		row3.Cells[0].Paragraphs.Add(fragment3);
		row3.Cells[1].Paragraphs.Add(fragment4);
		row3.Cells[2].Paragraphs.Add(fragment5);

		// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
		var table = new Aspose.Pdf.Table();

		table.ColumnWidths = "33% 33% 34%";
		table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
		table.DefaultCellPadding.Top = 10;
		table.DefaultCellPadding.Bottom = 10;

		// Add the table in paragraphs collection of the desired section
		page.Paragraphs.Add(table);

		// Set default cell border using BorderInfo object
		table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

		// Set table border using another customized BorderInfo object
		table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

		table.RepeatingRowsCount = 1;

		// Create rows in the table and then cells in the rows
		var row1 = table.Rows.Add();

		row1.Cells.Add("col1");
		row1.Cells.Add("col2");
		row1.Cells.Add("col3");
		const string CRLF = "\r\n";
		for (int i = 0; i <= 10; i++)
		{
			var row = table.Rows.Add();
			row.IsRowBroken = true;
			for (int c = 0; c <= 2; c++)
			{
				Aspose.Pdf.Cell c1;
				if (c == 2)
				{
					c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
				}
				else
				{
					c1 = row.Cells.Add("item1" + c);
				}
				c1.Margin = new Aspose.Pdf.MarginInfo();
				c1.Margin.Left = 30;
				c1.Margin.Top = 10;
				c1.Margin.Bottom = 10;
			}
		}

		// Save document
		document.Save(folderPath + "ReplaceableSymbolsInHeaderFooter_out.pdf");
	}
}
```

## Remove Unused Fonts from PDF File

Aspose.PDF for .NET supports the feature to embed fonts while creating a PDF document, as well as the capability to embed fonts in existing PDF files. From Aspose.PDF for .NET 7.3.0, it also lets you remove duplicate or unused fonts from PDF documents.

To replace fonts, use the following approach:

1. Call the [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) class.
1. Call the TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts parameter. (This removes fonts that have become unused during font replacement).
1. Set font individually for each text fragment.

The following code snippet replaces font for all text fragments of all document pages and removes unused fonts.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts(string folderPath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(folderPath + "ReplaceTextPage.pdf"))
	{
		var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
		var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
		document.Pages.Accept(absorber);

		// Iterate through all the TextFragments
		foreach (var textFragment in absorber.TextFragments)
		{
			textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
		}

		// Save updated document
		document.Save(folderPath + "RemoveUnusedFonts_out.pdf");
	}
}
```

## Remove All Text from PDF Document

### Remove All Text using Operators

In some text operation, you need to remove all text from PDF document and for that, you need to set found text as empty string value usually. The point is that changing the text for multitude text fragments invokes a number of checking and text position adjustment operations. They are essential in the text editing scenarios. The difficulty is that you cannot determine how many text fragments will be removed in the scenario where they are processed in a loop.

Therefore, we recommend using another approach for the scenario of removing all text from PDF pages. Please consider the following code snippet that works very fast.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument(string folderPath)
{
	// Open document
	using (var document = new Aspose.Pdf.Document(folderPath + "RemoveAllText.pdf"))
	{
		// Loop through all pages of PDF Document
		for (int i = 1; i <= document.Pages.Count; i++)
		{
			var page = document.Pages[i];
			var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
			// Select all text on the page
			page.Contents.Accept(operatorSelector);
			// Delete all text
			page.Contents.Delete(operatorSelector.Selected);
		}
		// Save the document
		document.Save(folderPath + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
	}
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
