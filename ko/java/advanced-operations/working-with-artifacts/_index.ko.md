---
title: 아티팩트 작업하기
linktitle: 아티팩트 작업하기
type: docs
weight: 110
url: /java/artifacts/
description: 이 페이지는 Aspose.PDF for Java를 사용하여 아티팩트 클래스를 다루는 방법을 설명합니다. 코드 스니펫은 PDF 페이지에 배경 이미지를 추가하는 방법과 PDF 파일의 첫 페이지에 있는 각 워터마크를 가져오는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

아티팩트는 일반적으로 작성된 콘텐츠의 일부가 아닌 그래픽 객체 또는 기타 표시입니다. PDF에서 아티팩트의 예로는 페이지 머리글 또는 바닥글, 페이지의 섹션을 구분하는 선 또는 기타 그래픽, 장식 이미지 등이 포함됩니다.

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 클래스는 다음을 포함합니다:

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값들을 지원하며, 여기에는 Background, Layout, Page, Pagination 및 Undefined 값이 포함됩니다).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – 아티팩트 하위 유형을 가져옵니다 (여기서 값은 Background, Footer, Header, Undefined, Watermark를 포함하는 Artifact.ArtifactSubtype 열거형의 값을 지원합니다).

Adobe Acrobat으로 생성된 워터마크는 아티팩트라고 불립니다 (PDF 사양의 14.8.2.2 실질 콘텐츠와 아티팩트에 설명된 것처럼). 아티팩트와 작업하기 위해, Aspose.PDF는 두 개의 클래스, [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact)와 [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection)를 제공합니다.

특정 페이지의 모든 아티팩트를 가져오기 위해, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스에는 Artifacts 속성이 있습니다. 이 주제는 PDF 파일에서 아티팩트와 작업하는 방법을 설명합니다.

다음 코드 스니펫은 PDF 파일의 첫 번째 페이지에 워터마크를 설정하는 방법을 보여줍니다.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


배경 이미지는 문서에 워터마크 또는 다른 은은한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for Java에서 각 PDF 문서는 페이지의 모음이며 각 페이지는 아티팩트의 모음입니다. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) 클래스는 페이지 객체에 배경 이미지를 추가하는 데 사용할 수 있습니다.

다음 코드 스니펫은 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```java

    public static void SetBackground() throws FileNotFoundException {

        // 문서 열기
        Document pdfDocument = new Document();
                
        // 문서 객체에 새 페이지 추가
        Page page = pdfDocument.getPages().add();

        // Background Artifact 객체 생성
        BackgroundArtifact background = new BackgroundArtifact();

        // 배경 아티팩트 객체에 대한 이미지 지정
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // 페이지의 아티팩트 컬렉션에 BackgroundArtifact 추가
        page.getArtifacts().add(background);

        // 수정된 PDF 저장
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## 프로그래밍 샘플: 워터마크 얻기

다음 코드 스니펫은 PDF 파일의 첫 번째 페이지에서 각 워터마크를 얻는 방법을 보여줍니다.

```java
    public static void GettingWatermarks() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // 아티팩트의 하위 유형, 텍스트 및 위치를 반복하여 얻기
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## 프로그래밍 샘플: 특정 유형의 아티팩트 수 계산

특정 유형의 아티팩트 총 수를 계산하려면 (예: 워터마크의 총 개수) 다음 코드를 사용하세요:

```java
    public static void CountingArtifacts() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // 아티팩트 유형이 워터마크인 경우 카운터 증가
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("페이지에는 " + count + "개의 워터마크가 포함되어 있습니다");
    }
```