---
title: Extract Data from Table in PDF using C++
linktitle: Extract Data from Table
type: docs
weight: 40
url: /cpp/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Tables from PDF programmatically

Since PDF is the most common format for exchanging documents, let's consider a document with several datasets that need analysis. In this article, we will describe the extraction of tables from PDF.

**Aspose.PDF for C++** provides developers with the tools they need to extract data from tables in PDF documents.

This example demonstrates the use of the [TableAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) Class to retrieve tabular data from tables in a PDF file.

The following example shows table extraction from the all pages:

```cpp
void ExtractTable() {
	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-table.pdf");


	auto document = MakeObject<Document>(_dataDir + infilename);
	auto absorber = MakeObject<TableAbsorber>();

	// Scan pages
	for (auto page : document->get_Pages()) {
		absorber->Visit(page);
		for (auto table : absorber->get_TableList()) {
			std::cout << "Table" << std::endl;
			// Iterate throught list of rows
			for (auto row : table->get_RowList()) {
				// Iterate throught list of cell
				for (auto cell : row->get_CellList()) {
					String sb;
					for (auto fragment : cell->get_TextFragments()) {
						sb += fragment->get_Text();
					}
					std::cout << sb << "|";
				}
				std::cout << std::endl;
			}
		}
	}
	std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract table in specific area of PDF page

Each abosorbed table has [Rectangle](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) property that describes position of the table on page.

So, if you need to extract tables located in a specific region, you have to work with specific coordinates.

The following example show how to extract table marked with Square Annotation:

```cpp
void ExtractMarkedTable()
{
	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-table.pdf");


	auto document = MakeObject<Document>(_dataDir + infilename);
	auto absorber = MakeObject<TableAbsorber>();

	auto page = document->get_Pages()->idx_get(1);
	auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
	auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


	auto list = annotationSelector->get_Selected();
	if (list->get_Count() == 0) {
		std::cerr << "Marked tables not found.." << std::endl;
		return;
	}

	auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

	absorber->Visit(page);

	for (auto table : absorber->get_TableList())
	{
		auto isInRegion =
			(squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
			(squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
			(squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
			(squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

		if (isInRegion)
		{
			for (auto row : table->get_RowList()) {
				// Iterate throught list of cell
				for (auto cell : row->get_CellList()) {
					String sb;
					for (auto fragment : cell->get_TextFragments()) {
						sb += fragment->get_Text();
					}
					std::cout << sb << "|";
				}
				std::cout << std::endl;
			}
		}
	}
	std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract Table Data from PDF and store it in CSV file

The following example shows how to extract table and store it as CSV file.
To see how to convert PDF to Excel Spreadsheet please refer to [Convert PDF to Excel](/pdf/cpp/convert-pdf-to-excel/) article.

```cpp
void ExtractTableSaveCSV()
{
	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-table.pdf");
	String outfilename("PDFToXLS_out.csv");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Instantiate ExcelSave Option object
	auto excelSave = MakeObject<ExcelSaveOptions>();
	excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

	// Save the output in XLS format
	document->Save(_dataDir + outfilename, excelSave);
	std::clog << __func__ << ": Finish" << std::endl;
}
```
