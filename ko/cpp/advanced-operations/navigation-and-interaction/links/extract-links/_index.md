---
title: PDF 파일에서 링크 추출
linktitle: 링크 추출
type: docs
weight: 30
url: ko/cpp/extract-links/
description: C#으로 PDF에서 링크를 추출합니다. 이 주제는 AnnotationSelector 클래스를 사용하여 링크를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에서 링크 추출

링크는 PDF 파일에서 주석으로 표현되므로, 링크를 추출하려면 모든 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 추출해야 합니다.

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성합니다.
1. 링크를 추출하려는 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 가져옵니다.
1. 문서의 지정된 페이지에서 모든 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 추출하기 위해 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 클래스를 사용하십시오.
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 객체를 Page 객체의 Accept 메서드에 전달합니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 객체의 Selected 속성을 사용하여 모든 선택된 링크 주석을 IList 객체에 가져옵니다.

다음 코드 스니펫은 PDF 파일에서 링크를 추출하는 방법을 보여줍니다.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // PDF 파일 로드
    String _dataDir("C:\\Samples\\");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation located: {0}", annot->get_Rect());
    }
}
```