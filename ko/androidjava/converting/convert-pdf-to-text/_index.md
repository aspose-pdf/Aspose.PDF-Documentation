---
title: PDF를 텍스트로 변환
linktitle: PDF를 텍스트로 변환
type: docs
weight: 120
url: /ko/androidjava/convert-pdf-to-txt/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java를 사용하면 전체 PDF 문서를 텍스트 파일로 변환하거나 PDF 페이지 하나만 텍스트 파일로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## PDF 페이지를 텍스트 파일로 변환

Aspose.PDF for Android via Java를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. Visit method of [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 이 작업을 해결하기 위한 클래스.

다음 코드 스니펫은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```java
public void convertPDFPagesToTXT() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Save the extracted text in text file
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

