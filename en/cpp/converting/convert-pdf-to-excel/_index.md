---
title: Convert PDF to spreadsheets in C++
linktitle: Convert PDF to Spreadsheets
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
description: Export PDFs to XLSX, XLSM, CSV, ODS, or SpreadsheetML and configure worksheet and column options.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to Spreadsheets Using C++
Abstract: Select spreadsheet output formats with ExcelSaveOptions. The XLSX variants request a blank first column or fewer worksheets, while other examples export XLSM, CSV, ODS, and SpreadsheetML 2003.
---

Export PDFs to XLSX, XLSM, CSV, ODS, or SpreadsheetML and configure worksheet and column options.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Convert PDF to XLSX

Select ExcelSaveOptions::ExcelFormat::XLSX.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::XLSX` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXlsx(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<ExcelSaveOptions>();
	options->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);
	document->Save(outputFile, options);
}
}
```

## Insert a blank first column

Set InsertBlankColumnAtFirst to true for XLSX output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::XLSX` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `InsertBlankColumnAtFirst` to `true` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.


```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXlsxWithBlankColumn(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<ExcelSaveOptions>();
	options->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);
	options->set_InsertBlankColumnAtFirst(true);
	document->Save(outputFile, options);
}
}
```

## Minimize the number of worksheets

Set MinimizeTheNumberOfWorksheets to true for XLSX output. The example requests fewer worksheets without manually merging worksheet content.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::XLSX` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `MinimizeTheNumberOfWorksheets` to `true` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXlsxSingleWorksheet(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<ExcelSaveOptions>();
	options->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);
	options->set_MinimizeTheNumberOfWorksheets(true);
	document->Save(outputFile, options);
}
}
```

## Convert PDF to XLSM

Select ExcelFormat::XLSM. This example does not add VBA macros.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::XLSM` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXlsm(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<ExcelSaveOptions>();
	options->set_Format(ExcelSaveOptions::ExcelFormat::XLSM);
	document->Save(outputFile, options);
}
}
```

## Convert PDF to CSV

Select ExcelFormat::CSV to save tabular output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::CSV` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToCsv(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<ExcelSaveOptions>();
		options->set_Format(ExcelSaveOptions::ExcelFormat::CSV);
		document->Save(outputFile, options);
	}
}
```

## Convert PDF to ODS

Select ExcelFormat::ODS for OpenDocument spreadsheet output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::ODS` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToOds(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<ExcelSaveOptions>();
		options->set_Format(ExcelSaveOptions::ExcelFormat::ODS);
		document->Save(outputFile, options);
	}
}
```

## Convert PDF to SpreadsheetML

Select ExcelFormat::XMLSpreadSheet2003 for the XML spreadsheet format.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Set `Format` to `ExcelSaveOptions::ExcelFormat::XMLSpreadSheet2003` in [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToSpreadsheetMl(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<ExcelSaveOptions>();
		options->set_Format(ExcelSaveOptions::ExcelFormat::XMLSpreadSheet2003);
		document->Save(outputFile, options);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

