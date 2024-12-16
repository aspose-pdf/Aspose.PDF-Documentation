---
title: PDF에서 동작 작업하기
linktitle: 동작
type: docs
weight: 20
url: /ko/cpp/actions/
description: 이 섹션에서는 C++로 문서 및 양식 필드에 동작을 프로그래밍적으로 추가하는 방법을 설명합니다.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 하이퍼링크 추가하기

PDF 문서는 정보를 공유하는 훌륭한 방법입니다. 읽기, 편집 및 배포가 쉽습니다. 그러나 PDF 문서에 링크를 만드는 것은 어려울 수 있습니다. 방법을 보여드리겠습니다.

PDF 파일에 하이퍼링크를 추가하여 독자가 PDF의 다른 부분으로 이동하거나 외부 콘텐츠로 이동할 수 있습니다.

예를 들어, 전자책에 클릭 가능한 목차를 추가하거나, 기사에 외부 리소스를 인용하거나, 주제에 대한 추가 정보를 얻기 위해 웹사이트의 다른 페이지로 독자를 빠르게 이동시키고 싶을 수 있습니다.

몇 번의 클릭으로 하이퍼링크를 만들려면 다음 간단한 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 생성합니다.  
1. 링크를 추가하고자 하는 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스를 가져옵니다.  
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 생성합니다. Rectangle 객체는 링크가 추가될 페이지의 위치를 지정하는 데 사용됩니다.  
1. 원격 URI의 위치를 지정하는 [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) 객체로 Action 속성을 설정합니다.  
1. 하이퍼링크 텍스트를 표시하려면 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) 객체가 배치된 위치와 유사한 위치에 텍스트 문자열을 추가합니다.  
1. 자유 텍스트를 추가하려면:

- [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) 객체를 인스턴스화합니다. Page 및 Rectangle 객체를 인수로 허용하므로 LinkAnnotation 생성자에 지정된 동일한 값을 제공할 수 있습니다.
- [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) 객체의 Contents 속성을 사용하여 출력 PDF에 표시될 문자열을 지정합니다.
- 선택적으로 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 및 FreeTextAnnotation 객체의 테두리 너비를 0으로 설정하여 PDF 문서에 나타나지 않도록 할 수 있습니다.
- [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 및 [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) 객체가 정의되면 이러한 링크를 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체의 Annotations 컬렉션에 추가합니다.

- 마지막으로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.
다음 코드 스니펫은 PDF 파일에 하이퍼링크를 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// 문서 열기

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// 링크 생성

auto page = document->get_Pages()->idx_get(1);

// 링크 주석 객체 생성

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// LinkAnnotation을 위한 경계 객체 생성

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// 경계 너비 값을 0으로 설정

border->set_Width(0);

// LinkAnnotation에 경계 설정

link->set_Border(border);

// 링크 유형을 원격 URI로 지정

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// PDF 파일의 첫 페이지의 주석 컬렉션에 링크 주석 추가

page->get_Annotations()->Add(link);


// 자유 텍스트 주석 생성

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// 자유 텍스트로 추가될 문자열

textAnnotation->set_Contents(u"Link to Aspose website");

// 자유 텍스트 주석에 경계 설정

textAnnotation->set_Border(border);

// 문서의 첫 페이지의 주석 컬렉션에 FreeText 주석 추가

page->get_Annotations()->Add(textAnnotation);


// 업데이트된 문서 저장

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## 동일한 PDF의 페이지에 하이퍼링크 생성

Aspose.PDF for C++는 PDF 생성 및 조작에 훌륭한 기능을 제공합니다. 또한 PDF 페이지에 링크를 추가하는 기능을 제공하며, 링크는 다른 PDF 파일의 페이지로 직접 연결되거나 웹 URL, 애플리케이션 실행 링크 또는 동일한 PDF 파일의 페이지로 연결될 수 있습니다. 로컬 하이퍼링크(동일한 PDF 파일의 페이지로의 링크)를 추가하기 위해 [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink)라는 클래스가 Aspose.PDF 네임스페이스에 추가되었으며, 이 클래스에는 하이퍼링크의 대상/목적 페이지를 지정하는 데 사용되는 TargetPageNumber라는 속성이 있습니다.

로컬 하이퍼링크를 추가하기 위해, 링크가 TextFragment와 연결될 수 있도록 TextFragment를 생성해야 합니다. [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) 클래스에는 LocalHyperlink 인스턴스를 연결하는 데 사용되는 Hyperlink이라는 속성이 있습니다. 다음 코드 스니펫은 이 요구 사항을 달성하는 단계를 보여줍니다.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// 문서 인스턴스 생성

auto document = MakeObject<Document>();


// PDF 파일의 페이지 컬렉션에 페이지 추가

auto page = document->get_Pages()->Add();


// Text Fragment 인스턴스 생성

auto text = MakeObject<TextFragment>(u"link page number test to page 2");


// 로컬 하이퍼링크 인스턴스 생성

auto link = MakeObject<LocalHyperlink>();


// 링크 인스턴스에 대상 페이지 설정

link->set_TargetPageNumber(2);


// TextFragment 하이퍼링크 설정

text->set_Hyperlink(link);


// 페이지의 단락 컬렉션에 텍스트 추가

page->get_Paragraphs()->Add(text);


// 새로운 TextFragment 인스턴스 생성

text = new TextFragment(u"link page number test to page 1");


// TextFragment는 새 페이지에 추가되어야 함

text->set_IsInNewPage(true);


// 또 다른 로컬 하이퍼링크 인스턴스 생성

link = new LocalHyperlink();


// 두 번째 하이퍼링크에 대한 대상 페이지 설정

link->set_TargetPageNumber(1);


// 두 번째 TextFragment에 대한 링크 설정

text->set_Hyperlink(link);


// 페이지 객체의 단락 컬렉션에 텍스트 추가

page->get_Paragraphs()->Add(text);


// 업데이트된 문서 저장

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## PDF 하이퍼링크 대상 (URL) 가져오기

링크는 PDF 파일에서 주석으로 표시되며 추가, 업데이트 또는 삭제할 수 있습니다. Aspose.PDF for C++는 또한 PDF 파일에서 하이퍼링크의 대상(URL)을 가져오는 것을 지원합니다.

링크의 URL을 가져오려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성합니다.
1. 링크를 추출하려는 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 가져옵니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 클래스를 사용하여 지정된 페이지에서 모든 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) 객체를 추출합니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 객체를 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체의 Accept 메서드에 전달합니다.
1. 모든 선택된 링크 주석을 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 객체의 Selected 속성을 사용하여 IList 객체로 가져옵니다.  
1. 마지막으로, LinkAnnotation Action을 GoToURIAction으로 추출합니다.

