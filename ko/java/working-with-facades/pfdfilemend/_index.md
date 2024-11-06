---
title: PdfFileMend Class
type: docs
weight: 20
url: ko/java/pdffilemend-class/
description: 이 섹션에서는 PdfFileMend 클래스를 사용하여 Aspose.PDF Facades를 사용하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText)를 PDF 문서에 삽입하는 것이 원본 편집 가능한 버전의 문서가 있는 경우 어려운 작업이 아닐 것 같습니다. 문서를 생성한 후 다른 줄을 추가해야 한다는 것을 기억하거나 더 많은 양의 문서에 대해 이야기하고 있다고 가정해 봅시다. 두 경우 모두 Aspose.PDF Facades가 도움이 될 것입니다. [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) 클래스를 사용하여 기존 PDF 파일에 텍스트를 추가할 가능성을 고려해 봅시다.

## 기존 PDF 파일에 텍스트 추가 (facades)

여러 가지 방법으로 텍스트를 추가할 수 있습니다.
 첫 번째를 고려하십시오. 우리는 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText)를 가져와서 페이지에 추가합니다. 그 후, 왼쪽 하단 모서리의 좌표를 지정한 다음, 페이지에 텍스트를 추가합니다.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Aspose에 오신 것을 환영합니다!");

        mender.AddText(message, 1, 10, 750);

        // 출력 파일 저장
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

어떻게 보이는지 확인하십시오:

![텍스트 추가](/pdf/net/images/add_text.png)

[FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext)를 추가하는 두 번째 방법입니다. 추가적으로, 텍스트가 맞아야 할 사각형을 지정합니다.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Aspose에 오신 것을 환영합니다! Aspose에 오신 것을 환영합니다!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // 출력 파일 저장
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

세 번째 예제는 지정된 페이지에 텍스트를 추가할 수 있는 기능을 제공합니다. 예를 들어, 문서의 1페이지와 3페이지에 캡션을 추가해 봅시다.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Aspose에 오신 것을 환영합니다!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // 출력 파일 저장
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## 기존 PDF 파일에 이미지 추가하기 (facades)

기존 PDF 파일에 이미지를 추가하려고 시도해 본 적이 있습니까?
 우리는 이것이 쉬운 일이 아니라는 것을 알고 있다고 확신합니다. 아마도 당신은 온라인 양식을 작성하고 있고 신원을 확인하기 위해 사진을 첨부하거나 기존 이력서에 사진을 첨부해야 할 것입니다. 이전에는 이러한 작업을 사진을 만들고, 문서에 첨부하고, 추가로 스캔하고 보내는 방식으로 해결했습니다. 이 과정은 번거롭고 시간이 많이 소요되었습니다.

기존 PDF 파일에 이미지와 텍스트를 추가하는 것은 일반적인 요구 사항이며, com.aspose.pdf.facades 네임스페이스는 이 요구 사항을 매우 잘 충족합니다. 이 네임스페이스는 PDF 파일에 이미지를 추가할 수 있는 클래스 [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend)를 제공합니다.

이 글에서는 com.aspose.pdf.facades를 사용하여 PDF에 이미지를 삽입하는 방법을 보여줍니다. PDF에 이미지를 추가하는 여러 옵션도 있습니다.

사각형의 매개변수를 설정하여 PDF 문서에 이미지를 삽입합니다.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // 이미지를 스트림에 로드합니다.
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // 출력 파일을 저장합니다.
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![이미지 추가](/pdf/net/images/add_image1.png)

두 번째 코드 스니펫을 고려해봅시다. [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters) 클래스 매개변수의 변형을 사용하여 다양한 디자인 효과를 얻을 수 있습니다. 우리는 그 중 하나를 시도했습니다.

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // 이미지를 스트림에 로드
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // 출력 파일 저장
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![이미지 추가](/pdf/net/images/add_image2.png)

다음 코드 스니펫에서는 [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType)을 사용합니다. ImageFilterType은 인코딩에 사용될 스트림 코덱의 유형을 나타내며, 기본적으로 Jpeg입니다. PNG 형식에서 이미지를 로드하면 문서에 JPEG(또는 내가 지정한 다른 형식)으로 저장됩니다.

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // 이미지를 스트림으로 로드
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // 출력 파일 저장
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


다음 코드 스니펫에서 [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) 메서드의 사용을 주목할 수 있습니다.

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--)는 플래그로, 원본 이미지의 투명성을 달성하기 위해 이미지에 마스크를 적용할지를 나타냅니다.

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // 스트림에 이미지를 로드합니다
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // 출력 파일을 저장합니다
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```