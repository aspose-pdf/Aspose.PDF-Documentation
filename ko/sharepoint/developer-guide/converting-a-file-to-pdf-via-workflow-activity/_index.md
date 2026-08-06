---
title: 워크플로 활동을 통해 파일을 PDF로 변환
linktitle: 워크플로 활동을 통해 파일을 PDF로 변환
type: docs
weight: 50
url: /ko/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: PDF SharePoint API는 문서를 PDF로 변환하는 SharePoint 워크플로에서 사용할 수 있습니다.
---

{{% alert color="primary" %}}

워크플로 지원은 Microsoft Office SharePoint Server의 핵심 기능입니다. 워크플로는 비즈니스 논리에 따라 문서 이동을 자동화하고 문서 구성에 드는 비용과 시간을 합리화하는 데 도움이 됩니다. 이 문서에서는 문서를 PDF로 변환하는 워크플로에서 SharePoint용 Aspose.PDF를 사용하는 방법을 보여줍니다.

{{% /alert %}}

## 워크플로 설정

이 예에서는 문서 라이브러리의 새 항목을 PDF 형식으로 변환하고 이를 다른 문서 라이브러리에 저장하는 워크플로를 만듭니다. 예제에서는 **개인 문서** 라이브러리를 소스 라이브러리로 사용하고 **공유 문서** 라이브러리의 **Pdf** 하위 폴더를 대상 라이브러리로 사용합니다.

SharePoint용 Aspose.PDF는 HTML, 텍스트 및 이미지 파일의 변환을 지원합니다.

### SharePoint Designer를 사용하여 워크플로 디자인

1. **SharePoint Designer**를 열고 워크플로가 구현될 사이트에 연결합니다.
1. **사이트 개체**에서 **워크플로**를 선택한 다음 **워크플로 목록**을 엽니다.
1. **개인 문서** 라이브러리를 선택하여 새 목록 워크플로를 만들고 문서 라이브러리에 첨부합니다.

   **메뉴에서 개인 문서 선택**

![Workflow Activity_1을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. 워크플로 이름과 설명을 입력하여 목록 워크플로를 만들고 **개인 문서** 라이브러리에 첨부합니다.
1. **확인**을 클릭하여 이 단계를 완료하세요.

   **목록 워크플로 생성**

![Workflow Activity_2를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_2.png)

워크플로 단계 편집기가 나타납니다. 이는 워크플로에 대한 조건과 작업을 정의하는 데 사용됩니다. 이제 **Aspose Actions**에서 조건 없이 새 문서를 PDF로 변환하는 작업을 추가하세요.

1. **작업** 메뉴에서 **Aspose.PDF를 통해 파일을 PDF로 변환** 작업을 선택합니다.

   **선택 및 실행**

![워크플로 Activity_3을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. 작업 매개변수를 구성합니다.
   1. **이 폴더** 매개변수를 대상 폴더로 설정합니다.
   1. 다른 작업 매개변수는 기본값으로 그대로 두거나 작업 속성 창을 사용하여 설정합니다. **덮어쓰기** 매개변수의 기본값은 false입니다.

      **워크플로 편집기**

![Workflow Activity_4를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_4.png)

**대상 라이브러리 설정**

![Workflow Activity_5를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_5.png)

**속성 설정**

![Workflow Activity_6을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. **워크플로** 메뉴에서 **워크플로 설정**을 선택합니다.
1. **새 항목이 생성되면 자동으로 워크플로 시작**을 선택하고 **시작 옵션**에서 다른 옵션을 선택 취소합니다.

   **시작 옵션 설정**

![Workflow Activity_7을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_7.png)

워크플로 디자인이 완료되었습니다.

1. 워크플로를 저장하고 게시하여 SharePoint 사이트에 구현합니다.

### 워크플로 테스트

워크플로우를 테스트하려면 다음을 수행하십시오.

1. SharePoint 사이트를 열고 **개인 문서** 문서 라이브러리에 새 문서를 업로드합니다.
   SharePoint용 Aspose.PDF는 HTML 파일, 텍스트 파일 및 이미지(JPG, PNG, GIF, TIFF 및 BMP*)에서 PDF로의 변환을 지원합니다. 워크플로는 새 항목이 생성될 때 자동으로 시작되도록 구성되어 있으므로 파일이 자동으로 처리됩니다.
1. 브라우저를 새로 고칩니다.
   이 경우 워크플로 상태는 워크플로 열 **Aspose.PDF Workflow**에 나타납니다.

   **소스 라이브러리에 문서 추가**

![Workflow Activity_8을 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. 변환된 문서를 보려면 대상 문서 라이브러리를 엽니다. **공유 문서/PDF**는 이 예에서 경로입니다.

   **대상 라이브러리**

![Workflow Activity_9를 통해 파일을 PDF로 변환](converting-a-file-to-pdf-via-workflow-activity_9.png)

