---
title: 스탬프에서 텍스트 추출
linktitle: 스탬프에서 텍스트 추출
type: docs
weight: 60
url: /ko/cpp/extract-text-from-stamps/
---

## 스탬프 주석에서 텍스트 추출

Aspose.PDF for C++를 사용하면 스탬프 주석에서 텍스트를 추출할 수 있습니다. PDF에서 스탬프 주석의 텍스트를 추출하기 위해 다음 단계를 사용할 수 있습니다.

1. Document 클래스 객체를 생성합니다.
1. 페이지의 주석 목록에서 원하는 주석을 가져옵니다.
1. TextAbsorber 클래스의 새 객체를 정의합니다.
1. TextAbsorber의 방문 메서드를 사용하여 텍스트를 가져옵니다.

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // 경로 이름에 대한 문자열
      String _dataDir("C:\\Samples\\Parsing\\");

      // 파일 이름에 대한 문자열
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