---
title: PDF 멀티미디어 주석 
linktitle: 멀티미디어 주석
type: docs
weight: 40
url: /java/multimedia-annotation/
description: Aspose.PDF for Java를 사용하여 PDF 문서에서 멀티미디어 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서의 주석은 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 Annotations 컬렉션에 포함됩니다. 이 컬렉션은 해당 개별 페이지에 대한 모든 주석을 포함합니다: 각 페이지는 자체 Annotations 컬렉션을 가지고 있습니다. 특정 페이지에 주석을 추가하려면, Add 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가하십시오.

Aspose.PDF.InteractiveFeatures.Annotations 네임스페이스의 [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) 클래스를 사용하여 PDF 문서에 주석으로 SWF 파일을 포함시키십시오.
 페이지의 특정 영역에 미디어 클립을 재생할 수 있도록 하는 화면 주석을 지정합니다.

PDF 문서에 외부 비디오 링크를 추가해야 할 때는 [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation)을 사용할 수 있습니다. 영화 주석은 컴퓨터 화면과 스피커를 통해 보여질 애니메이션 그래픽과 사운드를 포함합니다.

[Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation)은 텍스트 주석과 유사하지만, 텍스트 노트 대신 컴퓨터의 마이크에서 녹음되거나 파일에서 가져온 사운드를 포함합니다. 주석이 활성화되면 사운드가 재생됩니다. 주석은 대부분의 면에서 텍스트 주석과 유사하게 작동하며, 소리를 나타내기 위해 다른 아이콘(기본적으로 스피커)을 사용합니다.

그러나 PDF 문서 내에 미디어를 임베드해야 할 때는 [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation)을 사용해야 합니다.
RichMediaAnnotation 클래스의 다음 메서드/속성을 사용할 수 있습니다.

- Stream CustomPlayer { set; }: 비디오를 재생하는 데 사용되는 플레이어를 설정할 수 있습니다.
- string CustomFlashVariables { set; }: 플래시 애플리케이션에 전달되는 변수를 설정할 수 있습니다. 이 줄은 '&'로 구분된 "key=value" 쌍의 집합입니다.
- void AddCustomData(strig name, Stream data): 플레이어에 추가 데이터를 추가합니다. 예를 들어 source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: 플레이어를 활성화하는 이벤트; 가능한 값은 Click, PageOpen, PageVisible입니다.
- void SetContent(Stream stream, string name): 재생할 비디오/오디오 데이터를 설정합니다.
- void Update(): 주석의 데이터 구조를 생성합니다. 이 메서드는 마지막에 호출되어야 합니다.
- void SetPoster(Stream): 플레이어가 활성화되지 않았을 때 표시되는 비디오의 포스터, 즉, 그림을 설정합니다.

## 화면 주석 추가

다음 코드 스니펫은 PDF 파일에 화면 주석을 추가하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // 문서 디렉터리의 경로입니다.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // 화면 주석 생성
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## 사운드 주석 추가

다음 코드 스니펫은 PDF 파일에 사운드 주석을 추가하는 방법을 보여줍니다:

```java
          public static void AddSoundAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // 사운드 주석 생성
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("사운드 주석 데모");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## 리치 미디어 주석 추가

다음 코드 스니펫은 PDF 파일에 리치 미디어 주석을 추가하는 방법을 보여줍니다:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // 비디오 데이터에 이름을 지정합니다. 이 데이터는 이 이름으로 문서에 포함되고 이 이름으로 플래시 변수에서 참조됩니다.
        // videoName에는 파일 경로가 포함되지 않아야 합니다. 이는 PDF 문서 내부의 데이터에 액세스하는 "키"입니다.

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // 또한 비디오 플레이어에 스킨을 사용합니다.
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // 여기서 비디오 플레이어의 코드를 포함하는 스트림을 지정해야 합니다.
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // 플레이어를 위한 플래시 변수 라인을 구성합니다. 다른 플레이어는 플래시 변수 라인의 다른 형식을 가질 수 있습니다.
        // 플레이어에 대한 문서를 참조하세요.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // 스킨 코드를 추가합니다.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // 비디오 포스터 설정
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // 비디오 콘텐츠 설정
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // 콘텐츠 유형 설정 (비디오)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // 클릭 시 플레이어 활성화
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // 주석 데이터를 업데이트합니다. 이 메서드는 모든 할당/설정 후에 호출되어야 합니다.
        // 이 메서드는 주석의 데이터 구조를 초기화하고 필요한 데이터를 포함합니다.
        rma.update();

        // 페이지에 주석을 추가합니다.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## 멀티미디어 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 멀티미디어 주석을 가져와 보세요.

```java
public static void GetMultimediaAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## 멀티미디어 주석 삭제

다음 코드 스니펫은 PDF 파일에서 멀티미디어 주석을 삭제하는 방법을 보여줍니다.

```java
    public static void DeletePolyAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## 위젯 주석 추가

인터랙티브 양식은 필드의 모양을 나타내고 사용자 상호작용을 관리하기 위해 [위젯 주석](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation)을 사용합니다. 우리는 PDF에 추가되는 이러한 양식 요소를 사용하여 정보를 입력하거나 제출하거나 기타 사용자 상호작용을 수행하는 것을 더 쉽게 만듭니다.

위젯 주석은 특정 페이지에 있는 양식 필드의 그래픽 표현이므로 주석으로 직접 생성할 수 없습니다.

각 위젯 주석은 그 유형에 따라 적절한 그래픽(모양)을 가집니다. 생성 후에는 테두리 스타일과 배경색과 같은 특정 시각적 측면을 변경할 수 있습니다. 텍스트 색상과 글꼴과 같은 다른 속성은 필드에 연결되면 변경할 수 있습니다.

일부 경우에는 동일한 값이 반복되도록 필드가 여러 페이지에 나타나기를 원할 수 있습니다.
 그 경우, 일반적으로 하나의 위젯만 있는 필드는 여러 위젯이 첨부될 수 있습니다: TextField, ListBox, ComboBox, 및 CheckBox는 보통 하나씩만 가지고 있지만, RadioGroup은 각 라디오 버튼마다 여러 위젯을 가지고 있습니다. 양식을 작성하는 사람은 이러한 위젯 중 어느 것이든 사용하여 필드의 값을 업데이트할 수 있으며, 이는 다른 모든 위젯에도 반영됩니다.

문서의 각 위치에 대한 각 양식 필드는 하나의 위젯 주석을 나타냅니다. 위젯 주석의 위치별 데이터는 특정 페이지에 추가됩니다. 각 양식 필드는 여러 가지 변형이 있습니다. 버튼은 라디오 버튼, 체크박스, 또는 푸시 버튼이 될 수 있습니다. 선택 위젯은 리스트 박스나 콤보 박스가 될 수 있습니다.

이 예제에서는 문서 내비게이션을 위한 푸시 버튼을 추가하는 방법을 배웁니다.

## 문서에 버튼 추가

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("현재 문서 인쇄");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("문서 인쇄");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

이 버튼은 테두리가 있으며 배경이 설정되어 있습니다. 또한 버튼 이름 (Name), 도구 설명 (AlternateName), 라벨 (NormalCaption), 라벨 텍스트의 색상 (Color)도 설정합니다.

## 문서 탐색 작업 사용하기

PDF 문서에서 위젯 주석 사용의 더 복잡한 예로 문서 탐색이 있습니다. 이는 PDF 문서 프레젠테이션을 준비할 때 필요할 수 있습니다.

이 예제는 4개의 버튼을 만드는 방법을 보여줍니다:

```java
public static void AddDocumentNavigationActions() {
// PDF 파일 로드
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "첫 페이지로 이동", "이전 페이지로 이동", "다음 페이지로 이동", "마지막 페이지로 이동" };
String[] normalCaptions = { "첫", "이전", "다음", "마지막" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## 위젯 주석 삭제 방법

Aspose.PDF for Java에는 파일에서 주석을 제거하기 위한 규칙이 있습니다:

```java
public static void DeleteWidgetAnnotation() {
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // 주석 삭제
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

PDF 문서에서는 3D CAD 또는 3D 모델링 소프트웨어로 생성되고 PDF 문서에 포함된 고품질 3D 콘텐츠를 보고 관리할 수 있습니다.
 3D 요소를 손에 쥐고 있는 것처럼 모든 방향으로 회전할 수 있습니다.

왜 이미지의 3D 디스플레이가 필요한가요?

지난 몇 년 동안, 기술은 3D 프린팅 덕분에 모든 분야에서 큰 발전을 이루었습니다. 3D 프린팅 기술은 건설, 기계 공학, 디자인에서 주요 도구로서 기술적 기술을 가르치는 데 적용될 수 있습니다. 개인 프린팅 장치의 출현 덕분에 이러한 기술은 교육 과정의 새로운 형태의 조직 도입, 동기 부여의 증가, 졸업생과 교사의 필수 역량 형성에 기여할 수 있습니다.

3D 모델링의 주요 과제는 미래의 객체에 대한 아이디어입니다. 객체를 출시하기 위해서는 산업 디자인이나 건축에서 연속적인 재생을 위한 디자인 특징을 모든 세부 사항에서 이해해야 하기 때문입니다.

## 3D 주석 추가

3D 주석은 Aspose.PDF for Java로 U3D 형식으로 생성된 모델을 사용하여 추가됩니다.
1. 새 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)를 생성합니다.
1. 원하는 3D 모델(우리의 경우 "Ring.u3d")의 데이터를 불러와 [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)를 생성합니다.
1. [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) 객체를 생성하고 이를 문서와 3DContent에 연결합니다.
1. pdf3dArtWork 객체를 조정합니다:

    - 3DLightingScheme - (예제에서 `CAD`로 설정합니다)
    - 3DRenderMode - (예제에서 `Solid`로 설정합니다)
    - `ViewArray`를 채우고, 최소 하나의 [3D 뷰](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView)를 생성하여 배열에 추가합니다.

1. 주석에 3가지 기본 매개변수를 설정합니다:
    - 주석이 위치할 `페이지`,
    - 주석이 포함될 `사각형`,
    - 그리고 `3dArtWork` 객체.
1. 3D 객체의 더 나은 표현을 위해 테두리 프레임을 설정합니다.
1. 기본 뷰를 설정합니다 (예: TOP).

1. 추가 매개변수 추가: 이름, 미리보기 포스터 등
1. [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)에 주석 추가
1. 결과 저장

## 예시

다음 코드 스니펫을 확인하여 3D 주석을 추가하십시오.

```java
public class Example3DAnnotation
{
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
        // PDF 파일 로드
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        // 필요시 미리보기 이미지 설정
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example showed us such a model:

![3D Annotation demo](3d_demo.png)

이 코드 예제는 우리에게 이러한 모델을 보여주었습니다: