---
title: PDF를 PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 110
url: /ko/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF를 사용하면 PDF를 PowerPoint 형식으로 변환할 수 있습니다. 한 가지 방법은 PDF를 슬라이드가 이미지인 PPTX로 변환하는 것입니다.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

우리는 Aspose.Slides라는 API를 보유하고 있으며, 이 API는 PPT/PPTX 프레젠테이션을 생성하고 조작하는 기능을 제공합니다. 또한 이 API는 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능도 제공합니다. Aspose.PDF for Java에서는 PDF 문서를 PPTX 형식으로 변환하는 기능을 도입했습니다. 변환 과정에서 PDF 파일의 각 페이지가 PPTX 파일의 개별 슬라이드로 변환됩니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

PDF를 PPTX로 변환하는 동안 텍스트는 이미지로 렌더링되는 대신 선택/수정이 가능한 텍스트로 표시됩니다. PDF 파일을 PPTX 형식으로 변환하려면 Aspose.PDF에서 PptxSaveOptions라는 클래스를 제공한다는 점에 유의하십시오. 이 클래스의 객체는 [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 클래스는 두 번째 인수로 전달됩니다 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) 메서드.

다음 코드 스니펫을 확인하여 PDF를 PowerPoint 형식으로 변환하는 작업을 해결하십시오:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

