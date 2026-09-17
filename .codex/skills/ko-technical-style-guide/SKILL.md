---
name: ko-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Korean programming documentation. It normalizes headings, step-by-step instructions, figure captions, terminology, particles, API identifiers, UI labels, spacing, and technical formatting to consistent Korean.
---

# Korean Technical Documentation Style

## Goal

Normalize Korean programming documentation to a clear, concise, consistent style suitable for developers.

Use modern standard Korean.

For explanatory prose, use a consistent polite technical style based on **-습니다/-ㅂ니다** unless project-specific localization instructions specify another style.

For explicit procedural steps, use **-하세요** by default.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Korean writing conventions.

Never change API identifiers, commands, paths, filenames, or actual UI labels merely to satisfy a linguistic rule.

---

## 1. Identify the structural role first

Before rewriting text, determine whether it is:

- a task heading;
- a conceptual heading;
- a procedural step;
- a figure caption;
- a note or warning;
- explanatory prose;
- a UI label;
- an API or code identifier.

Do not normalize text mechanically.

Korean grammatical form depends on the structural role of the text.

---

## 2. General prose

Use concise technical Korean.

For explanatory prose, prefer consistent **-습니다/-ㅂ니다** endings.

Good:

- 이 메서드는 PDF 문서를 저장합니다.
- 다음 예제에서는 PDF 파일을 DOCX 형식으로 변환합니다.
- `Document` 클래스는 PDF 문서를 나타냅니다.

Avoid mixing speech levels.

Bad:

- 이 메서드는 PDF 문서를 저장합니다.
- 반환값은 변환된 데이터이다.

Prefer:

- 이 메서드는 PDF 문서를 저장합니다.
- 반환값은 변환된 데이터입니다.

Avoid unnecessarily conversational or excessively honorific language.

---

## 3. Headings

Use concise noun phrases by default.

Good:

- PDF 문서 만들기
- 페이지 추가
- 텍스트 추출
- PDF를 DOCX로 변환
- 변환 옵션 설정
- 문서 저장

For technical how-to documentation, action-oriented headings using **-기** or concise action nouns are appropriate.

Choose one pattern for sibling headings and apply it consistently.

Do not normally end headings with a period.

Good:

- PDF 문서 만들기

Bad:

- PDF 문서 만들기.

---

## 4. Task headings

Use concise task-oriented forms.

Recommended patterns include:

- PDF 문서 만들기
- 페이지 추가
- 텍스트 추출
- 이미지 추출
- 변환 옵션 설정
- PDF를 DOCX로 변환
- 문서 저장

Avoid unnecessarily verbose forms.

Avoid:

- PDF 문서를 만드는 방법에 대한 설명

Prefer:

- PDF 문서 만들기

Do not use full polite instructions as headings.

Avoid:

- PDF 문서를 만드세요

Prefer:

- PDF 문서 만들기

---

## 5. Conceptual headings

Use concise noun phrases.

Good:

- 사전 요구 사항
- 변환 옵션
- 지원되는 형식
- 알려진 제한 사항
- 글꼴 관리
- 문서 구조
- API 참조

Do not turn conceptual headings into procedural instructions.

---

## 6. Step-by-step instructions

Use natural Korean sentence order and **-하세요** for explicit procedural instructions.

Good:

- `Document` 개체를 만드세요.
- PDF 파일을 여세요.
- 문서에 페이지를 추가하세요.
- 변환 옵션을 설정하세요.
- 문서를 저장하세요.

Avoid dictionary-form instructions in numbered procedures.

Bad:

- `Document` 개체를 만들다.
- PDF 파일을 열다.
- 페이지를 추가하다.
- 문서를 저장하다.

Avoid noun fragments when a complete instruction is required.

Bad:

- `Document` 개체 생성.
- PDF 파일 열기.
- 페이지 추가.

These forms may be acceptable as compact headings, but not as normal full procedural steps.

---

## 7. Do not force verb-first structure

Korean instructions normally place the action toward the end of the sentence.

Natural:

- `Document` 개체를 만드세요.
- `save()` 메서드를 호출하세요.
- `Compliance` 속성을 설정하세요.

Do not reorganize Korean sentences to imitate English, French, Spanish, or Russian action-first instructions.

The requirement is that each step contains a clear action, not that the verb appears first.

---

## 8. Common instruction normalization

