---
title: 새로운 기능
linktitle: 새로운 기능
type: docs
weight: 10
url: ko/java/whatsnew/
description: 이 페이지에서는 최근 출시된 Aspose.PDF for Java의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Aspose.PDF 24.8의 새로운 기능

24.8부터 PDF/A-4 형식에 대한 지원 추가:

```java

    Document document = new Document(inputPdf);
    // PDF-2.x 문서만 PDF/A-4로 변환할 수 있습니다.
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

또한, 이미지 스탬프에 대체 텍스트를 추가할 수 있습니다:

ImageStamp에 AlternativeText 속성이 추가되었습니다 - 값이 할당되면 문서에 ImageStamp를 추가할 때 대체 텍스트가 포함됩니다.

```java

    String p1_Alt1 = "*** 페이지 1, 대체 텍스트 1 ***",
                    p1_Alt2 = "*** 페이지 1, 대체 텍스트 2 ***",
                    p2_Alt1 = "--- 페이지 1, 대체 텍스트 1 ---",
                    p2_Alt2 = "--- 페이지 1, 대체 텍스트 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // 페이지 1에 추가
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // 페이지 2에 추가
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // 문서 저장
    document.save(outFile);
```


다음 코드는 FigureElements의 기존 이미지에 AlternativeText를 추가하는 방법을 보여줍니다.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // 대체 텍스트 설정
            figureElement.setAlternativeText("Figure alternative text (technique 1)");
        }
    }

    // 문서 저장
    document.save(outFile);
```


## Aspose.PDF 24.7의 새로운 기능

24.7 릴리스 이후, 태그가 지정된 PDF 편집의 일부로 **Aspose.Pdf.LogicalStructure.Element**에 메서드가 추가되었습니다:

- Tag (이미지, 텍스트 및 링크와 같은 특정 연산자에 태그 추가)
- InsertChild
- RemoveChild
- ClearChilds

이 메서드를 통해 PDF 파일 태그를 편집할 수 있습니다. 예를 들어:

```java

    Document document = new Document(dataDir + "test.pdf");

    // 문서의 첫 페이지를 가져옵니다.
    Page page = document.getPages().get_Item(1);

    // 다양한 목적을 위한 BDC (Begin Dictionary Context) 요소를 보유할 변수를 초기화합니다.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // 페이지의 내용을 반복합니다.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // 페이지 내용에서 현재 연산자를 가져옵니다.
        Operator op = page.getContents().get_Item(i);

        // 연산자가 BDC의 인스턴스인지 확인합니다.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // 연산자를 BDC 타입으로 캐스팅합니다.
        if (bdc != null)
        {
            // BDC의 MCID (Mark Content Identifier)가 0인지 확인합니다.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // 나중에 사용할 BDC를 저장합니다.
            }
        }
    }

    // 연산자가 Do (Draw Object)의 인스턴스인지 확인합니다.
    if (op instanceof Do) {
        Do doXobj = (Do)op; // 연산자를 Do 타입으로 캐스팅합니다.
        if (doXobj != null)
        {
            // 이미지를 위한 새로운 BDC를 생성하고 페이지 내용에 삽입합니다.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // 현재 연산자 앞에 삽입합니다.
            i++; // 삽입된 BDC를 고려하여 인덱스를 증가시킵니다.
            page.getContents().insert(i + 1, new EMC()); // EMC (End Mark Content)를 삽입합니다.
            i++; // 인덱스를 다시 증가시킵니다.
        }
    }

    // 연산자가 TextShowOperator (텍스트 디스플레이)의 인스턴스인지 확인합니다.
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // 연산자를 TextShowOperator 타입으로 캐스팅합니다.
        if (tx != null)
        {
            // 특정 텍스트 콘텐츠를 확인하고 해당 BDC를 삽입합니다.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // 현재 연산자 앞에 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
                page.getContents().insert(i + 1, new EMC()); // EMC를 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // 현재 연산자 앞에 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
                page.getContents().insert(i + 1, new EMC()); // EMC를 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // 현재 연산자 앞에 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
                page.getContents().insert(i + 1, new EMC()); // EMC를 삽입합니다.
                i++; // 인덱스를 증가시킵니다.
            }
        }
    }
}
 
    // 문서에서 태그가 지정된 콘텐츠를 가져옵니다.
    ITaggedContent tagged = document.getTaggedContent();

    // 태그가 지정된 콘텐츠를 처리하여 구조 속성을 수정합니다.
    // 태그가 지정된 콘텐츠의 루트 요소에서 첫 번째 자식 요소를 가져옵니다.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // 기존 자식 요소를 지웁니다.

    // helloBdc에 부모 구조 요소를 태그로 지정합니다.
    MCRElement mcr = p.tag(helloBdc);

    // 태그가 지정된 요소에 대한 구조 속성을 생성하고 설정합니다.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // SpaceAfter 속성을 설정합니다.
    attrs.setAttribute(attr); // 구조에 속성을 적용합니다.

    // 태그가 지정된 콘텐츠에 새로운 FigureElement를 생성합니다.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // 두 번째 위치에 도형 요소를 삽입합니다.
    figure.setAlternativeText("A fly."); // 도형에 대한 대체 텍스트를 설정합니다.

    // imageBdc에 도형 요소를 태그로 지정합니다.
    MCRElement mcr = figure.tag(imageBdc);

    // 지정된 MCR (Marked Content Reference)의 부모 구조 요소를 가져옵니다.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 요소 뒤의 공백에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // 요소 뒤의 공백 값을 3.625 단위로 설정합니다.
    attrs.setAttribute(spaceAfter); // 구조 속성에 요소 뒤 공백 속성을 할당합니다.

    // 경계 상자 (BBox)에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // 구조 속성에 대한 경계 상자 값을 설정합니다.
    attrs.setAttribute(bbox); // 구조 속성에 경계 상자 속성을 할당합니다.

    // 배치에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // 배치 유형을 블록으로 설정합니다.
    attrs.setAttribute(placement); // 구조 속성에 배치 속성을 할당합니다.

    // 태그 구조의 루트 요소에서 네 번째 자식 요소를 가져옵니다.
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // p2에서 기존 자식 요소를 지웁니다.

    // p2에 추가할 새로운 SpanElement를 생성합니다.
    SpanElement span1 = tagged.createSpanElement();

    // 스팬 요소에 대한 구조 속성을 생성합니다.
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 텍스트 장식 유형에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // 텍스트 장식을 밑줄로 설정합니다.
    attrs.setAttribute(textDecorationType); // 구조 속성에 텍스트 장식 유형 속성을 할당합니다.

    // 텍스트 장식 두께에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // 텍스트 장식의 두께를 0으로 설정합니다.
    attrs.setAttribute(textDecorationThickness); // 구조 속성에 텍스트 장식 두께 속성을 할당합니다.

    // 텍스트 장식 색상에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // 텍스트 장식의 RGB 색상 값을 설정합니다.
    attrs.setAttribute(textDecorationColor); // 구조 속성에 텍스트 장식 색상 속성을 할당합니다.

    p2.appendChild(span1); // span1 요소를 p2에 첨부합니다.


    // 새로운 MCR 요소를 생성하고 pBdc로 태그를 지정합니다.
    MCRElement mcr = p2.tag(pBdc);
    // MCR의 부모 구조 요소를 가져오고 레이아웃 속성을 생성합니다.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 텍스트 정렬에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // 텍스트 정렬을 가운데로 설정합니다.
    attrs.setAttribute(textAlign); // 구조 속성에 텍스트 정렬 속성을 할당합니다.

    // 요소 뒤의 공백에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // 요소 뒤의 공백 값을 21.75 단위로 설정합니다.
    attrs.setAttribute(spaceAfter); // 구조 속성에 요소 뒤 공백 속성을 할당합니다.


    // p2에 추가할 새로운 SpanElement를 생성합니다.
    SpanElement span2 = tagged.createSpanElement();

    // 스팬 요소에 대한 구조 속성을 생성합니다.
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 텍스트 장식 유형에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // 텍스트 장식을 밑줄로 설정합니다.
    attrs.setAttribute(textDecorationType); // 구조 속성에 텍스트 장식 유형 속성을 할당합니다.

    // 지정된 키를 사용하여 텍스트 장식 색상에 대한 새로운 StructureAttribute를 생성합니다.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // 텍스트 장식 색상 속성에 대한 배열 숫자 값을 설정합니다.
    // 색상은 각 값이 Double인 RGB 값의 배열로 표현됩니다.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // 빨간색 구성 요소
    new Double[] { (0.384308) },  // 초록색 구성 요소
    new Double[] { (0.756866) }   // 파란색 구성 요소
    });

    // 텍스트 장식 색상 속성을 attrs 객체에 설정합니다.
    attrs.setAttribute(textDecorationColor);

    // 부모 요소 p2에 자식 스팬 요소를 첨부합니다.
    p2.appendChild(span2);

    // 두 번째 링크에 대한 새로운 LinkElement 인스턴스를 생성합니다.
    LinkElement link2 = tagged.createLinkElement();

    // 무작위로 생성된 UUID를 사용하여 링크 요소에 고유 ID를 할당합니다.
    link2.setId(UUID.randomUUID().toString());

    // link2 요소를 span2의 자식으로 첨부합니다.
    span2.appendChild(link2);

    // 페이지의 주석에서 해당 주석으로 link2 요소에 태그를 지정합니다.
    link2.tag(page.getAnnotations().get_Item(1));

    // link2 요소에 추가 메타데이터 또는 컨텍스트 (link2Bdc)를 태그로 지정합니다.
    link2.tag(link2Bdc);

    // 첫 번째 링크에 대한 또 다른 LinkElement 인스턴스를 생성합니다.
    LinkElement link1 = tagged.createLinkElement();

    // 무작위로 생성된 UUID를 사용하여 link1 요소에 고유 ID를 할당합니다.
    link1.setId(UUID.randomUUID().toString());

    // link1 요소를 span1의 자식으로 첨부합니다.
    span1.appendChild(link1);

    // 페이지의 주석에서 해당 주석으로 link1 요소에 태그를 지정합니다.
    link1.tag(page.getAnnotations().get_Item(2));

    // link1 요소에 추가 메타데이터 또는 컨텍스트 (link1Bdc)를 태그로 지정합니다.
    link1.tag(link1Bdc);

    // 태그가 지정된 문서의 루트 요소에서 첫 번째 자식 요소를 제거합니다.
    tagged.getRootElement().removeChild(0);

    // 지정된 출력 디렉토리에 "_out.pdf"라는 파일명으로 문서를 저장합니다.
    document.save(dataDir + "_out.pdf");

```