다음 코드 스니핏은 PDF 파일에서 하이퍼링크 목적지(URL)를 가져오는 방법을 보여줍니다.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// 작업 추출

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// 리스트 내부의 개별 항목 반복

if (list->get_Count() == 0)


Console::WriteLine(u"No Hyperlinks found...");

else {


// 모든 북마크를 반복


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// 목적지 URL 출력




Console::WriteLine(u"Destination: " + action->get_URI());



}


}

} // end else
}
```
## 하이퍼링크 텍스트 가져오기

하이퍼링크는 문서에 표시되는 텍스트와 대상 URL의 두 부분으로 구성됩니다. 경우에 따라 필요한 것은 URL이 아니라 텍스트입니다.

PDF 파일의 텍스트와 주석/작업은 서로 다른 엔티티로 표현됩니다. 페이지의 텍스트는 단지 단어와 문자 세트일 뿐이며, 주석은 하이퍼링크에 내재된 것과 같은 상호작용성을 제공합니다.

URL 내용을 찾으려면 주석과 텍스트 모두를 작업해야 합니다. [주석](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) 객체는 자체적으로 텍스트를 가지지 않지만 페이지의 텍스트 아래에 위치합니다. 따라서 텍스트를 얻으려면 주석이 URL의 경계를 제공하고, 텍스트 객체가 URL 내용을 제공합니다. 다음 코드 스니펫을 참조하십시오.

## PDF 파일에서 문서 열기 동작 제거하기

[문서 보기 시 PDF 페이지 지정 방법](#how-to-specify-pdf-page-when-viewing-document)에서는 문서가 첫 페이지가 아닌 다른 페이지에서 열리도록 지시하는 방법을 설명했습니다. 여러 문서를 연결할 때, 하나 이상의 문서에 GoTo 동작이 설정되어 있다면 이를 제거하고 싶을 것입니다. 예를 들어, 두 개의 문서를 결합할 때 두 번째 문서에 GoTo 동작이 설정되어 두 번째 페이지로 이동하게 되면, 출력 문서는 결합된 문서의 첫 페이지가 아닌 두 번째 문서의 두 번째 페이지에서 열리게 됩니다. 이러한 동작을 피하려면, 열기 동작 명령을 제거해야 합니다.

열기 동작을 제거하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) 속성을 null로 설정합니다.
1. Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 문서 열기 동작을 제거하는 방법을 보여줍니다.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// 문서 열기

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// 문서 열기 작업 제거

document->set_OpenAction(nullptr);


// 업데이트된 문서 저장

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## 문서 보기 시 PDF 페이지 지정 방법 {#how-to-specify-pdf-page-when-viewing-document}

Adobe Reader와 같은 PDF 뷰어에서 PDF 파일을 볼 때 파일은 일반적으로 첫 페이지에서 열립니다. 그러나 다른 페이지에서 파일을 열도록 설정할 수 있습니다.

'XYZExplicitDestination' 클래스는 열고자 하는 PDF 파일의 페이지를 지정할 수 있도록 합니다. GoToAction 객체 값을 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 OpenAction 속성에 전달하면, 문서는 XYZExplicitDestination 객체에 대해 지정된 페이지에서 열립니다. 다음 코드 스니펫은 문서 열기 작업으로 페이지를 지정하는 방법을 보여줍니다.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// PDF 파일 로드

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// 문서의 두 번째 페이지 인스턴스 가져오기

auto page2 = document->get_Pages()->idx_get(2);

// 대상 페이지의 확대 비율을 설정할 변수 생성

double zoom = 1;

// GoToAction 인스턴스 생성

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// 2페이지로 이동

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// 문서 열기 작업 설정

document->set_OpenAction(action);

// 업데이트된 문서 저장

document->Save(_dataDir + u"goto2page_out.pdf");
}
```