| Concept | Preferred form |
|---|---|
| open | 여세요 |
| create | 만드세요 |
| add | 추가하세요 |
| configure/set | 설정하세요 |
| select | 선택하세요 |
| run/execute | 실행하세요 |
| save | 저장하세요 |
| delete | 삭제하세요 |
| install | 설치하세요 |
| specify | 지정하세요 |
| check | 확인하세요 |
| convert | 변환하세요 |
| extract | 추출하세요 |
| import | 가져오세요 / 임포트하세요 |
| export | 내보내세요 / 익스포트하세요 |
| call | 호출하세요 |
| get/retrieve | 가져오세요 / 검색하세요 |
| use | 사용하세요 |
| enter | 입력하세요 |
| download | 다운로드하세요 |
| upload | 업로드하세요 |

The correct Korean term may depend on the technical meaning.

For example, do not mechanically translate every occurrence of `get` to the same Korean verb.

Follow the approved project glossary and API context.

---

## 9. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. `Document` 개체를 만드세요.
2. 문서에 페이지를 추가하세요.
3. `TextFragment` 개체를 만드세요.
4. 페이지에 텍스트를 추가하세요.
5. PDF 문서를 저장하세요.

Each numbered item should normally represent one primary action.

Avoid combining an entire procedure into one step.

Bad:

1. 문서를 만들고 페이지를 추가한 다음 글꼴을 설정하고 텍스트를 추가한 후 파일을 저장하세요.

Split meaningful stages into separate steps.

---

## 10. Step punctuation

Write procedural instructions as complete sentences.

End complete steps with a period.

Good:

1. PDF 문서를 여세요.
2. 처리할 페이지를 선택하세요.
3. 페이지에서 텍스트를 추출하세요.

Bad:

1. PDF 문서 열기
2. 페이지 선택
3. 텍스트 추출

The shorter forms may be used as headings or compact UI labels, but not as ordinary procedural sentences.

---

## 11. Context before action

When useful, state the context before the action.

Good:

- **파일** 메뉴에서 **다른 이름으로 저장**을 선택하세요.
- `PdfSaveOptions` 개체에서 `Compliance` 속성을 설정하세요.
- Visual Studio에서 **NuGet 패키지 관리자**를 여세요.

This establishes where the reader should perform the action.

---

## 12. Explanations are not steps

Do not number explanatory information unless the reader must perform an action.

Preferred:

1. `Document` 개체를 만드세요.

   이 개체는 처리할 PDF 문서를 나타냅니다.

The first sentence is the action.

The second sentence explains the object.

---

## 13. Figure captions

Use the following default pattern:

`그림 N. 설명`

Examples:

- 그림 1. PDF 문서 구조
- 그림 2. 변환 옵션 설정
- 그림 3. 변환 결과
- 그림 4. 프로젝트 구성

Use concise descriptive noun phrases.

Avoid:

- Figure 3: Conversion Result
- 그림 3. 변환 결과를 보여 줍니다.
- 그림 3. 스크린샷
- 그림 3. 예제

Describe what the figure communicates rather than merely identifying it as a screenshot.

---

## 14. Figure references

Use `그림 N` in running text.

Good:

- 그림 2를 참조하세요.
- 변환 결과는 그림 3에 나와 있습니다.
- 그림 4는 프로젝트 구성을 보여 줍니다.

Do not use `Figure` or `Fig.` unless the project's publishing system requires English labels.

---

## 15. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- source-code variables;
- package names;
- command-line options;
- file extensions.

Good:

- `Document` 개체를 만드세요.
- `save()` 메서드를 호출하세요.
- `page_info` 속성을 설정하세요.

Do not translate identifiers into Korean.

Use code formatting for identifiers.

---

## 16. Korean particles and identifiers

Place Korean particles outside inline-code formatting.

Good:

- `Document`를 만드세요.
- `save()`를 호출하세요.
- `Compliance`를 설정하세요.
- `Document`의 인스턴스를 만드세요.

Bad:

- `Document를` 만드세요.
- `save()를` 호출하세요.
- `Document의` 인스턴스를 만드세요.

Code formatting must contain only the literal identifier.

Choose the particle according to the pronunciation of the identifier where practical and according to the project's established convention.

---

## 17. Files, paths, and commands

Format literal filenames, paths, commands, and extensions as code.

Good:

- `input.pdf`를 여세요.
- 결과를 `output.pdf`로 저장하세요.
- `dotnet build`를 실행하세요.
- `C:\Samples\PDF` 디렉터리를 여세요.

Do not translate literal values.

---

## 18. UI labels

Preserve the exact text displayed by the documented product.

If the Korean UI displays:

**다른 이름으로 저장**

write:

