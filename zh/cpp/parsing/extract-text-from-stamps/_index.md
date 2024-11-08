---
title: 从印章中提取文本 
linktitle: 从印章中提取文本
type: docs
weight: 60
url: /zh/cpp/extract-text-from-stamps/
---

## 从印章注释中提取文本

Aspose.PDF for C++ 允许您从印章注释中提取文本。为了从 PDF 中的印章注释提取文本，可以使用以下步骤。

1. 创建一个 Document 类对象
1. 从页面的注释列表中获取所需的注释
1. 定义一个新的 TextAbsorber 类对象
1. 使用 TextAbsorber 的 visit 方法获取文本

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // 路径名称的字符串
      String _dataDir("C:\\Samples\\Parsing\\");

      // 文件名的字符串
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