## Aspose.PDF 24.6의 새로운 기능

24.6부터 Aspose.PDF for Java는 java.security.cert.X509Certificate, java.security.PrivateKey로 PDF를 서명할 수 있습니다:

이 코드는 인증서 저장소에서 인증서와 개인 키를 검색한 다음 이를 사용하여 PDF 문서의 첫 페이지에 디지털 서명을 적용합니다.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Aspose.PDF 24.5의 새로운 기능

25.4 릴리스 이후, 양식 편집기 플러그인이 구현되었습니다.

**양식 편집기를 사용하여 PDF에서 양식 편집하는 방법**

- 라이선스 키 설정
- PDF 양식을 조작하기 위한 메서드를 제공하는 FormEditor 클래스의 인스턴스를 생성합니다.
- PDF 문서에 양식 필드를 추가하기 위한 옵션을 지정하는 FormEditorAddOptions 클래스의 인스턴스를 생성합니다.
- 파일 경로나 스트림을 나타내는 FileDataSource 클래스를 사용하여 FormEditorAddOptions 객체에 입력 파일 소스와 출력 파일 소스를 추가합니다.
- FormEditor 객체의 Process 메서드를 호출하고 FormEditorAddOptions 객체를 매개변수로 전달합니다.
- ResultContainer.resultCollection을 사용하여 결과에 액세스합니다.

```java

    // PDF 파일의 입력 및 출력 경로를 지정합니다.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // FormEditor 플러그인의 인스턴스를 생성합니다.
    FormEditor pdfFormPlugin = new FormEditor();

    // 양식 필드를 추가하기 위한 옵션을 생성합니다.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // 텍스트 박스 양식 필드를 생성합니다.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // 콤보 박스 양식 필드를 생성합니다.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // 체크박스 양식 필드를 생성합니다.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // 체크박스 양식 필드를 생성합니다.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // 체크박스 양식 필드를 생성합니다.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // 옵션에 입력 및 출력 파일을 추가합니다.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // 플러그인을 사용하여 양식 필드를 처리합니다.
    ResultContainer results = pdfFormPlugin.process(opt);
```


이 릴리스는 PDF 레이어와 작업할 수 있도록 합니다. 예를 들어:

