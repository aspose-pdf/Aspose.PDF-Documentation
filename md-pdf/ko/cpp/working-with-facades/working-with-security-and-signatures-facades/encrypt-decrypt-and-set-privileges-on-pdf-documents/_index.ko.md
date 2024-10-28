---
title: PDF 문서 암호화, 복호화 및 권한 설정
type: docs
weight: 10
url: /cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**기존 PDF 파일에 권한 설정하기**
기존 PDF 문서에 권한을 설정하려면 **Document->Encrypt(...)** 메서드를 사용할 수 있으며, 이는 **DocumentPrivilege** 객체를 인수로 받습니다. **DocumentPrivilege** 클래스는 PDF 문서에 접근하기 위한 다양한 권한을 설정하는 데 사용됩니다. 이 클래스에는 다음과 같은 4가지 방법이 있습니다:

1. 미리 정의된 권한을 직접 사용합니다.
1. 미리 정의된 권한을 기반으로 특정 권한을 변경합니다.
1. 미리 정의된 권한을 기반으로 특정 Adobe Professional 권한 조합을 변경합니다.
1. 방법 2와 방법 3을 혼합합니다.

다음 코드 스니펫은 문서 권한을 설정하는 위의 4가지 방법을 보여줍니다: