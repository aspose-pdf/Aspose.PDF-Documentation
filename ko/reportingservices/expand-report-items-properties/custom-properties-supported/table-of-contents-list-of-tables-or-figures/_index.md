---
title: 목차 표 또는 그림 목록
linktitle: 목차 표 또는 그림 목록
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에 목차, 표 목록 또는 그림을 추가하는 방법을 알아보세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 디자이너는 보고서 문서에 대한 목차 추가를 지원하지 않습니다. Reporting Services용 Aspose.PDF를 사용하면 목차, 표 또는 그림 목록이 포함된 PDF 문서를 생성하도록 PDF 렌더링에 쉽게 지시할 수 있습니다. 다음 단계에 따라 수행할 수 있습니다.

{{% /alert %}}

Aspose.Pdf.ListSectionStyle.xml 파일이 ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin 디렉터리에 있는지 확인하고 그 안에 다음 마크업을 배치합니다.

## 목차

### 예

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

##  테이블 목록

### 예

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## 그림 목록

### 예

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Aspose.Pdf 온라인 문서의 'Working with TOC' 섹션을 참조하세요.

**2-** 보고서 매개변수 `IsListSectionSupported`을 추가하고 `List Section` 단락에 표시된 대로 값을 True로 설정합니다.
**3-** 목차, 표 또는 그림 목록에 나열하려는 보고서 항목에 대한 사용자 정의 속성을 추가합니다.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

현재 보고서 항목을 목차나 표 또는 그림 목록의 색인별로 나열하여 표시합니다.

```text
Custom Property Name: Title
Custom Property Type: String
```

목차, 표 또는 그림 목록에 표시되는 항목 제목입니다.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

목차에 표시되는 나열된 항목의 수준입니다.
