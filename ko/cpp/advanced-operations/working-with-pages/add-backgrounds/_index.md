---
title: PDF에 배경 추가하기 C++
linktitle: 배경 추가
type: docs
weight: 110
url: ko/cpp/add-backgrounds/
descriptions: C++로 PDF 파일에 배경 이미지를 추가합니다. BackgroundArtifact 객체를 사용합니다.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 파일에 배경을 추가하면 문서의 전체적인 가독성을 향상시키는 데 도움이 됩니다. PDF의 콘텐츠는 더욱 매력적으로 되며, 문서의 외관이 좋다면 독자들이 주목할 것입니다. 배경은 또한 PDF의 하이라이트를 강조하는 데 사용할 수 있습니다.

배경 이미지는 문서에 워터마크나 다른 미묘한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for C++에서는 각 PDF 문서가 페이지 모음이며 각 페이지는 아티팩트 모음을 포함하고 있습니다. [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) 클래스는 페이지 객체에 배경 이미지를 추가하는 데 사용할 수 있습니다.

다음 코드 조각은 C++로 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // 새 Document 객체 생성
    auto document = MakeObject<Document>();

    // 문서 객체에 새 페이지 추가
    auto page = document->get_Pages()->Add();

    // Background Artifact 객체 생성
    auto background = MakeObject<BackgroundArtifact>();

    // backgroundartifact 객체에 대한 이미지 지정
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // 페이지의 artifacts 컬렉션에 backgroundartifact 추가
    page->get_Artifacts()->Add(background);

    // 문서 저장
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```