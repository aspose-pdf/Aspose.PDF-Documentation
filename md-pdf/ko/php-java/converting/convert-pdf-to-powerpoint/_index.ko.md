---
title: PDF를 Microsoft PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF를 사용하여 PHP로 PDF를 PowerPoint 형식으로 변환할 수 있습니다. PDF를 이미지 슬라이드로 PPTX로 변환할 수 있는 방법이 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**PHP용 Aspose.PDF**는 PDF를 PPTX로 변환하는 진행 상황을 추적할 수 있게 해줍니다. 우리는 Aspose.Slides라는 API를 가지고 있으며, 이는 PPT/PPTX 프레젠테이션을 생성하고 조작할 수 있는 기능을 제공합니다. 이 API는 또한 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능을 제공합니다. PHP용 Aspose.PDF에서는 PDF 문서를 PPTX 형식으로 변환하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 PPTX 파일의 개별 슬라이드로 변환됩니다.

PDF를 PPTX로 변환하는 동안, 텍스트는 선택/업데이트할 수 있는 텍스트로 렌더링되며, 이미지로 렌더링되지 않습니다.
 PDF 파일을 PPTX 형식으로 변환하기 위해 Aspose.PDF는 PptxSaveOptions라는 클래스를 제공합니다. [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스의 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) 메서드의 두 번째 인자로 전달됩니다.

PDF를 PowerPoint 형식으로 변환하는 작업을 해결하기 위한 다음 코드 스니펫을 확인하세요:

```php
// 입력 PDF 문서를 로드합니다.
$document = new Document($inputFile);

// PptxSaveOptions의 인스턴스를 생성합니다.
$saveOption = new PptxSaveOptions();

// PDF 문서를 PPTX 파일로 저장합니다.
$document->save($outputFile, $saveOption);
```

## 슬라이드를 이미지로 변환하여 PDF를 PPTX로 변환

선택 가능한 텍스트 대신 이미지로 검색 가능한 PDF를 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스를 통해 이러한 기능을 제공합니다. 다음 코드 샘플에서 보여주듯이, [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스의 SlidesAsImages 속성을 'true'로 설정하여 이를 달성하십시오.

다음 코드 스니펫은 PDF 파일을 PPTX 형식 슬라이드로 이미지로 변환하는 과정을 보여줍니다.

```php
// 입력 PDF 문서 로드
$document = new Document($inputFile);

// PptxSaveOptions 인스턴스 생성
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// PDF 문서를 PPTX 파일로 저장
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // PDF 문서 로드
        Document doc = new Document(pdfDocumentFileName);
        // PptxSaveOptions 인스턴스 생성
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // PPTX 형식으로 출력 저장
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환 시도하기**

Aspose.PDF for PHP는 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 무료 앱을 사용한 PDF에서 PPTX로 변환](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}