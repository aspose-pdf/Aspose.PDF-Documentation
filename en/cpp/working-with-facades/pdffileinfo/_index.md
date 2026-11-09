---
title: Inspect PDF file information in C++
linktitle: PdfFileInfo Class
type: docs
weight: 90
url: /cpp/pdffileinfo-class/
description: Read and update metadata, inspect page dimensions, offsets, privileges, encryption flags, and PDF version using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Properties and Update Metadata in C++
Abstract: Use PdfFileInfo to inspect document metadata, page geometry, permissions, and file flags. The examples also write custom information, clear metadata, and save updated information with XMP.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) to read and update metadata, inspect page dimensions, offsets, privileges, encryption flags, and PDF version.

PdfFileInfo opens the PDF through its constructor. Page information examples inspect page 1; offset examples convert points to inches by dividing by 72.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Clear PDF metadata

Clear document information, save the output, and close PdfFileInfo.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Clear document information with [PdfFileInfo::ClearInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/clearinfo/).
1. Save the resulting PDF with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Save()`.
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void ClearPdfMetadata(String inputFile, String outputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		pdfInfo->ClearInfo();
		pdfInfo->Save(outputFile);
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```

## Get document privileges

Print the document's printing, copying, editing, annotation, form, accessibility, and assembly privileges.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read document permissions with [PdfFileInfo::GetDocumentPrivilege()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getdocumentprivilege/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void GetDocumentPrivileges(String inputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		auto privileges = pdfInfo->GetDocumentPrivilege();

		std::cout << "Document Privileges:" << std::endl;
		std::cout << "  Can Print: " << privileges->get_AllowPrint() << std::endl;
		std::cout << "  Can Degraded Print: " << privileges->get_AllowDegradedPrinting() << std::endl;
		std::cout << "  Can Copy: " << privileges->get_AllowCopy() << std::endl;
		std::cout << "  Can Modify Contents: " << privileges->get_AllowModifyContents() << std::endl;
		std::cout << "  Can Modify Annotations: " << privileges->get_AllowModifyAnnotations() << std::endl;
		std::cout << "  Can Fill In: " << privileges->get_AllowFillIn() << std::endl;
		std::cout << "  Can Screen Readers: " << privileges->get_AllowScreenReaders() << std::endl;
		std::cout << "  Can Assembly: " << privileges->get_AllowAssembly() << std::endl;
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```

## Get page information

Print page 1 width, height, and rotation.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the page width with [PdfFileInfo::GetPageWidth()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagewidth/).
1. Read the page height with [PdfFileInfo::GetPageHeight()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpageheight/).
1. Read the page rotation with [PdfFileInfo::GetPageRotation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagerotation/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetPageInformation(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << "Page Width: " << pdfInfo->GetPageWidth(1) << std::endl;
    std::cout << "Page Height: " << pdfInfo->GetPageHeight(1) << std::endl;
    std::cout << "Page Rotation: " << pdfInfo->GetPageRotation(1) << std::endl;
    pdfInfo->Close();
}
} // namespace  Facades::Examples::PDF_FileInfo
```

## Get page offsets

Print page 1 X and Y offsets in inches.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the X offset with [PdfFileInfo::GetPageXOffset()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagexoffset/).
1. Read the Y offset with [PdfFileInfo::GetPageYOffset()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpageyoffset/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void GetPageOffsets(String inputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		std::cout << "Page X Offset: " << (pdfInfo->GetPageXOffset(1) / 72.0) << " inches" << std::endl;
		std::cout << "Page Y Offset: " << (pdfInfo->GetPageYOffset(1) / 72.0) << " inches" << std::endl;
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```

## Get PDF metadata

Print document information, file-status flags, and the custom Reviewer metadata value when available.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read creation date through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read mod date through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read is pdf file through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read is encrypted through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has open password through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has edit password through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has collection through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read custom metadata with [PdfFileInfo::GetMetaInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getmetainfo/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetPdfMetadata(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << "Subject: " << pdfInfo->get_Subject() << std::endl;
    std::cout << "Title: " << pdfInfo->get_Title() << std::endl;
    std::cout << "Keywords: " << pdfInfo->get_Keywords() << std::endl;
    std::cout << "Creator: " << pdfInfo->get_Creator() << std::endl;
    std::cout << "Creation Date: " << pdfInfo->get_CreationDate() << std::endl;
    std::cout << "Modification Date: " << pdfInfo->get_ModDate() << std::endl;
    std::cout << "Is Valid PDF: " << pdfInfo->get_IsPdfFile() << std::endl;
    std::cout << "Is Encrypted: " << pdfInfo->get_IsEncrypted() << std::endl;
    std::cout << "Has Open Password: " << pdfInfo->get_HasOpenPassword() << std::endl;
    std::cout << "Has Edit Password: " << pdfInfo->get_HasEditPassword() << std::endl;
    std::cout << "Is Portfolio: " << pdfInfo->get_HasCollection() << std::endl;
    auto reviewer = pdfInfo->GetMetaInfo(u"Reviewer");
    std::cout << "Reviewer: " << (reviewer.IsNullOrEmpty() ? u"No Reviewer metadata found." : reviewer) << std::endl;
    pdfInfo->Close();
}
} // namespace  Facades::Examples::PDF_FileInfo
```

## Get PDF version

Print the PDF version.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the PDF version with [PdfFileInfo::GetPdfVersion()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpdfversion/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetPdfVersion(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << std::endl;
    std::cout << String(u"PDF Version: ") << pdfInfo->GetPdfVersion() << std::endl;
    pdfInfo->Close();
}
} // namespace Facades::Examples::PDF_FileInfo
```

## Save info with XMP

Set subject, title, keywords, and creator and save the updated document information with XMP.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Set subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Save document information and XMP with [PdfFileInfo::SaveNewInfoWithXmp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/savenewinfowithxmp/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void SaveInfoWithXmp(String inputFile, String outputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		pdfInfo->set_Subject(u"Aspose PDF for C++");
		pdfInfo->set_Title(u"Aspose PDF for C++");
		pdfInfo->set_Keywords(u"Aspose, PDF, C++");
		pdfInfo->set_Creator(u"Aspose Team");
		pdfInfo->SaveNewInfoWithXmp(outputFile);
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```

## Set PDF metadata

Set standard document information and the custom CustomKey value.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Set subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set custom metadata with [PdfFileInfo::SetMetaInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/setmetainfo/).
1. Save the resulting PDF with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Save()`.
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetPdfMetadata(String inputFile, String outputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    pdfInfo->set_Subject(u"Aspose PDF for C++");
    pdfInfo->set_Title(u"Aspose PDF for C++");
    pdfInfo->set_Keywords(u"Aspose, PDF, C++");
    pdfInfo->set_Creator(u"Aspose Team");
    pdfInfo->SetMetaInfo(u"CustomKey", u"CustomValue");
    pdfInfo->Save(outputFile);
    pdfInfo->Close();
}
} // namespace Facades::Examples::PDF_FileInfo
```