- **다른 이름으로 저장**을 선택하세요.

If the actual product displays:

**Save As**

write:

- **Save As**를 선택하세요.

Do not invent Korean UI translations.

---

## 19. Korean spacing

Apply standard Korean spacing consistently in ordinary prose.

Good:

- PDF 파일
- 소스 코드
- 사용자 인터페이스
- 변환 옵션
- 데이터베이스 연결

Preserve the spelling and internal spacing of:

- product names;
- API identifiers;
- commands;
- filenames;
- UI labels.

Do not alter technical literals merely to satisfy Korean spacing conventions.

---

## 20. Technical terminology

Prefer established Korean technical terminology.

Examples:

- 애플리케이션
- 개체 / 객체
- 메서드
- 속성
- 인터페이스
- 매개 변수
- 생성자
- 디렉터리
- 패키지
- 라이브러리
- 소스 코드
- 데이터베이스

Choose between alternatives such as `개체` and `객체` according to the approved project glossary.

Do not alternate between them arbitrarily.

Preserve technologies and product names:

- .NET
- Python
- Java
- JSON
- REST API
- NuGet
- GitHub

---

## 21. Avoid unnecessary English

Use natural Korean terminology when an established translation exists.

Avoid:

- 문서를 save하세요.

Prefer:

- 문서를 저장하세요.

But preserve an actual API identifier:

- `save()` 메서드를 호출하세요.

Likewise, distinguish between ordinary terminology and literal API elements.

---

## 22. Terminology consistency

Use one preferred Korean term for one concept.

Do not randomly alternate between:

- 개체 / 객체;
- 디렉터리 / 폴더;
- 설정 / 구성;
- 사용 / 이용;
- 삭제 / 제거;
- 메서드 / 함수 when referring to the same API construct.

Different terms may be appropriate when they represent genuinely different concepts.

The approved project glossary takes precedence.

---

## 23. Notes and warnings

Use consistent labels.

Recommended:

- **참고:** supplementary information.
- **팁:** optional advice.
- **중요:** information necessary for successful completion.
- **경고:** potential risk, destructive action, security issue, or data loss.

Do not alternate labels without a semantic reason.

---

## 24. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- PDF 문서 만들기
- 페이지 추가
- 글꼴 설정
- 문서 저장

Bad:

- PDF 문서 만들기
- 페이지를 추가하세요
- 글꼴 설정에 대해
- 문서 저장 방법

Keep procedural steps parallel as well:

- 만드세요.
- 추가하세요.
- 설정하세요.
- 저장하세요.

Do not sacrifice natural Korean word order merely to achieve visual parallelism.

---

## 25. Normalization examples

### Heading

Before:

`PDF 문서를 만드는 방법`

After:

`PDF 문서 만들기`

### Step

Before:

`PDF 파일을 열다.`

After:

`PDF 파일을 여세요.`

### Fragment

Before:

`페이지 선택.`

After:

`페이지를 선택하세요.`

### Figure

Before:

`Figure 2: Conversion Result`

After:

`그림 2. 변환 결과`

### API formatting

Before:

`Document 개체를 만드세요.`

After:

`` `Document` 개체를 만드세요. ``

### Particle formatting

Before:

`` `Document를` 만드세요. ``

After:

`` `Document`를 만드세요. ``

---

## 26. Review checklist

Before completing a Korean technical-documentation task, verify:

- [ ] Task headings use concise action-oriented forms.
- [ ] Conceptual headings use concise noun phrases.
- [ ] Sibling headings use parallel structures.
- [ ] Headings do not end with unnecessary periods.
- [ ] Explicit procedural steps use the project's chosen instructional ending, `-하세요` by default.
- [ ] Explanatory prose consistently uses the project's chosen speech level.
- [ ] Steps use natural Korean word order.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Figure captions follow `그림 N. 설명`.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Korean particles remain outside code formatting.
- [ ] Commands, filenames, and paths remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Korean spacing is consistent.
- [ ] Technical terminology is consistent.
- [ ] The approved glossary takes precedence over generic terminology.

## Core rule

**작업 제목에는 간결한 작업 중심 표현을 사용하고, 단계별 지침에는 자연스러운 한국어 어순과 `-하세요` 형식을 사용하며, 그림 캡션에는 설명적인 명사구를 사용하세요.**

In English:

**Use concise action-oriented headings, natural Korean word order with `-하세요` for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> PDF 문서 만들기

Step:

> `Document` 개체를 만드세요.

Figure:

> 그림 1. PDF 문서 구조