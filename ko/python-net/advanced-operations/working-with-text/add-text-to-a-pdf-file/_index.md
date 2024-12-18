---
title: 파이썬을 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/python-net/add-text-to-pdf-file/
description: 이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하거나 HTML 조각을 추가하거나 사용자 정의 OTF 글꼴을 사용하는 방법을 알아보세요.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF에 텍스트 추가",
    "alternativeHeadline": "PDF에 텍스트 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add text to pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "이 문서는 파이썬용 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하거나 HTML 조각을 추가하거나 사용자 정의 OTF 글꼴을 사용하는 방법을 알아보세요."
}
</script>


## 텍스트 추가

1. Aspose.PDF를 사용하여 입력 PDF 문서를 엽니다.
1. 텍스트를 추가하려는 특정 페이지를 선택합니다.
1. TextFragment 객체를 생성합니다. 텍스트 조각은 'main text'라는 내용으로 생성됩니다. 이 조각은 페이지의 좌표 (100, 600)에 위치합니다.
1. 텍스트 속성 설정. 글꼴 크기, 글꼴 유형(Times New Roman), 배경색(연한 회색), 전경색(빨간색)과 같은 텍스트의 다양한 속성을 설정합니다.
1. TextBuilder 객체 생성. 선택한 페이지로 TextBuilder 객체를 인스턴스화합니다.
1. 텍스트 조각 추가. 이전에 생성한 텍스트 조각을 TextBuilder 객체를 사용하여 PDF 페이지에 추가합니다.
1. [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 특정 페이지 가져오기
    page = document.pages[1]

    # 텍스트 조각 생성
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # 텍스트 속성 설정
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # TextBuilder 객체 생성
    builder = ap.text.TextBuilder(page)

    # PDF 페이지에 텍스트 조각 추가
    builder.append_text(text_fragment)

    # 결과 PDF 문서 저장
    document.save(output_pdf)             
```


## 스트림에서 폰트 로드하기

다음 코드 스니펫은 PDF 문서에 텍스트를 추가할 때 스트림 객체에서 폰트를 로드하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 입력 PDF 파일 로드
    document = ap.Document()
    document.pages.add()
    # 문서의 첫 번째 페이지에 대한 텍스트 빌더 객체 생성
    text_builder = ap.text.TextBuilder(document.pages[1])
    # 샘플 문자열로 텍스트 조각 생성
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # TrueType 폰트를 스트림 객체로 로드
        font_stream = open(input_ttf, "rb")
        # 텍스트 문자열에 대한 폰트 이름 설정
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # 텍스트 조각의 위치 지정
        text_fragment.position = ap.text.Position(10, 10)
        # 텍스트를 TextBuilder에 추가하여 PDF 파일 위에 배치할 수 있도록 함
        text_builder.append_text(text_fragment)
        # 결과 PDF 문서를 저장
        document.save(output_pdf)
```


## TextParagraph를 사용하여 텍스트 추가

다음 코드 스니펫은 [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 클래스를 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document()
    # Document 객체의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # 텍스트 단락 생성
    paragraph = ap.text.TextParagraph()
    # 후속 줄 들여쓰기 설정
    paragraph.subsequent_lines_indent = 20
    # TextParagraph를 추가할 위치 지정
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # 단어 줄 바꿈 모드 지정
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # 텍스트 조각 생성
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # 단락에 조각 추가
    paragraph.append_line(fragment1)
    # 단락 추가
    builder.append_paragraph(paragraph)

    # 결과 PDF 문서 저장.
    document.save(output_pdf)
```


## 텍스트 세그먼트에 하이퍼링크 추가

이 코드는 외부 리소스로의 하이퍼링크를 포함하여 PDF 문서 내에서 동적이고 상호작용적인 콘텐츠를 만드는 방법을 보여줍니다.

PDF 페이지는 하나 이상의 TextFragment 객체로 구성될 수 있으며, 각 TextFragment 객체는 하나 이상의 [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/) 인스턴스를 가질 수 있습니다.

다음 코드 스니펫을 사용하여 이 요구 사항을 달성해 보십시오:

```python

    import aspose.pdf as ap

    # 문서 인스턴스 생성
    document = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    page1 = document.pages.add()
    # TextFragment 인스턴스 생성
    tf = ap.text.TextFragment("샘플 텍스트 조각")
    # TextFragment의 수평 정렬 설정
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # 샘플 텍스트로 textsegment 생성
    segment = ap.text.TextSegment(" ... 텍스트 세그먼트 1...")
    # TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf.segments.append(segment)
    # 새로운 TextSegment 생성
    segment = ap.text.TextSegment("Google로의 링크")
    # TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf.segments.append(segment)
    # TextSegment에 하이퍼링크 설정
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # 텍스트 세그먼트에 전경색 설정
    segment.text_state.foreground_color = ap.Color.blue
    # 텍스트 서식을 이탤릭체로 설정
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # 또 다른 TextSegment 객체 생성
    segment = ap.text.TextSegment("하이퍼링크가 없는 텍스트 세그먼트")
    # TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf.segments.append(segment)
    # 페이지 객체의 단락 컬렉션에 TextFragment 추가
    page1.paragraphs.add(tf)
    # 결과 PDF 문서 저장
    document.save(output_pdf)
```


## OTF 폰트 사용

Aspose.PDF for Python via .NET은 PDF 파일 내용을 생성/조작할 때 사용자 정의/TrueType 폰트를 사용할 수 있는 기능을 제공하여 파일 내용이 기본 시스템 폰트가 아닌 다른 폰트를 사용하여 표시되도록 합니다.

```python

    import aspose.pdf as ap

    # 새 문서 인스턴스 생성
    document = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # 샘플 텍스트로 TextFragment 인스턴스 생성
    fragment = ap.text.TextFragment("OTF 폰트의 샘플 텍스트")
    # 또는 시스템 디렉토리에서 OTF 폰트의 경로를 지정할 수도 있습니다.
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # PDF 파일 내부에 폰트를 포함하도록 지정하여 올바르게 표시되도록 합니다,
    # 특정 폰트가 대상 기기에 설치/존재하지 않은 경우에도
    fragment.text_state.font.is_embedded = True
    # Page 인스턴스의 단락 컬렉션에 TextFragment 추가
    page.paragraphs.add(fragment)
    # 결과 PDF 문서를 저장합니다.
    document.save(output_pdf)
```


## DOM을 사용하여 HTML 문자열 추가하기

다음 파이썬 코드는 Aspose.PDF 라이브러리를 사용하여 HTML 조각을 포함한 PDF 문서를 생성합니다.

1. Document 인스턴스화. Document 클래스의 인스턴스를 생성하여 PDF 문서를 나타냅니다.
1. PDF 문서에 페이지 추가.
1. HTML 콘텐츠로 HtmlFragment 객체 인스턴스화
1. HTML 조각의 여백 설정. 이 경우, 하단 여백은 10 포인트로 설정되고 상단 여백은 200 포인트로 설정됩니다.
1. 페이지에 HTML 조각 추가.
1. PDF 파일 저장.

```python

    import aspose.pdf as ap

    # Document 객체 인스턴스화
    doc = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    page = doc.pages.add()
    # HTML 콘텐츠로 HtmlFragment 인스턴스화
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # 하단 여백 정보 설정
    title.margin.bottom = 10
    # 상단 여백 정보 설정
    title.margin.top = 200
    # 페이지의 단락 컬렉션에 HTML 조각 추가
    page.paragraphs.add(title)
    # PDF 파일 저장
    doc.save(output_pdf)
```


### FootNote에 대한 사용자 지정 선 스타일

다음 예제는 Pdf 페이지의 하단에 각주를 추가하고 사용자 지정 선 스타일을 정의하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    doc = ap.Document()
    # 페이지를 PDF의 페이지 컬렉션에 추가
    page = doc.pages.add()
    # GraphInfo 객체 생성
    graph = ap.GraphInfo()
    # 선 너비를 2로 설정
    graph.line_width = 2
    # 그래프 객체의 색상을 설정
    graph.color = ap.Color.red
    # 대시 배열 값을 3으로 설정
    graph.dash_array = [3]
    # 대시 위상 값을 1로 설정
    graph.dash_phase = 1
    # 페이지에 대한 각주 선 스타일을 그래프로 설정
    page.note_line_style = graph
    # TextFragment 인스턴스 생성
    text = ap.text.TextFragment("Hello World")
    # TextFragment에 대한 각주 값 설정
    text.foot_note = ap.Note("테스트 텍스트 1에 대한 각주")
    # 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page.paragraphs.add(text)
    # 두 번째 TextFragment 생성
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # 두 번째 텍스트 조각에 대한 각주 설정
    text.foot_note = ap.Note("테스트 텍스트 2에 대한 각주")
    # PDF 파일의 단락 컬렉션에 두 번째 텍스트 조각 추가
    page.paragraphs.add(text)
    # 결과 PDF 문서를 저장합니다.
    doc.save(output_pdf)
```


### 각주 레이블 사용자 정의

다음 코드 스니펫은 각주가 포함된 텍스트 조각으로 PDF 문서를 생성하는 방법을 보여줍니다.

기본적으로 각주 번호는 1부터 시작하여 증가합니다. 그러나 사용자 정의 각주 레이블을 설정해야 할 수도 있습니다. 이 요구 사항을 충족하려면 다음 코드 스니펫을 사용해 보세요.

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # PDF의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # GraphInfo 객체 생성
    graph = ap.GraphInfo()
    # 선 너비를 2로 설정
    graph.line_width = 2
    # 그래프 객체의 색상 설정
    graph.color = ap.Color.red
    # 대시 배열 값을 3으로 설정
    graph.dash_array = [3]
    # 대시 페이즈 값을 1로 설정
    graph.dash_phase = 1
    # 페이지의 각주 선 스타일을 그래프로 설정
    page.note_line_style = graph
    # TextFragment 인스턴스 생성
    text = ap.text.TextFragment("Hello World")
    # TextFragment에 각주 값 설정
    text.foot_note = ap.Note("테스트 텍스트 1에 대한 각주")
    # 각주에 대한 사용자 정의 레이블 지정
    text.foot_note.text = " Aspose"
    # 문서의 첫 페이지의 단락 컬렉션에 TextFragment 추가
    page.paragraphs.add(text)
    # 결과 PDF 문서를 저장합니다.
    document.save(output_pdf)
```


## 이미지 및 표를 각주에 추가하기

이 코드는 Aspose.PDF for Python을 사용하여 이미지, 텍스트 및 표를 포함하는 복잡한 각주를 포함하는 텍스트 조각으로 PDF 문서를 만드는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # 결과 PDF 문서를 저장합니다.
    document.save(output_pdf)
```

## 각주 생성 방법

각주는 독자가 논문 끝부분에서 정보의 출처나 논문에서 인용되거나 언급된 단어의 출처를 찾을 수 있는 특정 위치를 참조하는 출처 인용입니다.
 인용구나 요약된 자료를 사용할 때, 인용문이나 요약된 문장은 위첨자 번호가 뒤따릅니다.

이 코드는 Aspose.PDF for Python을 사용하여 PDF 문서에 각주가 포함된 텍스트 조각을 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # PDF의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # TextFragment 인스턴스 생성
    text = ap.text.TextFragment("Hello World")
    # TextFragment에 EndNote 값 설정
    text.end_note = ap.Note("샘플 각주")
    # FootNote에 사용자 지정 레이블 지정
    text.end_note.text = " Aspose"
    # 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page.paragraphs.add(text)
    # 결과 PDF 문서 저장.
    document.save(output_pdf)
```

## 인라인 단락으로서의 텍스트와 이미지

PDF 파일의 기본 레이아웃은 흐름 레이아웃(좌상단에서 우하단)입니다. 따라서 PDF 파일에 추가되는 모든 새로운 요소는 오른쪽 하단 흐름에 추가됩니다. 그러나 다양한 페이지 요소, 즉 이미지와 텍스트를 같은 수준(차례대로)으로 표시해야 할 수도 있습니다. 한 가지 접근 방식은 테이블 인스턴스를 생성하고 두 요소를 개별 셀 객체에 추가하는 것입니다. 그러나 또 다른 접근 방식은 인라인 단락이 될 수 있습니다. 이미지와 텍스트의 IsInLineParagraph 속성을 true로 설정하면 이러한 단락은 다른 페이지 요소에 인라인으로 나타납니다.

다음 코드 스니펫은 PDF 파일에 텍스트와 이미지를 인라인 단락으로 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 인스턴스 생성
    document = ap.Document()
    # 문서 인스턴스의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # TextFragment 생성
    text = ap.text.TextFragment("Hello World.. ")
    # 페이지 객체의 단락 컬렉션에 텍스트 조각 추가
    page.paragraphs.add(text)
    # 이미지 인스턴스 생성
    image = ap.Image()
    # 이미지가 이전 단락 객체(TextFragment) 바로 뒤에 나타나도록 인라인 단락으로 설정
    image.is_in_line_paragraph = True
    # 이미지 파일 경로 지정
    image.file = input_jpg
    # 이미지 높이 설정 (선택 사항)
    image.fix_height = 30
    # 이미지 너비 설정 (선택 사항)
    image.fix_width = 100
    # 페이지 객체의 단락 컬렉션에 이미지 추가
    page.paragraphs.add(image)
    # 다른 내용으로 TextFragment 객체 다시 초기화
    text = ap.text.TextFragment(" Hello Again..")
    # TextFragment를 인라인 단락으로 설정
    text.is_in_line_paragraph = True
    # 새로 생성된 TextFragment를 페이지의 단락 컬렉션에 추가
    page.paragraphs.add(text)
    # 결과 PDF 문서 저장
    document.save(output_pdf)
```

## 텍스트 추가 시 문자 간격 지정

다음 코드 스니펫은 문자 간격이 증가된 텍스트 조각을 포함하는 PDF 문서를 생성하는 방법을 보여줍니다.

텍스트는 TextFragment 인스턴스를 사용하거나 TextParagraph 객체를 사용하여 PDF 파일의 단락 컬렉션 내에 추가할 수 있으며, TextStamp 클래스를 사용하여 PDF 내에 텍스트를 스탬프로 찍을 수도 있습니다.

### TextBuilder와 TextFragment 사용

```python

    import aspose.pdf as ap

    # 문서 인스턴스 생성
    document = ap.Document()
    # 문서의 페이지 컬렉션에 페이지 추가
    document.pages.add()
    # TextBuilder 인스턴스 생성
    builder = ap.text.TextBuilder(document.pages[1])
    # 샘플 내용을 가진 텍스트 조각 인스턴스 생성
    wide_fragment = ap.text.TextFragment("문자 간격이 증가된 텍스트")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # TextFragment의 문자 간격 지정
    wide_fragment.text_state.character_spacing = 2.0
    # TextFragment의 위치 지정
    wide_fragment.position = ap.text.Position(100, 650)
    # TextBuilder 인스턴스에 TextFragment 추가
    builder.append_text(wide_fragment)
    # 결과 PDF 문서 저장
    document.save(output_pdf)
```


### Using TextParagraph

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # 페이지 컬렉션에 페이지 추가
    document.pages.add()
    # TextBuilder 인스턴스 생성
    builder = ap.text.TextBuilder(document.pages[1])
    # TextParagraph 인스턴스 초기화
    paragraph = ap.text.TextParagraph()
    # 폰트 이름과 크기를 지정하기 위해 TextState 인스턴스 생성
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # 문자 간격 지정
    state.character_spacing = 1.5
    # TextParagraph 객체에 텍스트 추가
    tt = "문자 간격이 있는 단락입니다"
    paragraph.append_line(tt, state)
    # TextParagraph의 위치 지정
    paragraph.position = ap.text.Position(100, 550)
    # TextBuilder 인스턴스에 TextParagraph 추가
    builder.append_paragraph(paragraph)
    # 결과 PDF 문서 저장.
    document.save(output_pdf)
```

### Using TextStamp

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # 샘플 텍스트로 TextStamp 인스턴스 초기화
    stamp = ap.TextStamp("문자 간격이 있는 텍스트 스탬프입니다")
    # Stamp 객체에 폰트 이름 지정
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # TextStamp의 폰트 크기 지정
    stamp.text_state.font_size = 12
    # 문자 간격을 1로 지정
    stamp.text_state.character_spacing = 1
    # Stamp의 x_indent 설정
    stamp.x_indent = 100
    # Stamp의 y_indent 설정
    stamp.y_indent = 500
    # 페이지 인스턴스에 텍스트 스탬프 추가
    stamp.put(page)
    # 결과 PDF 문서 저장.
    document.save(output_pdf)
```


## 다중 열 PDF 문서 만들기

[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/)은 또한 PDF 문서 페이지 내에 여러 열을 생성하는 기능을 제공합니다. 다중 열 PDF 파일을 생성하기 위해 FloatingBox 클래스를 사용할 수 있으며, 이 클래스는 FloatingBox 내 열 개수를 지정할 수 있는 column_info 속성을 제공합니다. 또한 column_spacing 및 width 속성을 사용하여 열 간 간격과 열 너비를 지정할 수 있습니다.

열 간 간격은 열 사이의 공간을 의미하며, 기본 열 간 간격은 1.25cm입니다. 열 너비가 지정되지 않은 경우, [Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/)은 페이지 크기와 열 간 간격에 따라 각 열의 너비를 자동으로 계산합니다.

아래 예제는 Graphs 객체(선)를 사용하여 두 개의 열을 생성하는 방법을 보여줍니다. 이 객체들은 FloatingBox의 단락 컬렉션에 추가되고, 이후 Page 인스턴스의 단락 컬렉션에 추가됩니다.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # PDF 파일의 왼쪽 여백 정보를 지정합니다.
    document.page_info.margin.left = 40
    # PDF 파일의 오른쪽 여백 정보를 지정합니다.
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # 섹션 객체의 문단 컬렉션에 선을 추가합니다.
    page.paragraphs.add(graph1)

    # 선의 좌표를 지정합니다.
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # HTML 태그가 포함된 텍스트로 문자열 변수를 생성합니다.
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> 돈 사기를 피하는 방법</<strong> "
        + "</font>"
    )
    # HTML 텍스트를 포함하는 텍스트 문단을 생성합니다.
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # 섹션에 네 개의 열을 추가합니다.
    box.column_info.column_count = 2
    # 열 사이의 간격을 설정합니다.
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # 선을 그리기 위한 그래프 객체를 생성합니다.
    graph2 = ap.drawing.Graph(50, 10)
    # 선의 좌표를 지정합니다.
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # 섹션 객체의 문단 컬렉션에 선을 추가합니다.
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # PDF 파일 저장
    document.save(output_pdf)
```


## 사용자 지정 탭 정지 사용

이 Python 코드 스니펫은 탭 정지를 사용하여 테이블 구조를 시뮬레이션하는 텍스트 조각을 포함하는 PDF 문서를 만드는 방법을 보여줍니다.

다음은 사용자 지정 TAB 정지를 설정하는 예입니다.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "이것은 TAB 정지를 사용하여 테이블을 형성하는 예입니다", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## PDF에 투명 텍스트 추가하는 방법

PDF 파일은 이미지, 텍스트, 그래프, 첨부 파일, 주석 객체를 포함하며 TextFragment를 생성할 때 전경, 배경 색상 정보뿐만 아니라 텍스트 서식을 설정할 수 있습니다. Aspose.PDF for Python via .NET은 알파 색상 채널을 사용하여 텍스트를 추가하는 기능을 지원합니다.

다음 코드 스니펫은 투명한 색상의 텍스트를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 생성
    page = document.pages.add()

    # 샘플 값으로 TextFragment 인스턴스 생성
    text = ap.text.TextFragment(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text "
    )
    # Alpha 채널에서 색상 객체 생성
    color = ap.Color.from_argb(30, 0, 255, 0)
    # 텍스트 인스턴스에 색상 정보 설정
    text.text_state.foreground_color = color
    # 페이지 인스턴스의 단락 컬렉션에 텍스트 추가
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## 글꼴의 줄 간격 지정

모든 글꼴에는 추상적인 사각형이 있으며, 이 사각형의 높이는 동일한 글꼴 크기에서 줄 간의 의도된 거리입니다. 이 사각형은 em 사각형이라고 하며 글리프 윤곽이 정의되는 디자인 그리드입니다. 입력 글꼴의 많은 문자는 글꼴의 em 사각형 경계를 벗어난 지점에 배치되어 있으므로 글꼴을 올바르게 표시하려면 특별한 설정이 필요합니다.

다음 코드 스니펫은 PDF를 로드하고, TrueType 글꼴을 사용하여 특정 줄 간격이 있는 텍스트 조각을 추가하고, 수정된 PDF 문서를 저장합니다:

```python

    import aspose.pdf as ap

    # 입력 PDF 파일 로드
    document = ap.Document()
    # LineSpacingMode.FULL_SIZE로 TextFormattingOptions 생성
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # 샘플 문자열로 텍스트 조각 생성
    text_fragment = ap.text.TextFragment("Hello world")

    # TrueType 글꼴을 스트림 객체에 로드
    font_stream = open(input_ttf, "rb")
    # 텍스트 문자열에 대한 글꼴 이름 설정
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # 텍스트 조각의 위치 지정
    text_fragment.position = ap.text.Position(100, 600)
    # 현재 조각의 TextFormattingOptions를 사전 정의된 것으로 설정(즉, LineSpacingMode.FULL_SIZE를 가리킴)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # 결과 PDF 문서 저장
    document.save(output_pdf)
```


## 텍스트 너비를 동적으로 얻기

이 Python 코드 스니펫은 Aspose.PDF에서 폰트 객체와 텍스트 상태 객체로부터 얻은 문자열의 측정을 비교합니다:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("예상치 못한 폰트 문자열 측정!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("예상치 못한 폰트 문자열 측정!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("폰트와 상태 문자열 측정이 일치하지 않음!")

        c_code += 1