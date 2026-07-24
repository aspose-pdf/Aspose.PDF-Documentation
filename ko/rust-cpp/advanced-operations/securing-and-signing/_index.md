---
title: Rust에서 PDF 보안 및 서명
linktitle: PDF 보안 및 서명
type: docs
weight: 50
url: /ko/rust-cpp/securing-and-signing/
description: 이 섹션에서는 Rust를 사용하여 서명을 적용하고 PDF 문서를 보호하는 기능에 대해 설명합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

이 섹션에서는 C++를 통해 Rust용 Aspose.PDF를 사용하여 보안이 적용된 PDF 문서를 작업하는 포괄적인 가이드를 제공합니다. PDF 파일을 비밀번호로 보호하고, 접근 권한을 관리하며, Rust에서 암호화된 문서를 안전하게 열거나 잠금 해제하는 방법을 설명합니다.

이 문서에서는 최신 암호화 알고리즘을 사용한 PDF 암호화, 비밀번호로 보호된 파일 복호화, 권한 플래그를 통한 사용자 접근 제어 등 일반적인 보안 관련 PDF 작업을 단계별로 안내합니다. 또한 기존 권한 설정을 검사하고 소유자 자격 증명을 사용하여 보안 문서를 열어 추가 처리하는 방법도 배울 수 있습니다.

PDF 문서를 생성하고, AES 기반 암호화를 사용하여 최신 암호화 보호를 적용하며, 인쇄, 콘텐츠 편집, 양식 작성 등 사용자 기능을 제어하는 방법을 배웁니다. 또한 소유자 자격 증명을 사용해 비밀번호 보호된 PDF를 열고 복호화하여 추가 처리에 적합한 제한 없는 문서를 생성하는 방법도 시연합니다.

- [PDF 파일 암호화](/pdf/ko/rust-cpp/encrypt-pdf/)
- [PDF 파일 복호화](/pdf/ko/rust-cpp/decrypt-pdf/)
- [권한 가져오기](/pdf/ko/rust-cpp/get-permissions/)
- [권한 설정](/pdf/ko/rust-cpp/set_permissions/)
- [비밀번호로 보호된 PDF 열기](/pdf/ko/rust-cpp/open-password-protected-pdf/)

Set Permissions와 Get Permissions를 진행하려면 PDF Permissions Reference 표를 참조하십시오. 이 표에는 최종 사용자가 PDF 문서와 상호 작용하는 방식을 제어하기 위해 적용할 수 있는 사용 가능한 권한 플래그가 나열되어 있습니다.

## PDF 권한 참조

| **권한** | **설명** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | 인쇄 허용 |
| Permissions::MODIFY_CONTENT | 콘텐츠 수정 허용 (양식/주석 제외) |
| Permissions::EXTRACT_CONTENT | 텍스트 및 그래픽 복사/추출 허용 |
| Permissions::MODIFY_TEXT_ANNOTATIONS | 텍스트 주석 추가/수정 허용 |
| Permissions::FILL_FORM | 대화형 양식 채우기 허용 |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | 접근성을 위한 콘텐츠 추출 허용 |
| Permissions::ASSEMBLE_DOCUMENT | 페이지 삽입/회전/삭제 또는 구조 변경 허용 |
| Permissions::PRINTING_QUALITY | 고품질 / 정확한 인쇄 허용 |
