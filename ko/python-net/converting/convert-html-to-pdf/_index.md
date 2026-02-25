---
title: Python에서 HTML을 PDF로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: /ko/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Aspose.PDF for Python via .NET을 사용하여 HTML 콘텐츠를 PDF 문서로 변환하는 방법을 배우세요
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python을 사용하여 HTML을 PDF로 변환하는 방법
Abstract: Aspose.PDF for Python via .NET은 애플리케이션 내에서 웹 페이지와 원시 HTML 코드를 PDF 파일로 생성할 수 있는 강력한 솔루션을 제공합니다. 이 문서는 Python을 사용하여 HTML을 PDF로 변환하는 가이드를 제공하며, HTML 문서를 PDF 형식으로 원활하게 변환할 수 있는 PDF 조작 API인 Aspose.PDF for Python의 사용법을 설명합니다. 변환 과정은 필요에 따라 맞춤 설정이 가능합니다. 이 문서에는 HtmlLoadOptions 클래스를 인스턴스화하고 Document 객체를 초기화한 후 Document.Save() 메서드를 사용하여 출력 PDF 문서를 저장하는 과정을 보여주는 Python 코드 샘플이 포함되어 있습니다. 또한 Aspose는 HTML을 PDF로 변환하는 온라인 도구를 제공하여 사용자가 변환 기능과 품질을 직접 확인할 수 있도록 합니다.
---

## Python HTML을 PDF로 변환

**Aspose.PDF for Python**은 기존 HTML 문서를 PDF로 원활하게 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 맞춤 설정할 수 있습니다.

## HTML을 PDF로 변환

다음 Python 코드 샘플은 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다.
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 초기화합니다.
1. **document.save()** 메서드를 호출하여 출력 PDF 문서를 저장합니다.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 HTML을 PDF로 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)을 제공하며, 해당 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 HTML to PDF 무료 앱](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 미디어 유형을 사용하여 HTML을 PDF로 변환

이 예제는 특정 렌더링 옵션을 사용하여 Aspose.PDF for Python via .NET으로 HTML 파일을 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다. 'html_media_type'은 화면 표시용 CSS 규칙을 적용합니다. 'html_media_type' 속성은 여러 값을 가질 수 있으며, HtmlMediaType.SCREEN 또는 HtmlMediaType.PRINT로 설정할 수 있습니다.
1. 로드 옵션을 사용하여 HTML을 ap.Document에 로드합니다.
1. 문서를 PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## HTML을 PDF로 변환할 때 우선순위 CSS 페이지 규칙

일부 문서는 레이아웃을 생성할 때 모호성을 일으킬 수 있는 [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)을 활용한 레이아웃 설정을 포함할 수 있습니다. 'is_priority_css_page_rule' 속성을 사용하여 우선순위를 제어할 수 있습니다. 이 속성이 'True'로 설정되면 CSS 규칙이 먼저 적용됩니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다.
1. 'is_priority_css_page_rule = False'를 설정하여 @page CSS 규칙의 우선순위를 비활성화하고 다른 스타일이 우선 적용되도록 합니다.
1. 구성된 옵션으로 HTML을 ap.Document에 로드합니다.
1. 문서를 PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 임베디드 폰트를 사용하여 HTML을 PDF로 변환

이 예제는 폰트를 임베드하면서 HTML 파일을 PDF로 변환하는 방법을 보여줍니다. 임베디드 폰트가 포함된 PDF 문서가 필요하면 'is_embed_fonts'를 True로 설정해야 합니다.

1. HTML을 PDF로 변환하도록 'HtmlLoadOptions()'를 생성합니다.
1. 'is_embed_fonts = True'를 설정하여 HTML에 사용된 모든 폰트가 PDF에 직접 임베드되어 시각적 일관성을 유지하도록 합니다.
1. 이 옵션을 사용하여 HTML을 ap.Document에 로드합니다.
1. 문서를 PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## HTML을 PDF로 변환할 때 단일 페이지에 내용 렌더링

이 예제는 Aspose.PDF for Python을 사용하여 HTML 파일을 단일 페이지 PDF로 변환하는 방법을 보여줍니다.
'is_render_to_single_page' 속성을 사용하면 모든 내용을 한 페이지에 표시할 수 있습니다.

1. 변환 프로세스를 구성하기 위해 'HtmlLoadOptions()' 인스턴스를 생성합니다.
1. 'is_render_to_single_page'를 활성화하여 전체 HTML 내용을 단일 연속 PDF 페이지에 렌더링합니다.
1. 구성된 옵션을 사용하여 문서를 'ap.Document'에 로드합니다.
1. 결과를 PDF 파일로 저장합니다.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## MHTML을 PDF로 변환

이 예제는 특정 페이지 크기를 사용하여 Aspose.PDF for Python으로 MHT(MHTML) 파일을 PDF 문서로 변환하는 방법을 보여줍니다.

1. MHT 파일 처리를 구성하기 위해 ap.MhtLoadOptions() 인스턴스를 생성합니다.
1. 페이지 크기와 같은 다양한 매개변수를 설정합니다.
1. 입력 파일과 구성된 로드 옵션을 사용하여 문서를 초기화합니다.
1. 결과 문서를 PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
