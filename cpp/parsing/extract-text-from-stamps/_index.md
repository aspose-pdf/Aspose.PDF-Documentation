---
title: Extract Text From Stamps using C#
type: docs
weight: 60
url: /cpp/extract-text-from-stamps/
---

## Extract Text from Stamp Annotations

Aspose.PDF for C++ lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used.

1. Create a Document class object
1. Get the desired Annotation from list of annotations of a page
1. Define a new object of TextAbsorber class
1. Use the TextAbsorber's visit method to get the Text

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // String for path name
      String _dataDir("C:\\Samples\\Parsing\\");

      // String for file name
      String infilename("ExtractStampText.pdf");

      auto document = MakeObject<Document>(_dataDir + infilename);

      auto item = document->get_Pages()->idx_get(1)->get_Annotations()->idx_get(1);
      if (item->get_AnnotationType() == Annotations::AnnotationType::Stamp) {
            auto annot = System::DynamicCast<Aspose::Pdf::Annotations::StampAnnotation>(item);
            auto ta = MakeObject<TextAbsorber>();
            auto ap = annot->get_Appearance()->idx_get(u"N");
            ta->Visit(ap);
            Console::WriteLine(ta->get_Text());
      }
}
```
