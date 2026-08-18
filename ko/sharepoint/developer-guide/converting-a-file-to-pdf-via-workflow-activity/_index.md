---
title: 워크플로우 활동을 통한 파일을 PDF로 변환
linktitle: 워크플로우 활동을 통한 파일을 PDF로 변환
type: docs
weight: 50
url: /ko/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-08-10"
description: PDF SharePoint API는 문서를 PDF로 변환하는 SharePoint 워크플로우에서 사용할 수 있습니다.
---

{{% alert color="primary" %}}

워크플로우 지원은 Microsoft Office SharePoint Server의 핵심 기능입니다. 워크플로우는 비즈니스 논리에 따라 문서 이동을 자동화하고 문서 조직의 비용과 시간을 효율화하는 데 도움이 됩니다. 이 문서에서는 문서를 PDF로 변환하는 워크플로우에서 Aspose.PDF for SharePoint를 사용하는 방법을 보여줍니다.

{{% /alert %}}

## 워크플로우 설정

이 예제는 문서 라이브러리의 새 항목을 PDF 형식으로 변환하고 다른 문서 라이브러리에 저장하는 워크플로우를 생성합니다. 예제는 **Personal Documents** 라이브러리를 소스 라이브러리로 사용하고 **Shared Documents** 라이브러리의 **Pdf** 하위 폴더를 대상 라이브러리로 사용합니다.

Aspose.PDF for SharePoint는 HTML, 텍스트 및 이미지 파일의 변환을 지원합니다.

### SharePoint Designer를 사용하여 워크플로우를 설계합니다

1. **SharePoint Designer**를 열고 워크플로우가 구현될 사이트에 연결합니다.
1. **site objects**에서 **Workflows**를 선택한 다음 **List Workflow**를 엽니다.
1. 문서 라이브러리에 새 목록 워크플로우를 생성하고 연결하려면 **Personal Documents** 라이브러리를 선택합니다.

   **메뉴에서 개인 문서 선택**

![Workflow Activity_1을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. 워크플로 이름과 설명을 입력하여 **Personal Documents** 라이브러리에 목록 워크플로를 생성하고 연결합니다.
1. 이 단계를 완료하려면 **OK**를 클릭합니다.

   **목록 워크플로 생성**

![Workflow Activity_2을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_2.png)

워크플로 단계 편집기가 표시됩니다. 이것은 워크플로의 조건 및 작업을 정의하는 데 사용됩니다. 이제 **Aspose Actions**에서 조건 없이 새 문서를 PDF로 변환하는 작업을 추가합니다.

1. **Action** 메뉴에서 **Convert file to PDF via Aspose.PDF** 작업을 선택합니다.

   **작업 선택**

![Workflow Activity_3를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. 작업 매개변수를 구성합니다:
   1. **this folder** 매개변수를 대상 폴더로 설정합니다.
   1. 다른 작업 매개변수는 기본값으로 두거나 작업 속성 창을 사용하여 설정하십시오. **Overwrite** 매개변수의 기본값은 false입니다.

      **워크플로 편집기**

![Workflow Activity_4를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_4.png)

**대상 라이브러리 설정**

![Workflow Activity_5를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_5.png)

**속성 설정**

![Workflow Activity_6를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. **Workflow** 메뉴에서 **Workflow Settings**를 선택합니다.
1. **start workflow automatically when a new item created**를 선택하고 **Start Options**에서 다른 옵션을 지웁니다.

   **시작 옵션 설정**

![Workflow Activity_7를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_7.png)

워크플로우 설계가 완료되었습니다.

1. 워크플로를 저장하고 게시하여 SharePoint 사이트에 구현합니다.

### 워크플로 테스트

워크플로를 테스트하려면:

1. SharePoint 사이트를 열고 **Personal Documents** 문서 라이브러리에 새 문서를 업로드합니다.
   Aspose.PDF for SharePoint는 HTML 파일, 텍스트 파일 및 이미지(JPG, PNG, GIF, TIFF 및 BMP*)를 PDF로 변환하는 것을 지원합니다. 워크플로는 새 항목이 생성될 때 자동으로 시작되도록 구성되어 있으므로 파일이 자동으로 처리됩니다.
1. 브라우저를 새로고침합니다.
   워크플로 상태는 워크플로 열에 표시되며, 이 경우 **Aspose.PDF Workflow**입니다.

   **소스 라이브러리에 문서 추가**

![Workflow Activity_8을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. 변환된 문서를 보려면 대상 문서 라이브러리를 엽니다. 이 예시에서 경로는 **Shared Documents/Pdf**입니다.

   **대상 라이브러리**

![Workflow Activity_9을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_9.png)
