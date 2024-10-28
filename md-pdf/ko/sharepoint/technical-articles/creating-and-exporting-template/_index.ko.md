---
title: 템플릿 만들기 및 내보내기
type: docs
weight: 10
url: /sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: PDF SharePoint API를 사용하여 SharePoint에서 템플릿을 만들고 PDF로 내보낼 수 있습니다.
---

{{% alert color="primary" %}}

이 문서에서는 Aspose.PDF for SharePoint를 사용하여 템플릿을 만들고 내보내는 방법을 보여줍니다.

Aspose.PDF for SharePoint 1.9.2부터 PDF 템플릿 지원은 SharePoint 하위 사이트도 포함합니다.

{{% /alert %}}

## **템플릿 만들기 및 내보내기**
{{% alert color="primary" %}}

Aspose.PDF for SharePoint 내보내기 기능을 사용하려면 먼저 "PDF 템플릿"을 사용하는 목록을 만들어야 합니다.

PDF 템플릿을 사용하는 목록 만들기:

![todo:image_alt_text](creating-and-exporting-template_1.png)

두 개의 문서 템플릿, 작업 양식 템플릿 및 작업 목록 템플릿이 생성됩니다:

![todo:image_alt_text](creating-and-exporting-template_2.png)

템플릿 양식을 통해 다음 정보를 입력할 수 있습니다:

- **Name**: 템플릿의 파일 이름.
- **Title**: 템플릿의 제목.
  (기본적으로 파일 이름과 동일합니다.)
- **설명**: 템플릿에 대한 설명. 좋은 설명은 템플릿을 사용하기 쉽게 만듭니다.
- **할당된 목록 유형**: 쉼표로 구분된 목록 ID (템플릿과 관련됨. 이 필드는 **AllListTypes** 값을 포함할 수 있습니다. 이 필드는 **Type** 필드가 **List**로 설정된 경우에만 적용됩니다).
- **할당된 콘텐츠 유형**: 쉼표로 구분된 콘텐츠 유형 ID (템플릿과 관련됨. 이 필드는 **AllListTypes**로 설정될 수 있습니다. 이 필드는 **Type** 필드가 **Item**으로 설정된 경우에만 적용됩니다).
- **유형**: 목록 템플릿 또는 항목 템플릿 중 하나.
- **상태**: 옵션은 활성, 비활성 (모두에게 보이지 않음), 디버깅 (관리자에게만 보임)입니다.

**작업 목록 템플릿 양식:**

![todo:image_alt_text](creating-and-exporting-template_3.png)

**작업 양식 템플릿 양식:**

![todo:image_alt_text](creating-and-exporting-template_4.png)

저장되면 새 템플릿은 템플릿 목록에 나타나 사용 준비가 됩니다:

**두 개의 작업 목록 템플릿:**
![todo:image_alt_text](creating-and-exporting-template_5.png)



**작업 양식 템플릿:**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **템플릿 개발**
템플릿은 Aspose XML PDF에 기반한 XML 파일입니다. 목록을 위한 템플릿을 만들기 위해, SharePoint 목표 콘텐츠 유형 필드의 내부 이름과 관련된 특별한 마커를 XML PDF 파일에 배치하십시오.
##### **마커**
- **SPListItemsCount** – 목록 항목의 수로 대체됩니다.
- **SPListTitle** – 목록 제목으로 대체됩니다.
- **SPTableIterator** – 첫 번째 테이블 셀에 배치되고 전체 반복을 위한 테이블을 표시합니다.
- **SPRowIterator** – 첫 번째 테이블 셀에 배치되고 행 반복을 위한 테이블을 표시합니다.
- **SPField** – 항목 필드의 값으로 대체됩니다.

참고를 위해, [템플릿 XML 파일](attachments/8421394/8618082.zip)을 다운로드하십시오.
#### **PDF로 내보내기**
템플릿이 완전히 구성되면, 목록이나 항목을 PDF 파일로 내보낼 준비가 된 것입니다.

**작업 목록 템플릿을 사용하여 목록을 PDF로 내보내기:**


![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}