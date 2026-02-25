---
title: Python에서 PDF를 HTML로 변환
linktitle: PDF를 HTML 형식으로 변환
type: docs
weight: 50
url: /ko/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: 이 주제에서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python에서 PDF를 HTML로 변환하는 방법
Abstract: 이 문서는 Python, 특히 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일을 HTML로 변환하는 포괄적인 가이드를 제공합니다. 프로그램matically 변환을 수행하기 위한 필요한 단계들을 설명하며, 소스 PDF에서 `Document` 객체를 생성하고 `HtmlSaveOptions`를 사용하여 문서를 HTML 형식으로 저장하는 방법을 강조합니다. 문서에는 변환 과정을 보여주는 간결한 Python 코드 스니펫이 포함되어 있습니다. 또한 사용자가 변환 기능과 품질을 확인할 수 있도록 Aspose.PDF의 "PDF to HTML" 애플리케이션이라는 온라인 도구를 소개합니다. 이 문서는 다양한 관련 주제를 다루도록 구성되어 있어 Python을 사용한 PDF를 HTML로 변환하는 것에 대해 충분히 이해할 수 있도록 합니다.
---

## PDF를 HTML로 변환

**Aspose.PDF for Python via .NET**은 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서는 PDF 파일을 <abbr title="HyperText Markup Language">HTML</abbr>로 변환하는 방법을 설명합니다. Python으로 PDF를 HTML로 변환하기 위해 몇 줄의 코드만 사용할 수 있습니다. 웹사이트를 만들거나 온라인 포럼에 콘텐츠를 추가하려면 PDF를 HTML로 변환해야 할 수도 있습니다. PDF를 HTML로 변환하는 한 가지 방법은 Python을 프로그래밍 방식으로 사용하는 것입니다.

{{% alert color="success" %}}
**PDF를 온라인으로 HTML로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF를 HTML로"](https://products.aspose.app/pdf/conversion/pdf-to-html)를 제공합니다. 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF to HTML 무료 앱](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

단계: Python에서 PDF를 HTML로 변환

1. 소스 PDF 문서를 사용하여 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/)에 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 지정된 폴더에 이미지를 저장하면서 PDF를 HTML로 변환

이 함수는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 HTML 형식으로 변환합니다. 추출된 모든 이미지는 HTML 파일에 포함되는 대신 지정된 폴더에 저장됩니다.

1. HTML 저장 옵션을 구성합니다.
1. 외부 이미지와 함께 HTML로 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 다중 페이지 HTML로 변환

이 함수는 PDF 파일을 다중 페이지 HTML로 변환합니다. 각 PDF 페이지가 별개의 HTML 파일로 내보내져 출력물을 더 쉽게 탐색할 수 있게 하고 큰 PDF의 로딩 시간을 줄여줍니다.

1. 'ap.Document'를 사용하여 소스 PDF를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 'set split_into_pages'를 설정합니다.
1. 페이지가 별도 파일로 분할된 HTML로 문서를 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 지정된 폴더에 SVG 이미지를 저장하면서 PDF를 HTML로 변환

이 함수는 PDF를 HTML 형식으로 변환하면서 모든 이미지를 SVG 파일로 지정된 폴더에 저장합니다. 이미지는 HTML에 직접 포함되지 않습니다.

1. 'ap.Document'를 사용하여 소스 PDF를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 'set special_folder_for_svg_images'를 대상 폴더로 설정합니다.
1. 외부 SVG 이미지와 함께 HTML로 문서를 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 HTML로 변환하고 압축된 SVG 이미지를 저장

이 스니펫은 PDF를 HTML 형식으로 변환하면서 모든 이미지를 지정된 폴더에 SVG 파일로 저장하고 파일 크기를 줄이기 위해 압축합니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고:
- 'special_folder_for_svg_images'를 설정하여 SVG 이미지를 외부에 저장합니다.
- 'compress_svg_graphics_if_any'를 활성화하여 SVG 이미지를 압축합니다.
1. 압축된 외부 SVG 이미지와 함께 HTML로 문서를 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 삽입된 래스터 이미지 제어와 함께 PDF를 HTML로 변환

이 스니펫은 PDF를 HTML 형식으로 변환하면서 래스터 이미지를 PNG 페이지 배경으로 삽입합니다. 이 방법은 이미지 품질과 페이지 레이아웃을 HTML 내에 보존합니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 'raster_images_saving_mode'를 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'로 설정합니다.
1. 래스터 이미지를 포함하여 문서를 HTML로 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 본문 전용 HTML 페이지로 변환

이 함수는 PDF를 HTML 형식으로 변환하여 'html' 또는 'head' 태그 없이 'body-only' 콘텐츠를 생성하고, 출력을 개별 페이지로 분할합니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 구성합니다:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT'를 설정하여 'body' 콘텐츠만 생성합니다.
- 'split_into_pages'를 설정하여 각 PDF 페이지마다 별도의 HTML 파일을 생성합니다.
1. 지정된 옵션으로 문서를 HTML로 저장합니다.
1. 확인 메시지를 출력합니다.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 투명 텍스트 렌더링으로 HTML로 변환

이 함수는 PDF를 HTML 형식으로 변환하여 그림자 텍스트를 포함한 모든 텍스트를 투명하게 렌더링합니다. 이는 시각적 정확성을 유지하면서 출력 HTML에서 유연한 스타일링을 가능하게 합니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 구성합니다:
- 'save_transparent_texts'를 설정하여 일반 텍스트를 투명하게 렌더링합니다.
- 'save_shadowed_texts_as_transparent_texts'를 설정하여 그림자 텍스트를 투명하게 렌더링합니다.
1. 투명 텍스트 렌더링 옵션으로 문서를 HTML로 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 문서 레이어 렌더링으로 HTML로 변환

이 함수는 PDF를 HTML 형식으로 변환하면서 마크된 콘텐츠를 출력 HTML의 개별 레이어로 변환하여 문서 레이어를 보존합니다. 이를 통해 주석, 배경 및 오버레이와 같은 레이어 요소가 정확하게 렌더링됩니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HtmlSaveOptions'를 생성하고 'convert_marked_content_to_layers'를 활성화하여 레이어를 보존합니다.
1. 레이어가 적용된 콘텐츠로 문서를 HTML로 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


