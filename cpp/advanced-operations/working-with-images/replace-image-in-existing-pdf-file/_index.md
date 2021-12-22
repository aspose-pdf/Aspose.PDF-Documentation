---
title: Replace Image in Existing PDF File uisng C++
linktitle: Replace Image
type: docs
weight: 70
url: /cpp/replace-image-in-existing-pdf-file/
description: This section describes about replace image in existing PDF file using ++ library.
lastmod: "2021-12-18"
---

The Images collection’s Replace method allows you to replace an image in an existing PDF file.

The Images collection can be found in a page’s Resources collection. To replace an image:

1. Open the PDF file using the Document object.
2. Replace a particular image, save the updated PDF file using Save method of the Document object.

The following code snippet shows you how to replace an image in a PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Replace a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Save updated PDF file
    document->Save(_dataDir + u"output.pdf");
}
```
