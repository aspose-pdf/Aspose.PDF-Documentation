---
title: 워크플로 활동을 통해 파일을 PDF로 변환하기
linktitle: 워크플로 활동을 통해 파일을 PDF로 변환하기
type: docs
weight: 50
url: /ko/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: PDF SharePoint API는 문서를 PDF로 변환하는 SharePoint 워크플로에서 사용할 수 있습니다.
---

{{% alert color="primary" %}}

워크플로에 대한 지원은 Microsoft Office SharePoint Server의 핵심 기능입니다. 워크플로는 비즈니스 로직에 따라 문서의 이동을 자동화하고 문서 조직의 비용과 시간을 효율화하는 데 도움을 줍니다. 이 문서에서는 Aspose.PDF for SharePoint를 사용하여 문서를 PDF로 변환하는 워크플로를 구현하는 방법을 보여줍니다.

{{% /alert %}}
## **워크플로 설정**

이 예제는 문서 라이브러리의 새 항목을 PDF 형식으로 변환하고 다른 문서 라이브러리에 저장하는 워크플로를 생성합니다. 예제에서는 **Personal Documents** 라이브러리를 소스 라이브러리로, **Shared Documents** 라이브러리의 **Pdf** 하위 폴더를 대상 라이브러리로 사용합니다.

Aspose.PDF for SharePoint는 HTML, 텍스트 및 이미지 파일 변환을 지원합니다.

### **SharePoint Designer를 사용하여 워크플로우 설계**

1. **SharePoint Designer**를 열고 워크플로우가 구현될 사이트에 연결합니다.
1. 사이트 개체에서 **Workflows**를 선택하고 **List Workflow**를 엽니다.
1. **Personal Documents** 라이브러리를 선택하여 문서 라이브러리에 새 목록 워크플로우를 만들고 첨부합니다.

   **메뉴에서 Personal Documents 선택**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. 워크플로우 이름과 설명을 입력하여 **Personal Documents** 라이브러리에 목록 워크플로우를 만들고 첨부합니다.
1. 이 단계를 완료하려면 **OK**를 클릭하십시오.

   **리스트 워크플로우 생성**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



워크플로우 단계 편집기가 나타납니다. 이는 워크플로우의 조건 및 작업을 정의하는 데 사용됩니다. 이제 **Aspose Actions**에서 조건 없이 새 문서를 PDF로 변환하는 작업을 추가합니다.

1. **Action** 메뉴에서 **Convert file to PDF via Aspose.PDF** 작업을 선택합니다.

   **작업 선택**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. 작업 매개변수를 구성합니다:
   1. 목적지 폴더에 **이 폴더** 매개변수를 설정합니다.
   1. 다른 작업 매개변수는 기본값으로 두거나 작업 속성 창을 사용하여 설정합니다. **Overwrite** 매개변수의 기본값은 false입니다.

      **워크플로우 편집기**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**대상 라이브러리 설정**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**속성 설정**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. **Workflow** 메뉴에서 **Workflow Settings**를 선택합니다.
1. 새 항목이 생성될 때 **워크플로우 자동 시작**을 선택하고 **시작 옵션**에서 다른 옵션을 모두 해제합니다.

   **시작 옵션 설정**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



워크플로우 설계가 완료되었습니다.

1. 워크플로우를 저장하고 게시하여 SharePoint 사이트에 적용합니다.

### **워크플로우 테스트**

워크플로우를 테스트하려면:

1. SharePoint 사이트를 열고 **Personal Documents** 문서 라이브러리에 새 문서를 업로드합니다.
   Aspose.PDF for SharePoint는 HTML 파일, 텍스트 파일 및 이미지(JPG, PNG, GIF, TIFF 및 BMP*)를 PDF로 변환하는 것을 지원합니다. 워크플로는 새 항목이 생성될 때 자동으로 시작되도록 구성되어 있어 파일이 자동으로 처리됩니다.
1. 브라우저를 새로 고칩니다.
   워크플로 상태는 워크플로 열에 표시되며, 이 경우 **Aspose.PDF Workflow** 입니다.

   **소스 라이브러리에 문서 추가**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. 변환된 문서를 보려면 대상 문서 라이브러리를 엽니다. **Shared Documents/Pdf**는 이 예시의 경로입니다.

   **대상 라이브러리**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

