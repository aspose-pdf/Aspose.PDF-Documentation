---
title: HTML을 PDF로 변환하기
linktitle: HTML 파일을 PDF로 변환하기
type: docs
weight: 40
url: /ko/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: 이 주제는 Aspose.PDF를 사용하여 HTML을 PDF로, MHTML을 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 개요

Aspose.PDF for Python via Java는 웹 페이지와 원시 HTML 코드를 응용 프로그램에서 PDF 파일로 생성할 수 있는 전문 솔루션입니다.

이 문서에서는 **Python을 사용하여 HTML을 PDF로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **HTML**
- [Python HTML을 PDF로](#python-html-to-pdf)
- [Python HTML을 PDF로 변환하기](#python-html-to-pdf)
- [Python HTML을 PDF로 변환하는 방법](#python-html-to-pdf)

## Python HTML을 PDF로 변환

**Aspose.PDF for Python**은 기존 HTML 문서를 원활하게 PDF로 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 사용자 정의할 수 있습니다.

## HTML을 PDF로 변환하기

다음 Python 코드 샘플은 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다.
2. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 초기화합니다.
3. **Document.Save()** 메서드를 호출하여 출력 PDF 문서를 저장합니다.

```python

from asposepdf import Api


# 라이센스 초기화
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# 바이트 배열에서의 변환
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# 파일에서의 변환
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**온라인으로 HTML을 PDF로 변환해보세요**


Aspose는 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)라는 무료 온라인 애플리케이션을 제공하여 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}