- PDF 레이어 잠금
- PDF 레이어 요소 추출
- 레이어가 있는 PDF 평탄화
- PDF 내부의 모든 레이어를 하나로 병합

**PDF 레이어 잠금**

24.5 릴리스 이후로, 특정 페이지의 첫 번째 페이지에서 특정 레이어를 열고 잠근 후 변경 사항을 저장할 수 있습니다. 두 가지 새로운 메서드와 하나의 속성이 추가되었습니다:

Layer.Lock(); - 레이어를 잠급니다.
Layer.Unlock(); - 레이어 잠금을 해제합니다.
Layer.Locked; - 레이어 잠금 상태를 나타내는 속성입니다.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**PDF 레이어 요소 추출**

Aspose.PDF for Java 라이브러리는 첫 페이지에서 각 레이어를 추출하고 각 레이어를 별도의 파일로 저장할 수 있게 합니다.

레이어에서 새 PDF를 생성하기 위해, 다음 코드 스니펫을 사용할 수 있습니다:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**레이어가 있는 PDF 평탄화**

Aspose.PDF for Java 라이브러리는 PDF를 열고 첫 페이지의 각 레이어를 반복하며 각 레이어를 평탄화하여 페이지에 영구적으로 만듭니다.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

Layer.flatten(boolean cleanupContentStream) 메서드는 콘텐츠 스트림에서 선택적 콘텐츠 그룹 마커를 제거할지를 지정하는 boolean 매개변수를 받습니다. cleanupContentStream 매개변수를 false로 설정하면 평탄화 프로세스가 빨라집니다.

**PDF 내부의 모든 레이어를 하나로 병합**

Aspose.PDF for Java 라이브러리는 모든 PDF 레이어 또는 첫 페이지의 특정 레이어를 새 레이어로 병합하고 업데이트된 문서를 저장할 수 있습니다.

페이지의 모든 레이어를 병합하기 위해 두 가지 메서드가 추가되었습니다:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

두 번째 매개변수는 선택적 콘텐츠 그룹 마커의 이름을 바꿀 수 있습니다. 기본값은 "oc1" (/OC /oc1 BDC)입니다.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // 또는 page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Aspose.PDF 24.4의 새로운 기능

이번 릴리스에는 PDF용 Java 플러그인이 도입되었습니다:

- 폼 플래트너 플러그인

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // 결과 확인.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- 폼 익스포터

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // 플러그인 사용.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // 결과 확인.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- 병합 플러그인

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- 최적화 플러그인

PDF 문서의 크기를 어떻게 줄일 수 있습니까?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

PDF 문서의 크기를 어떻게 조정할 수 있습니까?

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


PDF 문서를 회전하는 방법?

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Aspose.PDF 24.3의 새로운 기능

24.3부터 TextFragmentAbsorber에서 문구 목록을 통한 검색을 구현합니다.

```java

    String[] expressions = new String[] {
      // 전화번호 감지
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      // 카드 번호 감지
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


다음 기능은 PDF를 Markdown 변환기로 변환할 때 테이블을 변환하는 기능을 추가하는 것입니다.

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Aspose.PDF 24.2의 새로운 기능

24.2 버전부터 AcroForms를 사용하여 PDF에 워터마크를 추가할 수 있습니다. TextStamp는 AcroForm 파일과 함께 사용하기에 적합합니다. XFA 파일에 TextStamp를 사용하면, 텍스트가 일반 PDF 파일처럼 페이지에 그려집니다 (예를 들어, XFA 파일을 읽을 수 없는 Chrome 브라우저와 같은 PDF 뷰어에서 볼 수 있습니다). XFA 파일에 텍스트를 추가하려면 XFA 파일의 내부 XML에서 변경해야 합니다.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


상태 모델 설정을 위한 주석
MarkupAnnotation 클래스의 setReviewState 및 setMarkedState를 사용하여 필요한 상태를 설정할 수 있습니다.
모든 마크업 주석에는 상태 설정 옵션이 제공됩니다.

```java

    // 소스 PDF 문서 열기
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // 주석 생성
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    // 주석 제목 설정
    textAnnotation.setTitle("샘플 주석 제목");

    // 주석 주제 설정
    textAnnotation.setSubject("샘플 주제");
    // 주석 내용 지정
    textAnnotation.setContents("주석에 대한 샘플 내용");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    // 페이지의 주석 컬렉션에 주석 추가
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    // 출력 파일 저장
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


