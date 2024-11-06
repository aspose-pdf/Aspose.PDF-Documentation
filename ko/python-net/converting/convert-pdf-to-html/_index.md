---
title: Convert PDF to HTML in Python 
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: ko/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 이 주제는 Aspose.PDF for Python .NET 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Overview

이 문서는 **Python을 사용하여 PDF를 HTML로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **HTML**
- [Python PDF to HTML](#python-pdf-to-html)
- [Python Convert PDF to HTML](#python-pdf-to-html)
- [Python How to convert PDF file to HTML](#python-pdf-to-html)


## Convert PDF to HTML

**Aspose.PDF for Python via .NET**은 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다.
 이 기사는 PDF 파일을 <abbr title="HyperText Markup Language">HTML</abbr>로 변환하는 방법에 대해 설명합니다. PDF를 HTML로 변환하려면 파이썬 코드를 몇 줄만 사용하면 됩니다. 웹사이트를 만들거나 온라인 포럼에 콘텐츠를 추가하려는 경우 PDF를 HTML로 변환해야 할 수도 있습니다. PDF를 HTML로 변환하는 한 가지 방법은 파이썬을 사용하여 프로그래밍하는 것입니다.

{{% alert color="success" %}}
**PDF를 HTML로 온라인에서 변환해 보세요**

Aspose.PDF for Python은 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)이라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사할 수 있습니다.

[![무료 앱으로 Aspose.PDF 변환 PDF to HTML](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>단계: Python에서 PDF를 HTML로 변환하기</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/)에 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 문서를 HTML 형식으로 저장
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## 참조 항목

이 문서에서는 다음 주제들도 다룹니다. 코드는 위와 동일합니다.

_형식_: **HTML**
- [Python PDF to HTML Code](#python-pdf-to-html)
- [Python PDF to HTML API](#python-pdf-to-html)
- [Python PDF to HTML Programmatically](#python-pdf-to-html)
- [Python PDF to HTML Library](#python-pdf-to-html)
- [Python Save PDF as HTML](#python-pdf-to-html)
- [Python Generate HTML from PDF](#python-pdf-to-html)
- [Python Create HTML from PDF](#python-pdf-to-html)

- [Python PDF to HTML Converter](#python-pdf-to-html)