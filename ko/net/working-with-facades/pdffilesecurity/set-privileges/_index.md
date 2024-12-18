---
title: PDF에 권한 설정
type: docs
weight: 50
url: /ko/net/set-privileges/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 기존 PDF 파일에 권한을 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에 권한 설정

PDF 파일의 권한을 설정하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성하고 SetPrivilege 메서드를 호출하십시오. DocumentPrivilege 객체를 사용하여 권한을 지정한 다음 이 객체를 SetPrivilege 메서드에 전달할 수 있습니다. 다음 코드 스니펫은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```csharp
public static void SetPrivilege1()
 {
    // DocumentPrivileges 객체 생성
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // PdfFileSecurity 객체 생성
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

다음 메서드를 암호를 지정하여 참조하십시오:

```csharp
 public static void SetPrivilege2()
 {
    // DocumentPrivileges 객체 생성
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // PdfFileSecurity 객체 생성
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## PDF에서 확장 권한 기능 제거

PDF 문서는 Adobe Acrobat Reader를 사용하여 최종 사용자가 양식 필드에 데이터를 입력하고 채워진 양식의 복사본을 저장할 수 있도록 확장 권한 기능을 지원합니다. 그러나 PDF 파일이 수정되지 않도록 보장하며, PDF의 구조에 수정이 가해지면 확장 권한 기능이 상실됩니다. 이러한 문서를 볼 때, 문서가 수정되어 확장 권한이 제거되었다는 오류 메시지가 표시됩니다. 최근에 PDF 문서에서 확장 권한을 제거하라는 요구 사항을 받았습니다.

PDF 파일에서 확장 권한을 제거하기 위해 PdfFileSignature 클래스에 RemoveUsageRights()라는 새 메서드가 추가되었습니다. 소스 PDF에 확장 권한이 있는지 여부를 확인하기 위해 ContainsUsageRights()라는 또 다른 메서드가 추가되었습니다.

{{% alert color="primary" %}}
Aspose.PDF for .NET 9.5.0부터 다음 메서드의 이름이 업데이트되었습니다. 이전 메서드가 여전히 API에 있지만 더 이상 사용되지 않음으로 표시되어 제거될 예정임을 유의하십시오. 따라서 업데이트된 메서드를 사용하는 것이 좋습니다.

- IsContainSignature(.) 메서드는 ContainsSignature(..)로 이름이 변경되었습니다.

- IsCoversWholeDocument(..) 메서드는 CoversWholeDocument(..)로 이름이 변경되었습니다.{{% /alert %}}

다음 코드는 문서에서 사용 권한을 제거하는 방법을 보여줍니다:

```csharp
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```