---
title: استخراج المحتوى الموسوم من ملفات PDF في Java
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: /ar/java/extract-tagged-content-from-tagged-pdfs/
description: تعرّف على كيفية فحص محتوى PDF الموسوم في Java باستخدام Aspose.PDF، بما في ذلك الوصول إلى المحتوى الموسوم، الوصول إلى الجذر الهيكلي، وعناصر الهيكل الفرعية.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
استخدم هذه APIs عندما تحتاج إلى فحص شجرة الهيكل المنطقي لملف PDF الموسوم وفحص أو تحديث بيانات تعريف عناصر الهيكل.

## احصل على بيانات تعريف المحتوى الموسوم

استخدم هذا المثال عندما تحتاج إلى الوصول إلى حاوية المحتوى الموسوم وتريد تعريف بيانات تعريف المستند الأساسية مثل العنوان واللغة.

1. أنشئ مستند PDF جديدًا باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الكائن [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) من المستند.
1. عيّن بيانات تعريف المحتوى الموسوم واحفظ ملف الإخراج.

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## احصل على الهيكل الجذري لملف PDF معلم

يعرض هذا المثال كيفية فحص الكائنات الجذرية التي تمثل شجرة البنية لمستند PDF معلم.

1. أنشئ مستند PDF جديدًا باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) والحصول على محتواه المعلم.
1. عيّن البيانات الوصفية المطلوبة للمستند.
1. اقرأ واطبع جذر شجرة البنية والعنصر الجذري المنطقي، ثم احفظ الملف.

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## الوصول إلى عناصر Structure Elements الفرعية وتحديثها

استخدم هذا المثال عندما تحتاج إلى التكرار عبر العناصر الفرعية في شجرة البنية، فحص خصائصها، وتحديث البيانات الوصفية المحددة.

1. افتح ملف Tagged PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ العناصر الفرعية من جذر شجرة البنية واطبع الخصائص المتاحة.
1. انتقل إلى العناصر الفرعية للطف الأول للجذر، تحديث بيانات التعريف الخاصة بها، واحفظ المستند.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
