---
title: Button Fields and Images in C++
linktitle: Button Fields and Images
type: docs
weight: 40
url: /cpp/button-fields-and-images/
description: Button Fields and Images in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Button Fields and Images with the Form Facade
Abstract: Fill the Image1_af_image button image field from an image stream.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add image appearance to button field

Fill the Image1_af_image button image field from an image stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the field image appearance with [Form::FillImageField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillimagefield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;
	using Form = Aspose::Pdf::Facades::Form;

	void AddImageAppearanceToButtonField(String inputFile, String imageFile, String outputFile)
	{
		auto form = MakeObject<Form>();
		auto imageStream = System::IO::File::OpenRead(imageFile);

		form->Facade::BindPdf(inputFile);
		form->FillImageField(u"Image1_af_image", imageStream);
		form->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_Form
```
