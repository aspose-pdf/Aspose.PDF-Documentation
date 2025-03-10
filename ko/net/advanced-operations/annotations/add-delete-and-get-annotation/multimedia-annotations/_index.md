---
title: PDF 멀티미디어 주석 사용하기 C#
linktitle: 멀티미디어 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/multimedia-annotation/
description: Aspose.PDF for .NET은 PDF 문서에서 멀티미디어 주석을 추가, 가져오기 및 삭제할 수 있게 해줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET은 고급 멀티미디어 주석 기능을 소개하여 사용자가 PDF 문서에 다양한 멀티미디어 유형을 원활하게 추가, 검색 및 삭제할 수 있도록 합니다. 이 기능은 화면, 소리 및 리치 미디어 주석을 지원하여 문서의 상호작용을 향상시키고 외부 비디오 콘텐츠, 오디오 노트 및 임베디드 미디어의 통합을 가능하게 하여 PDF 문서를 더욱 역동적이고 매력적으로 만듭니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

PDF 문서의 주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 Annotations 컬렉션에 포함되어 있습니다. 이 컬렉션은 해당 개별 페이지의 모든 주석을 포함합니다: 각 페이지는 고유한 Annotations 컬렉션을 가지고 있습니다. 특정 페이지에 주석을 추가하려면 Add 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가하십시오.

Aspose.PDF.InteractiveFeatures.Annotations 네임스페이스의 [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) 클래스를 사용하여 PDF 문서에 주석으로 SWF 파일을 포함할 수 있습니다. 화면 주석은 미디어 클립이 재생될 수 있는 페이지의 영역을 지정합니다.

PDF 문서에 외부 비디오 링크를 추가해야 할 때는 [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation)을 사용할 수 있습니다.
Movie Annotation은 컴퓨터 화면과 스피커에서 표시될 애니메이션 그래픽과 소리를 포함합니다.

[Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)은 텍스트 주석과 유사하지만 텍스트 노트 대신 컴퓨터의 마이크로폰에서 녹음된 소리 또는 파일에서 가져온 소리를 포함합니다. 주석이 활성화되면 소리가 재생됩니다. 주석은 대부분의 방식에서 텍스트 주석처럼 동작하며, 소리를 나타내는 다른 아이콘(기본적으로 스피커)을 사용합니다.

그러나 PDF 문서에 미디어를 임베드해야 할 경우 [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation)을 사용해야 합니다.

RichMediaAnnotation 클래스의 다음 메서드/속성을 사용할 수 있습니다.

- Stream CustomPlayer { set; }: 비디오를 재생하는 데 사용되는 플레이어를 설정할 수 있습니다.
- string CustomFlashVariables { set; }: 플래시 애플리케이션에 전달되는 변수를 설정할 수 있습니다. 이 줄은 '&'로 구분된 "key=value" 쌍의 집합입니다.
- void AddCustomData(strig name, Stream data): 플레이어에 추가 데이터를 추가합니다. 예: source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}: 플레이어를 활성화하는 이벤트; 가능한 값은 Click, PageOpen, PageVisible입니다.
- void SetContent(Stream stream, string name): 재생할 비디오/오디오 데이터를 설정합니다.
- void Update(): 주석의 데이터 구조를 생성합니다. 이 메서드는 마지막에 호출해야 합니다.
- void SetPoster(Stream): 플레이어가 활성화되지 않았을 때 표시되는 비디오의 포스터(즉, 그림)를 설정합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 화면 주석 추가

다음 코드 스니펫은 PDF 파일에 화면 주석을 추가하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## 소리 주석 추가

다음 코드 스니펫은 PDF 파일에 소리 주석을 추가하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## RichMediaAnnotation 추가

다음 코드 스니펫은 PDF 파일에 RichMediaAnnotation을 추가하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### 멀티미디어 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 멀티미디어 주석을 가져와 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### 멀티미디어 주석 삭제

다음 코드 스니펫은 PDF 파일에서 멀티미디어 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## 위젯 주석 추가

인터랙티브 양식은 [Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation)를 사용하여 필드의 모양을 나타내고 사용자 상호작용을 관리합니다.
우리는 PDF에 추가되는 이러한 양식 요소를 사용하여 정보를 입력하고 제출하거나 다른 사용자 상호작용을 수행하기 쉽게 만듭니다.

위젯 주석은 특정 페이지의 양식 필드를 그래픽적으로 나타내므로 주석으로 직접 생성할 수 없습니다.

