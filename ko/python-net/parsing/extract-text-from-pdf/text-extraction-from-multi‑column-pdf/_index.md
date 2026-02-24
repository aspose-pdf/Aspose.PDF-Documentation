---
title: 다중 열 PDF에서 텍스트 추출 개선
linktitle: 다중 열 PDF에서 텍스트 추출
type: docs
weight: 30
url: /ko/python-net/text-extraction-from-multi‑column-pdf/
description: 이 섹션에는 Python에서 Aspose.PDF를 사용한 텍스트 서식 지정 및 스케일링에 관한 기사들이 들어 있습니다.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## 폰트 크기를 수동으로 줄이고 추출하기

다중 열 PDF에서 추출 정확도는 모든 텍스트 조각의 폰트 크기를 먼저 줄인 후 추출함으로써 달성됩니다. 이 과정은 긴밀하게 서식이 지정되었거나 다중 열 레이아웃에서 발생할 수 있는 텍스트 겹침 문제를 방지하는 데 도움이 됩니다.
잡지, 학술 논문, 브로셔와 같이 복잡한 레이아웃에서 텍스트 크기를 조정하면 레이아웃이 명확해지고 추출 결과가 향상됩니다.

1. PDF를 로드합니다.
1. 기존 텍스트 조각의 폰트 크기를 줄이고, 저장한 뒤 문서를 다시 엽니다.
1. 'TextAbsorber'를 사용하여 페이지에서 텍스트를 추출합니다.
1. 추출된 텍스트를 기록합니다.

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
    try:
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
    finally:
        doc.close()
```

## 스케일 팩터를 사용하여 텍스트 추출

다중 열 레이아웃이 있는 PDF에서 문서에 스케일 팩터를 적용하여 텍스트를 추출합니다. 스케일 팩터를 조정하면 텍스트 조각이 올바르게 해석되어 추출 중 겹침이나 정렬 오류가 감소합니다.
열, 표 또는 밀집된 레이아웃이 있는 PDF에 유용하며, 스케일링을 통해 추출된 텍스트의 올바른 읽기 순서와 구조를 유지할 수 있습니다.

1. PDF를 로드합니다.
1. 'TextExtractionOptions.ScaleFactor'를 구성합니다.
1. 'TextAbsorber'를 사용하여 페이지에서 텍스트를 추출합니다.
1. 추출된 텍스트를 기록합니다.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