24.2부터 OFD를 PDF로 변환 구현:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Aspose.PDF 24.1의 새로운 기능

24.1 릴리스부터 PDF를 Markdown으로 변환 구현:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

또한, 24.1에서는 InterruptMonitor를 사용한 스레드 중단이 구현되었습니다.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");

          //foreach to while statements conversion
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("text");
          row2.getCells().add("text");
          row2.getCells().add("text");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("text");
          row2.getCells().add("text");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interrupting the save thread at " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Process is started thread at " + System.currentTimeMillis());

    // The timeout should be less than the time required for full document save (without interruption).
    Thread.sleep(500);

    // Interrupt the process
    monitor.interrupt();

    System.out.println("Interrupted the save thread at " + System.currentTimeMillis());
```


## Aspose.PDF 23.12의 새로운 기능

다음 코드 스니펫을 사용하여 양식을 찾고 텍스트를 교체할 수 있습니다:

```java

    Document document = new Document(input);
    String expectedText = "This is a text added while creating new PDF in Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```

또는, 양식을 완전히 제거할 수 있습니다:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    // foreach를 while 문으로 변환
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


폼을 제거하는 또 다른 방법:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- 다음 코드 스니펫을 사용하여 모든 폼을 삭제할 수 있습니다:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Aspose.PDF 23.11의 새로운 기능

이 릴리스부터 PDF 파일에서 숨겨진 텍스트를 제거할 수 있습니다:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // foreach를 while 문으로 변환
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Aspose.PDF 23.10의 새로운 기능

현재 업데이트에서는 태그가 지정된 PDF에서 태그를 제거하는 세 가지 버전을 제공합니다.

- documentElement(루트 트리 요소)에서 일부 노드 요소 제거:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // structElement 자체를 삭제할 수도 있습니다.
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- 문서에서 모든 마크된 요소 태그 제거, 구조 요소는 유지:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- 모든 태그 제거:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

우리는 문자 높이를 측정하는 새로운 기능을 구현했습니다. 다음 코드를 사용하여 문자의 높이를 측정하세요:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

측정은 문서에 포함된 글꼴을 기반으로 한다는 점에 유의하세요. 치수에 대한 정보가 누락된 경우 이 메서드는 0을 반환합니다.

## Aspose.PDF 23.9의 새로운 기능

23.9부터 채우기 가능한 필드에서 자식 주석을 제거하는 지원.

예제 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "option 1";
    String option2 = "option 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: 사용 중*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // 첫 번째 체크박스 그룹 옵션 값을 설정합니다
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


이미지를 ImageFilterType.Flate로 추가하면 투명성이 유지되지 않습니다.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Aspose.PDF 23.8의 새로운 기능

The function for detecting Incremental Updates in a PDF document has been added in 23.8. This function returns 'true' where document was saved with incremental updates, otherwise, it returns 'false'.

PDF 문서에서 증분 업데이트를 감지하는 기능이 23.8에 추가되었습니다. 이 기능은 문서가 증분 업데이트로 저장된 경우 'true'를 반환하고, 그렇지 않으면 'false'를 반환합니다.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

One more feature is Copy OutputIntents from input PDF to destination PDF

또 하나의 기능은 입력 PDF에서 대상 PDF로 OutputIntents를 복사하는 것입니다.

We add a new public property Document.getOutputIntents() to allow access to output intents in a document. For a time being only the usage of already existing in some document output intents is supported, user can't create OutputIntent from scratch.

문서의 출력 의도에 접근할 수 있도록 새로운 공용 프로퍼티 Document.getOutputIntents()를 추가했습니다. 현재로서는 이미 존재하는 문서의 출력 의도만 사용할 수 있으며, 사용자가 처음부터 OutputIntent를 생성할 수는 없습니다.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


Aspose.PDF 23.8부터 도형 추출 추가 지원:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // foreach를 while 문으로 변환
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // 페이지 크기가 원본 PDF와 다르기 때문에 새 위치를 다시 계산
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


문자열 추가 시 오버플로우를 감지하는 기능도 지원합니다:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Aspose.PDF 23.7의 새로운 기능

23.7 버전부터 인쇄 대화 상자 프리셋 페이지 축척을 지원합니다:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Aspose.PDF 23.6의 새로운 기능

23.6 버전부터 HTML, Epub 페이지의 제목을 설정할 수 있는 기능을 추가로 지원합니다.

HTML 코드:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


