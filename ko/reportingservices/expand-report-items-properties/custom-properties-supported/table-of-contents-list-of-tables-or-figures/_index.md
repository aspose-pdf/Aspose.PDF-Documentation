---
title: 목차, 표 목록 또는 그림
linktitle: 목차, 표 목록 또는 그림
type: docs
weight: 10
url: /ko/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에 목차, 표 목록 또는 그림을 추가하는 방법을 알아보세요.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer는 보고서 문서에 목차를 추가하는 것을 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 PDF 렌더에 목차 또는 표 목록, 그림이 포함된 PDF 문서를 생성하도록 쉽게 지시할 수 있습니다. 다음 단계에 따라 수행할 수 있습니다:

{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Pdf.ListSectionStyle.xml 파일이 존재하는지 확인하세요 ```<Instance>```/bin, 어디에 ```<Instance>``` 은(는) Report Server의 디렉터리입니다. 파일이 존재하지 않으면 해당 디렉터리에 생성하십시오. ```<Instance>```/bin 디렉터리 안에 다음 마크업을 넣으세요.

## 목차

**예시**

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

##  표 목록

**예시**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## 그림 목록

**예시**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Please refer to 'Working with TOC' section of the Aspose.Pdf online documentation.

**2-** 보고서 매개변수 'IsListSectionSupported'를 추가하고 'List Section' 단락에 표시된 대로 값을 True로 설정하십시오.
**3-** 목차, 표 목록 또는 그림에 나열하려는 보고서 항목에 대한 사용자 지정 속성을 추가하십시오.

{{% /alert %}}

{{% alert color="primary" %}}

**사용자 지정 속성 이름** :IsInList
**속성 값** :Boolean
**사용자 지정 속성 값** : True 또는 False

{{% alert color="primary" %}}

현재 보고서 항목을 목차, 표 목록 또는 그림 목록에서 인덱스로 표시합니다.

{{% /alert %}}

**사용자 정의 속성 이름** : 제목
**사용자 정의 속성 유형** : 문자열

{{% alert color="primary" %}}

목차, 표 또는 그림 목록에 표시되는 항목 제목입니다.
{{% /alert %}}

**사용자 정의 속성 이름** : 목록 수준
**맞춤 속성 유형** : 정수

{{% alert color="primary" %}}

목차에 표시되는 항목들의 수준입니다.

{{% /alert %}}

{{% /alert %}}


