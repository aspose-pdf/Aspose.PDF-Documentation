---
title: استخدام تعليقات الروابط في PDF
linktitle: تعليقات الروابط
type: docs
weight: 70
url: /ar/python-net/link-annotations/
description: تتيح لك Aspose.PDF للبايثون عبر .NET إضافة، الحصول على، وحذف تعليقات الروابط من مستند PDF الخاص بك.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## إضافة تعليق رابط إلى ملف PDF موجود

[الروابط](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) هي تعليقات تفتح عناوين URL أو تنتقل إلى مواقع معينة داخل نفس الوثيقة أو داخل وثيقة خارجية عند النقر.

تعليق الرابط هو منطقة مستطيلة يمكن وضعها في أي مكان على الصفحة. كل رابط له إجراء PDF مرتبط به. يتم تنفيذ هذا الإجراء عندما ينقر المستخدم داخل منطقة هذا الرابط.

توضح المقتطف البرمجي التالي كيفية إضافة تعليق رابط إلى ملف PDF باستخدام مثال رقم هاتف:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### الحصول على تعليق رابط

يرجى تجربة استخدام المقتطف البرمجي التالي للحصول على [تعليق الرابط](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) من مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### حذف تعليق رابط

يوضح المقتطف البرمجي التالي كيفية حذف تعليق رابط من ملف PDF. لهذا نحتاج إلى العثور على جميع تعليقات الروابط وإزالتها في الصفحة الأولى. بعد ذلك سنحفظ المستند مع حذف التعليق.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
