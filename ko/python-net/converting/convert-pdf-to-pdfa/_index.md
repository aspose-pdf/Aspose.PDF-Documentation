---
title: Python에서 PDF를 PDF/A 형식으로 변환
linktitle: PDF를 PDF/A 형식으로 변환
type: docs
weight: 100
url: /ko/python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: 이 주제에서는 Aspose.PDF for Python을 통해 PDF 파일을 PDF/A 호환 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python**을 사용하면 PDF 파일을 <abbr title="Portable Document Format / A">PDF/A</abbr> 호환 PDF 파일로 변환할 수 있습니다. 이를 수행하기 전에 파일을 검증해야 합니다. 이 주제에서는 그 방법을 설명합니다.

{{% alert color="primary" %}}

PDF/A 적합성을 검증하기 위해 Adobe Preflight을 따릅니다. 시장에 나와 있는 모든 도구는 자신만의 PDF/A 적합성 "표현"을 가지고 있습니다. 참조를 위해 PDF/A 검증 도구에 대한 이 기사를 확인하세요. Aspose.PDF가 PDF 파일을 생성하는 방법을 확인하기 위해 Adobe 제품을 선택한 이유는 Adobe가 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

{{% /alert %}}

Document 클래스의 Convert 메서드를 사용하여 파일을 변환합니다.
 PDF를 PDF/A 준수 파일로 변환하기 전에 Validate 메서드를 사용하여 PDF를 검증하십시오. 검증 결과는 XML 파일에 저장되고, 이 결과는 Convert 메서드에도 전달됩니다. ConvertErrorAction 열거형을 사용하여 변환할 수 없는 요소에 대한 작업을 지정할 수도 있습니다.

{{% alert color="success" %}}
**PDF를 PDF/A로 온라인 변환 시도하기**

Aspose.PDF for Python은 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)라는 무료 온라인 애플리케이션을 제공합니다. 이곳에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PDF/A로 무료 앱을 사용하여](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## PDF 파일을 PDF/A-1b로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 준수 PDF로 변환하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # PDF 문서 열기
    document = ap.Document(input_pdf)
    # PDF/A 준수 문서로 변환하기
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # 출력 문서 저장
    document.save(output_pdf)
```