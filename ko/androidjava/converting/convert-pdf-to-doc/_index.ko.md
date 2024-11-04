---
title: Convert PDF to DOC 
linktitle: Convert PDF to DOC
type: docs
weight: 70
url: /androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java를 사용하여 PDF 파일을 DOC 형식으로 쉽게 변환하고 완벽하게 제어하세요. Microsoft Word Doc 파일을 PDF로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠를 쉽게 조작할 수 있게 해줍니다. Aspose.PDF for Android via Java를 사용하면 PDF 파일을 DOC로 변환할 수 있습니다.

**Aspose.PDF for Android via Java**는 처음부터 PDF 문서를 생성할 수 있으며, 기존 PDF 문서를 업데이트, 편집 및 조작하기 위한 훌륭한 도구입니다.
 중요한 기능 중 하나는 페이지와 전체 PDF 문서를 이미지로 변환할 수 있는 기능입니다. 또 다른 인기 있는 기능은 PDF를 Microsoft Word DOC로 변환하는 것으로, 이는 콘텐츠를 쉽게 조작할 수 있게 해줍니다. (대부분의 사용자는 PDF 문서를 편집할 수 없지만 Microsoft Word에서 표, 텍스트 및 이미지를 쉽게 작업할 수 있습니다.)

이해하기 쉽고 간단하게 하기 위해, Aspose.PDF for Android via Java는 소스 PDF 파일을 DOC 파일로 변환하는 두 줄의 코드를 제공합니다.

{{% alert color="primary" %}}

온라인으로 시도해보세요. Aspose.PDF 변환의 품질을 확인하고 결과를 온라인에서 이 링크를 통해 확인할 수 있습니다 [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

다음 코드 조각은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

```java
 public void convertPDFtoDOC() {
        // 소스 PDF 문서를 엽니다
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // 파일을 MS 문서 형식으로 저장합니다
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```