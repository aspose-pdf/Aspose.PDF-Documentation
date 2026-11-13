---
title: Get Document Privileges in C++
linktitle: Get Document Privileges
type: docs
weight: 10
url: /cpp/get-document-privileges/
description: Get Document Privileges in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get Document Privileges with the PdfFileInfo Facade
Abstract: Print the document's printing, copying, editing, annotation, form, accessibility, and assembly privileges.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

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