EPUB을 위한 코드:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

23.6부터 벡터 그래픽의 위치를 지정할 수 있는 API 지원:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Aspose.PDF 23.1의 새로운 기능

23.1 버전부터 PrinterMark 주석 생성을 지원합니다. 주석 변형 중 하나인 ColorBarAnnotation이 추가되었습니다.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Aspose.PDF 22.12의 새로운 기능

이번 릴리스부터 PDF를 DICOM 이미지로 변환하는 기능을 지원합니다:

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Aspose.PDF 22.9의 새로운 기능

22.09부터 서명에 주제 루브릭의 순서를 수정하는 속성을 추가하는 것을 지원합니다 (E=, CN=, O=, OU=, ).

```java

    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Aspose.PDF 22.8의 새로운 기능

Aspose.PDF 23.8부터 xref 테이블을 재구성하기 위한 메서드 추가 지원:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```


## Aspose.PDF 22.6의 새로운 기능

PDF를 PDF_A_1A로 변환할 때 큰 출력 파일 크기를 피하기 위해 투명 색상을 제거하는 옵션을 구현했습니다.

버전 22.5부터 고객은 변환된 투명도의 품질을 제어하고 결과적으로 출력 파일 크기를 제어할 수 있습니다:

```java
    opts.setTransparencyResolution(300);
```

## Aspose.PDF 22.5의 새로운 기능

PDF/A 변환 시 투명한 콘텐츠가 제거되고 이미지로 대체됩니다.
새로운 기능을 구현하여 이제 고객이 TransparencyResolution 매개변수를 사용하여 이미지의 품질을 제어할 수 있습니다:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Aspose.PDF 22.4의 새로운 기능

이 릴리스에는 Aspose.PDF for Java에 대한 정보가 포함되어 있습니다:

- PDF를 ODS로: 아래 첨자 및 위 첨자에서 텍스트 인식;

**예제**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF를 XMLSpreadSheet2003로: 아래 첨자 및 위 첨자에서 텍스트 인식;

- PDF를 Excel로: 아래 첨자 및 위 첨자에서 텍스트 인식;

## Aspose.PDF 22.3의 새로운 기능

PDF를 ODS로: RTL 지원이 버전 22.3에서 가능합니다

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Aspose.PDF 22.2의 새로운 기능

이 릴리스에는 PDF를 XSLX로 변환하는 기능이 포함되어 있습니다: RTL (히브리어, 아랍어) 지원.

## Aspose.PDF 22.1의 새로운 기능

Aspose.PDF for Java는 문서 로딩을 허용합니다. Portable Document Format (PDF) 버전 2.0.

## Aspose.PDF 21.10의 새로운 기능

### 숨겨진 텍스트를 감지하는 방법?

다음 코드를 사용하세요:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Aspose.PDF 21.8의 새로운 기능

### 디지털 서명에서 텍스트 색상을 변경하는 방법?

21.8 버전에서는 setForegroundColor를 사용하여 디지털 서명의 텍스트 색상을 변경할 수 있습니다:

```java
다음 코드를 사용하세요:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    // 서명 위치를 위한 사각형 생성
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
// 텍스트 색상 설정
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // PDF 파일에 서명
                    pdfSign.sign(1, true, rect, pkcs);
                    // 출력 PDF 파일 저장
                    pdfSign.save(outFile);
```

## Aspose.PDF 21.6의 새로운 기능

### 문서에서 ImagePlacementAbsorber를 사용하여 이미지 숨기기

Aspose.PDF for Java를 사용하여 문서에서 ImagePlacementAbsorber를 사용하여 이미지를 숨길 수 있습니다:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Aspose.PDF 21.5의 새로운 기능

### 이미지 병합을 위한 API 추가

Aspose.PDF 21.4는 이미지를 결합할 수 있게 해줍니다. 이미지 스트림 목록을 하나의 이미지 스트림으로 병합합니다. 지원되지 않는 형식을 사용할 경우 기본적으로 Jpeg로 인코딩되는 Png/jpg/tiff 출력 형식이 지원됩니다. 다음 코드 스니펫을 따르세요:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


문서를 Tiff 형식으로 병합할 수도 있습니다:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Aspose.PDF 21.02의 새로운 기능

Aspose.PDF v21.02 PAdES LTV 서명으로 PDF 서명

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //PAdES LTV 서명으로 PDF 서명
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```