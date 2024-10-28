---
title: 목차 목록 또는 표 목록
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 디자이너는 보고서 문서에 대한 목차 추가를 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 PDF 렌더러가 목차 또는 표 또는 그림 목록이 있는 PDF 문서를 쉽게 생성하도록 지시할 수 있습니다. 다음 단계에서 수행할 수 있습니다:

{{% /alert %}}

{{% alert color="primary" %}}
Aspose.Pdf.ListSectionStyle.xml 파일이 ```<Instance>```/bin에 있는지 확인하세요. 여기서 ```<Instance>```는 보고서 서버의 디렉토리입니다. 파일이 없으면 ```<Instance>```/bin 디렉토리에 파일을 생성하고 다음 마크업을 내부에 배치하세요.

## 목차

**예제**

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

## 테이블 목록

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

Aspose.Pdf 온라인 문서의 'TOC 작업' 섹션을 참조하십시오.

**2-** 보고서 매개변수 'IsListSectionSupported'를 추가하고 'List Section' 단락에 표시된 대로 값을 True로 설정합니다.
**3-** 목차, 테이블 목록 또는 그림 목록에 나열하고자 하는 보고서 항목에 대한 사용자 정의 속성을 추가합니다.

{{% /alert %}}

{{% alert color="primary" %}}

**사용자 정의 속성 이름** :IsInList
**속성 값** :Boolean
**사용자 정의 속성 값** : True 또는 False

{{% alert color="primary" %}}

현재 보고서 항목을 목차, 테이블 목록 또는 그림 목록의 인덱스로 나열된 것으로 표시합니다.

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

목차, 표 목록 또는 그림 목록에 표시되는 항목 제목.
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

목차에 표시되는 항목의 수준.

{{% /alert %}}

{{% /alert %}}