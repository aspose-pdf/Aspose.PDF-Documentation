---
title: PDF를 Microsoft PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF를 사용하여 Java로 PDF를 PowerPoint 형식으로 변환할 수 있습니다. 한 가지 방법으로는 슬라이드를 이미지로 하여 PDF를 PPTX로 변환할 수 있는 가능성이 있습니다.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Java**는 PDF를 PPTX로 변환하는 과정을 추적할 수 있게 해줍니다. 우리는 Aspose.Slides라는 API를 가지고 있으며, 이를 통해 PPT/PPTX 프레젠테이션을 생성하고 조작할 수 있는 기능을 제공합니다. 이 API는 또한 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능도 제공합니다. Aspose.PDF for Java에서는 PDF 문서를 PPTX 형식으로 변환하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 PPTX 파일의 개별 슬라이드로 변환됩니다.

PDF를 PPTX로 변환하는 동안, 텍스트는 이미지로 렌더링되는 대신, 선택/업데이트할 수 있는 텍스트로 렌더링됩니다.
 문서 파일을 PPTX 형식으로 변환하려면 Aspose.PDF는 PptxSaveOptions라는 클래스를 제공합니다. [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스의 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) 메서드에 두 번째 인수로 전달됩니다.

PDF를 PowerPoint 형식으로 변환하는 작업을 해결하려면 다음 코드 스니펫을 확인하세요:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // PDF 문서 불러오기
        Document document = new Document(documentFileName);

        // PptxSaveOptions 인스턴스 생성
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // 출력물을 PPTX 형식으로 저장
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## PDF를 슬라이드 이미지로 PPTX로 변환하기

검색 가능한 PDF를 선택 가능한 텍스트 대신 이미지로 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스를 통해 이러한 기능을 제공합니다. 이를 달성하기 위해, [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스의 속성 SlidesAsImages를 'true'로 설정하십시오. 다음 코드 샘플에 표시된 대로입니다.

다음 코드 스니펫은 PDF 파일을 PPTX 형식의 슬라이드 이미지로 변환하는 과정을 보여줍니다.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // PDF 문서 로드
    Document document = new Document(documentFileName);
    // PptxSaveOptions 인스턴스 생성
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // 출력물을 PPTX 형식으로 저장
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Aspose.PDF for Java로 콘솔에 진행 상황 표시하기는 다음과 같습니다:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDF를 PPTX로 변환합니다.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // PDF 문서를 로드합니다
        Document document = new Document(documentFileName);

        // PptxSaveOptions 인스턴스를 생성합니다
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // 사용자 지정 진행 상황 처리기 지정
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // 출력물을 PPTX 형식으로 저장합니다
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## PPTX 변환의 진행 상황 세부 정보

Aspose.PDF for Java는 PDF를 PPTX로 변환하는 과정을 추적할 수 있도록 합니다. [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스는 변환 진행 상황을 추적하기 위한 사용자 지정 메서드에 지정할 수 있는 [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) 속성을 제공합니다. 다음 코드 샘플에 설명된 대로 사용할 수 있습니다.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - 변환 진행 상황 : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - 결과 페이지의 %s가 %d 레이아웃에서 생성되었습니다.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - 결과 페이지 %d가 %d에서 내보내졌습니다.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - 원본 페이지 %d가 %d에서 분석되었습니다.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인에서 변환해보세요**

Aspose.PDF for Java는 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 작동 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to PPTX 무료 앱](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}