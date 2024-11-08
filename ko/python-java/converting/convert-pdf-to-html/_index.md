---
title: PDF를 HTML로 변환하기 - Python
linktitle: PDF를 HTML 형식으로 변환하기
type: docs
weight: 50
url: /ko/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 이 주제는 Aspose.PDF for Python Java 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 개요

이 문서는 **Python을 사용하여 PDF를 HTML로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **HTML**
- [Python PDF를 HTML로](#python-pdf-to-html)
- [Python PDF를 HTML로 변환](#python-pdf-to-html)
- [Python PDF 파일을 HTML로 변환하는 방법](#python-pdf-to-html)

## PDF를 HTML로 변환하기

**Aspose.PDF for Python via .NET**은 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하기 위한 많은 기능을 제공합니다.
 이 기사는 PDF 파일을 <abbr title="HyperText Markup Language">HTML</abbr>로 변환하는 방법에 대해 논의합니다. PDF를 HTML로 변환하기 위해 몇 줄의 Python 코드를 사용할 수 있습니다. 웹사이트를 만들거나 온라인 포럼에 콘텐츠를 추가하려면 PDF를 HTML로 변환해야 할 수도 있습니다. PDF를 HTML로 변환하는 한 가지 방법은 Python을 사용하여 프로그래밍적으로 수행하는 것입니다.

{{% alert color="success" %}}
**온라인에서 PDF를 HTML로 변환해보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)을 제공하여 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>단계: Python에서 PDF를 HTML로 변환</strong></a>

1. 원본 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드를 호출하여 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/)에 저장합니다.

```python
from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# PDF 문서 열기
document = Api.Document(documentName)

# 문서를 HTML 형식으로 저장
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## 관련 항목

이 문서에서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **HTML**
- [Python PDF를 HTML로 변환하는 코드](#python-pdf-to-html)
- [Python PDF를 HTML로 변환하는 API](#python-pdf-to-html)
- [Python PDF를 HTML로 프로그래밍 방식으로 변환하기](#python-pdf-to-html)
- [Python PDF를 HTML로 변환하는 라이브러리](#python-pdf-to-html)
- [Python PDF를 HTML로 저장하기](#python-pdf-to-html)
- [Python PDF에서 HTML 생성하기](#python-pdf-to-html)
- [Python PDF에서 HTML 만들기](#python-pdf-to-html)

- [Python PDF를 HTML로 변환기](#python-pdf-to-html)