각 위젯 주석은 유형에 따라 적절한 그래픽(모양)을 가집니다. 생성 후에는 테두리 스타일 및 배경색과 같은 특정 시각적 측면을 변경할 수 있습니다.
텍스트 색상 및 글꼴과 같은 다른 속성은 필드에 첨부된 후 변경할 수 있습니다.

경우에 따라 필드가 여러 페이지에 나타나고 동일한 값을 반복하도록 하려는 경우가 있습니다. 이 경우 일반적으로 하나의 위젯만 있는 필드는 여러 위젯이 첨부될 수 있습니다: TextField, ListBox, ComboBox 및 CheckBox는 일반적으로 정확히 하나를 가지며, RadioGroup은 각 라디오 버튼에 대해 여러 위젯을 가집니다.
양식을 작성하는 사람은 이러한 위젯 중 하나를 사용하여 필드의 값을 업데이트할 수 있으며, 이는 다른 모든 위젯에도 반영됩니다.

문서의 각 위치에 대한 각 양식 필드는 하나의 위젯 주석을 나타냅니다. 위젯 주석의 위치별 데이터는 특정 페이지에 추가됩니다. 각 양식 필드는 여러 변형을 가집니다. 버튼은 라디오 버튼, 체크박스 또는 푸시 버튼이 될 수 있습니다. 선택 위젯은 목록 상자 또는 콤보 상자가 될 수 있습니다.

이 샘플에서는 문서 내 탐색을 위한 푸시 버튼을 추가하는 방법을 배웁니다.

### 문서에 버튼 추가

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

이 버튼은 테두리가 있으며 배경이 설정되어 있습니다. 또한 버튼 이름(Name), 툴팁(AlternateName), 레이블(NormalCaption) 및 레이블 텍스트의 색상(Color)을 설정합니다.

### 문서 탐색 작업 사용

위젯 주석 사용의 더 복잡한 예가 존재합니다 - PDF 문서에서의 문서 탐색. 이는 PDF 문서 프레젠테이션을 준비하는 데 필요할 수 있습니다.

이 예제는 4개의 버튼을 만드는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

이 기능에 대한 더 자세한 정보와 가능성은 [양식 작업하기](/pdf/net/acroforms/)를 참조하십시오.

PDF 문서에서는 3D CAD 또는 3D 모델링 소프트웨어로 생성된 고품질 3D 콘텐츠를 보고 관리할 수 있으며, PDF 문서에 임베드되어 있습니다. 3D 요소를 손에 쥐고 있는 것처럼 모든 방향으로 회전할 수 있습니다.

왜 3D 이미지의 디스플레이가 필요할까요?

지난 몇 년 동안 기술은 3D 프린팅 덕분에 모든 분야에서 큰 발전을 이루었습니다. 3D 프린팅 기술은 건설, 기계 공학, 디자인에서 기술적 기술을 가르치는 주요 도구로 적용될 수 있습니다. 이러한 기술은 개인 인쇄 장치의 출현 덕분에 교육 과정의 새로운 형태를 도입하고 동기를 높이며 졸업생과 교사의 필수 역량을 형성하는 데 기여할 수 있습니다.

3D 모델링의 주요 작업은 미래의 객체나 물체에 대한 아이디어입니다. 왜냐하면 객체를 출시하기 위해서는 산업 디자인이나 건축에서의 연속적인 재생을 위해 그 설계 특징을 모두 이해해야 하기 때문입니다.

## 3D 주석 추가

3D 주석은 U3D 형식으로 생성된 모델을 사용하여 추가됩니다.

1. 새로운 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 생성합니다.
1. 원하는 3D 모델의 데이터를 로드합니다(우리의 경우 "Ring.u3d")하여 [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)를 생성합니다.
1. [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) 객체를 생성하고 문서 및 3DContent에 연결합니다.
1. pdf3dArtWork 객체를 조정합니다:

    - 3DLightingScheme - (예제에서는 `CAD`로 설정합니다)
    - 3DRenderMode - (예제에서는 `Solid`로 설정합니다)
    - Fill `ViewArray`, 최소한 하나의 [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)를 생성하고 배열에 추가합니다.

1. 주석의 3가지 기본 매개변수를 설정합니다:
    - 주석이 배치될 `page`.
    - 주석이 들어갈 `rectangle`.
    - 그리고 `3dArtWork` 객체.
1. 3D 객체의 더 나은 프레젠테이션을 위해 테두리 프레임을 설정합니다.
1. 기본 보기를 설정합니다(예: - TOP).
1. 추가 매개변수: 이름, 미리보기 포스터 등을 추가합니다.
1. [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)에 주석을 추가합니다.
1. 결과를 저장합니다.

### 예제

다음 코드 스니펫을 확인하여 3D 주석을 추가하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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