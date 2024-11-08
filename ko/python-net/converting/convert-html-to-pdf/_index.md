---
title: Python에서 HTML을 PDF로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: /ko/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: 이 주제는 Aspose.PDF를 사용하여 HTML을 PDF로 변환하고 MHTML을 PDF로 변환하는 방법을 보여줍니다. for Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 개요 

Aspose.PDF for Python via .NET은 애플리케이션에서 웹 페이지와 원시 HTML 코드를 PDF 파일로 생성할 수 있는 전문 솔루션입니다.

이 문서는 **Python을 사용하여 HTML을 PDF로 변환하는 방법**을 설명합니다. 이 문서는 다음 주제를 다룹니다.

_포맷_: **HTML**
- [Python HTML을 PDF로](#python-html-to-pdf)
- [Python HTML을 PDF로 변환](#python-html-to-pdf)
- [Python HTML을 PDF로 변환하는 방법](#python-html-to-pdf)

## Python HTML을 PDF로 변환

**Aspose.PDF for Python**은 기존의 HTML 문서를 원활하게 PDF로 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 사용자 정의할 수 있습니다.

## HTML을 PDF로 변환

다음 Python 코드 예제는 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다.
2. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 초기화합니다.
3. **Document.Save()** 메서드를 호출하여 출력 PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**HTML을 PDF로 온라인 변환 시도하기**

Aspose는 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)라는 온라인 무료 애플리케이션을 제공합니다. 여기에서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}