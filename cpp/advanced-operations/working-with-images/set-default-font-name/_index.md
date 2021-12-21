---
title: Set Default Font Name
linktitle: Set Default Font Name
type: docs
weight: 90
url: /cpp/set-default-font-name/
description: This section describes how to set default font name using C++ library.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** API allows you to set a default font name when a font is not available in the document. You can use DefaultFontName property of RenderingOptions class to set the default font name. In case DefaultFontName is set to null the **Times New Roman** font will be used. The following code snippet shows how to set a default font name when saving PDF into an image:

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
	String _dataDir("C:\\Samples\\");
	auto document = MakeObject<Document>(_dataDir + u"input.pdf");

	auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

	auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
	auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
	auto ro = MakeObject<RenderingOptions>();
	ro->set_DefaultFontName(u"Arial");
	pngDevice->set_RenderingOptions(ro);
	pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```
