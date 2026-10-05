---
name: ar-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Arabic programming documentation. It normalizes headings, procedural instructions, figure captions, terminology, UI labels, punctuation, and right-to-left prose while preserving API identifiers and technical literals.
---

# Arabic Technical Documentation Style

## Goal and priority

Use clear, concise Modern Standard Arabic (العربية الفصحى المعاصرة) for developer documentation. Avoid regional dialects and unnecessarily ornate language.

When rules conflict, follow project-specific localization instructions, then the approved glossary, then established product and API terminology, then this guide.

Preserve technical meaning, Markdown structure, Hugo shortcodes, embedded HTML, and structured data. Keep edits within the requested language and section. Do not change canonical URLs, aliases, navigation weights, or code behavior as part of a language-style correction.

## 1. Identify the role of the text

Distinguish task headings, conceptual headings, procedural steps, explanations, figure captions, UI labels, and technical literals before editing.

Use verbal nouns for task headings, imperatives for procedural steps, and descriptive noun phrases for concepts and captions. Do not apply one grammatical pattern to every occurrence of an action word.

## 2. General prose

Prefer short, direct sentences with an explicit technical subject when it helps comprehension.

Good:

- تحفظ هذه الطريقة مستند PDF.
- يحوّل المثال التالي ملف PDF إلى تنسيق DOCX.
- تمثل الفئة `Document` مستند PDF.

Avoid lengthy introductory phrases such as تجدر الإشارة إلى أن when the sentence can state the information directly.

Translate ordinary English prose into Arabic, but preserve product names, technology names, and actual API identifiers:

- Prefer احفظ المستند. to قم بعمل save للمستند.
- Preserve استدعِ الطريقة `save()`.
- Keep Aspose.PDF, .NET, Java, Python, JSON, NuGet, and GitHub unchanged.

Do not add full vocalization to ordinary prose. Preserve meaningful hamzas and normal spelling; use limited diacritics where they resolve ambiguity, such as حدّد and نزّل. Do not add decorative tatweel (ـ).

## 3. Headings

Use concise verbal-noun phrases for task headings:

- إنشاء مستند PDF
- فتح ملف PDF
- إضافة صفحة
- استخراج النص
- تحويل PDF إلى DOCX
- إعداد خيارات التحويل
- حفظ المستند

Use noun phrases for conceptual headings:

- المتطلبات الأساسية
- التنسيقات المدعومة
- خيارات التحويل
- بنية المستند
- إدارة الخطوط
- القيود المعروفة
- مرجع واجهة برمجة التطبيقات

Keep sibling headings parallel. Avoid terminal periods and unnecessary prefixes such as كيفية when a concise heading states the task clearly. Do not apply English capitalization rules to Arabic text.

Do not use a full instruction such as أنشئ مستند PDF. as a task heading when sibling headings use verbal nouns.

## 4. Procedural instructions

Use the singular imperative consistently as the default instructional convention. This grammatical convention addresses the reader without inferring their gender. Follow explicit project instructions if another address form is established.

Good:

1. أنشئ كائنًا من الفئة `Document`.
2. أضف صفحة إلى المستند.
3. أنشئ كائنًا من الفئة `TextFragment`.
4. أضف النص إلى الصفحة.
5. احفظ مستند PDF.

Avoid verbal-noun fragments in procedural steps:

- إنشاء كائن من الفئة `Document`.
- إضافة صفحة.
- حفظ المستند.

These forms are suitable for headings, not complete instructions.

Prefer a direct imperative such as افتح الملف. to a routine circumlocution such as قم بفتح الملف. Do not turn explanations or requirements into commands merely because they mention an action.

Use numbered lists for sequences and bullets for independent actions. Each step should contain one primary action and end with a period. Keep existing Markdown list markers and nesting intact unless structural correction is requested.

## 5. Common action forms

| Action | Task heading | Procedural instruction |
|---|---|---|
| create | إنشاء | أنشئ |
| open | فتح | افتح |
| add | إضافة | أضف |
| configure | إعداد | اضبط |
| specify | تحديد | حدّد |
| select | اختيار | اختر |
| run | تشغيل | شغّل |
| save | حفظ | احفظ |
| delete | حذف | احذف |
| install | تثبيت | ثبّت |
| convert | تحويل | حوّل |
| extract | استخراج | استخرج |
| import | استيراد | استورد |
| export | تصدير | صدّر |
| call | استدعاء | استدعِ |
| use | استخدام | استخدم |
| enter | إدخال | أدخل |
| download | تنزيل | نزّل |
| upload | رفع | ارفع |
| check | التحقق | تحقّق |

Choose the verb by meaning and glossary. For example, اضبط الخاصية sets a property, while حدّد المسار specifies a path. Do not substitute verbs mechanically or confuse uploading with downloading.

## 6. Context and explanations

Provide the location of an action when needed:

- من قائمة **File**، اختر **Save As**.
- في Visual Studio، افتح **NuGet Package Manager**.
- اضبط الخاصية `Compliance` في الكائن `PdfSaveOptions`.

Context may precede the imperative when this makes the Arabic sentence clearer.

Keep explanatory text distinct from the action:

1. أنشئ كائنًا من الفئة `Document`.

   يمثل هذا الكائن مستند PDF المراد معالجته.

Preserve the distinction between possibility, requirement, and recommendation: يمكن for capability, يجب for a requirement, and يُنصح for a recommendation. Do not strengthen or weaken the source's obligation.

## 7. Figure captions and references

Use the default caption pattern `الشكل N. الوصف`, subject to established project conventions:

- الشكل 1. بنية مستند PDF
- الشكل 2. خيارات التحويل
- الشكل 3. نتيجة التحويل

Describe what the image communicates, rather than labeling it only لقطة شاشة or مثال.

In running text:

- راجع الشكل 2.
- يوضّح الشكل 3 نتيجة التحويل.

Keep caption numbers consistent with references. Do not renumber figures during a wording-only edit.

## 8. Technical literals and Arabic grammar

Never translate or alter class names, methods, properties, namespaces, enum members, source-code variables, package names, command options, file extensions, URLs, paths, or literal filenames.

Use Arabic category words around identifiers:

- أنشئ كائنًا من الفئة `Document`.
- استدعِ الطريقة `save()`.
- اضبط الخاصية `page_info`.
- افتح الملف `input.pdf`.
- احفظ النتيجة في الملف `output.pdf`.
- شغّل الأمر `dotnet build`.

Do not attach an Arabic article or grammatical ending inside an identifier. Prefer الفئة `Document` to modifying the literal into `الDocument`.

For new prose, format technical literals as inline code. During review, preserve existing inline-code formatting unless formatting changes are part of the request; an unformatted identifier is still a protected literal.

Preserve fenced code blocks and their language identifiers. Translate surrounding explanations rather than code, string literals, comments, or API calls unless the user explicitly requests their localization.

## 9. UI labels

Match the text displayed by the documented product. Do not invent an Arabic label for an English interface.

- English UI: اختر **Save As**.
- Verified Arabic UI: اختر **حفظ باسم**.

Use bold for UI labels where that matches the local pattern. If a translation is useful for explanation, put it outside the literal label and clearly distinguish it from the displayed text.

## 10. Terminology

Follow the approved glossary and nearby pages. Suggested defaults when no local terminology is established:

| Concept | Arabic |
|---|---|
| file | ملف |
| document | مستند |
| page | صفحة |
| class | فئة |
| object | كائن |
| instance | مثيل |
| method | طريقة |
| function | دالة |
| property | خاصية |
| parameter | معلمة |
| argument | وسيطة |
| return value | قيمة الإرجاع |
| library | مكتبة |
| package | حزمة |
| directory | دليل |
| source code | الشفرة المصدرية |
| user interface | واجهة المستخدم |
| API | واجهة برمجة التطبيقات |

Use different terms where the concepts differ, especially method/function, parameter/argument, and file/document. Do not replace a project's established term merely to match this default table.

## 11. Punctuation and numbers

Use Arabic punctuation in ordinary Arabic prose where appropriate: comma `،`, semicolon `؛`, and question mark `؟`. Use the ordinary period and colon for sentence endings and labels. Put no space before punctuation and normally one space after it.

Never replace punctuation inside code, URLs, paths, version strings, commands, or literal UI labels.

Preserve the project's numeral convention in prose and captions. When none is established, use digits `0–9` consistently for developer documentation. Keep Markdown numbering syntax, technical values, versions, and code literals unchanged; do not convert their digits to Arabic-Indic forms.

Arabic has no uppercase/lowercase distinction. Preserve the exact case of Latin product names and identifiers.

## 12. Right-to-left prose and left-to-right literals

Write Arabic in normal logical Unicode order. Never reverse letters, filenames, identifiers, path segments, or code to imitate their visual appearance.

Keep technical literals together using existing Markdown code formatting. Separate them from Arabic text with ordinary spaces and clear category words when this improves readability.

Preserve existing direction markup. Do not add page-wide `dir="rtl"`, CSS, HTML wrappers, or invisible direction-control characters during an ordinary language edit.

If a demonstrated rendering issue requires direction isolation and markup changes are authorized, use the project's supported pattern; for example, `<bdi dir="ltr">...</bdi>` for a left-to-right literal in HTML. Confirm renderer support before applying it. Inline code alone does not guarantee bidirectional isolation in every renderer.

Never insert direction-control characters into copyable commands, code, URLs, or paths. Do not mirror punctuation manually or reorder a command's arguments to repair a visual issue.

## 13. Notes and warnings

Use labels consistently according to meaning:

- **ملاحظة:** supplementary information.
- **نصيحة:** optional advice.
- **مهم:** information needed to complete the task successfully.
- **تحذير:** a risk such as data loss or a destructive action.

Preserve existing Hugo alert shortcodes and their attributes. Translate their visible prose without changing the alert's severity or inventing warnings.

## 14. Normalization examples

| Role | Before | After |
|---|---|---|
| Heading | كيفية إنشاء مستند PDF. | إنشاء مستند PDF |
| Step | إنشاء كائن من الفئة `Document`. | أنشئ كائنًا من الفئة `Document`. |
| Step | قم بحفظ المستند. | احفظ المستند. |
| Mixed prose | قم بعمل save للمستند. | احفظ المستند. |
| Caption | Figure 2: Conversion Result | الشكل 2. نتيجة التحويل |

These examples change prose, not API behavior. Never guess an API name when the source appears mistranslated; verify it or flag the uncertainty.

## 15. Review checklist

- [ ] Prose uses Modern Standard Arabic and consistent terminology.
- [ ] Task headings use verbal nouns; conceptual headings use noun phrases.
- [ ] Procedural steps use clear, consistent imperatives.
- [ ] Explanations remain separate from actions, and obligation levels are preserved.
- [ ] Captions and figure references use consistent labels and numbers.
- [ ] Identifiers, product names, technical values, and UI labels remain exact.
- [ ] Arabic punctuation changes affect prose only.
- [ ] Mixed-direction text remains in logical order without new hidden controls.
- [ ] Markdown, front matter, links, code blocks, shortcodes, and structured data retain their integrity.

## Core rule

**Use verbal nouns for task headings, direct imperatives for procedural steps, and descriptive noun phrases for captions. Preserve technical literals in their original logical order.**
