---
title: PDF 멀티미디어 주석 사용하기 C#
linktitle: 멀티미디어 주석
type: docs
weight: 40
url: /net/multimedia-annotation/
description: Aspose.PDF for .NET을 사용하면 PDF 문서에서 멀티미디어 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 멀티미디어 주석 사용하기 C#",
    "alternativeHeadline": "PDF에서 멀티미디어 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 멀티미디어 주석, 화면 주석, 사운드 주석, 위젯 주석, 3D 주석",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 PDF 문서에서 멀티미디어 주석을 추가, 가져오기 및 삭제할 수 있습니다."
}
</script>
PDF 문서의 주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 주석 컬렉션에 포함되어 있습니다. 이 컬렉션은 해당 개별 페이지의 모든 주석을 포함합니다: 각 페이지는 자체 주석 컬렉션을 가지고 있습니다. 특정 페이지에 주석을 추가하려면 Add 메소드를 사용하여 해당 페이지의 주석 컬렉션에 추가하십시오.

PDF 문서에 SWF 파일을 주석으로 포함하려면 Aspose.PDF.InteractiveFeatures.Annotations 네임스페이스의 [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) 클래스를 사용하십시오. 스크린 주석은 미디어 클립이 재생될 수 있는 페이지의 영역을 지정합니다.

PDF 문서에 외부 비디오 링크를 추가할 필요가 있을 때는 [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation)을 사용할 수 있습니다.
영화 주석은 컴퓨터 화면과 스피커를 통해 제시될 애니메이션 그래픽과 사운드를 포함합니다.

[Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)은 텍스트 주석과 유사하지만 텍스트 노트 대신 컴퓨터 마이크로폰에서 녹음된 소리나 파일에서 가져온 소리를 포함합니다.
[사운드 주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)은 텍스트 주석과 유사하지만 텍스트 노트 대신 컴퓨터 마이크로폰에서 녹음된 소리 또는 파일에서 가져온 소리를 포함합니다.

그러나 PDF 문서 내에 미디어를 포함해야 할 경우 [리치미디어주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation)을 사용해야 합니다.

다음은 RichMediaAnnotation 클래스의 메소드/속성들입니다.

- Stream CustomPlayer { set; }: 비디오를 재생하는 데 사용되는 플레이어 설정을 허용합니다.
- string CustomFlashVariables { set; }: 플래시 애플리케이션에 전달되는 변수를 설정합니다. 이 줄은 '&'로 구분된 "key=value" 쌍의 집합입니다.
- void AddCustomData(strig name, Stream data): 플레이어를 위한 추가 데이터를 추가합니다. 예를 들어 source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: 플레이어를 활성화하는 이벤트; 가능한 값은 Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): 재생할 비디오/오디오 데이터를 설정합니다.
- void SetContent(Stream stream, string name): 비디오/오디오 데이터를 재생할 수 있도록 설정합니다.
- void Update(): 주석의 데이터 구조를 생성합니다. 이 메소드는 마지막에 호출해야 합니다.
- void SetPoster(Stream): 비디오의 포스터 즉, 플레이어가 활동하지 않을 때 보여지는 그림을 설정합니다.

[Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동하는 다음 코드 조각도 있습니다.

## 스크린 주석 추가하기

다음 코드 조각은 PDF 파일에 스크린 주석을 추가하는 방법을 보여줍니다:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // 문서 디렉토리로의 경로입니다.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // PDF 파일을 로드합니다
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // 스크린 주석 생성
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## 사운드 주석 추가

다음 코드 스니펫은 PDF 파일에 사운드 주석을 추가하는 방법을 보여줍니다:

```csharp
        public static void AddSoundAnnotation()
        {
            // PDF 파일을 불러옵니다
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // 사운드 주석 생성
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "사운드 주석 데모",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## 리치미디어주석 추가

다음 코드 스니펫은 PDF 파일에 리치미디어주석을 추가하는 방법을 보여줍니다:
다음 코드 조각은 PDF 파일에 RichMediaAnnotation을 추가하는 방법을 보여줍니다:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //동영상 데이터에 이름을 부여합니다. 이 데이터는 이 이름으로 문서에 포함되며 플래시 변수에서 이 이름으로 참조됩니다.
            //videoName은 파일 경로를 포함해서는 안 되며, PDF 문서 내의 데이터에 접근하기 위한 "키"입니다.
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //또한 비디오 플레이어용 스킨을 사용합니다.
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //비디오 플레이어의 코드가 포함된 스트림을 지정해야 합니다.
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //플레이어용 플래시 변수 라인을 구성합니다. 다른 플레이어는 플래시 변수 라인의 형식이 다를 수 있습니다. 사용하는 플레이어의 문서를 참조하세요.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //스킨 코드를 추가합니다.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //비디오에 포스터를 설정합니다.
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //비디오 콘텐츠를 설정합니다.
            rma.SetContent(videoName, fs);

            //콘텐츠의 유형을 설정합니다 (비디오).
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //클릭 시 플레이어 활성화
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //주석 데이터를 업데이트합니다. 모든 할당/설정 후에 이 메서드를 호출해야 합니다. 이 메서드는 주석의 데이터 구조를 초기화하고 필요한 데이터를 포함합니다.
            rma.Update();

            //페이지에 주석을 추가합니다.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### 멀티미디어 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 멀티미디어 주석을 가져오십시오.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // PDF 파일 로드
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### 멀티미디어 주석 삭제하기

PDF 파일에서 멀티미디어 주석을 삭제하는 방법을 보여주는 다음 코드 스니펫입니다.

```csharp
        public static void DeletePolyAnnotation()
        {
            // PDF 파일 로드
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## 위젯 주석 추가

대화형 양식은 [위젯 주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation)을 사용하여 필드의 모양을 나타내고 사용자 상호작용을 관리합니다.
PDF에 추가하여 정보 입력, 제출 또는 다른 사용자 상호작용을 쉽게 할 수 있도록 이러한 양식 요소를 사용합니다.

위젯 주석은 특정 페이지에서 양식 필드의 그래픽 표현이므로 주석으로 직접 생성할 수 없습니다.

각 위젯 주석은 그 유형에 따라 적절한 그래픽(모양)을 가지며 생성 후에는 테두리 스타일 및 배경색과 같은 특정 시각적 측면을 변경할 수 있습니다.
글꼴 및 글꼴 색상과 같은 다른 속성은 필드에 연결된 후에 변경할 수 있습니다.

어떤 경우에는 필드가 여러 페이지에 나타나게 하여 같은 값을 반복하고 싶을 수도 있습니다.
어떤 경우에는 하나의 필드가 여러 페이지에 나타나도록 하고 싶을 수 있으며, 같은 값을 반복합니다.
양식을 작성하는 사람은 이러한 위젯 중 하나를 사용하여 필드의 값을 업데이트할 수 있고, 이는 다른 모든 위젯에도 반영됩니다.

문서의 각 위치에 대한 각 양식 필드는 하나의 위젯 주석을 나타냅니다. 위젯 주석의 위치별 데이터는 특정 페이지에 추가됩니다. 각 양식 필드는 여러 변형을 가지고 있습니다. 버튼은 라디오 버튼, 체크박스 또는 푸시 버튼일 수 있습니다. 선택 위젯은 리스트 박스 또는 콤보 박스일 수 있습니다.

이 예제에서는 문서 내에서 네비게이션을 위한 푸시 버튼을 추가하는 방법을 배워봅시다.

### 문서에 버튼 추가

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "현재 문서 인쇄",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "문서 인쇄"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
이 버튼은 테두리가 있고 배경을 설정합니다. 또한 버튼 이름(Name), 툴팁(AlternateName), 레이블(NormalCaption), 레이블 텍스트의 색상(Color)을 설정합니다.

### 문서 탐색 작업 사용하기

PDF 문서에서 문서 탐색을 위해 위젯 주석 사용의 복잡한 예가 있습니다. 이는 PDF 문서 프레젠테이션을 준비하는 데 필요할 수 있습니다.

이 예제는 4개의 버튼을 생성하는 방법을 보여줍니다:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "첫 페이지로 이동", "이전 페이지로 이동", "다음 페이지로 이동", "마지막 페이지로 이동" };
var normalCaptions = new[] { "첫 번째", "이전", "다음", "마지막" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

페이지에 첨부하지 않고 버튼을 생성해야 합니다.
페이지에 부착하지 않고 버튼을 생성해야 합니다.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

문서의 각 페이지에 이 버튼 배열을 복제해야 합니다.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

이 필드가 추가될 페이지의 인덱스와 함께 다음 매개변수들을 사용하여 [Form.Add 메소드](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2)를 호출합니다: field, name.
[Form.Add 메소드](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2)를 다음 매개변수와 함께 호출합니다: field, name, 그리고 이 필드가 추가될 페이지의 인덱스.

전체 결과를 얻기 위해 첫 번째 페이지에서 "First" 및 "Prev" 버튼을 비활성화하고 마지막 페이지에서 "Next" 및 "Last" 버튼을 비활성화해야 합니다.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

이 기능의 자세한 정보와 가능성에 대해서는 [폼 작업하기](/pdf/net/acroforms/)도 참조하십시오.

PDF 문서에서는 3D CAD 또는 3D 모델링 소프트웨어로 생성된 고품질 3D 콘텐츠를 볼 수 있으며 PDF 문서에 포함됩니다. 마치 손으로 들고 있는 것처럼 모든 방향으로 3D 요소를 회전할 수 있습니다.

왜 이미지의 3D 디스플레이가 필요한가요?

지난 몇 년 동안 기술은 3D 프린팅 덕분에 모든 분야에서 엄청난 돌파구를 이루었습니다.
지난 몇 년 동안 기술은 3D 프린팅 덕분에 모든 분야에서 큰 돌파구를 이루었습니다.

3D 모델링의 주요 임무는 미래의 물체나 객체에 대한 아이디어입니다. 왜냐하면 객체를 출시하기 위해서는 산업 디자인이나 건축에서 연속적으로 재생성하기 위해 그 설계 특징을 모든 세부 사항에서 이해할 필요가 있기 때문입니다.

## 3D 주석 추가

3D 주석은 U3D 형식으로 생성된 모델을 사용하여 추가됩니다.

1. 새 [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 생성합니다.
1. 원하는 3D 모델의 데이터를 로드합니다(우리 경우 "Ring.u3d") [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)를 생성하기 위해
1. [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) 객체를 생성하고 문서 및 3DContent에 연결합니다.
1. pdf3dArtWork 객체 조정:

    - 3DLightingScheme - (예시에서 `CAD` 설정)
    - 3DRenderMode - (예시에서 `Solid` 설정)
    - `ViewArray`를 채우고, 최소한 하나의 [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)를 생성하여 배열에 추가합니다.

- `ViewArray`를 채우고, 하나 이상의 [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)를 생성하여 배열에 추가하세요.

1. 주석에 3가지 기본 매개변수 설정:
    - 주석이 배치될 `page`,
    - 주석이 들어갈 `rectangle`,
    - 그리고 `3dArtWork` 객체.
1. 3D 객체의 표현을 개선하기 위해 테두리 프레임 설정
1. 기본 뷰 설정 (예 - TOP)
1. 몇 가지 추가 매개변수 추가: 이름, 미리보기 포스터 등.
1. 주석을 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)에 추가
1. 결과 저장

### 예시

다음 코드 조각을 확인하여 3D 주석을 추가하세요.

```csharp
    public static void Add3dAnnotation()
    {
    // PDF 파일 로드
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    // 필요한 경우 미리보기 이미지 설정
    // pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
이 코드 예제는 다음과 같은 모델을 보여줍니다:

![3D Annotation demo](3d_demo.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

