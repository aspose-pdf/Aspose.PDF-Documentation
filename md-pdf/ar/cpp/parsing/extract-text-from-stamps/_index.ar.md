---
title: استخراج النص من الأختام
linktitle: استخراج النص من الأختام
type: docs
weight: 60
url: /cpp/extract-text-from-stamps/
---

## استخراج النص من التعليقات التوضيحية للأختام

تتيح لك Aspose.PDF for C++ استخراج النص من التعليقات التوضيحية للأختام. من أجل استخراج النص من التعليقات التوضيحية للأختام في ملف PDF، يمكن استخدام الخطوات التالية.

1. قم بإنشاء كائن من فئة Document
1. احصل على التعليق التوضيحي المطلوب من قائمة التعليقات التوضيحية لصفحة
1. قم بتعريف كائن جديد من فئة TextAbsorber
1. استخدم طريقة visit الخاصة بـ TextAbsorber للحصول على النص

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
```