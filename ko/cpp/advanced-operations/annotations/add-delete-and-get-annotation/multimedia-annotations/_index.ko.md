---
title: PDF 멀티미디어 주석 사용 C++
linktitle: 멀티미디어 주석
type: docs
weight: 40
url: /cpp/multimedia-annotation/
description: Aspose.PDF for C++를 사용하여 PDF 문서에서 멀티미디어 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

비디오, 오디오 및 대화형 콘텐츠를 추가하면 PDF가 문서에 대한 관심과 참여를 높이는 다차원 커뮤니케이션 도구로 바뀝니다. PDF 형식 파일의 이러한 콘텐츠를 멀티미디어 주석이라고 합니다.

PDF 문서의 주석은 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체의 Annotations 컬렉션에 포함되어 있습니다. 이 컬렉션은 해당 개별 페이지에 대한 모든 주석을 포함하며, 각 페이지는 자체 Annotations 컬렉션을 가지고 있습니다. 특정 페이지에 주석을 추가하려면 Add 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가하십시오.

Aspose.PDF.InteractiveFeatures.Annotations 네임스페이스의 [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) 클래스를 사용하여 PDF 문서에 주석으로 SWF 파일을 대신 포함하십시오. A screen annotation specifies a region of a page upon which media clips may be played.

When you need to add an external video link in PDF document, you can use [MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation).
A Movie Annotation contains animated graphics and sound to be presented on the computer screen and through the speakers.

A [Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) shall analogous to a text annotation except that instead of a text note, it contains sound recorded from the computer's microphone or imported from a file. When the annotation is activated, the sound shall be played. The annotation shall behave like a text annotation in most ways, with a different icon (by default, a speaker) to indicate that it represents a sound.

However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
## 화면 주석 추가

다음 코드 조각은 PDF 파일에 화면 주석을 추가하는 방법을 보여줍니다:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일을 로드합니다
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // 화면 주석 생성
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## 소리 주석 추가

다음 코드 조각은 PDF 파일에 소리 주석을 추가하는 방법을 보여줍니다:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // PDF 파일을 로드합니다
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // 소리 주석 생성
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Sound Annotation demo");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}
```

## RichMediaAnnotation 추가

다음 코드 스니펫은 PDF 파일에 RichMediaAnnotation을 추가하는 방법을 보여줍니다:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // 비디오 데이터에 이름을 지정합니다. 이 데이터는 문서에 이 이름으로 포함되고, 
    // 이 이름으로 플래시 변수에서 참조됩니다.
    // videoName은 파일 경로를 포함해서는 안됩니다; 이는 PDF 문서 내 데이터를 
    // 액세스하기 위한 "키"입니다.

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // 또한 비디오 플레이어에 대한 스킨을 사용합니다.
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // 여기서 비디오 플레이어의 코드가 포함된 스트림을 지정해야 합니다.
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // 플레이어에 대한 플래시 변수 라인을 구성합니다. 다른 플레이어는 
    // 플래시 변수 라인의 다른 형식을 가질 수 있음을 유의하십시오.
    // 플레이어의 문서를 참조하십시오.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // 스킨 코드를 추가합니다.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // 비디오에 대한 포스터를 설정합니다.
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // 비디오 콘텐츠를 설정합니다.
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // 콘텐츠 유형을 설정합니다 (비디오)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // 클릭으로 플레이어 활성화
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // 주석 데이터를 업데이트합니다. 이 메서드는 모든 할당/설정 후에 호출해야 합니다.
    // 이 메서드는 주석의 데이터 구조를 초기화하고 필요한 데이터를 포함합니다.
    rma->Update();

    // 페이지에 주석을 추가합니다.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### 멀티미디어 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 멀티미디어 주석을 가져오십시오.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### 멀티미디어 주석 삭제

다음 코드 스니펫은 PDF 파일에서 멀티미디어 주석을 삭제하는 방법을 보여줍니다.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## 3D 주석 추가

오늘날 PDF 파일은 논리 구조, 주석 및 양식 필드와 같은 상호작용 요소, 레이어, 멀티미디어(비디오 콘텐츠 포함), 3D 객체를 포함하여 단순한 텍스트 및 그래픽 외에도 다양한 콘텐츠를 포함할 수 있습니다.

이러한 3D 콘텐츠는 3D 주석을 사용하여 PDF 파일에서 볼 수 있습니다.

이 섹션은 Aspose.PDF의 C++ 라이브러리를 사용하여 PDF 문서에 3D 주석을 생성하는 기본 단계를 보여줍니다.

3D 주석은 U3D 형식으로 생성된 모델을 사용하여 추가됩니다.

1. 새 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 생성
1. 원하는 3D 모델의 데이터를 로드하여 [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/) 생성
1. [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) 객체를 생성하고 문서 및 3DContent에 연결
1. pdf3dArtWork 객체 조정:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // PDF 파일 로드
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //필요한 경우 미리보기 이미지 설정
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

이 코드 예제는 우리에게 이런 모델을 보여주었습니다:

![3D Annotation demo](3d_demo.png)


## 위젯 주석 추가

위젯 주석은 대화형 PDF 양식에서 양식 필드의 외관을 나타냅니다.

PDF v 1.2 이후로 우리는 위젯 주석을 사용할 수 있습니다. 이러한 주석은 PDF에 추가하여 사용자와 함께 정보를 입력하거나 제출하거나 다른 작업을 수행하는 것을 쉽게 해주는 대화형 양식 요소입니다. 위젯은 특별한 유형의 주석이지만, 특정 페이지에 있는 양식 필드의 그래픽 표현이기 때문에 직접 주석으로 만들 수는 없습니다.

문서의 각 위치에 대한 각 양식 필드는 하나의 주석 위젯을 나타냅니다. 위젯에 대한 위치별 주석 데이터는 특정 페이지에 추가됩니다. 각 양식 필드는 여러 옵션을 가지고 있습니다. 버튼은 토글, 체크박스 또는 버튼이 될 수 있습니다. 선택 위젯은 리스트 박스 또는 콤보 박스가 될 수 있습니다.

Aspose.PDF for C++를 사용하면 [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/) 클래스를 사용하여 이 주석을 추가할 수 있습니다.

페이지에 버튼을 추가하려면 다음 코드 스니펫을 사용해야 합니다: 

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"현재 문서 인쇄");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"문서 인쇄");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### 문서 탐색 작업 사용하기

이 예제는 4개의 버튼을 만드는 방법을 보여줍니다:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"첫 페이지로 이동", u"이전 페이지로 이동", u"다음 페이지로 이동", u"마지막 페이지로 이동" });
    auto normalCaptions = MakeArray<String>({ u"처음", u"이전", u"다음", u"마지막" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// 버튼을 페이지에 연결하지 않고 만들어야 합니다.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// 문서의 각 페이지에 이 버튼 배열을 복제해야 합니다.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### 위젯 주석 삭제

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // 주석 삭제
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```