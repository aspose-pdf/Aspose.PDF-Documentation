---
title: Licensing and evaluation
linktitle: Licensing and limitations
type: docs
weight: 50
url: /cpp/licensing/
description: Evaluate Aspose.PDF for C++, understand evaluation restrictions, and apply a license from a file or stream.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Apply a License to Aspose.PDF for C++
Abstract: Evaluate the library with documented trial restrictions or apply a license before processing documents. The examples show how to load a license from an explicit file path or a readable stream.
---

Aspose.PDF for C++ can be evaluated before purchase. The evaluation documentation describes watermarked output and a limit of four processed items per collection.

Request a [temporary license](https://purchase.aspose.com/temporary-license/) when you need to evaluate without these restrictions. See [pricing and purchase options](https://purchase.aspose.com/pricing/pdf/cpp/) for commercial licensing.

## Apply a license from a file

1. Create a [License](https://reference.aspose.com/pdf/cpp/aspose.pdf/license/) object.
1. Call [SetLicense()](https://reference.aspose.com/pdf/cpp/aspose.pdf/license/setlicense/) with the license path before processing PDFs.

```cpp
#include <Aspose.PDF.Cpp/License.h>
#include <system/string.h>

void ApplyLicense(System::String licenseFile)
{
    auto license = System::MakeObject<Aspose::Pdf::License>();
    license->SetLicense(licenseFile);
}
```

## Apply a license from a stream

Open the license file as a readable stream and pass it to SetLicense().

```cpp
#include <Aspose.PDF.Cpp/License.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

void ApplyLicenseFromStream(System::String licenseFile)
{
    auto stream = System::IO::File::OpenRead(licenseFile);
    auto license = System::MakeObject<Aspose::Pdf::License>();
    license->SetLicense(stream);
    stream->Close();
}
```

Use an explicit path to avoid relying on working-directory lookup. Use the same initialization for a purchased or temporary license.
