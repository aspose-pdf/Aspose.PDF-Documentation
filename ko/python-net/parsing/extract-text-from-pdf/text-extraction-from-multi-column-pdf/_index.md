---
title: 여러 열로 구성된 PDF의 텍스트 추출 개선
linktitle: 여러 열로 구성된 PDF에서 텍스트 추출
type: docs
weight: 30
url: /ko/python-net/text-extraction-from-multi-column-pdf/
description: Python용 Aspose.PDF 를 사용하여 다중 열 PDF 레이아웃에서 텍스트 추출을 개선하는 기술을 알아보십시오.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 수동으로 글꼴 크기를 줄인 다음 추출

일부 다중 열 레이아웃에서는 추출하기 전에 텍스트 조각의 글꼴 크기를 줄이면 읽기 순서를 개선하고 중복 문제를 줄일 수 있습니다.이 방법은 잡지, 연구 논문, 브로셔 또는 빽빽한 텍스트 열이 있는 보고서와 같이 형식이 엄격한 문서에 유용할 수 있습니다.

1. PDF를 로드합니다.
1. 용도 [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 텍스트 조각을 수집합니다.
1. 각 조각의 글꼴 크기를 줄인 다음 문서를 저장하고 다시 엽니다.
1. 용도 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 텍스트를 추출합니다.
1. 추출한 텍스트를 출력 파일에 씁니다.

```python
import io
import aspose.pdf as ap


def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)

    frag_absorber = ap.text.TextFragmentAbsorber()
    doc.pages.accept(frag_absorber)
    for frag in frag_absorber.text_fragments:
        frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
    # Save to memory stream and reopen (to apply changes)
    ms = io.BytesIO()
    doc.save(ms)
    ms.seek(0)
    doc2 = ap.Document(ms)
    text_absorber = ap.text.TextAbsorber()
    doc2.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## 스케일 팩터로 텍스트 추출

다중 열 추출을 위한 또 다른 옵션은 다음과 같습니다. [텍스트 추출 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) 스케일 팩터 포함.스케일 팩터를 조정하면 빽빽한 레이아웃, 표 또는 열 기반 문서에서 조밀하게 구성된 조각의 해석을 개선하고 읽기 순서를 더 정확하게 유지할 수 있습니다.

1. PDF를 로드합니다.
1. 만들기 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. 구성 `TextExtractionOptions.scale_factor`.
1. 흡수 장치에 추출 옵션을 지정합니다.
1. 페이지 텍스트를 추출하고 결과를 출력 파일에 씁니다.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
