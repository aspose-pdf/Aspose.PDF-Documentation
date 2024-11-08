---
title: PDF를 텍스트로 변환
linktitle: PDF를 텍스트로 변환
type: docs
weight: 120
url: /ko/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java를 사용하여 전체 PDF 문서를 텍스트 파일로 변환하거나 PDF 페이지만 텍스트 파일로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

온라인으로 시도해보세요. 이 링크에서 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## PDF 페이지를 텍스트 파일로 변환

Aspose.PDF for Android via Java를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 이 작업을 해결하려면 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 클래스의 Visit 메서드를 사용해야 합니다.

다음 코드 스니펫은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```java
public void convertPDFPagesToTXT() {
        // 문서 열기
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

        // 추출된 텍스트를 텍스트 파일에 저장
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