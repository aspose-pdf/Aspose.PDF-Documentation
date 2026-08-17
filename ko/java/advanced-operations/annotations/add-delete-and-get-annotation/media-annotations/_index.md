---
title: PDF의 미디어 주석
linktitle: 미디어 주석
type: docs
weight: 40
url: /java/media-annotations/
description: 일반적인 멀티미디어 워크플로우에 대한 단계별 지침을 통해 Java에서 사운드, 화면, 리치 미디어 및 3D PDF 주석 API를 사용하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java의 미디어 관련 PDF 주석 작업 흐름.
Abstract: 이 페이지에서는 사운드, 화면, 리치 미디어, 3D, 삭제 및 검사 시나리오를 포함하여 Aspose.PDF for Java의 일반적인 미디어 주석 작업 흐름을 설명합니다. 현재 저장소에는 전용 `workingwithannotations` 미디어 예제 클래스가 포함되어 있지 않으므로 이 문서에서는 단계별 지침을 통해 Java API 패턴을 직접 문서화합니다.
---

PDF의 미디어 주석은 일반적으로 사운드 클립, 화면 재생 영역, 리치 미디어 컨테이너 및 3D 모델과 같은 포함되거나 연결된 멀티미디어 콘텐츠를 다룹니다.


## 
리치 미디어 주석 추가



PDF 페이지에 사용자 정의 플레이어, 포스터 이미지 및 스킨이 포함된 비디오 컨텐츠를 호스팅해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/)을 만들고 플레이어 자산, 포스터 및 콘텐츠 스트림을 구성합니다.

1. 
페이지에 주석을 추가하고 출력 문서를 저장합니다.


```java
public static void richMediaAnnotationsAdd(Path mediaDir, Path outputFile) throws Exception {
    String pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";

    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation richMediaAnnotation = new RichMediaAnnotation(
                page,
                new Rectangle(100, 500, 300, 600, true));

        String playerPath = pathToAdobeApp + "\\Players\\Videoplayer.swf";
        richMediaAnnotation.setCustomPlayer(new FileInputStream(playerPath));
        richMediaAnnotation.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        String skinPath = pathToAdobeApp + "\\" + skinName;
        richMediaAnnotation.addCustomData(skinName, new FileInputStream(skinPath));

        Path posterPath = mediaDir.resolve(posterName);
        richMediaAnnotation.setPoster(new FileInputStream(posterPath.toString()));

        Path videoPath = mediaDir.resolve(videoName);
        try (FileInputStream videoStream = new FileInputStream(videoPath.toString())) {
            richMediaAnnotation.setContent(videoName, videoStream);
        }

        richMediaAnnotation.setType(RichMediaAnnotation.ContentType.Video);
        richMediaAnnotation.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);
        richMediaAnnotation.update();

        page.getAnnotations().add(richMediaAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
리치 미디어 주석 삭제



이 예에서는 페이지에서 기존 리치 미디어 주석을 제거합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia` 유형의 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 업데이트된 문서를 저장합니다.


```java
public static void richMediaAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.RichMedia) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
멀티미디어 주석 받기



이 예를 사용하여 페이지에 이미 존재하는 화면, 사운드 및 리치 미디어 주석을 검사합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
감지하려는 멀티미디어 주석 유형 세트를 정의하십시오.

1. 
페이지 주석을 반복하고 일치하는 각 항목의 유형과 직사각형을 인쇄합니다.


```java
public static void multimediaAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Set<AnnotationType> targetTypes = Set.of(
                AnnotationType.Screen,
                AnnotationType.Sound,
                AnnotationType.RichMedia);

        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (targetTypes.contains(annotation.getAnnotationType())) {
                System.out.println(annotation.getAnnotationType() + " [" + annotation.getRect() + "]");
            }
        }
    }
}
```

## 
3D 주석 추가



이 예에서는 사전 정의된 관점과 렌더링 옵션이 포함된 대화형 3D 모델 보기를 추가합니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
모델을 [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/)에 로드하고 [PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/)를 구성합니다.

1. 
[PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/)을 작성하고 페이지에 추가한 후 문서를 저장하세요.


```java
public static void annotation3dAdd(Path modelFile, Path outputFile) {
    try (Document document = new Document()) {
        PDF3DContent pdf3dContent = new PDF3DContent(modelFile.toString());
        PDF3DArtwork pdf3dArtwork = new PDF3DArtwork(document, pdf3dContent);
        pdf3dArtwork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtwork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        Matrix3D topMatrix = new Matrix3D(
                1, 0, 0,
                0, -1, 0,
                0, 0, -1,
                0.10271, 0.08184, 0.273836);

        Matrix3D frontMatrix = new Matrix3D(
                0, -1, 0,
                0, 0, 1,
                -1, 0, 0,
                0.332652, 0.08184, 0.085273);

        pdf3dArtwork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top"));
        pdf3dArtwork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left"));

        Page page = document.getPages().add();

        PDF3DAnnotation pdf3dAnnotation = new PDF3DAnnotation(
                page,
                new Rectangle(100, 500, 300, 700, true),
                pdf3dArtwork);

        pdf3dAnnotation.setBorder(new com.aspose.pdf.Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName(modelFile.getFileName().toString());

        page.getAnnotations().add(pdf3dAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
화면 주석 추가



페이지가 화면 재생 영역을 통해 미디어 파일을 참조해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
미디어 파일 및 대상 사각형에 대한 [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


```java
public static void screenAnnotationWithMediaAdd(Path mediaFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ScreenAnnotation screenAnnotation = new ScreenAnnotation(
                page,
                new Rectangle(170, 190, 470, 380, true),
                mediaFile.toString());

        page.getAnnotations().add(screenAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
사운드 주석 추가



이 예에서는 페이지에 사운드 주석을 배치하고 이를 WAV 파일과 연결합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 오디오 파일에 대한 [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/)을 생성하고 해당 메타데이터를 구성합니다.

1. 
페이지에 주석을 추가하고 출력 문서를 저장합니다.


```java
public static void soundAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Path mediaFile = inputFile.getParent().resolve("file_example_WAV_1MG.wav");

        SoundAnnotation soundAnnotation = new SoundAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true),
                mediaFile.toString());

        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Sound Annotation demo");

        soundAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true)));

        page.getAnnotations().add(soundAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
관련 주석 주제


- 
[대화형 주석](/pdf/java/interactive-annotations/)

- 
[마크업 주석](/pdf/java/markup-annotations/)

- 
[보안 주석](/pdf/java/security-annotations/)

- 
[도형 주석](/pdf/java/shape-annotations/)

- 
[텍스트 주석](/pdf/java/text-based-annotations/)

- 
[워터마크 주석](/pdf/java/watermark-annotations/)

- 
[주석 가져오기 및 내보내기](/pdf/java/import-export-annotations/)
